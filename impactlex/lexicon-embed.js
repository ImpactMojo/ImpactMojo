/**
 * ImpactLex lexicon embed helper.
 *
 * Course lexicon pages can use this to progressively enhance toward the shared
 * glossary. Drop a tagged `<div data-impactlex-banner data-course="mel">` on
 * the page and this script will render a banner linking into the filtered
 * main ImpactLex view.
 *
 * Optional: for pages that want to fully migrate to the shared data source,
 * call `window.ImpactLexEmbed.render({ course, container })` and pass a
 * container element. This will fetch the snapshot and render cards scoped
 * to that course — replacing any hardcoded data.
 */

(function (global) {
  const SNAPSHOT_URL = '/impactlex/data/seed-snapshot.json';

  function fetchSnapshot() {
    if (global.__impactlexSnapshotPromise) return global.__impactlexSnapshotPromise;
    global.__impactlexSnapshotPromise = fetch(SNAPSHOT_URL).then((r) => r.json());
    return global.__impactlexSnapshotPromise;
  }

  function esc(s) {
    return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;').replace(/'/g, '&#39;');
  }

  async function renderBanners() {
    const banners = document.querySelectorAll('[data-impactlex-banner]');
    if (!banners.length) return;
    let data;
    try { data = await fetchSnapshot(); } catch { return; }
    const total = (data.terms || []).length;
    banners.forEach((el) => {
      const course = el.getAttribute('data-course') || '';
      const courseTerms = (data.terms || []).filter((t) => (t.courses || []).includes(course));
      const href = course ? `/impactlex/?course=${encodeURIComponent(course)}` : '/impactlex/';
      el.innerHTML = `
        <a href="${href}" style="display:flex;align-items:center;gap:1rem;padding:1rem 1.25rem;background:linear-gradient(135deg, rgba(14, 165, 233, 0.08), rgba(99, 102, 241, 0.08));border:1px solid var(--border-color, #e2e8f0);border-radius:12px;text-decoration:none;color:inherit;margin:1rem auto;max-width:900px;transition:all 0.2s ease;">
          <div style="width:40px;height:40px;border-radius:10px;background:linear-gradient(135deg, #0284C7, #4338CA);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
            <svg viewBox="0 0 24 24" width="20" height="20" stroke="white" fill="none" stroke-width="2" aria-hidden="true"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
          </div>
          <div style="flex:1;">
            <div style="font-family:'Inter',sans-serif;font-weight:600;font-size:1rem;">Looking for more development terms?</div>
            <div style="color:#64748B;font-size:0.9rem;margin-top:0.15rem;">This course has ${courseTerms.length ? `<strong>${courseTerms.length} terms</strong> in ` : ''}<strong>ImpactLex</strong> — ${total} terms across all ImpactMojo courses.</div>
          </div>
          <div style="color:#0284C7;font-weight:600;font-size:0.9rem;white-space:nowrap;">Open ImpactLex →</div>
        </a>
      `;
    });
  }

  async function render({ course, container }) {
    if (!container) return;
    let data;
    try { data = await fetchSnapshot(); } catch {
      container.innerHTML = '<p style="color:#64748B;padding:2rem;text-align:center;">Could not load glossary. Please check your connection.</p>';
      return;
    }
    const terms = (data.terms || []).filter((t) => !course || (t.courses || []).includes(course));
    if (!terms.length) {
      container.innerHTML = '<p style="color:#64748B;padding:2rem;text-align:center;">No terms for this course.</p>';
      return;
    }
    container.innerHTML = terms.map((t) => `
      <a class="lexicon-embed-card" href="/impactlex/term.html?id=${encodeURIComponent(t.id)}" style="display:block;background:var(--card-bg,#fff);border:1px solid var(--border-color,#e2e8f0);border-radius:12px;padding:1rem 1.25rem;text-decoration:none;color:inherit;">
        <div style="font-family:'Inter',sans-serif;font-weight:700;font-size:1.05rem;margin-bottom:0.25rem;">${esc(t.term)}${t.acronym ? ` <span style="color:#64748B;font-weight:500;font-size:0.85rem;">(${esc(t.acronym)})</span>` : ''}</div>
        <div style="color:#64748B;font-size:0.85rem;line-height:1.55;">${esc(String(t.definition || '').slice(0, 180))}${(t.definition || '').length > 180 ? '…' : ''}</div>
      </a>
    `).join('');
  }

  global.ImpactLexEmbed = { render, renderBanners, fetchSnapshot };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', renderBanners);
  } else {
    renderBanners();
  }
})(window);
