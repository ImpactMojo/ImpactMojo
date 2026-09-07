import { chromium } from 'playwright-core';
const B='http://localhost:8080';
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
for (const w of [390,768,1280]){
  const c=await b.newContext({viewport:{width:w,height:1000}});
  await c.route('**/*', r=>r.request().url().startsWith(B)?r.continue():r.abort());
  const p=await c.newPage();
  await p.goto(B+'/fundamentals/results-chain.html',{waitUntil:'domcontentloaded'});
  await p.waitForTimeout(700);
  const r=await p.evaluate(()=>{
    const li=document.querySelector('#rcLegend li');
    const items=[...li.childNodes].map(n=>n.nodeType===3?'TEXTNODE("'+n.textContent.trim().slice(0,20)+'")':n.tagName+'.'+n.className);
    // the anonymous grid item's rendered width: measure via a Range around the text node
    const tn=[...li.childNodes].find(n=>n.nodeType===3&&n.textContent.trim());
    let box=null;
    if(tn){const rg=document.createRange();rg.selectNodeContents(tn);const r=rg.getBoundingClientRect();box={w:Math.round(r.width),h:Math.round(r.height)};}
    return {items, liW:Math.round(li.getBoundingClientRect().width), liH:Math.round(li.getBoundingClientRect().height),
      noteBox:box, cols:getComputedStyle(li).gridTemplateColumns};
  });
  console.log(`${String(w).padStart(4)}px  li=${r.liW}x${r.liH}  cols=${r.cols}  noteBox=${r.noteBox?r.noteBox.w+'x'+r.noteBox.h:'-'}`);
  console.log(`        children: ${r.items.join(' | ')}`);
  await c.close();
}
await b.close();
