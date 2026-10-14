#!/usr/bin/env python3
"""Reading lists for the flagship courses.

data/course-readings.json holds every reading each flagship course assigns,
module by module, with the best legitimate link for it. This script writes
one page per course, courses/<folder>/readings.html, from that file.

  python3 scripts/build-reading-lists.py              write the pages
  python3 scripts/build-reading-lists.py --check      fail if a page is stale
  python3 scripts/build-reading-lists.py --lookup     find free legal copies
  python3 scripts/build-reading-lists.py --merge DIR  fold sourcing output in

Each reading has `access`:
  open     free full text from the publisher, an official body, a repository
           or the author
  library  a paywalled article or chapter, linked by DOI or publisher page
  book     an in-copyright book, linked to the publisher's page

--lookup asks Unpaywall, then OpenAlex, for every `library` reading with a
DOI. A free copy they report (an author's accepted manuscript in a university
repository, a working-paper version, an open publisher copy) is stored as
`free` and only kept if its address answers. Run it now and then; repository
copies appear long after publication.

A `library` reading with no free copy gets a "Request a copy" button. It posts
to the Netlify form `paper-request`, and netlify/functions/submission-created
emails the request to ImpactMojo. Nothing is sent to the reader automatically.
Books get no button.
"""
import html
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / 'data' / 'course-readings.json'
CONTACT = 'hello@impactmojo.in'   # Unpaywall asks callers to identify themselves

# course_id in Supabase -> (folder under courses/, page that is the course)
FOLDERS = {'SEL': 'sel', 'powerBI': 'powerBI'}
COURSE_PAGE = {'powerBI': 'powerbi.html'}

VERSION_LABEL = {
    'publishedVersion': 'Free copy of the published version',
    'acceptedVersion': "Free copy, the author's accepted manuscript",
    'submittedVersion': 'Free copy, a working-paper version',
}


def folder(cid):
    return FOLDERS.get(cid, cid)


def course_title(cid):
    page = ROOT / 'courses' / folder(cid) / COURSE_PAGE.get(cid, 'index.html')
    s = page.read_text(encoding='utf-8')
    m = re.search(r'<title>(.*?)</title>', s, re.S)
    t = html.unescape(m.group(1)).strip() if m else cid
    return re.split(r'\s*[|—–]\s*', t)[0].strip()


def doi_of(r):
    if r.get('doi'):
        return r['doi'].lower()
    m = re.search(r'doi\.org/(10\.\d{4,9}/\S+)', r.get('url', ''), re.I)
    return urllib.parse.unquote(m.group(1)).rstrip('.').lower() if m else None


# ---------------------------------------------------------------- merge

def merge(src):
    data = json.loads(DATA.read_text(encoding='utf-8')) if DATA.exists() else {'courses': {}}
    old = data['courses']
    for f in sorted(Path(src).glob('out-*.json')):
        o = json.loads(f.read_text(encoding='utf-8'))
        cid = o['course']
        keep = {}
        for m in old.get(cid, {}).get('modules', []):
            for r in m['readings']:
                if r.get('free'):
                    keep[r['cite']] = r['free']
        mods = []
        for m in o['modules']:
            rs = []
            for r in m.get('readings', []):
                if r.get('access') not in ('open', 'library', 'book'):
                    raise SystemExit(f'{f.name}: bad access {r.get("access")!r} in module {m["n"]}')
                e = {k: r[k] for k in ('cite', 'url', 'access') if k in r}
                if r['cite'] in keep:
                    e['free'] = keep[r['cite']]
                rs.append(e)
            mods.append({'n': m['n'], 'title': m['title'], 'readings': rs})
        old[cid] = {'modules': mods}
        print(f'{cid}: {sum(len(m["readings"]) for m in mods)} readings')
    data['courses'] = dict(sorted(old.items(), key=lambda kv: kv[0].lower()))
    DATA.write_text(json.dumps(data, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')


# ---------------------------------------------------------------- lookup

def get_json(url):
    req = urllib.request.Request(url, headers={'User-Agent': f'ImpactMojo reading lists ({CONTACT})'})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def answers(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=25) as r:
            return r.status == 200
    except Exception:
        return False


def find_free(doi):
    q = urllib.parse.quote(doi)
    try:
        u = get_json(f'https://api.unpaywall.org/v2/{q}?email={CONTACT}')
        loc = u.get('best_oa_location')
        if loc and loc.get('url'):
            return {'url': loc.get('url_for_landing_page') or loc['url'],
                    'version': loc.get('version') or '', 'host': loc.get('host_type') or '',
                    'via': 'Unpaywall'}
    except Exception:
        pass
    try:
        o = get_json(f'https://api.openalex.org/works/doi:{q}?mailto={CONTACT}')
        loc = o.get('best_oa_location') or {}
        url = loc.get('landing_page_url') or loc.get('pdf_url')
        if url:
            return {'url': url, 'version': loc.get('version') or '',
                    'host': 'repository' if (loc.get('source') or {}).get('type') == 'repository' else 'publisher',
                    'via': 'OpenAlex'}
    except Exception:
        pass
    return None


def lookup():
    data = json.loads(DATA.read_text(encoding='utf-8'))
    seen, found, asked = {}, 0, 0
    for cid, c in data['courses'].items():
        for m in c['modules']:
            for r in m['readings']:
                if r['access'] != 'library':
                    continue
                d = doi_of(r)
                if not d:
                    continue
                if d not in seen:
                    asked += 1
                    f = find_free(d)
                    if f and not answers(f['url']):
                        f = None
                    seen[d] = f
                    time.sleep(0.2)
                if seen[d]:
                    r['free'] = dict(seen[d], checked=date.today().isoformat())
                    found += 1
                else:
                    r.pop('free', None)
    DATA.write_text(json.dumps(data, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(f'looked up {asked} DOIs; {found} paywalled readings now carry a free copy')


# ---------------------------------------------------------------- pages

CSS = """
body{background:#FFFFFF;color:#111827}
html[data-theme="dark"] body,html.dark body,body.dark-mode{background:#0F172A;color:#F1F5F9}
@media (prefers-color-scheme:dark){html:not([data-theme]) body:not(.light-mode){background:#0F172A;color:#F1F5F9}}
.rl,.rl-dlg{--rl-ink:#111827;--rl-field:#6B7280;font-family:Amaranth,Arial,sans-serif;--rl-muted:#4B5563;--rl-line:#E3E6EB;--rl-link:#075985;--rl-chip:#F1F5F9;--rl-btn:#0369A1;--rl-btn-ink:#FFFFFF;color:var(--rl-ink)}
.rl{max-width:860px;margin:0 auto;padding:0 max(16px,env(safe-area-inset-right,0px)) 64px max(16px,env(safe-area-inset-left,0px))}
html[data-theme="dark"] :is(.rl,.rl-dlg),html.dark :is(.rl,.rl-dlg),body.dark-mode :is(.rl,.rl-dlg){--rl-field:#94A3B8;--rl-ink:#F1F5F9;--rl-muted:#CBD5E1;--rl-line:#2A3550;--rl-link:#7DD3FC;--rl-chip:#1E293B;--rl-btn:#7DD3FC;--rl-btn-ink:#0F172A}
@media (prefers-color-scheme:dark){html:not([data-theme]) body:not(.light-mode) :is(.rl,.rl-dlg){--rl-field:#94A3B8;--rl-ink:#F1F5F9;--rl-muted:#CBD5E1;--rl-line:#2A3550;--rl-link:#7DD3FC;--rl-chip:#1E293B;--rl-btn:#7DD3FC;--rl-btn-ink:#0F172A}}
.rl-key{color:var(--rl-muted);font-size:.95rem;line-height:1.6;margin:0 0 28px;max-width:68ch}
.rl-mod{border-top:1px solid var(--rl-line);padding:22px 0 6px}
.rl-mod h2{font:600 1.1rem/1.35 Inter,system-ui,sans-serif;margin:0 0 12px}
.rl-mod ol{margin:0;padding-left:1.3em;display:grid;gap:14px}
.rl-mod li{line-height:1.55}
.rl-cite{display:block}
.rl-acts{display:flex;flex-wrap:wrap;gap:6px 14px;margin-top:4px;font-size:.92rem}
.rl-acts a{color:var(--rl-link);text-decoration:underline;text-underline-offset:2px}
.rl-tag{font-size:.78rem;letter-spacing:.03em;text-transform:uppercase;color:var(--rl-muted);background:var(--rl-chip);border-radius:4px;padding:1px 6px}
.rl-ask{font:inherit;font-size:.92rem;color:var(--rl-link);background:none;border:0;padding:0;text-decoration:underline;text-underline-offset:2px;cursor:pointer}
.rl a:focus-visible,.rl button:focus-visible,.rl input:focus-visible,.rl textarea:focus-visible{outline:2px solid var(--rl-link);outline-offset:2px}
.rl-none{color:var(--rl-muted)}
.rl-dlg{border:1px solid var(--rl-line);border-radius:10px;padding:0;max-width:min(520px,calc(100vw - 32px));width:100%;background:var(--rl-bg,#FFFFFF);color:var(--rl-ink)}
html[data-theme="dark"] .rl-dlg,html.dark .rl-dlg,body.dark-mode .rl-dlg{--rl-bg:#0F172A}
.rl-dlg::backdrop{background:rgba(15,23,42,.55)}
.rl-dlg form{display:grid;gap:12px;padding:20px}
.rl-dlg h2{font:600 1.05rem/1.35 Inter,system-ui,sans-serif;margin:0}
.rl-dlg a{color:var(--rl-link)}
.rl-dlg p{margin:0;font-size:.92rem;line-height:1.5;color:var(--rl-muted)}
.rl-dlg label{display:grid;gap:4px;font-size:.9rem}
.rl-dlg input,.rl-dlg textarea{font:inherit;padding:8px 10px;border:1px solid var(--rl-field);border-radius:6px;background:transparent;color:var(--rl-ink)}
.rl-dlg .rl-row{display:flex;gap:10px;justify-content:flex-end;flex-wrap:wrap}
.rl-dlg button[type=submit]{background:var(--rl-btn);color:var(--rl-btn-ink);border:0;border-radius:6px;padding:9px 16px;font:600 .95rem Inter,system-ui,sans-serif;cursor:pointer}
.rl-dlg button[value=cancel]{background:none;border:1px solid var(--rl-line);color:var(--rl-ink);border-radius:6px;padding:9px 16px;font:inherit;cursor:pointer}
.rl-hp{position:absolute;left:-9999px}
.ph-eyebrow a{color:inherit;text-decoration:underline;text-underline-offset:2px}
.im-skip-link{position:absolute;left:-9999px;top:8px;z-index:1000;padding:8px 12px;border-radius:6px;background:#FFFFFF;color:#075985}
.im-skip-link:focus{left:16px}
"""

JS = """
(function () {
  var dlg = document.getElementById('rl-dlg'); if (!dlg) return;
  var form = dlg.querySelector('form'), note = document.getElementById('rl-status'), last = null;
  document.addEventListener('click', function (e) {
    var b = e.target.closest('[data-rl-ask]'); if (!b) return;
    last = b;
    form.reset(); note.textContent = '';
    form.elements.paper.value = b.getAttribute('data-rl-ask');
    document.getElementById('rl-dlg-paper').textContent = b.getAttribute('data-rl-ask');
    form.querySelector('[type=submit]').disabled = false;
    dlg.showModal();
  });
  dlg.addEventListener('close', function () { if (last) last.focus(); });
  form.addEventListener('submit', function (e) {
    if (e.submitter && e.submitter.value === 'cancel') return;
    e.preventDefault();
    var btn = form.querySelector('[type=submit]'); btn.disabled = true;
    fetch('/', { method: 'POST', headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: new URLSearchParams(new FormData(form)).toString() })
      .then(function (r) {
        if (!r.ok) throw new Error(r.status);
        note.textContent = 'Thank you. Your request has reached us, and we will reply by email.';
      })
      .catch(function () {
        btn.disabled = false;
        note.textContent = 'The request did not go through. Please try again, or write to hello@impactmojo.in with the title.';
      });
  });
})();
"""


def esc(s):
    return html.escape(s, quote=True)


def actions(r, course):
    a = []
    if r['access'] == 'open':
        a.append(f'<a href="{esc(r["url"])}" rel="noopener" target="_blank">Read it free</a>')
    elif r['access'] == 'library':
        f = r.get('free')
        if f:
            label = VERSION_LABEL.get(f.get('version'), 'Free copy')
            a.append(f'<a href="{esc(f["url"])}" rel="noopener" target="_blank">{label}</a>')
        a.append(f'<a href="{esc(r["url"])}" rel="noopener" target="_blank">Publisher page</a>')
        if not f:
            a.append('<span class="rl-tag">Subscription</span>')
            a.append(f'<button type="button" class="rl-ask" data-rl-ask="{esc(r["cite"])}">Request a copy</button>')
    else:
        a.append(f'<a href="{esc(r["url"])}" rel="noopener" target="_blank">Publisher page</a>')
        a.append('<span class="rl-tag">Book</span>')
    return '<span class="rl-acts">' + ''.join(a) + '</span>'


def page(cid, c):
    title = course_title(cid)
    fold = folder(cid)
    course_url = f'/courses/{fold}/' + ('' if COURSE_PAGE.get(cid, 'index.html') == 'index.html' else COURSE_PAGE[cid])
    rs = [r for m in c['modules'] for r in m['readings']]
    n_open = sum(1 for r in rs if r['access'] == 'open' or r.get('free'))
    n_req = sum(1 for r in rs if r['access'] == 'library' and not r.get('free'))
    n_book = sum(1 for r in rs if r['access'] == 'book')
    mods = []
    for m in c['modules']:
        if m['readings']:
            items = ''.join(f'<li><span class="rl-cite">{esc(r["cite"])}</span>{actions(r, cid)}</li>' for r in m['readings'])
            body = f'<ol>{items}</ol>'
        else:
            body = '<p class="rl-none">This module assigns no readings.</p>'
        mods.append(f'<section class="rl-mod" aria-labelledby="m{m["n"]}"><h2 id="m{m["n"]}">Module {m["n"]}. {esc(m["title"])}</h2>{body}</section>')
    desc = (f'Every reading assigned in {title}, module by module, with a free legal copy '
            f'where one exists. {n_open} of {len(rs)} readings can be read free.')
    form = '' if not n_req else f'''
<dialog id="rl-dlg" class="rl-dlg" aria-labelledby="rl-dlg-h">
  <form name="paper-request" method="post" data-netlify="true" netlify-honeypot="bot-field">
    <input type="hidden" name="form-name" value="paper-request">
    <input type="hidden" name="course" value="{esc(title)}">
    <input type="hidden" name="paper" value="">
    <p class="rl-hp" hidden><label>Leave this empty <input name="bot-field" tabindex="-1" autocomplete="off"></label></p>
    <h2 id="rl-dlg-h">Request a copy</h2>
    <p id="rl-dlg-paper"></p>
    <p>Tell us where to send it. We read every request and reply by email when we can share a copy.</p>
    <label>Your name <input name="name" required autocomplete="name" autofocus></label>
    <label>Email <input name="email" type="email" required autocomplete="email"></label>
    <label>Institution or organisation (optional) <input name="institution" autocomplete="organization"></label>
    <label>Anything we should know (optional) <textarea name="note" rows="3"></textarea></label>
    <p>We use these details only to answer this request. See the <a href="/privacy-policy.html">privacy policy</a>.</p>
    <p id="rl-status" role="status" aria-live="polite"></p>
    <div class="rl-row"><button type="submit" value="cancel" formmethod="dialog" formnovalidate>Close</button><button type="submit">Send request</button></div>
  </form>
</dialog>
<script>{JS}</script>'''
    meta = [f'<span>{len(rs)} reading{"" if len(rs) == 1 else "s"}</span>', f'<span>{n_open} free to read</span>']
    if n_req:
        meta.append(f'<span>{n_req} on request</span>')
    if n_book:
        meta.append(f'<span>{n_book} book{"" if n_book == 1 else "s"}</span>')
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Reading list: {esc(title)} | ImpactMojo</title>
<meta name="description" content="{esc(desc)}">
<meta name="robots" content="index, follow">
<link rel="icon" href="/assets/images/favicon.png" type="image/png">
<link rel="stylesheet" href="/css/fonts.css">
<link rel="stylesheet" href="/css/site-chrome.css">
<link rel="stylesheet" href="/css/plain-hero.css">
<style>{CSS}</style>
<script async src="/js/ga-load.js"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('consent','default',{{analytics_storage:(function(){{try{{var v=localStorage.getItem('im-analytics-consent');if(v==='granted'||v==='denied')return v}}catch(e){{}}return 'denied'}})(),ad_storage:'denied',ad_user_data:'denied',ad_personalization:'denied'}});
  gtag('config', 'G-JRCMEB9TBW');
</script>
</head>
<body>
<a href="#main-content" class="im-skip-link">Skip to content</a>
<main id="main-content" class="rl">
  <section class="ph ph--sky ph--tight">
    <span class="ph-bar" aria-hidden="true"></span>
    <p class="ph-eyebrow"><a href="{course_url}">{esc(title)}</a></p>
    <h1 class="ph-title">Reading list</h1>
    <p class="ph-lede">Every reading this course assigns, module by module, with the best free copy we could find.</p>
    <p class="ph-meta">{''.join(meta)}</p>
  </section>
  <p class="rl-key">A free copy is the published text, or the author's own manuscript held by a university repository, which has the same content without the journal's layout. A subscription reading opens at the publisher, where your library may give you access. If it does not, request a copy and we will reply by email. Books link to their publisher.</p>
  {''.join(mods)}
</main>{form}
<script src="/js/theme.js"></script>
<script defer src="/js/vendor/supabase-js-2.114.0.js"></script>
<script defer src="/js/state-manager.js"></script>
<script defer src="/js/config.js"></script>
<script defer src="/js/auth.js"></script>
<script src="/js/translate-sarvam.js" defer></script>
<script src="/js/site-chrome.js" defer></script>
</body>
</html>
'''


def _share():
    """The share-tag pass (scripts/build-social-tags.py), applied to each page as
    it is written, so a rebuild keeps the canonical, Open Graph and card tags."""
    import importlib.util as u
    sp = u.spec_from_file_location('build_social_tags', ROOT / 'scripts' / 'build-social-tags.py')
    m = u.module_from_spec(sp)
    sp.loader.exec_module(m)
    return m


def build(check):
    data = json.loads(DATA.read_text(encoding='utf-8'))
    share = _share()
    norm = lambda t: re.sub(r'\?v=[0-9a-f]+', '', t or '')   # stamp-assets.py adds these after the build
    stale = []
    for cid, c in data['courses'].items():
        out = ROOT / 'courses' / folder(cid) / 'readings.html'
        rel = str(out.relative_to(ROOT))
        text = share.apply(rel, page(cid, c))
        cur = out.read_text(encoding='utf-8') if out.exists() else None
        if norm(cur) == norm(text):
            continue
        if check:
            stale.append(rel)
        else:
            out.write_text(text, encoding='utf-8')
            print('wrote', rel)
    if check:
        if stale:
            print('FAIL: stale or missing reading lists, run scripts/build-reading-lists.py:\n  ' + '\n  '.join(stale))
            sys.exit(1)
        print(f'PASS: {len(data["courses"])} reading lists match data/course-readings.json')


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['--merge']:
        merge(a[1])
    elif a[:1] == ['--lookup']:
        lookup()
    else:
        build('--check' in a)
