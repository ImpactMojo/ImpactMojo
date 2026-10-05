#!/usr/bin/env python3
"""Advisory scan for the language tells the owner's style rules ban.

Not a CI gate: several banned words are real terms of the field (empowerment,
robust standard errors, leverage points, paradigm in Kuhn's sense,
gender-transformative programming), so a hit is a place to read, not an error.
It lists banned words, banned phrases and negative-parallelism constructions in
reader-facing text, per page, worst first. Run from the repository root:

    python3 scripts/scan-ai-language.py

The scan cannot measure whether prose is plain, persuasive or explanatory.
That needs a reader.
"""
import os,re,sys,json,collections,html
WORDS=r"delv\w*|certainly|utilis\w*|utiliz\w*|leverag\w*|robust\w*|streamlin\w*|harness\w*|foster\w*|enhanc\w*|testament|pivotal|intricate|intricacies|crucial\w*|transformative|groundbreaking|tapestry|landscape\w*|paradigm\w*|synerg\w*|architecture|liminal|palpable|ineffable|visceral|register|ledger|showcas\w*|meticulous\w*|notabl[ey]|noteworthy|commendable|versatil\w*|seamless\w*|multifaceted|nuanced?|holistic\w*|invaluable|unparalleled|garner\w*|bolster\w*|elucidat\w*|interplay|underpin\w*|solidif\w*|vibrant|bustling|nestled|picturesque|breathtaking|stunning\w*|boasts?|renowned|must-visit|indelible|poignant|captivat\w*|evocative|embark\w*|navigat\w*|unlock\w*|unleash\w*|empower\w*|elevat\w*|amplif\w*|resonat\w*|evok\w*|facilitat\w*|spearhead\w*|realm|domain|arena|myriad|plethora|sphere|genuine\w*|honestly|truly|arguably"
PHR=[r"rich (cultural|tapestry|history|heritage)",r"enduring legacy",r"plays? an? (vital|key|significant|crucial) role",r"leaves? a lasting impact",r"watershed moment",r"turning point",r"deeply rooted",r"unwavering commitment",r"a stark reminder",r"in today's (fast-paced )?world",r"in the digital age",r"in an era of",r"ever-evolving",r"at the intersection of",r"when it comes to",r"needless to say",r"it'?s (important|worth) (to )?(note|remember)",r"it is (important|worth) (to )?(note|remember)",r"look no further",r"hidden gem",r"embark on",r"navigate the complexit",r"unlock the (power|potential)",r"pave the way",r"shed(s|ding)? light on",r"gain valuable insights?",r"at the forefront",r"here'?s the (kicker|thing|deal)",r"let'?s (break|unpack|dive)",r"think of it as",r"imagine a world",r"the question is not whether",r"(moreover|furthermore|additionally|consequently),",r"in conclusion",r"to sum up",r"at the end of the day",r"all in all",r"(cutting-edge|game-chang\w+|deep dive|dive (in|into)|journey)"]
NP=[r"\b(it'?s|it is|this is|that'?s|that is|they'?re|these are|isn'?t|aren'?t|wasn'?t)\s+not\s+(just|only|merely|simply)?\s*[^.;:!?]{2,70}[,;]?\s+(it'?s|but|it is|they'?re|rather|instead)",r"\bnot only\b[^.]{3,90}\bbut (also|\w+)",r"\bnot just\b[^.]{3,60}\bbut\b",r"\bmore than (just|merely|simply)\b",r"\bless about\b[^.]{3,60}\bmore about\b",r"\bnot\s+[a-z\- ]{2,40},\s+but\b",r"\bnever\s+[^.]{3,50},\s+(always|but)\b"]
wre=re.compile(r'\b(?:'+WORDS+r')\b',re.I)
pre=[re.compile(p,re.I) for p in PHR];nre=[re.compile(p,re.I) for p in NP]
BLOCK=re.compile(r'<(script|style|pre|code|textarea|svg)\b[^>]*>.*?</\1\s*>',re.S|re.I)
def text(h):
    h=re.sub(r'<!--.*?-->','',h,flags=re.S);h=BLOCK.sub(' ',h)
    h=re.sub(r'<(nav|header|footer)\b.*?</\1>',' ',h,flags=re.S|re.I)
    return html.unescape(re.sub(r'<[^>]+>',' ',h))
def scan(t):
    w=collections.Counter(m.group(0).lower() for m in wre.finditer(t))
    ph=collections.Counter();ng=0;ex=[]
    for r in pre:
        for m in r.finditer(t): ph[m.group(0).lower()]+=1
    for r in nre:
        for m in r.finditer(t):
            ng+=1
            if len(ex)<2: ex.append(m.group(0)[:100])
    return w,ph,ng,ex
if __name__=='__main__':
    skip={'Backups','node_modules','.git','i18n','tests','archive','BookSummaries'}
    rows=[];W=collections.Counter();P=collections.Counter();tot=0
    for r,d,fs in os.walk('.'):
        d[:]=[x for x in d if x not in skip and not x.startswith('.')]
        for f in fs:
            if not f.endswith('.html'):continue
            p=os.path.join(r,f);t=text(open(p,encoding='utf-8').read())
            wc=len(t.split())
            if wc<30:continue
            w,ph,ng,ex=scan(t);n=sum(w.values())+sum(ph.values())+ng
            W.update(w);P.update(ph);tot+=n
            rows.append((n,round(1000*n/wc,1),wc,p,ng))
    rows.sort(reverse=True)
    print('pages',len(rows),'hits',tot)
    print('top words',W.most_common(25));print('top phrases',P.most_common(15))
    print('pages with >=1 hit',sum(1 for x in rows if x[0]),' >=10:',sum(1 for x in rows if x[0]>=10))
    print('top 25 by hits');[print(x) for x in rows[:25]]
