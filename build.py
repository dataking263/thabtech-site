#!/usr/bin/env python3
"""Static site generator for thabtech.com redesign — 'Signal' direction."""
import pathlib, re, html

OUT = pathlib.Path(__file__).parent

LOGO = '''<svg class="brand__mark" viewBox="0 0 28 28" fill="none" aria-hidden="true">
<path d="M3 5h22" stroke="currentColor" stroke-width="2.6" stroke-linecap="square"/>
<path d="M14 5v18" stroke="currentColor" stroke-width="2.6" stroke-linecap="square"/>
<path d="M19.5 14h6" stroke="#FF8A3D" stroke-width="2.6" stroke-linecap="square"/>
<path d="M19.5 20.5h3.5" stroke="#FF8A3D" stroke-width="2.6" stroke-linecap="square" opacity=".55"/>
</svg>'''

FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 28 28'%3E"
           "%3Crect width='28' height='28' fill='%230A0B0D'/%3E"
           "%3Cpath d='M4 6h20M14 6v17' stroke='%23F2F1EF' stroke-width='2.6'/%3E"
           "%3Cpath d='M18.5 14h6' stroke='%23FF8A3D' stroke-width='2.6'/%3E%3C/svg%3E")

ARROW = '<svg width="14" height="14" viewBox="0 0 14 14" fill="none" aria-hidden="true"><path d="M2 7h9M7.5 3.5 11 7l-3.5 3.5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'

NAV = [("index.html", "Home"), ("services.html", "Consulting"),
       ("ai.html", "AI &amp; Risk"), ("staffing.html", "Staffing"),
       ("about.html", "About")]


def words(text):
    """Split a headline into per-word spans for the staggered reveal."""
    out, i = [], 0
    for w in text.split(" "):
        out.append(f'<span class="rv-word"><span style="--i:{i}">{w}</span></span>')
        i += 1
    return " ".join(out)


def head(title, desc, page):
    return f'''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0A0B0D">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<link rel="icon" href="{FAVICON}">
<link rel="preconnect" href="https://api.fontshare.com" crossorigin>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="style.css">
<script>
  document.documentElement.classList.add('js');
  var m = document.cookie.match(/(?:^|; )tt-theme=(dark|light)/);
  if (m) document.documentElement.dataset.theme = m[1];
</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{header(page)}
<main id="main">'''


def header(page):
    links = "".join(
        f'<a href="{h}"{" aria-current=\"page\"" if h == page else ""}>{t}</a>'
        for h, t in NAV)
    return f'''<header class="hdr">
<div class="hdr__in">
  <a class="brand" href="index.html" aria-label="ThabTech home">{LOGO}<span class="brand__txt">Thab<em>Tech</em></span></a>
  <nav class="nav" id="nav">
    {links}
    <a class="btn btn--primary btn--sm" href="contact.html">Start a conversation</a>
  </nav>
  <button class="icbtn" id="theme" type="button" aria-label="Toggle colour theme">
    <svg class="icbtn__moon" width="15" height="15" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M14 9.5A6.2 6.2 0 0 1 6.5 2a6.5 6.5 0 1 0 7.5 7.5Z" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"/></svg>
    <svg class="icbtn__sun" width="15" height="15" viewBox="0 0 16 16" fill="none" aria-hidden="true"><circle cx="8" cy="8" r="3.2" stroke="currentColor" stroke-width="1.4"/><path d="M8 1v1.6M8 13.4V15M1 8h1.6M13.4 8H15M3.2 3.2l1.1 1.1M11.7 11.7l1.1 1.1M12.8 3.2l-1.1 1.1M4.3 11.7l-1.1 1.1" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/></svg>
  </button>
  <button class="icbtn burger" id="burger" type="button" aria-label="Menu" aria-expanded="false" aria-controls="nav">
    <svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M2 4.5h12M2 11.5h12" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
  </button>
</div>
</header>'''


CTA = '''<section class="band sec">
<div class="wrap cta rv">
  <span class="eyebrow">Next step</span>
  <h2>Tell us what&rsquo;s breaking, stalling, or unstaffed.</h2>
  <p>Send a few sentences. You&rsquo;ll get a real reply from a person who has done the work &mdash; not a sequence of marketing emails.</p>
  <div class="cta__btns">
    <a class="btn btn--primary" href="contact.html">Start a conversation ''' + ARROW + '''</a>
    <a class="btn btn--ghost" href="about.html#capability">Capability statement</a>
  </div>
  <div class="cta__meta">
    <span class="mono">support@thabtech.com</span>
    <span class="mono">866&thinsp;755&thinsp;6007</span>
    <span class="mono">Mon&ndash;Fri&nbsp;&middot;&nbsp;9&ndash;5&nbsp;CT</span>
  </div>
</div>
</section>'''


FOOTER = '''</main>
<footer class="ftr">
<div class="wrap">
  <div class="ftr__top">
    <div class="ftr__bl">
      <a class="brand" href="index.html" aria-label="ThabTech home">''' + LOGO + '''<span class="brand__txt">Thab<em>Tech</em></span></a>
      <p>An IT consulting, AI and risk advisory, and technical staffing firm. We help organisations pick the right technology, govern it properly, and put the right people behind it.</p>
    </div>
    <div>
      <h4>Consulting</h4>
      <ul>
        <li><a href="services.html#cloud">Cloud &amp; infrastructure</a></li>
        <li><a href="services.html#security">Cybersecurity &amp; compliance</a></li>
        <li><a href="services.html#apps">Application development</a></li>
        <li><a href="services.html#advisory">Strategy &amp; advisory</a></li>
      </ul>
    </div>
    <div>
      <h4>AI &amp; risk</h4>
      <ul>
        <li><a href="ai.html#enablement">AI enablement</a></li>
        <li><a href="ai.html#governance">AI governance</a></li>
        <li><a href="ai.html#model-risk">Model risk management</a></li>
        <li><a href="ai.html#enterprise-risk">Technology &amp; enterprise risk</a></li>
      </ul>
    </div>
    <div>
      <h4>Staffing</h4>
      <ul>
        <li><a href="staffing.html#models">Engagement models</a></li>
        <li><a href="staffing.html#vetting">How we vet</a></li>
        <li><a href="staffing.html#roles">Roles we fill</a></li>
        <li><a href="staffing.html#candidates">For candidates</a></li>
      </ul>
    </div>
    <div>
      <h4>Company</h4>
      <ul>
        <li><a href="about.html">About</a></li>
        <li><a href="about.html#capability">Capability statement</a></li>
        <li><a href="contact.html">Contact</a></li>
        <li><a href="mailto:support@thabtech.com">support@thabtech.com</a></li>
      </ul>
    </div>
  </div>
  <div class="ftr__bot">
    <span class="mono">&copy; 2026 ThabTech LLC</span>
    <span class="mono">Dallas, Texas &middot; Serving clients nationwide</span>
  </div>
</div>
</footer>
<script>
(function () {
  var doc = document.documentElement;

  /* theme */
  var tbtn = document.getElementById('theme');
  tbtn && tbtn.addEventListener('click', function () {
    var next = doc.dataset.theme === 'light' ? 'dark' : 'light';
    doc.dataset.theme = next;
    document.cookie = 'tt-theme=' + next + ';path=/;max-age=31536000;SameSite=Lax';
  });

  /* mobile nav */
  var burger = document.getElementById('burger'), nav = document.getElementById('nav');
  burger && burger.addEventListener('click', function () {
    var open = nav.classList.toggle('open');
    burger.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
  nav && nav.addEventListener('click', function (e) {
    if (e.target.tagName === 'A') { nav.classList.remove('open'); burger.setAttribute('aria-expanded', 'false'); }
  });

  /* sticky header state */
  var hdr = document.querySelector('.hdr');
  var onScroll = function () { hdr.classList.toggle('stuck', window.scrollY > 8); };
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  /* scroll reveals */
  var targets = document.querySelectorAll('.rv, .rv-s, .steps');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.06 });
    targets.forEach(function (t) { io.observe(t); });
  } else {
    targets.forEach(function (t) { t.classList.add('in'); });
  }

  /* count-up on stat values */
  var stats = document.querySelectorAll('[data-count]');
  if (stats.length && 'IntersectionObserver' in window && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
    var so = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        var el = en.target, end = parseFloat(el.dataset.count), suffix = el.dataset.suffix || '';
        var t0 = null, dur = 900;
        var tick = function (ts) {
          if (!t0) t0 = ts;
          var p = Math.min((ts - t0) / dur, 1);
          var eased = 1 - Math.pow(1 - p, 3);
          el.textContent = Math.round(end * eased) + suffix;
          if (p < 1) requestAnimationFrame(tick);
        };
        requestAnimationFrame(tick);
        so.unobserve(el);
      });
    }, { threshold: 0.4 });
    stats.forEach(function (s) { so.observe(s); });
  }

  /* cursor spotlight on cards */
  if (matchMedia('(hover: hover) and (min-width: 900px)').matches) {
    document.querySelectorAll('.card').forEach(function (c) {
      c.addEventListener('pointermove', function (e) {
        var r = c.getBoundingClientRect();
        c.style.setProperty('--mx', (e.clientX - r.left) + 'px');
        c.style.setProperty('--my', (e.clientY - r.top) + 'px');
      });
    });
  }
})();
</script>
</body>
</html>'''


def hero(eyebrow, h1, lead, art=None, btns=None, pulse=None):
    art_html = (f'<div class="hero__art"><img src="{art}" alt="" loading="eager" decoding="async"></div>'
                if art else '')
    pulse_html = (f'<span class="pulse"><i></i>{pulse}</span>' if pulse else '')
    b = btns if btns is not None else (
        f'<a class="btn btn--primary" href="contact.html">Start a conversation {ARROW}</a>'
        f'<a class="btn btn--ghost" href="about.html#capability">Capability statement</a>')
    return f'''<section class="hero field">
{art_html}
<div class="wrap">
  <div class="hero__tags">{pulse_html}<span class="eyebrow">{eyebrow}</span></div>
  <h1>{words(h1)}</h1>
  <p class="lead">{lead}</p>
  <div class="hero__cta">{b}</div>
</div>
</section>'''


# ============================================================ HOME
STATS = [
    ("3", "", "Disciplines under one accountability"),
    ("50", "+", "US states we can staff into"),
    ("1", "", "Business day to a human reply"),
    ("4", "", "Governance frameworks we build to"),
]

MARQUEE = ["Azure", "AWS", "Microsoft 365", "Entra ID", "Azure OpenAI", "Amazon Bedrock",
           "NIST AI RMF", "ISO 42001", "EU AI Act", "SR 11-7", "Model Inventory", "RAG",
           "Copilot", "LangChain", "Zero Trust", "SOC 2", "HIPAA", "Terraform", "Kubernetes",
           "Power BI", "Snowflake", "Python", ".NET", "ServiceNow", "Workday", "Okta", "CI/CD"]


def marquee():
    grp = "".join(f'<span>{w}</span><i></i>' for w in MARQUEE)
    return f'''<div class="marq" aria-hidden="true">
<div class="marq__t"><div class="marq__g">{grp}</div><div class="marq__g">{grp}</div></div>
</div>'''


HOME_WHY = [
    ("01", "One firm, one throat to choke",
     "The team that recommends the architecture is the team that staffs it. No consultant blaming the contractor, no contractor blaming the plan."),
    ("02", "Scoped before it&rsquo;s sold",
     "Every engagement starts with a fixed-fee assessment. You see the plan, the cost and the risks before you commit to delivery."),
    ("03", "Built to be easy to buy from",
     "W-9, COI, MSA and NAICS codes are ready to go. We&rsquo;ve been through enough vendor onboarding portals to make yours painless."),
    ("04", "Senior people, no bench-warming",
     "You get practitioners who have run the systems they&rsquo;re advising on. We don&rsquo;t staff a project to keep a bench busy."),
]

HOME_STEPS = [
    ("01", "Scoping call", "Thirty minutes. What&rsquo;s broken, what you&rsquo;ve already tried, and what &ldquo;fixed&rdquo; looks like to you."),
    ("02", "Written assessment", "A fixed-fee document: findings, options with costs, a recommendation and the risks of doing nothing."),
    ("03", "Delivery or placement", "We execute the plan, or we place the people who will. Weekly written status, named owner throughout."),
    ("04", "Handover that holds", "Documentation, runbooks and a named contact. You should be able to fire us and still be fine."),
]


def home():
    stats = "".join(
        f'<div class="stat"><span class="stat__k tnum" data-count="{k}" data-suffix="{s}">{k}{s}</span>'
        f'<span class="stat__l mono">{l}</span></div>'
        for k, s, l in STATS)

    # bento: rows 1 and 4 span two columns, creating an asymmetric rhythm
    span = {"01": " card--wide card--say", "04": " card--wide card--say"}
    why = "".join(
        f'<div class="card{span.get(n, "")}"><span class="card__n">{n}</span><h3>{t}</h3><p>{d}</p></div>'
        for n, t, d in HOME_WHY)

    steps = "".join(
        f'<div class="step"><span class="step__n">{n}</span><h3>{t}</h3><p>{d}</p></div>'
        for n, t, d in HOME_STEPS)

    return head("ThabTech — IT Consulting, AI &amp; Risk, Technical Staffing",
                "ThabTech is an IT consulting, AI and risk advisory, and technical staffing firm. Dallas, Texas — serving clients nationwide.",
                "index.html") + f'''
{hero("IT consulting &middot; AI &amp; risk &middot; technical staffing",
      "Your systems are only as strong as the people behind them.",
      "ThabTech pairs hands-on IT consulting with AI and risk advisory and technical staffing, so the plan, the controls and the people arrive together.",
      art="assets/atmo-lattice.webp",
      pulse="Taking on new engagements")}

<div class="wrap"><div class="stats rv-s">{stats}</div></div>

{marquee()}

<section class="sec">
<div class="wrap">
  <div class="head head--wide rv">
    <span class="eyebrow">The practice</span>
    <h2>Three disciplines. One line of accountability.</h2>
    <p class="lead">Most organisations buy strategy from one firm, AI from a second and people from a third, then spend the project managing the seams between them. We removed the seams.</p>
  </div>
  <div class="grid g-3 rv-s pcards">
    <article class="card pcard">
      <div class="pcard__img"><img src="assets/atmo-machined.webp" alt="Machined precision component lit by a warm edge light" loading="lazy" decoding="async"></div>
      <div class="pcard__body">
        <span class="mono">Consulting</span>
        <h3>Fix the architecture, not the symptom</h3>
        <p>Cloud migrations, identity and access, security posture, custom applications and the IT roadmap that ties them together.</p>
        <ul>
          <li>Cloud &amp; infrastructure modernisation</li>
          <li>Cybersecurity &amp; compliance readiness</li>
          <li>Application development &amp; integration</li>
          <li>IT strategy, roadmap &amp; vendor selection</li>
        </ul>
        <a class="tlink" href="services.html">Explore consulting {ARROW}</a>
      </div>
    </article>
    <article class="card pcard">
      <div class="pcard__img"><img src="assets/atmo-gates.webp" alt="Receding row of glowing gates with a beam of light passing through each" loading="lazy" decoding="async"></div>
      <div class="pcard__body">
        <span class="mono">AI &amp; risk</span>
        <h3>Put AI to work without losing control of it</h3>
        <p>Where AI actually pays, how to deploy it safely, and the governance and model-risk structure that lets you defend it later.</p>
        <ul>
          <li>AI use-case triage &amp; enablement</li>
          <li>AI governance &amp; policy build-out</li>
          <li>Model risk management &amp; validation</li>
          <li>Technology &amp; enterprise risk</li>
        </ul>
        <a class="tlink" href="ai.html">Explore AI &amp; risk {ARROW}</a>
      </div>
    </article>
    <article class="card pcard">
      <div class="pcard__img"><img src="assets/atmo-network.webp" alt="Constellation of connected glowing nodes across dark space" loading="lazy" decoding="async"></div>
      <div class="pcard__body">
        <span class="mono">Staffing</span>
        <h3>The right engineer, not the fastest résumé</h3>
        <p>Contract, contract-to-hire and direct placement for infrastructure, security, data and application teams.</p>
        <ul>
          <li>Contract &amp; contract-to-hire</li>
          <li>Direct-hire search</li>
          <li>Statement-of-work project teams</li>
          <li>Technical screening you can audit</li>
        </ul>
        <a class="tlink" href="staffing.html">Explore staffing {ARROW}</a>
      </div>
    </article>
  </div>
</div>
</section>

<section class="band sec">
<div class="wrap">
  <div class="head head--wide rv">
    <span class="eyebrow">How engagements run</span>
    <h2>A predictable sequence, every time.</h2>
    <p class="lead">You should never be guessing what happens next or what it will cost. Four stages, in the same order, on every engagement.</p>
  </div>
  <div class="steps">{steps}</div>
</div>
</section>

<section class="sec">
<div class="wrap">
  <div class="head rv">
    <span class="eyebrow">Why ThabTech</span>
    <h2>Small enough to answer. Structured enough to trust.</h2>
  </div>
  <div class="bento rv-s">{why}</div>
</div>
</section>

{CTA}
''' + FOOTER


# ============================================================ SERVICES
SERVICES = [
    ("cloud", "01", "Cloud &amp; infrastructure",
     "Move what should move, leave what shouldn&rsquo;t, and stop paying for both.",
     "Most cloud bills are the residue of a migration nobody finished. We assess what you&rsquo;re actually running, model the cost of each option, and execute the path you pick.",
     ["Azure and AWS migration &amp; landing-zone design",
      "Microsoft 365 and Entra ID tenant cleanup",
      "Cost review and right-sizing with a written savings model",
      "Backup, disaster recovery and business-continuity testing",
      "Network, VPN and remote-access architecture"]),
    ("security", "02", "Cybersecurity &amp; compliance",
     "Get to a posture you can defend in an audit and in an incident.",
     "We start with what an attacker would find, not with a product pitch. The output is a prioritised remediation plan with effort and cost against each item.",
     ["Security posture assessment and gap analysis",
      "Identity, MFA and privileged-access hardening",
      "Zero-trust and endpoint policy rollout",
      "SOC 2, HIPAA and cyber-insurance readiness",
      "Incident-response runbooks and tabletop exercises"]),
    ("apps", "03", "Application development &amp; integration",
     "Build the thing that doesn&rsquo;t exist yet &mdash; and connect the ten that already do.",
     "Internal tools, workflow automation, reporting layers and the integrations that stop your team from re-typing data between systems.",
     ["Internal line-of-business applications",
      "Workflow automation and process re-engineering",
      "API and system-to-system integration",
      "Reporting and dashboard layers over existing data",
      "Legacy application assessment and modernisation"]),
    ("advisory", "04", "IT strategy &amp; advisory",
     "A roadmap your leadership can approve and your team can execute.",
     "For organisations without a CIO, or with one who needs a second opinion. Vendor selection, budget planning and the honest read on what to do first.",
     ["Technology roadmap and multi-year budget planning",
      "Vendor evaluation, RFP support and contract review",
      "Fractional IT leadership and steering-committee support",
      "Due-diligence and post-acquisition IT integration",
      "Build-versus-buy analysis"]),
]

BUY = [
    ("Assessment", "Fixed fee", "A scoped, written deliverable in two to four weeks. Findings, options with costs, a recommendation. Yours to keep whether or not you hire us for delivery."),
    ("Project delivery", "Fixed fee or milestone", "A defined outcome with a named owner, a written plan and weekly status. Change orders in writing before scope moves."),
    ("Ongoing advisory", "Monthly retainer", "A set number of hours a month for architecture review, escalations and roadmap work. Cancel with thirty days&rsquo; notice."),
]


def services():
    rows = ""
    for anchor, n, title, tag, body, items in SERVICES:
        li = "".join(f"<li>{i}</li>" for i in items)
        rows += f'''<article class="row rv" id="{anchor}">
  <span class="row__n">{n}</span>
  <div>
    <h3>{title}</h3>
    <p style="margin-top:.7rem;color:var(--text)">{tag}</p>
    <p style="margin-top:.7rem">{body}</p>
  </div>
  <ul class="pcard" style="border:0;background:none;padding:0;display:grid;gap:.45rem;list-style:none;margin:0">{li}</ul>
</article>'''

    buy = "".join(
        f'<div class="card"><span class="mono">{t}</span><h3 style="margin-top:1rem">{n}</h3><p style="margin-top:.6rem">{d}</p></div>'
        for n, t, d in BUY)

    return head("IT Consulting — ThabTech",
                "Cloud and infrastructure, cybersecurity and compliance, application development, and IT strategy. Fixed-fee assessments and defined-outcome delivery.",
                "services.html") + f'''
{hero("Consulting",
      "Advice you can act on, delivered by the people who&rsquo;ll build it.",
      "Four practice areas. Every engagement starts with a written, fixed-fee assessment, so you see the plan and the cost before you commit to delivery.",
      art="assets/atmo-machined.webp")}

<section class="sec">
<div class="wrap">
  <div class="head rv">
    <span class="eyebrow">Practice areas</span>
    <h2>What we&rsquo;re actually good at.</h2>
  </div>
  <div class="rows">{rows}</div>
</div>
</section>

<section class="band sec">
<div class="wrap">
  <div class="head head--wide rv">
    <span class="eyebrow">Commercials</span>
    <h2>Three ways to buy consulting from us.</h2>
    <p class="lead">Pick the one that matches your risk tolerance. Most clients start with an assessment and decide from there.</p>
  </div>
  <div class="grid g-3 rv-s">{buy}</div>
</div>
</section>

<section class="sec sec--tight">
<div class="wrap">
  <div class="spec rv">
    <div class="spec__r"><div class="spec__k">Also available</div><div class="spec__v">AI enablement, AI governance and model risk management run as a separate practice with its own frameworks and deliverables.<br><a class="tlink" style="margin-top:.6rem" href="ai.html">See AI &amp; risk management {ARROW}</a></div></div>
  </div>
</div>
</section>

{CTA}
''' + FOOTER


# ============================================================ STAFFING
MODELS = [
    ("Contract", "Weekly rate, no conversion fee after 1,040 hours",
     "For surge capacity, parental-leave cover and defined projects. We carry the employment, payroll, taxes and insurance."),
    ("Contract-to-hire", "Convert at any point on a declining fee",
     "Try before you commit. The candidate works as our employee, and you convert them to your payroll when you&rsquo;re confident."),
    ("Direct hire", "Percentage of first-year base, guaranteed 90 days",
     "For permanent roles. If the placement doesn&rsquo;t last ninety days, we replace them or refund."),
    ("SOW project team", "Fixed fee against a defined outcome",
     "When you want the outcome rather than the headcount. We assemble and manage the team and own the deliverable."),
]

VETTING = [
    ("01", "Technical screen by a practitioner", "Every candidate is screened by someone who has held the role. Not a keyword match against your job description."),
    ("02", "Work-history verification", "We confirm the last two engagements directly. Titles, dates, and what they actually owned versus what the résumé claims."),
    ("03", "Written submission summary", "You get a one-page brief per candidate: strengths, gaps, rate expectation, availability and why we think it fits."),
    ("04", "Post-placement check-ins", "Day 7, day 30 and day 90 with both sides. Problems surface while they&rsquo;re still cheap to fix."),
]

ROLES = ["Cloud Engineer", "DevOps Engineer", "Site Reliability Engineer", "Systems Administrator",
         "Network Engineer", "Security Analyst", "Security Engineer", "GRC Analyst",
         "Identity &amp; Access Engineer", "Data Engineer", "Data Analyst", "BI Developer",
         "Database Administrator", "Software Engineer", "Front-End Engineer", "Back-End Engineer",
         "Full-Stack Engineer", "QA Engineer", "Business Analyst", "Systems Analyst",
         "Project Manager", "Scrum Master", "Product Owner", "Help Desk Analyst",
         "Desktop Support Technician", "ERP / Workday Analyst", "Salesforce Administrator",
         "Technical Writer"]


def staffing():
    models = "".join(
        f'<div class="card"><h3>{n}</h3><p class="mono" style="margin-top:.7rem;color:var(--ember)">{t}</p>'
        f'<p style="margin-top:.8rem">{d}</p></div>'
        for n, t, d in MODELS)

    vet = "".join(
        f'<div class="step"><span class="step__n">{n}</span><h3>{t}</h3><p>{d}</p></div>'
        for n, t, d in VETTING)

    chips = "".join(f'<span class="chip">{r}</span>' for r in ROLES)

    return head("Technical Staffing — ThabTech",
                "Contract, contract-to-hire and direct-hire technical staffing for infrastructure, security, data and application teams. Screened by practitioners, nationwide.",
                "staffing.html") + f'''
{hero("Staffing",
      "The right engineer, not the fastest résumé.",
      "Contract, contract-to-hire, direct placement and SOW project teams. Every candidate is screened by someone who has held the role, and you see our reasoning in writing.",
      art="assets/atmo-network.webp")}

<section class="sec" id="models">
<div class="wrap">
  <div class="head head--wide rv">
    <span class="eyebrow">Engagement models</span>
    <h2>Four ways to add capacity.</h2>
    <p class="lead">Terms are written down before we send a single résumé. No surprise conversion fees, no hidden markup escalators.</p>
  </div>
  <div class="grid g-4 rv-s">{models}</div>
</div>
</section>

<section class="band sec" id="vetting">
<div class="wrap">
  <div class="head head--wide rv">
    <span class="eyebrow">How we vet</span>
    <h2>Four filters before a résumé reaches you.</h2>
    <p class="lead">A staffing firm&rsquo;s only real product is judgement. Here is ours, written down so you can hold us to it.</p>
  </div>
  <div class="steps">{vet}</div>
</div>
</section>

<section class="sec" id="roles">
<div class="wrap">
  <div class="head rv">
    <span class="eyebrow">Coverage</span>
    <h2>Roles we fill.</h2>
    <p>If a role isn&rsquo;t listed, ask. We&rsquo;d rather tell you it&rsquo;s outside our network than waste three weeks of your search.</p>
  </div>
  <div class="chips rv">{chips}</div>
</div>
</section>

<section class="sec sec--tight" id="candidates">
<div class="wrap">
  <div class="grid g-2 rv-s">
    <div class="card">
      <span class="mono">For hiring managers</span>
      <h3 style="margin-top:1rem">Send the role, get a shortlist</h3>
      <p style="margin-top:.8rem">Give us the job description, the rate range and your must-haves. You&rsquo;ll get a small, reasoned shortlist &mdash; not a volume dump you have to filter yourself.</p>
      <a class="tlink" style="margin-top:1.2rem" href="contact.html">Submit a role {ARROW}</a>
    </div>
    <div class="card">
      <span class="mono">For candidates</span>
      <h3 style="margin-top:1rem">We&rsquo;ll tell you the truth about the role</h3>
      <p style="margin-top:.8rem">Real rate ranges, real conversion odds, real reason the last person left. Send a résumé and the kind of work you want next &mdash; we won&rsquo;t submit you anywhere without asking first.</p>
      <a class="tlink" style="margin-top:1.2rem" href="contact.html">Send your résumé {ARROW}</a>
    </div>
  </div>
</div>
</section>

{CTA}
''' + FOOTER


# ============================================================ ABOUT
COMMITMENTS = [
    ("01", "We put it in writing", "Scope, price, assumptions and risks. If it wasn&rsquo;t written down, it isn&rsquo;t part of the engagement &mdash; in either direction."),
    ("02", "We tell you when it&rsquo;s not us", "If your problem is outside what we do well, we&rsquo;ll say so on the first call and point you somewhere better."),
    ("03", "We don&rsquo;t create dependency", "Documentation and runbooks are a deliverable, not an upsell. You should be able to end the engagement and still operate."),
    ("04", "One named owner", "Every engagement has a single person accountable for it. You always know who to call, and they answer."),
]

CAPABILITY = [
    ("Legal name", "ThabTech LLC"),
    ("Entity type", "Limited Liability Company &middot; United States"),
    ("Core competencies", "IT consulting &middot; cloud &amp; infrastructure modernisation &middot; cybersecurity &amp; compliance readiness &middot; AI enablement &amp; AI governance &middot; model risk management &middot; technology &amp; enterprise risk &middot; application development &amp; integration &middot; IT strategy &amp; advisory &middot; technical staffing"),
    ("Service delivery", "Remote nationwide &middot; on-site by arrangement &middot; headquartered in Dallas, Texas"),
    ("NAICS codes", "541512 Computer Systems Design Services &middot; 541511 Custom Computer Programming Services &middot; 541519 Other Computer Related Services &middot; 541618 Other Management Consulting Services &middot; 561320 Temporary Help Services &middot; 541612 Human Resources Consulting"),
    ("Contract vehicles", "Time &amp; materials &middot; fixed fee &middot; milestone &middot; staffing MSA &middot; statement of work &middot; subcontract to prime"),
    ("Documentation", "W-9 &middot; certificate of insurance &middot; MSA and mutual NDA templates &middot; signed vendor forms on request"),
    ("Point of contact", "support@thabtech.com &middot; 866&thinsp;755&thinsp;6007"),
    ("Business hours", "Monday&ndash;Friday, 9:00&nbsp;am &ndash; 5:00&nbsp;pm Central"),
]


def about():
    comm = "".join(
        f'<div class="step"><span class="step__n">{n}</span><h3>{t}</h3><p>{d}</p></div>'
        for n, t, d in COMMITMENTS)

    spec = "".join(
        f'<div class="spec__r"><div class="spec__k">{k}</div><div class="spec__v">{v}</div></div>'
        for k, v in CAPABILITY)

    return head("About — ThabTech",
                "ThabTech LLC is an IT consulting and technical staffing firm based in Dallas, Texas. Capability statement, NAICS codes and procurement documentation.",
                "about.html") + f'''
{hero("About ThabTech",
      "The gap between the plan and the people.",
      "ThabTech exists because that gap is where most technology projects fail &mdash; and because no one was accountable for both sides of it.",
      art="assets/atmo-bloom.webp",
      btns=f'<a class="btn btn--primary" href="#capability">Capability statement {ARROW}</a>'
           f'<a class="btn btn--ghost" href="contact.html">Start a conversation</a>')}

<section class="sec">
<div class="wrap">
  <div class="grid g-2 rv-s" style="align-items:start;gap:clamp(2rem,5vw,4rem)">
    <div>
      <span class="eyebrow">Why we exist</span>
      <h2>Good advice, no one to execute it.</h2>
    </div>
    <div style="display:grid;gap:1.15rem">
      <p class="lead">The pattern repeats. An organisation buys a strategy deck, agrees with it, and then discovers there&rsquo;s no one internally with the time or the skill set to carry it out. Six months later the deck is stale and the problem is worse.</p>
      <p>The reverse happens too. A team hires three contractors quickly, without a plan for what they&rsquo;re building toward, and ends up with three different opinions and no architecture.</p>
      <p>ThabTech was built to own both halves. We write the plan, and we can supply or place the people who execute it &mdash; so the person who has to live with the recommendation is the person who made it.</p>
      <p>Our mission is straightforward: empower businesses with the right technology and the right talent, at the right time.</p>
    </div>
  </div>
</div>
</section>

<section class="band sec">
<div class="wrap">
  <div class="head head--wide rv">
    <span class="eyebrow">How we operate</span>
    <h2>Four commitments we&rsquo;ll be judged on.</h2>
  </div>
  <div class="steps">{comm}</div>
</div>
</section>

<section class="sec" id="capability">
<div class="wrap">
  <div class="head head--wide rv">
    <span class="eyebrow">Procurement</span>
    <h2>Capability statement.</h2>
    <p class="lead">Everything a vendor-onboarding form or bid package typically asks for, in one place. Need it as a signed PDF on your template? Ask and it&rsquo;ll be back the same day.</p>
  </div>
  <div class="spec rv">{spec}</div>
</div>
</section>

{CTA}
''' + FOOTER


# ============================================================ AI & RISK
AI_AREAS = [
    ("enablement", "01", "AI enablement",
     "Find the two use cases worth building &mdash; and kill the eight that aren&rsquo;t.",
     "Most AI programmes stall because they start with a tool and hunt for a problem. We start with your processes, score candidate use cases on value against feasibility and risk, and build the short list you can actually fund.",
     ["AI opportunity assessment across a business function",
      "Use-case scoring: value, data readiness, risk, effort",
      "Data-readiness review &mdash; quality, access, lineage, retention",
      "Pilot build on Azure OpenAI, Amazon Bedrock or Copilot",
      "Retrieval-augmented generation over your own documents",
      "Adoption plan, training and change management"]),
    ("governance", "02", "AI governance",
     "The policy, the inventory and the evidence trail &mdash; before someone asks for it.",
     "Governance is what turns a pilot into something your board, your auditor and your customers can live with. We build to the recognised frameworks so your position is defensible rather than improvised.",
     ["AI policy, acceptable-use standards and role definitions",
      "AI system inventory and risk tiering",
      "NIST AI RMF alignment across Govern, Map, Measure and Manage",
      "ISO/IEC 42001 readiness and Statement of Applicability support",
      "EU AI Act applicability screening and transparency obligations",
      "Third-party and vendor AI due-diligence questionnaires",
      "Human-oversight design, logging and incident escalation paths"]),
    ("model-risk", "03", "Model risk management",
     "Independent challenge, documented validation and a model inventory that holds up.",
     "For lenders, insurers and anyone whose decisions ride on a model. Built on the supervisory expectations regulated institutions are already measured against &mdash; conceptually sound development, ongoing monitoring, and outcomes analysis that back-tests against reality.",
     ["Model inventory build-out and risk-tier assignment",
      "Independent validation and effective-challenge reviews",
      "Model documentation to supervisory standard",
      "Ongoing monitoring, drift detection and outcomes analysis",
      "Fair-lending and adverse-action explainability review",
      "Remediation plans and issue tracking to closure"]),
    ("enterprise-risk", "04", "Technology &amp; enterprise risk",
     "Risk work that produces decisions, not a register nobody reads.",
     "Risk and control assessments, issue management and the reporting layer that lets leadership see what is actually exposed. Practical process design over framework theatre.",
     ["Technology risk and control self-assessment design",
      "Control testing, gap analysis and remediation roadmaps",
      "Third-party and vendor risk programme build",
      "Issue and action management with traceable ownership",
      "Business-continuity and operational-resilience testing",
      "Executive and board-level risk reporting"]),
]

FRAMEWORKS = [
    ("NIST AI RMF 1.0",
     "Voluntary &middot; United States",
     "Four functions &mdash; Govern, Map, Measure, Manage &mdash; give the organisation a shared vocabulary for AI risk. Voluntary and non-certifiable; the deliverable is an internal operating model.",
     "https://airc.nist.gov/docs/NIST_AI_RMF_to_ISO_IEC_42001_Crosswalk.pdf",
     "NIST AI RMF to ISO/IEC 42001 crosswalk"),
    ("ISO/IEC 42001:2023",
     "Certifiable &middot; International",
     "The AI management-system standard. Same clause structure as ISO 27001, plus an AI-specific control catalogue in Annex A. This is the instrument you can actually be certified against.",
     "https://airc.nist.gov/docs/NIST_AI_RMF_to_ISO_IEC_42001_Crosswalk.pdf",
     "NIST crosswalk to ISO/IEC 42001"),
    ("EU AI Act",
     "Binding law &middot; European Union",
     "Risk-tiered regulation. Transparency duties under Article&nbsp;50 have applied since 2&nbsp;August&nbsp;2026, and the high-risk obligations for Annex&nbsp;III use cases now run to 2&nbsp;December&nbsp;2027 following the AI Omnibus amendment.",
     "https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai",
     "European Commission AI Act overview"),
    ("SR 11-7 &amp; SR 26-2",
     "Supervisory guidance &middot; US banking",
     "The Federal Reserve and OCC guidance on model risk management: sound development, independent validation, and governance with real effective challenge. SR&nbsp;26-2 is the 2026 revision of the original 2011 letter.",
     "https://www.federalreserve.gov/supervisionreg/srletters/SR2602.pdf",
     "Federal Reserve SR 26-2, Revised Guidance on Model Risk Management"),
]

AI_SIGNALS = [
    ("01", "&ldquo;We have twelve pilots and nothing in production&rdquo;",
     "Usually a scoping problem, not a technology problem. Nobody defined what &lsquo;working&rsquo; meant or who owned the decision to ship."),
    ("02", "&ldquo;Legal won&rsquo;t sign off and we don&rsquo;t know why&rdquo;",
     "There is no policy, no inventory and no impact assessment to point at. Governance is the unblock, not the obstacle."),
    ("03", "&ldquo;Our people are already pasting data into chatbots&rdquo;",
     "Shadow AI is a symptom of an unmet need plus an unwritten rule. Give them a sanctioned path and a clear line they can see."),
    ("04", "&ldquo;A regulator or a client asked how the model decides&rdquo;",
     "This is a documentation and validation gap. It is fixable, but not on the timeline of the request unless the inventory already exists."),
]

AI_DELIVER = [
    ("AI readiness assessment", "Fixed fee &middot; 2&ndash;4 weeks",
     "A scored use-case short list, a data-readiness read, a risk and regulatory applicability screen, and a costed recommendation on what to build first."),
    ("Governance build", "Fixed fee or milestone",
     "Policy, inventory, risk tiering, impact-assessment template and oversight design, mapped to NIST AI RMF and ISO/IEC 42001 so the evidence trail exists from day one."),
    ("Validation &amp; risk review", "Fixed fee per model or scope",
     "Independent challenge on a model or an AI system: documentation review, testing, findings rated by severity, and a remediation plan with owners and dates."),
]


def ai():
    rows = ""
    for anchor, n, title, tag, body, items in AI_AREAS:
        li = "".join(f"<li>{i}</li>" for i in items)
        rows += f'''<article class="row rv" id="{anchor}">
  <span class="row__n">{n}</span>
  <div>
    <h3>{title}</h3>
    <p style="margin-top:.7rem;color:var(--text)">{tag}</p>
    <p style="margin-top:.7rem">{body}</p>
  </div>
  <ul class="pcard" style="border:0;background:none;padding:0;display:grid;gap:.45rem;list-style:none;margin:0">{li}</ul>
</article>'''

    fw = "".join(
        f'''<div class="card"><span class="mono">{scope}</span>
<h3 style="margin-top:1rem">{name}</h3>
<p style="margin-top:.7rem">{desc}</p>
<a class="tlink" style="margin-top:1rem" href="{url}" target="_blank" rel="noopener">{label} {ARROW}</a></div>'''
        for name, scope, desc, url, label in FRAMEWORKS)

    signals = "".join(
        f'''<div class="card"><span class="card__n">{n}</span><h3>{t}</h3><p>{d}</p></div>'''
        for n, t, d in AI_SIGNALS)

    deliver = "".join(
        f'''<div class="card"><span class="mono" style="color:var(--ember)">{t}</span>
<h3 style="margin-top:1rem">{n}</h3><p style="margin-top:.6rem">{d}</p></div>'''
        for n, t, d in AI_DELIVER)

    return head("AI &amp; Risk Management — ThabTech",
                "AI enablement, AI governance, model risk management and technology risk. Built to NIST AI RMF, ISO/IEC 42001, the EU AI Act and US model-risk supervisory guidance.",
                "ai.html") + f'''
{hero("AI enablement &amp; risk management",
      "Deploy AI you can defend in an audit.",
      "We help you find the AI use cases worth funding, build them safely, and stand up the governance and model-risk structure that keeps them running when someone starts asking questions.",
      art="assets/atmo-gates.webp",
      btns=f'<a class="btn btn--primary" href="contact.html">Book an AI readiness assessment {ARROW}</a>'
           f'<a class="btn btn--ghost" href="#frameworks">Frameworks we build to</a>')}

<section class="sec">
<div class="wrap">
  <div class="grid g-2 rv-s" style="align-items:start;gap:clamp(2rem,5vw,4rem)">
    <div>
      <span class="eyebrow">The problem</span>
      <h2>Everyone has a pilot. Almost nobody has a control.</h2>
    </div>
    <div style="display:grid;gap:1.15rem">
      <p class="lead">AI moved from experiment to expectation faster than most organisations could build the scaffolding around it. The result is a familiar split: enthusiastic pilots on one side, and a legal, risk or audit function on the other that has no way to say yes.</p>
      <p>Both halves are solvable, but not separately. A use case scoped without a risk view gets blocked late and expensively. A governance programme built without knowing what the business is actually trying to do produces a policy nobody follows.</p>
      <p>We work both halves in the same engagement &mdash; the same team that scopes the use case writes the impact assessment, so the control design and the build assumption never drift apart.</p>
    </div>
  </div>
</div>
</section>

<section class="band sec">
<div class="wrap">
  <div class="head rv">
    <span class="eyebrow">Where we usually come in</span>
    <h2>Four sentences we hear a lot.</h2>
  </div>
  <div class="bento rv-s">{signals}</div>
</div>
</section>

<section class="sec">
<div class="wrap">
  <div class="head rv">
    <span class="eyebrow">Practice areas</span>
    <h2>What this practice covers.</h2>
  </div>
  <div class="rows">{rows}</div>
</div>
</section>

<section class="band sec" id="frameworks">
<div class="wrap">
  <div class="head head--wide rv">
    <span class="eyebrow">Standards</span>
    <h2>We build to the frameworks your auditor already knows.</h2>
    <p class="lead">Nothing bespoke, nothing invented. These four are the instruments that AI and model governance consolidates around, and they are complementary rather than competing &mdash; one supplies the risk vocabulary, one makes it a certifiable management system, one makes parts of it law, and one sets the supervisory bar for models that drive decisions.</p>
  </div>
  <div class="grid g-2 rv-s">{fw}</div>
</div>
</section>

<section class="sec">
<div class="wrap">
  <div class="head head--wide rv">
    <span class="eyebrow">Commercials</span>
    <h2>Three ways to start.</h2>
    <p class="lead">Most clients begin with a readiness assessment. It is a fixed fee, it produces a document you keep, and it is deliberately structured so you can take it elsewhere if you would rather.</p>
  </div>
  <div class="grid g-3 rv-s">{deliver}</div>
</div>
</section>

<section class="sec sec--tight">
<div class="wrap">
  <div class="spec rv">
    <div class="spec__r"><div class="spec__k">A note on scope</div><div class="spec__v">We are a consulting and staffing firm, not a law firm and not an accredited certification body. We prepare you for certification and audit, and we work alongside your counsel &mdash; we do not issue certificates or legal opinions.<br><span class="muted">Regulatory dates and framework requirements change. Anything time-sensitive gets re-confirmed against the primary source at the start of an engagement.</span></div></div>
  </div>
</div>
</section>

{CTA}
''' + FOOTER


# ============================================================ CONTACT
def contact():
    opts = ["IT consulting engagement", "AI enablement or AI governance",
            "Model risk / technology risk review", "Technical staffing &mdash; contract",
            "Technical staffing &mdash; direct hire", "I&rsquo;m a candidate looking for work",
            "Vendor onboarding / documentation request", "Something else"]
    options = "".join(f'<option>{o}</option>' for o in opts)

    cards = [
        ("Hiring managers", "Send the job description, the rate or salary range and your two non-negotiables. A shortlist follows, usually within a week."),
        ("Candidates", "Send a résumé and the kind of work you want next. We won&rsquo;t submit you anywhere without asking you first."),
        ("Procurement &amp; primes", "W-9, COI, NAICS codes and MSA templates are ready now. Send your vendor form and it comes back completed."),
    ]
    audience = "".join(
        f'<div class="card"><span class="mono">{t}</span><p style="margin-top:.9rem">{d}</p></div>'
        for t, d in cards)

    return head("Contact — ThabTech",
                "Contact ThabTech LLC for IT consulting, technical staffing, or vendor documentation. support@thabtech.com — 866 755 6007.",
                "contact.html") + f'''
{hero("Contact",
      "Start a conversation.",
      "A few sentences is enough. Tell us the situation and you&rsquo;ll get a reply from a person, normally within one business day.",
      art="assets/atmo-lattice.webp",
      btns=f'<a class="btn btn--primary" href="mailto:support@thabtech.com">Email support@thabtech.com {ARROW}</a>'
           f'<a class="btn btn--ghost" href="tel:+18667556007">866 755 6007</a>')}

<section class="sec">
<div class="wrap">
  <div class="grid g-2 rv-s" style="align-items:start;gap:clamp(2rem,5vw,3.5rem)">
    <div>
      <span class="eyebrow">Send a message</span>
      <h2 style="font-size:var(--t-h3);margin-bottom:1.5rem">Tell us what you need</h2>
      <form class="form" onsubmit="event.preventDefault();this.querySelector('.note').textContent='This is a design mockup — the live form will deliver to support@thabtech.com.';">
        <div class="f-row">
          <label class="field-l"><span>Name</span><input type="text" name="name" autocomplete="name" required></label>
          <label class="field-l"><span>Company</span><input type="text" name="company" autocomplete="organization"></label>
        </div>
        <div class="f-row">
          <label class="field-l"><span>Email</span><input type="email" name="email" autocomplete="email" required></label>
          <label class="field-l"><span>Phone</span><input type="tel" name="phone" autocomplete="tel"></label>
        </div>
        <label class="field-l"><span>What do you need?</span><select name="topic">{options}</select></label>
        <label class="field-l"><span>Details</span><textarea name="message" placeholder="What&rsquo;s the situation, what have you already tried, and what does a good outcome look like?" required></textarea></label>
        <button class="btn btn--primary" type="submit" style="justify-self:start">Send message {ARROW}</button>
        <p class="note">Mockup form &mdash; on the live site this delivers to support@thabtech.com.</p>
      </form>
    </div>
    <div>
      <span class="eyebrow">Direct</span>
      <h2 style="font-size:var(--t-h3);margin-bottom:1.5rem">Reach us without the form</h2>
      <div class="spec">
        <div class="spec__r"><div class="spec__k">Email</div><div class="spec__v"><a href="mailto:support@thabtech.com" style="color:var(--ember)">support@thabtech.com</a></div></div>
        <div class="spec__r"><div class="spec__k">Phone</div><div class="spec__v"><a href="tel:+18667556007" style="color:var(--ember)">866&thinsp;755&thinsp;6007</a></div></div>
        <div class="spec__r"><div class="spec__k">Hours</div><div class="spec__v">Monday&ndash;Friday, 9:00&nbsp;am &ndash; 5:00&nbsp;pm Central<br><span class="muted">Closed Saturday and Sunday</span></div></div>
        <div class="spec__r"><div class="spec__k">Based in</div><div class="spec__v">Dallas, Texas<br><span class="muted">Serving clients nationwide</span></div></div>
        <div class="spec__r"><div class="spec__k">Response time</div><div class="spec__v">Within one business day</div></div>
      </div>
    </div>
  </div>
</div>
</section>

<section class="band sec sec--tight">
<div class="wrap">
  <div class="head rv"><span class="eyebrow">What to send</span><h2 style="font-size:var(--t-h2)">Three kinds of enquiry.</h2></div>
  <div class="grid g-3 rv-s">{audience}</div>
</div>
</section>
''' + FOOTER


PAGES = {"index.html": home, "services.html": services, "ai.html": ai,
         "staffing.html": staffing, "about.html": about, "contact.html": contact}

if __name__ == "__main__":
    for name, fn in PAGES.items():
        (OUT / name).write_text(fn(), encoding="utf-8")
        print("wrote", name)
