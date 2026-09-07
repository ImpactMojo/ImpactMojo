import { chromium } from 'playwright-core';
const B='http://localhost:8080';
const PAGES=['wheel','ladder','power-cube','capabilities','gender-needs','livelihoods','social-model','who-counts','results-chain','empowerment','index'];
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
let total=0;
for (const pg of PAGES){
  const c=await b.newContext({viewport:{width:1280,height:1000}});
  await c.route('**/*', r=>r.request().url().startsWith(B)?r.continue():r.abort());
  const p=await c.newPage();
  await p.goto(`${B}/fundamentals/${pg}.html`,{waitUntil:'domcontentloaded'});
  await p.waitForTimeout(800);
  const hits=await p.evaluate(()=>{
    // A grid or flex container with BOTH element children and a non-empty bare
    // text node child: the text becomes an anonymous item and is laid out as a
    // cell, which is almost never what was meant.
    const out=[];
    for (const el of document.querySelectorAll('*')){
      const d=getComputedStyle(el).display;
      if(!/grid|flex/.test(d)) continue;
      const els=[...el.children].length;
      const bare=[...el.childNodes].filter(n=>n.nodeType===3&&n.textContent.trim());
      if(els&&bare.length){
        const rg=document.createRange(); rg.selectNodeContents(bare[0]);
        const r=rg.getBoundingClientRect();
        out.push({sel:el.tagName.toLowerCase()+'.'+(el.className||'').toString().split(' ')[0], d,
          els, text:bare[0].textContent.trim().slice(0,30), w:Math.round(r.width), h:Math.round(r.height)});
      }
    }
    return out;
  });
  if(hits.length){ total+=hits.length; console.log('## '+pg);
    hits.forEach(h=>console.log(`   ${h.sel} display:${h.d} elemChildren=${h.els} bareText ${h.w}x${h.h} "${h.text}"`)); }
  await c.close();
}
console.log(total? `\n${total} anonymous grid/flex items` : '\nnone found');
await b.close();
