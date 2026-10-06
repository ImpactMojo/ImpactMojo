/* Code Studio engine: shared by every page under /code/.
 *
 * Runs code in the visitor's browser, nothing on a server:
 *   R       WebR (webr.r-wasm.org), packages from repo.r-wasm.org
 *   Python  Pyodide (cdn.jsdelivr.net/pyodide)
 *   SQL     sql.js, which is SQLite compiled to WebAssembly (cdnjs)
 *   Shiny   not run here: the cell opens the app in Posit's Shinylive editor
 *
 * Each engine downloads once, on the first Run, and is reused by every cell
 * on the page. Datasets listed in <body data-datasets="survey,..."> are
 * fetched from /code/data/<name>.csv and placed in each engine as a file
 * (survey.csv) and, for SQL, as a table (survey).
 *
 * Cell markup (written by scripts/build-code-studio.py):
 *   <div class="code-cell" data-lang="r|py|sql|shiny-r|shiny-py" data-pkgs="...">
 *   <div class="code-cell" data-r="..." data-py="..." data-pkgs="...">   (R and Python tabs)
 */
(function () {
    'use strict';

    var WEBR_VERSION = 'latest';
    var PYODIDE_VERSION = 'v0.26.4';
    var SQLJS_VERSION = '1.10.3';
    var LZ_URL = 'https://cdnjs.cloudflare.com/ajax/libs/lz-string/1.5.0/lz-string.min.js';

    /* ---------- theme ---------- */
    function applyTheme(theme) {
        var root = document.documentElement;
        if (theme === 'light' || theme === 'dark') root.setAttribute('data-theme', theme);
        else root.removeAttribute('data-theme');
        document.querySelectorAll('.im-theme-btn').forEach(function (b) {
            b.classList.toggle('active', b.dataset.theme === theme);
        });
    }
    var savedTheme = 'system';
    try { savedTheme = localStorage.getItem('impactmojo-theme') || 'system'; } catch (e) {}
    applyTheme(savedTheme);
    document.querySelectorAll('.im-theme-btn').forEach(function (btn) {
        btn.addEventListener('click', function () {
            try { localStorage.setItem('impactmojo-theme', btn.dataset.theme); } catch (e) {}
            applyTheme(btn.dataset.theme);
        });
    });

    /* ---------- tabs (lesson pages) ---------- */
    var tabBtns = document.querySelectorAll('.tab-btn');
    var panels = document.querySelectorAll('.tab-panel');
    var visited = { 0: true };
    function switchTab(idx) {
        visited[idx] = true;
        tabBtns.forEach(function (b, i) {
            b.classList.toggle('active', i === idx);
            b.classList.toggle('completed', i !== idx && visited[i]);
            b.setAttribute('aria-selected', i === idx ? 'true' : 'false');
        });
        panels.forEach(function (p, i) { p.classList.toggle('active', i === idx); });
        var fill = document.getElementById('progressFill');
        if (fill && panels.length) fill.style.width = ((idx + 1) / panels.length * 100) + '%';
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }
    window.switchTab = switchTab;
    tabBtns.forEach(function (b, i) { b.addEventListener('click', function () { switchTab(i); }); });
    document.querySelectorAll('[data-goto]').forEach(function (b) {
        b.addEventListener('click', function () { switchTab(parseInt(b.dataset.goto, 10)); });
    });
    if (panels.length) switchTab(0);

    /* ---------- helpers ---------- */
    function loadScript(src) {
        return new Promise(function (resolve, reject) {
            var s = document.createElement('script');
            s.src = src; s.onload = resolve;
            s.onerror = function () { reject(new Error('Failed to load ' + src)); };
            document.head.appendChild(s);
        });
    }
    function bitmapToDataURL(bitmap) {
        var c = document.createElement('canvas');
        c.width = bitmap.width; c.height = bitmap.height;
        c.getContext('2d').drawImage(bitmap, 0, 0);
        return c.toDataURL('image/png');
    }

    /* ---------- datasets ---------- */
    var DATASETS = (document.body.dataset.datasets || '').split(',')
        .map(function (s) { return s.trim(); }).filter(Boolean);
    var dataPromise = null;
    function getData() {
        if (!dataPromise) {
            dataPromise = Promise.all(DATASETS.map(function (name) {
                return fetch('/code/data/' + name + '.csv').then(function (r) {
                    if (!r.ok) throw new Error('Failed to fetch dataset ' + name);
                    return r.text();
                }).then(function (text) { return { name: name, text: text }; });
            }));
        }
        return dataPromise;
    }
    function parseCSV(text) {
        var rows = [], row = [], field = '', q = false;
        for (var i = 0; i < text.length; i++) {
            var c = text[i];
            if (q) {
                if (c === '"' && text[i + 1] === '"') { field += '"'; i++; }
                else if (c === '"') q = false;
                else field += c;
            } else if (c === '"') q = true;
            else if (c === ',') { row.push(field); field = ''; }
            else if (c === '\n' || c === '\r') {
                if (c === '\r' && text[i + 1] === '\n') i++;
                row.push(field); field = '';
                if (row.length > 1 || row[0] !== '') rows.push(row);
                row = [];
            } else field += c;
        }
        if (field !== '' || row.length) { row.push(field); rows.push(row); }
        return rows;
    }

    /* ---------- R ---------- */
    var webrPromise = null, rInstalled = {};
    function getWebR() {
        if (!webrPromise) {
            webrPromise = (async function () {
                var mod = await import('https://webr.r-wasm.org/' + WEBR_VERSION + '/webr.mjs');
                var webR = new mod.WebR();
                await webR.init();
                var data = await getData();
                for (var i = 0; i < data.length; i++) {
                    await webR.FS.writeFile('/home/web_user/' + data[i].name + '.csv',
                        new TextEncoder().encode(data[i].text));
                }
                if (data.some(function (d) { return d.name === 'survey'; })) {
                    await webR.evalRVoid('SURVEY_CSV <- paste(readLines("survey.csv"), collapse = "\\n")');
                }
                return webR;
            })();
        }
        return webrPromise;
    }
    async function runR(code, pkgs) {
        var webR = await getWebR();
        var need = (pkgs || '').split(',').map(function (s) { return s.trim(); })
            .filter(function (p) { return p && !rInstalled[p]; });
        if (need.length) {
            await webR.installPackages(need, { quiet: true });
            need.forEach(function (p) { rInstalled[p] = true; });
        }
        var shelter = await new webR.Shelter();
        try {
            var cap = await shelter.captureR(code, {
                withAutoprint: true,
                captureGraphics: { width: 640, height: 420 }
            });
            var text = cap.output.filter(function (o) { return o.type === 'stdout' || o.type === 'stderr'; })
                .map(function (o) { return o.data; }).join('\n');
            var images = (cap.images || []).map(bitmapToDataURL);
            return { text: text, images: images };
        } finally { shelter.purge(); }
    }

    /* ---------- Python ---------- */
    var pyodidePromise = null;
    function getPyodide() {
        if (!pyodidePromise) {
            pyodidePromise = (async function () {
                var base = 'https://cdn.jsdelivr.net/pyodide/' + PYODIDE_VERSION + '/full/';
                await loadScript(base + 'pyodide.js');
                var py = await window.loadPyodide({ indexURL: base });
                var data = await getData();
                data.forEach(function (d) { py.FS.writeFile(d.name + '.csv', d.text); });
                if (data.some(function (d) { return d.name === 'survey'; })) {
                    py.globals.set('SURVEY_CSV', data.filter(function (d) { return d.name === 'survey'; })[0].text);
                }
                await py.runPythonAsync(
                    'import io, base64, warnings\n' +
                    'warnings.filterwarnings("ignore", category=DeprecationWarning)\n' +
                    'def show(fig=None):\n' +
                    '    import matplotlib.pyplot as plt\n' +
                    '    fig = fig or plt.gcf()\n' +
                    '    b = io.BytesIO(); fig.savefig(b, format="png", dpi=110, bbox_inches="tight"); plt.close(fig)\n' +
                    '    print("IMG:" + base64.b64encode(b.getvalue()).decode())\n'
                );
                return py;
            })();
        }
        return pyodidePromise;
    }
    async function runPython(code, pkgs) {
        var py = await getPyodide();
        if (pkgs) await py.loadPackage(pkgs.split(',').map(function (s) { return s.trim(); }).filter(Boolean));
        var buf = '';
        py.setStdout({ batched: function (s) { buf += s + '\n'; } });
        py.setStderr({ batched: function (s) { buf += s + '\n'; } });
        var result = await py.runPythonAsync(code);
        if (!buf.trim() && result !== undefined && result !== null) {
            buf = String(result);
            if (result && typeof result.destroy === 'function') result.destroy();
        }
        var images = [], kept = [];
        buf.split('\n').forEach(function (ln) {
            if (ln.indexOf('IMG:') === 0) images.push('data:image/png;base64,' + ln.slice(4));
            else kept.push(ln);
        });
        return { text: kept.join('\n').replace(/\n+$/, ''), images: images };
    }

    /* ---------- SQL (SQLite via sql.js) ---------- */
    var sqlPromise = null;
    function getSQL() {
        if (!sqlPromise) {
            sqlPromise = (async function () {
                var base = 'https://cdnjs.cloudflare.com/ajax/libs/sql.js/' + SQLJS_VERSION + '/';
                await loadScript(base + 'sql-wasm.js');
                var SQL = await window.initSqlJs({ locateFile: function (f) { return base + f; } });
                var db = new SQL.Database();
                var data = await getData();
                data.forEach(function (d) {
                    var rows = parseCSV(d.text);
                    var head = rows[0], body = rows.slice(1);
                    var numeric = head.map(function (_, j) {
                        return body.every(function (r) { return r[j] === '' || !isNaN(Number(r[j])); });
                    });
                    var cols = head.map(function (h, j) { return '"' + h + '" ' + (numeric[j] ? 'REAL' : 'TEXT'); });
                    db.run('CREATE TABLE "' + d.name + '" (' + cols.join(', ') + ')');
                    var stmt = db.prepare('INSERT INTO "' + d.name + '" VALUES (' + head.map(function () { return '?'; }).join(',') + ')');
                    body.forEach(function (r) {
                        stmt.run(r.map(function (v, j) { return v === '' ? null : (numeric[j] ? Number(v) : v); }));
                    });
                    stmt.free();
                });
                return db;
            })();
        }
        return sqlPromise;
    }
    async function runSQL(code) {
        var db = await getSQL();
        var results = db.exec(code);
        return { tables: results, text: results.length ? '' : '(statement ran, no rows returned)', images: [] };
    }
    function renderTable(res) {
        var t = document.createElement('table');
        var tr = document.createElement('tr');
        res.columns.forEach(function (c) { var th = document.createElement('th'); th.textContent = c; tr.appendChild(th); });
        t.appendChild(tr);
        res.values.slice(0, 200).forEach(function (row) {
            var r = document.createElement('tr');
            row.forEach(function (v) {
                var td = document.createElement('td');
                td.textContent = (v === null ? 'NULL' : (typeof v === 'number' ? String(Math.round(v * 10000) / 10000) : v));
                r.appendChild(td);
            });
            t.appendChild(r);
        });
        return t;
    }

    /* ---------- Shiny (opens in Shinylive) ---------- */
    var lzPromise = null;
    function getLZ() {
        if (!lzPromise) lzPromise = loadScript(LZ_URL).then(function () { return window.LZString; });
        return lzPromise;
    }
    async function shinyURL(code, lang) {
        var LZ = await getLZ();
        var file = lang === 'shiny-py' ? 'app.py' : 'app.R';
        var payload = LZ.compressToEncodedURIComponent(JSON.stringify([{ name: file, content: code }]));
        return 'https://shinylive.io/' + (lang === 'shiny-py' ? 'py' : 'r') + '/editor/#code=' + payload;
    }

    /* ---------- wire each cell ---------- */
    var LABEL = { r: 'R', py: 'Python', sql: 'SQL', 'shiny-r': 'Shiny (R)', 'shiny-py': 'Shiny (Python)' };
    function el(tag, cls, text) {
        var e = document.createElement(tag);
        if (cls) e.className = cls;
        if (text !== undefined) e.textContent = text;
        return e;
    }
    document.querySelectorAll('.code-cell').forEach(function (cell) {
        var dual = cell.hasAttribute('data-r') && cell.hasAttribute('data-py');
        var lang = dual ? 'r' : (cell.dataset.lang || 'r');
        var input = cell.querySelector('.code-input');
        var original = input.value;
        function snippet(l) { return dual ? (l === 'py' ? cell.dataset.py : cell.dataset.r) : original; }

        var tabsRow = el('div', 'cell-tabs');
        if (dual) {
            ['r', 'py'].forEach(function (l) {
                var t = el('button', 'cell-tab' + (l === lang ? ' active' : ''), LABEL[l]);
                t.type = 'button'; t.dataset.lang = l;
                t.addEventListener('click', function () {
                    if (input.value === snippet(lang)) input.value = snippet(l);
                    lang = l;
                    tabsRow.querySelectorAll('.cell-tab').forEach(function (x) { x.classList.toggle('active', x === t); });
                });
                tabsRow.appendChild(t);
            });
        } else {
            tabsRow.appendChild(el('span', 'cell-lang-badge', LABEL[lang] || lang));
        }
        tabsRow.appendChild(el('span', 'cell-lang-note', 'editable'));
        cell.insertBefore(tabsRow, input);

        var actions = el('div', 'cell-actions');
        var runBtn = el('button', 'run-btn', lang.indexOf('shiny') === 0 ? 'Open in Shinylive' : 'Run');
        runBtn.type = 'button';
        var resetBtn = el('button', 'reset-btn', 'Reset');
        resetBtn.type = 'button';
        var status = el('span', 'run-status');
        status.setAttribute('aria-live', 'polite');
        actions.appendChild(runBtn); actions.appendChild(resetBtn); actions.appendChild(status);
        var output = el('pre', 'code-output');
        cell.appendChild(actions);
        cell.appendChild(output);

        resetBtn.addEventListener('click', function () {
            input.value = snippet(lang);
            output.classList.remove('show'); status.textContent = ''; status.classList.remove('err');
        });

        runBtn.addEventListener('click', async function () {
            var code = input.value;
            if (lang.indexOf('shiny') === 0) {
                var w = window.open('about:blank', '_blank');
                try {
                    var url = await shinyURL(code, lang);
                    if (w) { w.opener = null; w.location = url; } else { window.location = url; }
                } catch (e) {
                    if (w) w.close();
                    status.classList.add('err');
                    status.textContent = 'Could not load the Shinylive link builder. Check your connection.';
                }
                return;
            }
            runBtn.disabled = true;
            status.classList.remove('err');
            status.textContent = 'Running ' + (LABEL[lang] || lang) + '...';
            try {
                var res = lang === 'r' ? await runR(code, cell.dataset.pkgs)
                        : lang === 'py' ? await runPython(code, cell.dataset.pypkgs || cell.dataset.pkgs)
                        : await runSQL(code);
                output.textContent = '';
                output.appendChild(el('span', 'out-label', (LABEL[lang] || lang) + ' output'));
                if (res.tables && res.tables.length) res.tables.forEach(function (t) { output.appendChild(renderTable(t)); });
                if (res.text) output.appendChild(document.createTextNode(res.text));
                else if (!(res.images && res.images.length) && !(res.tables && res.tables.length)) {
                    output.appendChild(document.createTextNode('(ran with no printed output)'));
                }
                (res.images || []).forEach(function (src) {
                    var img = el('img'); img.src = src; img.alt = 'Plot output';
                    output.appendChild(img);
                });
                output.classList.add('show');
                status.textContent = 'done';
            } catch (e) {
                status.classList.add('err'); status.textContent = 'error';
                output.textContent = '';
                output.appendChild(el('span', 'out-label', 'Error'));
                var msg = (e && e.message) ? e.message : String(e);
                if (/Failed to (fetch|load)|NetworkError|import/i.test(msg)) {
                    msg += '\n\n(Could not download the language engine, a package or the dataset. ' +
                           'Check your internet connection and run again; the first run fetches the engine once.)';
                }
                output.appendChild(document.createTextNode(msg));
                output.classList.add('show');
            } finally { runBtn.disabled = false; }
        });
    });
})();
