(function(){
  // Prevent double-install
  if (window.__mojiniFlags?.faqBankV1) return;
  (window.__mojiniFlags || (window.__mojiniFlags = {})).faqBankV1 = true;

  const AGENT_NAME = window.IM_AGENT_NAME || "Mojini";

  // "" "" "" Reuse (or define) minimal KB so we can answer course/lab questions crisply "" "" "" 
  const COURSES = (window.__MOJINI_COURSES__) || [
    { t:"Causal Inference for Development: Designs, Estimators & Judgement", u:"/courses/causal/", o:"A free, design-based course in causal inference for development."},
    { t:"Seeing Data: Visualization for Impact", u:"/courses/dataviz/", o:"A flagship course on data visualization for development professionals."},
    { t:"AI for Impact: Data Monitoring & Evaluation in Development", u:"/courses/devai/", o:"Learn when and how to use AI tools in development M&E: from data collection and computer vision to algorithmic targeting and ethical frameworks."},
    { t:"Understanding Development: An Economics Perspective", u:"/courses/devecon/", o:"A comprehensive, free course exploring poverty, growth, and economic transformation in developing nations."},
    { t:"Sustainability, ESG & Corporate Responsibility for Development Practice", u:"/courses/esg/", o:"A practitioner's flagship on corporate money and corporate conduct in India."},
    { t:"Gandhi's Political Thought: Philosophy for Praxis", u:"/courses/gandhi/", o:"A comprehensive journey through Gandhi's political thought: from Swaraj and Satyagraha to Gram Swaraj and Trusteeship."},
    { t:"Gender Studies: Feminisms, Power & Social Change", u:"/courses/gender/", o:"A flagship course on feminist theory, gender & power, care work, law, movements, and development practice: with deep South Asian focus."},
    { t:"Gender-Sensitive Monitoring, Evaluation & Learning", u:"/courses/gender-mel/", o:"A practitioner's flagship on measuring gender rather than counting women."},
    { t:"Designing What Works: Development Interventions from Model to Scale", u:"/courses/intervention/", o:"A free flagship on development intervention and programme design."},
    { t:"Constitution & Law for Development Practice", u:"/courses/law/", o:"A practitioner's guide to constitutional law and rights-based frameworks across South Asia."},
    { t:"Livelihoods in India: Rural, Urban, and Skills", u:"/courses/livelihoods/", o:"Comprehensive flagship on Indian livelihoods: rural (NRLM, SHGs, agriculture), urban (informal work, gig economy, vendors), and skills (Skill India, FLFPR)."},
    { t:"Media for Development: Communicating Impact", u:"/courses/media/", o:"A rigorous, free course on development communication, ethical storytelling, and media impact."},
    { t:"The Evidence Question: Monitoring, Evaluation & Learning for Practice", u:"/courses/mel/", o:"A comprehensive, free course on MEL systems for development professionals."},
    { t:"Nothing About Us Without Us: Disability, Justice & Development", u:"/courses/nothing-about-us/", o:"A comprehensive, free course on disability, justice and development for practitioners in South Asia."},
    { t:"Nonviolence in Practice: Communication, Resistance & Repair", u:"/courses/nvc-rj/", o:"A flagship course on three canonical traditions of applied nonviolence (Marshall Rosenberg's Nonviolent Communication (NVC), Haim Omer's Non-Violent Resistance / New..."},
    { t:"Politics of Aspiration: Rights, Insurance & Social Mobility in South Asia", u:"/courses/poa/", o:"How India's rights-based architecture (RTI, NREGA, Food Security, Forest Rights) creates enabling conditions for poor households to imagine and pursue better futures."},
    { t:"Public Choice: Decisions, Incentives & Institutions", u:"/courses/pubchoice/", o:"A flagship course on the mechanics of collective decision-making: voting rules, rent-seeking, bureaucracy, commons governance, and institutional design."},
    { t:"Public Policy: Process, Design & Governance in India", u:"/courses/pubpol/", o:"A comprehensive free course on public policy, fiscal federalism, regulatory governance, and Indian development."},
    { t:"Social-Emotional Learning for Development Practice", u:"/courses/sel/", o:"How social-emotional competencies shape effective development practice."},
    { t:"Social Movements & Protests: Theory and South Asian Practice", u:"/courses/social-movements/", o:"A rigorous, South Asia-first flagship on how social movements form, act, and change society, movement theory (Tilly, Tarrow, Sharp, Chenoweth) grounded in South Asian..."},
    { t:"Power BI for Practitioners: A Free Hands-On Course", u:"/courses/powerBI/powerbi.html", o:"A free, hands-on Power BI flagship for South Asian development practitioners."},
    { t:"Sexual Health 101", u:"/101-courses/SRHR-basics.html", o:"Sexual Health 101, a free, rights-based foundational course on sexual and reproductive health and rights (SRHR) for development and health practitioners in South..."},
    { t:"Academic Writing & Publishing 101", u:"/101-courses/academic-writing.html", o:"Academic Writing & Publishing 101: a free foundational course for researchers and practitioners in South Asia."},
    { t:"Advocacy Basics 101", u:"/101-courses/advocacy-basics.html", o:"Advocacy Basics 101, a free foundational course for development and civil-society practitioners in South Asia: how to analyse power, frame an issue, map stakeholders,..."},
    { t:"Behaviour Change Communication 101", u:"/101-courses/bcc-comms.html", o:"Behaviour Change Communication 101: a free foundational course for development and public-health communicators in South Asia."},
    { t:"Bivariate Analysis 101", u:"/101-courses/bi-analysis.html", o:"Bivariate Analysis 101: a free foundational course for development practitioners and researchers in South Asia."},
    { t:"Care Economy 101", u:"/101-courses/care-economy-101.html", o:"Care Economy 101: a free foundational course for development practitioners and policy folk in South Asia."},
    { t:"Child Development 101", u:"/101-courses/child-development.html", o:"Child Development 101, a free foundational course on early childhood development for health and development practitioners in South Asia: the first 1,000 days, domains..."},
    { t:"Climate Essentials 101", u:"/101-courses/climate-essentials.html", o:"Climate Essentials 101: free development education from ImpactMojo."},
    { t:"Community Development 101", u:"/101-courses/community-dev.html", o:"Community Development 101: a free foundational course for development practitioners in South Asia."},
    { t:"Cost Effectiveness 101", u:"/101-courses/cost-effectiveness.html", o:"Cost Effectiveness 101: a free foundational course for development practitioners and funders in South Asia."},
    { t:"CSR & ESG 101", u:"/101-courses/csr-esg.html", o:"Corporate social responsibility and ESG for India: Section 135 of the Companies Act 2013, Schedule VII, the two per cent, unspent-money rules, CSR-1, impact..."},
    { t:"Data Feminism 101", u:"/101-courses/data-feminism.html", o:"Data Feminism 101: a free foundational course for development practitioners and researchers in South Asia."},
    { t:"Data Literacy 101", u:"/101-courses/data-lit.html", o:"Data Literacy 101: a free foundational course for development practitioners in South Asia."},
    { t:"Data Protection & the DPDP Act 101", u:"/101-courses/data-protection-dpdp.html", o:"Data Literacy 101: a free foundational course for development practitioners in South Asia."},
    { t:"Data Visualization 101", u:"/101-courses/data-viz.html", o:"Data Visualization 101 - a free foundational course for development practitioners in South Asia."},
    { t:"Decolonial Development 101", u:"/101-courses/decolonize-dev.html", o:"Decolonial Development 101: a free foundational course for practitioners, researchers and students in the Global South and South Asia."},
    { t:"Global Development Governance 101", u:"/101-courses/dev-architecture.html", o:"Global Development Governance 101: a free foundational course for development practitioners in South Asia."},
    { t:"Development Economics 101", u:"/101-courses/dev-economics.html", o:"Development Economics 101: free development education from ImpactMojo."},
    { t:"Development Finance 101", u:"/101-courses/development-finance.html", o:"Development Finance 101 - a free foundational course for practitioners in South Asia."},
    { t:"Digital Ethics 101", u:"/101-courses/digital-ethics.html", o:"Digital Ethics 101, a free foundational course for development practitioners in South Asia on deploying digital technology responsibly: data privacy and the DPDP Act,..."},
    { t:"Disability Inclusion 101", u:"/101-courses/disability-inclusion.html", o:"Data Literacy 101: a free foundational course for development practitioners in South Asia."},
    { t:"Econometrics 101", u:"/101-courses/econometrics-101.html", o:"Econometrics 101: a free foundational course for development practitioners and researchers in South Asia."},
    { t:"Exploratory Data Analysis 101", u:"/101-courses/eda-hhs.html", o:"Exploratory Data Analysis 101: a free foundational course for development practitioners in South Asia."},
    { t:"Education and Pedagogy 101", u:"/101-courses/edu-pedagogy.html", o:"Education and Pedagogy 101: a free foundational course for educators and education-programme staff in South Asia."},
    { t:"English for Development 101", u:"/101-courses/eng-dev.html", o:"English for Development 101, a free, practical communication course for NGO staff, researchers and grant writers across South Asia working in English as a second or..."},
    { t:"Environmental Justice 101", u:"/101-courses/env-justice.html", o:"Environmental Justice 101: a free foundational course for development and environment practitioners in South Asia."},
    { t:"Feminist Research 101", u:"/101-courses/feminist-research.html", o:"Feminist Research 101: a free foundational course for development researchers and practitioners in South Asia."},
    { t:"Fundraising Basics 101", u:"/101-courses/fundraising-basics.html", o:"Fundraising Basics 101: a free foundational course for NGO and nonprofit staff in India and South Asia."},
    { t:"GenAI for Practitioners 101", u:"/101-courses/genai-practitioners.html", o:"Data Literacy 101: a free foundational course for development practitioners in South Asia."},
    { t:"Gender Mainstreaming 101", u:"/101-courses/gender-mainstreaming.html", o:"Gender Mainstreaming 101, a free foundational course for development practitioners and programme managers in South Asia: from the Beijing Platform and ECOSOC..."},
    { t:"Impact Evaluation 101", u:"/101-courses/impact-eval.html", o:"Impact Evaluation 101, a free foundational course for development programme and MEL practitioners in South Asia on designing, commissioning and using credible impact..."},
    { t:"Indian Constitution 101", u:"/101-courses/ind-constitution.html", o:"Indian Constitution 101: a free foundational course on the making, structure and living practice of the Constitution of India, for development practitioners, students..."},
    { t:"Inequality Basics 101", u:"/101-courses/inequality-basics.html", o:"Inequality Basics 101: free development education from ImpactMojo."},
    { t:"Item Response Theory 101", u:"/101-courses/irt-basics.html", o:"Item Response Theory 101: a free foundational course for development M&E and assessment practitioners in South Asia."},
    { t:"Logframe 101", u:"/101-courses/logframe-101.html", o:"Logframe 101 - a free foundational course for development practitioners in South Asia."},
    { t:"Maternal Health 101", u:"/101-courses/maternal-health.html", o:"Maternal Health 101, a free foundational course for development and public-health practitioners in South Asia: why mothers die, the three delays, the continuum of..."},
    { t:"MEL Basics 101", u:"/101-courses/mel-basics.html", o:"MEL Basics 101: free development education from ImpactMojo."},
    { t:"Mixed Methods 101", u:"/101-courses/mixed-methods.html", o:"Mixed Methods 101, a free foundational course for development researchers and MEL practitioners in South Asia on intentionally combining quantitative and qualitative..."},
    { t:"Multivariate Analysis 101", u:"/101-courses/multivariate-basics.html", o:"Multivariate Analysis 101: a free foundational course for development practitioners and analysts in South Asia."},
    { t:"Observation to Insight 101", u:"/101-courses/obs2insight.html", o:"Observation to Insight 101: a free foundational course for development practitioners in South Asia."},
    { t:"Political Economy 101", u:"/101-courses/pol-economy.html", o:"Political Economy 101: a free foundational course for development practitioners and analysts in South Asia."},
    { t:"Post-Truth Politics 101", u:"/101-courses/post-truth-101.html", o:"Post-Truth Politics 101, a free foundational course for development practitioners, communicators and citizens in South Asia on why emotion, identity and falsehood..."},
    { t:"Public Health 101", u:"/101-courses/pub-health-basics.html", o:"Public Health 101, a free foundational course for development and health practitioners in South Asia: population health and prevention, social determinants,..."},
    { t:"Public Finance & Budgeting 101", u:"/101-courses/public-finance-budgeting.html", o:"Public Finance & Budgeting 101: fiscal architecture, budget cycles, taxation, and intergovernmental transfers in South Asia."},
    { t:"Qualitative Analysis Software 101", u:"/101-courses/qda-software.html", o:"Qualitative Analysis Software 101: a free foundational course on NVivo, MAXQDA, ATLAS.ti and the free tools Taguette and QualCoder."},
    { t:"Qualitative Methods 101", u:"/101-courses/qual-methods.html", o:"Qualitative Methods 101: a free foundational course for development practitioners and researchers in South Asia."},
    { t:"Research Ethics 101", u:"/101-courses/research-ethics.html", o:"Research Ethics 101: a free foundational course for development practitioners and researchers in South Asia."},
    { t:"Safeguarding & PSEA 101", u:"/101-courses/safeguarding-psea.html", o:"Data Literacy 101: a free foundational course for development practitioners in South Asia."},
    { t:"SEL Basics 101", u:"/101-courses/sel-basics.html", o:"SEL Basics 101: a free foundational course for educators and education-programme staff in South Asia."},
    { t:"Structural Equation Modelling 101", u:"/101-courses/sem.html", o:"Structural Equation Modelling 101: a free foundational course for applied social researchers in South Asia."},
    { t:"Social Margins 101", u:"/101-courses/social-margins.html", o:"Social Margins 101: identity, structure, intersectionality, and inequality in South Asia."},
    { t:"Statistics Without Code 101", u:"/101-courses/stats-without-code.html", o:"Statistics Without Code 101: a free foundational course on jamovi and JASP, the free point-and-click statistics tools built on R."},
    { t:"Survey Design 101", u:"/101-courses/survey-design.html", o:"Survey Design 101: a free foundational course for development and MEL practitioners running field surveys in South Asia."},
    { t:"Systematic Reviews & Evidence Synthesis 101", u:"/101-courses/systematic-reviews.html", o:"Systematic Reviews & Evidence Synthesis 101: a free foundational course for development researchers and practitioners in South Asia."},
    { t:"Time Series Analysis 101", u:"/101-courses/time-series.html", o:"Time Series Analysis 101: a free foundational course for applied researchers in South Asia."},
    { t:"Theory of Change 101", u:"/101-courses/toc-workbench.html", o:"Theory of Change 101, a free, practical course for development practitioners in programme design and M&E across South Asia: build a causal map from activities to..."},
    { t:"Visual Ethnography 101", u:"/101-courses/visual-eth.html", o:"Visual Ethnography 101: a free foundational course for development researchers and communicators in South Asia."},
    { t:"Women's Economic Empowerment 101", u:"/101-courses/wee-studies.html", o:"Women's Economic Empowerment 101, a free foundational course for gender and development practitioners in South Asia: resources, agency and achievements; the unpaid..."},
    { t:"Work, Labour & Livelihoods 101", u:"/101-courses/work-labour-livelihoods.html", o:"Work, Labour & Livelihoods 101: informality, the gig economy, agrarian labour, decent work, and labour rights frameworks across South Asia."}
  ];
  const LABS = (window.__MOJINI_LABS__) || [
    { t:"Before We Fall Apart: Group Conflict-Preparedness Studio", u:"/Labs/before-we-fall-apart-lab.html" },
    { t:"Budget & Fiscal Analysis Studio", u:"/Labs/budget-fiscal-lab.html" },
    { t:"Climate Risk & Adaptation Studio", u:"/Labs/climate-adaptation-lab.html" },
    { t:"Community Engagement Studio", u:"/Labs/community-lab.html" },
    { t:"Conflict-Sensitive Programming Studio", u:"/Labs/conflict-sensitive-lab.html" },
    { t:"Data Feminism & Intersectional Analysis Studio", u:"/Labs/data-feminism-lab.html" },
    { t:"Design Thinking Studio", u:"/Labs/design-thinking-lab.html" },
    { t:"Disability-Inclusive MEL Studio", u:"/Labs/disability-inclusive-mel-lab.html" },
    { t:"Digital Public Infrastructure Studio", u:"/Labs/dpi-lab.html" },
    { t:"Ethics & Research Integrity Studio", u:"/Labs/ethics-research-lab.html" },
    { t:"Gender Analysis Studio", u:"/Labs/gender-studies-lab.html" },
    { t:"Grant Writing & Proposal Studio", u:"/Labs/grant-writing-lab.html" },
    { t:"Impact Evaluation Designer", u:"/Labs/impact-evaluation-lab.html" },
    { t:"Impact Partnerships Studio", u:"/Labs/impact-partnerships-lab.html" },
    { t:"Livelihoods & Value-Chain Studio", u:"/Labs/livelihoods-value-chain-lab.html" },
    { t:"LogFrame Builder", u:"/Labs/logframe-builder-lab.html" },
    { t:"MEL Studio", u:"/Labs/mel-lab.html" },
    { t:"MEL Rosetta Lab: translate between MEL frameworks", u:"/Labs/mel-rosetta-lab.html" },
    { t:"NVC & Mediation Practice", u:"/Labs/nvc-mediation-lab.html" },
    { t:"Participatory Methods Studio", u:"/Labs/participatory-methods-lab.html" },
    { t:"Policy Advocacy Studio", u:"/Labs/policy-advocacy-lab.html" },
    { t:"Policy Analysis Studio: Structured Tools for Policy Reasoning", u:"/Labs/policy-analysis-lab.html" },
    { t:"Policy Brief Writing Studio", u:"/Labs/policy-brief-lab.html" },
    { t:"RCT Readiness Diagnostic", u:"/Labs/rct-readiness-lab.html" },
    { t:"Resource Sustainability Studio", u:"/Labs/resource-sustainability-lab.html" },
    { t:"Risk & Mitigation Studio", u:"/Labs/risk-mitigation-lab.html" },
    { t:"Sampling Basics: A Plain-Language Primer", u:"/Labs/sampling-basics-lab.html" },
    { t:"Sampling Design Studio", u:"/Labs/sampling-design-lab.html" },
    { t:"Stakeholder Mapping & Power Analysis Studio", u:"/Labs/stakeholder-mapping-lab.html" },
    { t:"Impact Storytelling Studio", u:"/Labs/storytelling-lab.html" },
    { t:"Survey Design Studio", u:"/Labs/survey-design-lab.html" },
    { t:"Systems Thinking & Complexity Studio", u:"/Labs/systems-thinking-lab.html" },
    { t:"Teacher Evidence Studio: What Actually Works for Teacher Effectiveness", u:"/Labs/teacher-evidence-lab.html" },
    { t:"Theory of Change Studio", u:"/Labs/toc-lab.html" },
    { t:"Why City Boundaries Lie", u:"/Labs/urban-boundaries-lab.html" }
  ];
  // expose once for other scripts if needed
  window.__MOJINI_COURSES__ = COURSES;
  window.__MOJINI_LABS__ = LABS;

  // "" "" "" Helpers "" "" "" 
  const norm = s => String(s||"").toLowerCase();
  const listCourses = () => COURSES.map(c=>`• ${c.t}: ${c.o}\n  ${c.u}`).join("\n");
  const listLabs = () => LABS.map(l=>`• ${l.t}\n  ${l.u}`).join("\n");
  const byTitle = (arr, text) => {
    const s = norm(text);
    return arr.find(x => s.includes(norm(x.t)) || norm(x.t).includes(s));
  };

  function replyBot(text){
    if (typeof window.addBotMessage === 'function') { window.addBotMessage(text); return; }
    const box = document.getElementById('chatMessages') || document.querySelector('.chat-messages');
    if (!box) return;
    const wrap = document.createElement('div'); wrap.className = 'message bot-message';
    const bub = document.createElement('div'); bub.className = 'bot-bubble'; bub.textContent = text;
    wrap.appendChild(bub); box.appendChild(wrap); box.scrollTop = box.scrollHeight;
  }

  // "" "" "" FAQ BANK (30+) "" "" "" 
  // Each item: {re: /pattern/i, a: "answer" }  (safe, non-inventive wording)
  const FAQ = [
    // Credentials / Certificates / Accreditation
    { re: /(certificate|certification)s?\b/i,
      a: "Every signed-up learner gets a free certificate of completion for each course they finish. It appears in your account and has an ID that anyone can check on our verification page. Practitioner members and above can also download it as a PDF and show it in a portfolio. It marks completion, not accreditation." },
    { re: /\bcredential(s)?\b|\bbadge(s)?\b|\bportfolio\b/i,
      a: "Beyond the certificate, the work you make in labs and Practice Packs is yours to show: a Theory of Change, a sampling design, a policy brief." },
    { re: /\baccredit(ed|ation)|academic credit|university|ugc\b/i,
      a: "ImpactMojo is not an accredited degree program and doesn't offer academic credit. It's a practitioner-focused learning platform." },

    // Premium / Pricing
    { re: /\bpremium\b(?!.*(what|include|benefit|price))/i,
      a: "**Practitioner** (₹399 a month) opens all 18 Practice Packs in full, the Research Question Builder Pro and Theory of Change Workbench Pro, and certificates with PDF download. **Professional** (₹999 a month) adds Qualitative Insights Lab Pro, Statistical Code Converter Pro, VaniScribe AI transcription, copying code from the Visualization Cookbook, the DevEconomics Toolkit, and priority coaching. DevData Practice is free to use. Field Notes from a Dev Economist is free. See the Premium page for current prices." },
    { re: /\b(what('| i)?s|about).+premium|\bpremium\b.+(include|cover|benefit)/i,
      a: "**Practitioner** (₹399 a month) opens all 18 Practice Packs in full, the Research Question Builder Pro and Theory of Change Workbench Pro, and certificates with PDF download. **Professional** (₹999 a month) adds Qualitative Insights Lab Pro, Statistical Code Converter Pro, VaniScribe AI transcription, copying code from the Visualization Cookbook, the DevEconomics Toolkit, and priority coaching. DevData Practice is free to use. Field Notes from a Dev Economist is free. See the Premium page for current prices." },
    { re: /\b(price|cost|fee|paid|free).+premium|\bpremium.+(price|cost|fee)/i,
      a: "Premium has two plans: **Practitioner** (₹399 a month) and **Professional** (₹999 a month). The Premium page lists what each includes. The courses, labs and games are free." },

    // Courses (catalog, objectives, level, format)
    { re: /\b(list|show|see).+course(s)?\b|^\s*courses?\s*$/i,
      a: () => `Here are our core courses:\n\n${listCourses()}` },
    { re: /(which|what)\s+course(s)?\s+(do you have|are available)/i,
      a: () => `We currently offer:\n\n${listCourses()}` },
    { re: /(beginner|new to this|where to start)/i,
      a: "Start with any **101** course. They're beginner-friendly and focus on practical understanding." },
    { re: /(advanced|deeper|next step)/i,
      a: "For deeper work, explore **labs** and **Premium** deeper-dives." },
    { re: /(duration|time|how long).+course/i,
      a: "Most courses are **self-paced**. Time varies by learner: check each course page for modules and suggested pace." },
    { re: /\blive\b.+(class|session|cohort)/i,
      a: "Most learning is self-paced. When live/cohort options are offered, the course page will say so." },
    { re: /enrol|enroll|join|sign ?up/i,
      a: "Open the course you want and follow the on-page steps. Some items are open access; others may prompt you to sign in." },

    // Labs
    { re: /\b(list|show).+lab(s)?\b|^\s*labs?\s*$/i,
      a: () => `Here are our labs:\n\n${listLabs()}` },
    { re: /\bTOC\b|\btheor(y|ies) of change\b/i,
      a: () => `**TOC Lab** helps you structure a Theory of Change quickly and clearly.\n/Labs/toc-lab.html` },
    { re: /MLE (framework|builder|workbench)/i,
      a: () => `The **MLE Framework Workbench/Builder** help you design monitoring & learning frameworks.\nWorkbench: /Labs/mel-design-lab.html\nBuilder:   /Labs/mel-plan-lab.html` },
    { re: /how (to )?access.+lab|use.+lab/i,
      a: "Labs are web tools. Click a lab link and start; most open directly in your browser." },

    // Resources / Games / Testimonials / Ratings / Founders
    { re: /resource(s)?|reading list|tool(s)?|template(s)?/i,
      a: "Resources include reading lists, tools, data links, and templates referenced across courses and labs." },
    { re: /\bgame(s)?\b|interactive/i,
      a: "Games are short, interactive learning modules that reinforce key ideas in a playful way." },
    { re: /(testimonial|review|what people say)/i,
      a: "Testimonials are showcased on-site when available. You can also leave feedback here and we may feature excerpts." },
    { re: /rating(s)?|stars?/i,
      a: "Ratings vary by context. Where available, they appear with the relevant course or lab: Mojini avoids quoting numbers out of context." },
    { re: /founder|who.*(behind|lead)/i,
      a: "ImpactMojo is led by **Dr. Varna Sri Raman**. (Additional leadership may be featured on the site.)" },

    // Access, language, privacy, support
    { re: /\bmobile|phone|tablet|responsive\b/i,
      a: "ImpactMojo works on modern browsers across desktop and mobile. For the best experience, keep your browser up to date." },
    { re: /\blanguage(s)?\b|hindi|translation/i,
      a: "Content is in **English**. The home, About and Books pages and the site menus can be switched into Hindi, Bengali, Marathi, Tamil and Telugu, but those translations are produced by machine and may contain errors. Course content is in English only." },
    { re: /\bprivacy\b|\bgdpr\b|\bdpdp\b|data protection|\bmy data\b/i,
      a: "We respect your privacy. Feedback is used to improve ImpactMojo. Please refer to the site's Privacy/Terms pages for details." },
    { re: /(support|help|contact|reach|email)/i,
      a: "For support, use this chat's **Report Bug** or **Feature Request** options. We'll follow up using the info you provide." },
    { re: /(suggest|request).+course/i,
      a: "Use the **Suggest Course** shortcut here in chat to propose a new course or topic." },

    // Services: Dojos, Workshops, Coaching
    { re: /\bdojo(s)?\b/i,
      a: "**Dojos** are practice-based skill sessions: 90-minute cohort workshops that build practitioner skills through doing. There are 56 sessions in the series. ₹1,500 per session in Delhi, Bangalore, or online. Check the **Dojos** page under Services." },
    { re: /\bworkshop(s)?\b/i,
      a: "We run intensive three-day **Workshops** for NGOs and development teams, with cohort pricing from ₹12,000 for up to 6 participants. The **Workshops** page under Services has the topics, dates and booking form." },
    { re: /\bcoaching\b/i,
      a: "**Coaching** is one-on-one or group sessions. The **Coaching** page under Services lists the coaches, topics and how to book." },
    { re: /(service|what do you offer|training|consulting)/i,
      a: "ImpactMojo offers **Courses** (self-paced learning), **Labs** (hands-on tools), **Coaching** (1:1 sessions), **Workshops** (group training), and **Dojos** (practice-based skill sessions). Explore the Services menu!" },

    // Org / team use
    { re: /(organization|organisation|team|ngo|gov|company)/i,
      a: "ImpactMojo is designed for practitioners and teams. Courses build foundations; labs help teams design, test, and improve programs." },

    // WhatsApp PLC
    { re: /whatsapp|plc|community|peer.*learn/i,
      a: "Join our **WhatsApp Professional Learning Community**! Connect with practitioners, researchers, and changemakers across South Asia. Share resources, discuss fieldwork challenges, and grow together. Look for the green WhatsApp section on the homepage." },

    // Flagship count
    { re: /how many.*course|flagship|all.*course/i,
      a: () => "We have **21 flagship courses** and **59 foundational courses**, 80 in all. The full list is on the courses page, and a selection follows.\n\n" + listCourses() },

    // PoA specific
    { re: /poa|politics.*aspiration|nrega|rti|nfsa|forest.*right/i,
      a: () => { const c = byTitle(COURSES,"Politics of Aspiration"); return "**" + c.t + "**: 13 modules covering NREGA, RTI, NFSA, and Forest Rights Act. 60-term interactive lexicon.\n" + c.u; } },

    // Media specific
    { re: /media.*dev|development.*media|journalism|humanitarian.*comm/i,
      a: () => { const c = byTitle(COURSES,"Media for Development"); return "**" + c.t + "**: 12 modules covering ethics, P. Sainath, Khabar Lahariya, Video Volunteers, data journalism. 65-term lexicon.\n" + c.u; } },

    // ImpactLex
    { re: /impactlex|glossary|dictionary|terminology|acronym/i,
      a: "**ImpactLex** is our searchable glossary with more than 490 development terms, acronyms, formulas, and case studies. Features 'Finance Word of the Day'. Visit: https://on-web.link/ImpactLex" },

    // FieldCases Library
    { re: /fieldcases|case.?stud|evidence.*library|cited.*research|country.*studies|dev.*case/i,
      a: "**FieldCases** is our free, searchable library of more than 200 cited development case studies, each with its sources listed. Browse it at: https://varnasr.github.io/dev-case-studies/" },

    // Development Discourses
    { re: /dev.*discourse|discourse|open.?access.*paper|research.*paper|grey.*lit|academic.*library|curated.*library|research.*library/i,
      a: "**Development Discourses** is a curated open-access library of more than 600 research papers, books and grey literature on development and public policy, sorted by topic. Every resource is open access, so you can read and cite it without a paywall. Explore it at: https://on-web.link/DevDiscourses" },

    // DevData Practice
    { re: /devdata|dataset|data.*practice|realistic.*data|household.*survey|rct.*data/i,
      a: "**DevData Practice** is free to use. It has 36 dataset generators that produce more than 840,000 synthetic rows in the style of household surveys, trials and labour force surveys, for practising analysis. None of it is real survey data. Open it at /premium-tools/devdata-practice.html" },
    // Constitution & Law
    { re: /constitution|law.*course|pil|article.*21|fundamental.*right|basic.*structure|rights.*based/i,
      a: "**Constitution & Law for Development Practice** is our flagship course on rights, institutions and justice in South Asia. 13 modules covering the Indian Constitution, fundamental rights, PIL, Article 21, reservations, rights-based legislation, criminal justice, environmental law, digital rights, and comparative constitutional systems. Visit: /courses/law/" },
    // Social-Emotional Learning
    { re: /sel|social.*emotional|practitioner.*wellbeing|facilitation.*skill|conflict.*resolution|reflective.*practice/i,
      a: "**Social-Emotional Learning for Practitioners** is our flagship course on practitioner wellbeing, burnout prevention, empathy, resilience, facilitation skills, conflict resolution, and reflective practice. 13 modules with 55+ term interactive lexicon. Visit: /courses/sel/" },
    // VaniScribe
    { re: /vaniscribe|transcri|field.*interview|fgd.*transcri|kii.*transcri|south.*asian.*language|sarvam|diarization/i,
      a: "**VaniScribe** is our premium AI transcription tool for development researchers. Transcribe field interviews, FGDs, and KIIs in Hindi, Tamil, Bengali, and 10+ South Asian languages using Sarvam AI. Features speaker diarization, auto-timestamping, and export to structured formats for qualitative analysis. Visit: /premium.html" },
    // Visualization Cookbook
    { re: /viz.*cookbook|visualization.*cookbook|chart.*recipe|chart.*type|python.*chart|data.*viz.*code/i,
      a: "The **Visualization Cookbook** has 63 chart recipes with Python code, organised by the question you are asking of your data (comparison, distribution, relationship, composition, time series, spatial). Browsing is free. Copying the code needs a Professional plan. Open it at /premium-tools/viz-cookbook.html" },
    { re: /deveconomics.*toolkit|shiny.*app|rct.*power|did.*simulator|rdd.*explorer|synthetic.*control|gini.*tool|mpi.*explorer|logframe|wdi.*dashboard|poverty.*line.*analysis|cost.*benefit.*tool/i,
      a: "**DevEconomics Toolkit** is our premium collection of 11 interactive Shiny apps for development economics. Includes RCT power calculator, DiD simulator, RDD explorer, synthetic control visualizer, Gini and Lorenz curve tool, MPI explorer, poverty line analysis, Theory of Change visualizer, cost-benefit analysis tool, LogFrame builder, and WDI dashboard. Visit: https://impactmojo-devecon-toolkit.netlify.app/" }
  ];

  // Dynamic course objective matcher (covers "What's the objective of X?"  without listing all regexes)
  function tryCourseObjective(text){
    const s = norm(text);
    if (!/(objective|about|overview|syllabus|what is)/i.test(text)) return null;
    // Find best matching course title token
    let best = null, bestScore = 0;
    COURSES.forEach(c => {
      const title = norm(c.t);
      let score = 0;
      title.split(/[^a-z0-9]+/).forEach(tok => { if (tok.length > 2 && !['and','the','for','with','from'].includes(tok) && s.includes(tok)) score++; });
      if (score > bestScore) { bestScore = score; best = c; }
    });
    if (best && bestScore >= 2) return `${best.t}: ${best.o}\n${best.u}`;
    return null;
  }

  // Whatever answerer was installed before this file; captured now because the next block replaces it.
  const __prevAnswer = window.mojiniAnswer;

  // Main answerer: bank -> dynamic course objective -> (optional) existing mojiniAnswer -> fallback null
  function answerFromFAQ(userText){
    const text = String(userText||"");
    // 1) Hardcoded bank
    for (const item of FAQ) {
      if (item.re.test(text)) {
        const out = (typeof item.a === "function") ? item.a(text) : item.a;
        return out;
      }
    }
    // 2) Dynamic course objective
    const dyn = tryCourseObjective(text);
    if (dyn) return dyn;

    // 3) If an earlier global answerer exists, let it try next (keeps compatibility)
    if (typeof __prevAnswer === "function") {
      const maybe = __prevAnswer(text);
      if (maybe) return maybe;
    }
    return null;
  }

  // Expose so other blocks (wrappers) can use it too
  window.mojiniAnswer = answerFromFAQ;

  // Handle KB chips: answer first and stop propagation so we don't double-reply
  window.addEventListener("immojo:user", function(e){
    const q = e?.detail?.text || "";
    if (!q) return;
    const a = answerFromFAQ(q);
    if (a) {
      replyBot(a);
      // avoid duplicate responses from other listeners
      if (e.stopImmediatePropagation) e.stopImmediatePropagation();
    }
  }, true); // capture first

  // Wrap current sendMessage again (without breaking the existing fallback chain)
  const __prevSend = window.sendMessage;
  window.sendMessage = function(){
    const inp = document.getElementById("chatInput");
    const text = (inp?.value || "").trim();
    if (!text) return;
    const a = answerFromFAQ(text);
    if (a) {
      if (typeof window.addUserMessage === "function") window.addUserMessage(text);
      replyBot(a);
      if (inp) inp.value = "";
      return;
    }
    // Not matched -> pass through to whatever was there before
    if (typeof __prevSend === "function") return __prevSend.apply(this, arguments);
  };
})();
