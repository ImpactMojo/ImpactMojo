(function(){
  'use strict';

  var TRACKS = {"Data & Methods": {"courses": ["Excel for M&E", "R Programming", "Python Data Analysis", "EDA", "Bivariate Analysis", "Multivariate Analysis", "Data Visualization", "Stata Basics", "Survey Data Analysis"], "labs": ["Excel Lab", "R Lab", "Python Lab", "Visualization Lab"], "games": ["Lorenz Curve Game", "Sampling Strategy Game"], "resources": ["Handouts Library", "Method Guides"]}, "Economics & Policy": {"courses": ["Development Economics", "Cost-Effectiveness Analysis", "Impact Evaluation", "Program Evaluation", "Public Finance", "Poverty & Inequality", "Economic Policy Analysis", "Labor Markets"], "labs": ["CEA Lab", "Impact Evaluation Lab", "Policy Simulation Lab"], "games": ["Budget Trade-offs Game", "Targeting Game"], "resources": ["Policy Briefs", "Cost-Effectiveness Notes"]}, "Gender & Social Justice": {"courses": ["Gender & Development", "Women's Empowerment", "Gender Analysis Frameworks", "Data Feminism", "WEE", "Gender & Health", "Gender & Education", "Gandhi's Political Thought"], "labs": ["Gender Budgeting Lab", "Inclusive Survey Design Lab"], "games": ["Equity Trade-offs Game", "Bias Awareness Game"], "resources": ["Gender Analysis Sheets", "WEE Metrics Pack"]}, "Public Health & Climate": {"courses": ["Public Health 101", "Epidemiology 101", "Health Systems", "Nutrition & Food Systems", "WASH", "Climate & Health", "Adaptation & Resilience"], "labs": ["Epidemiology Lab", "Health Systems Lab", "Risk Mapping Lab"], "games": ["Outbreak Simulation Game", "Resource Allocation Game"], "resources": ["Health Indicators Pack", "Climate Resilience Toolkit"]}, "Political Philosophy & History": {"courses": ["Gandhi's Political Thought", "Political Economy 101", "Law and Constitution 101", "Caste 101", "Environmental Justice 101"], "labs": ["Policy and Advocacy Lab"], "games": [], "resources": ["Political Philosophy Reading List"]}};

  // Normalize text -> key
  function keyize(s){
    return (s||'').toLowerCase().replace(/[^a-z0-9\s]/g,'').replace(/\s+/g,' ').trim();
  }

  // Find nearest "card" container for an element (loose heuristic)
  function nearestCard(el){
    var e = el;
    for (var i=0;i<6 && e;i++){
      if (e.classList && (e.classList.contains('card') || e.classList.contains('course-card') ||
                          e.classList.contains('lab-card') || e.classList.contains('game-card') ||
                          e.classList.contains('premium-card') || e.classList.contains('resource-card'))) return e;
      e = e.parentElement;
    }
    return null;
  }

  // Build a very rich index of names -> hrefs from anchors and card containers
  function buildIndex(){
    var idxPrimary = {}; // prefers 101.impactmojo.in
    var idxOther   = {};

    var anchors = Array.prototype.slice.call(document.querySelectorAll('a[href]'));
    anchors.forEach(function(a){
      var href = a.getAttribute('href') || '';
      if (!href) return;
      var bucket = href.indexOf('101.impactmojo.in') !== -1 ? idxPrimary : idxOther;

      // direct anchor text and data-title
      [a.getAttribute('data-title'), a.textContent].forEach(function(t){
        if (!t) return;
        var k1 = keyize(t);
        if (k1) bucket[k1] = href;
      });

      // if anchor sits in a card with a title element, index those too
      var card = nearestCard(a);
      if (card){
        var heading = card.querySelector('h1,h2,h3,h4,h5,.title,[data-title],[data-name]');
        if (heading){
          var k2 = keyize(heading.getAttribute('data-title') || heading.getAttribute('data-name') || heading.textContent);
          if (k2) bucket[k2] = href;
        }
      }
    });

    // Also index elements that carry titles but are not anchors
    var titled = Array.prototype.slice.call(document.querySelectorAll('[data-title],[data-name],[data-course]'));
    titled.forEach(function(el){
      var text = el.getAttribute('data-title') || el.getAttribute('data-name') || el.getAttribute('data-course');
      var k = keyize(text);
      if (!k) return;
      // find an anchor within the same card/container
      var host = nearestCard(el) || el;
      var a = host.querySelector('a[href]');
      if (a){
        var href = a.getAttribute('href') || '';
        if (!href) return;
        var bucket = href.indexOf('101.impactmojo.in') !== -1 ? idxPrimary : idxOther;
        bucket[k] = href;
      }
    });

    return {primary: idxPrimary, other: idxOther};
  }

  function resolve(idx, name){
    var k = keyize(name);
    if (!k) return null;
    if (idx.primary[k]) return idx.primary[k];
    if (idx.other[k])   return idx.other[k];
    // partial contains scan
    for (var key in idx.primary){ if (key.indexOf(k) !== -1) return idx.primary[key]; }
    for (var key2 in idx.other){ if (key2.indexOf(k) !== -1) return idx.other[key2]; }
    return null;
  }

  
  function chips(list, idx){
    var map = (window.IMPACTMOJO && window.IMPACTMOJO.urlMap) ? window.IMPACTMOJO.urlMap : {};
    var frag = document.createDocumentFragment();
    list.forEach(function(name){
      var span = document.createElement('span');
      var key = (name||'').toLowerCase();
      var href = map[key] || resolve(idx, name);
      if (href){
        var a=document.createElement('a'); 
        a.href=href; a.target='_blank'; a.rel='noopener'; a.textContent=name; 
        a.className='imx-btn';
        span.appendChild(a);
      } else {
        span.className='imx-chip imx-disabled';
        span.textContent = name;
      }
      frag.appendChild(span);
    });
    return frag;
  }

  function openTrackModal(trackName){
    var d = TRACKS[trackName]; if (!d) return;
    document.getElementById('imxTrackTitle').textContent = trackName;
    var idx = buildIndex();
    var c=document.getElementById('imxRowCourses');  c.innerHTML=''; c.appendChild(chips(d.courses, idx));
    var l=document.getElementById('imxRowLabs');     l.innerHTML=''; l.appendChild(chips(d.labs, idx));
    var g=document.getElementById('imxRowGames');    g.innerHTML=''; g.appendChild(chips(d.games, idx));
    var r=document.getElementById('imxRowResources');r.innerHTML=''; r.appendChild(chips(d.resources, idx));
    document.getElementById('imxTrackModal').style.display='block';
  }

  document.addEventListener('DOMContentLoaded', function(){
    Array.prototype.slice.call(document.querySelectorAll('.imx-track-card')).forEach(function(card){
      card.addEventListener('click', function(){ openTrackModal(card.getAttribute('data-track')); });
    });
  });

  window.addEventListener('click', function(e){
    var modal=document.getElementById('imxTrackModal');
    if (modal && e.target===modal) modal.style.display='none';
  });

  // Filter/tag injector for existing modals
  var ITEM_SELECTORS = ['.modal-item','.course-card','.lab-card','.game-card','.premium-card','.resource-card','.card','.grid-item','[data-track]'];
  function injectFilter(modal){
    if (!modal || modal.querySelector('.imx-filterbar')) return;
    var body = modal.querySelector('.modal-body') || modal;
    var items=[]; ITEM_SELECTORS.forEach(function(sel){ body.querySelectorAll(sel).forEach(function(el){ items.push(el); }); });
    if (!items.length) return;
    var bar=document.createElement('div'); bar.className='imx-filterbar';
    var input=document.createElement('input'); input.type='search'; input.placeholder='Filter by keyword or tag'; bar.appendChild(input);
    var tagSet={}; items.forEach(function(el){
      (el.getAttribute('data-tag')||'').split(/[\\s,]+/).forEach(function(t){ if(t) tagSet[t]=true; });
      (el.getAttribute('data-tags')||'').split(/[\\s,]+/).forEach(function(t){ if(t) tagSet[t]=true; });
    });
    Object.keys(tagSet).slice(0,20).forEach(function(t){
      var chip=document.createElement('span'); chip.className='imx-chip imx-tag'; chip.textContent=t;
      chip.addEventListener('click', function(){ input.value=t; apply(); });
      bar.appendChild(chip);
    });
    function apply(){
      var q=(input.value||'').toLowerCase().trim();
      items.forEach(function(el){
        var text=(el.innerText||'').toLowerCase();
        var tags=((el.getAttribute('data-tag')||'')+' '+(el.getAttribute('data-tags')||'')).toLowerCase();
        if(!q || text.indexOf(q)!==-1 || tags.indexOf(q)!==-1) el.classList.remove('imx-hidden');
        else el.classList.add('imx-hidden');
      });
    }
    input.addEventListener('input', apply);
    body.insertBefore(bar, body.firstChild);
  }
  var obs=new MutationObserver(function(){ document.querySelectorAll('.modal').forEach(injectFilter); });
  obs.observe(document.body, {childList:true, subtree:true});
  document.addEventListener('DOMContentLoaded', function(){ document.querySelectorAll('.modal').forEach(injectFilter); });

  window.IMPACTMOJO = window.IMPACTMOJO || {};
  window.IMPACTMOJO.openTrack = openTrackModal;
})();
