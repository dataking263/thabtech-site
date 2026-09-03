#!/usr/bin/env python3
"""Generate the ThabTech static site."""
import pathlib

OUT = pathlib.Path(__file__).parent

LOGO = """<svg viewBox="0 0 32 32" fill="none" aria-hidden="true"><rect x="1" y="4" width="30" height="4.2" fill="currentColor"/><rect x="13.9" y="8.2" width="4.2" height="19.8" fill="currentColor"/><rect x="21.4" y="14" width="9.6" height="4.2" fill="var(--accent)"/></svg>"""

ARROW = """<svg width="14" height="14" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M2 8h11M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="square"/></svg>"""

NAV = [
    ("index.html", "Home"),
    ("services.html", "Consulting"),
    ("staffing.html", "Staffing"),
    ("about.html", "About"),
    ("contact.html", "Contact"),
]

EMAIL = "support@thabtech.com"
PHONE_D = "866-755-6007"
PHONE_H = "tel:+18667556007"


def head(title, desc, page):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:image" content="assets/hero.webp">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' fill='%2316171A'/%3E%3Crect x='4' y='7' width='24' height='3.4' fill='%23EAE7E2'/%3E%3Crect x='14.3' y='10.4' width='3.4' height='15' fill='%23EAE7E2'/%3E%3Crect x='20.5' y='14.8' width='7.5' height='3.4' fill='%23DE8B4C'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://api.fontshare.com">
<link href="https://api.fontshare.com/v2/css?f[]=cabinet-grotesk@700,800&f[]=satoshi@400,500,700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{header(page)}
<main id="main">
"""


def header(page):
    links = "".join(
        f'<a href="{h}"{" aria-current=\"page\"" if h == page else ""}>{t}</a>'
        for h, t in NAV[:-1]
    )
    return f"""<header class="header">
  <div class="header__inner">
    <a class="brand" href="index.html" aria-label="ThabTech home">{LOGO}<span class="brand__name">Thab<em>Tech</em></span></a>
    <nav class="nav" id="nav" aria-label="Main">
      {links}
      <a class="btn btn--primary" href="contact.html">Start a conversation {ARROW}</a>
    </nav>
    <div class="header__actions">
      <button class="icon-btn" id="theme-toggle" type="button" aria-label="Switch color theme">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><circle cx="12" cy="12" r="4.5"/><path d="M12 2v2M12 20v2M4.2 4.2l1.4 1.4M18.4 18.4l1.4 1.4M2 12h2M20 12h2M4.2 19.8l1.4-1.4M18.4 5.6l1.4-1.4"/></svg>
      </button>
      <button class="icon-btn menu-btn" id="menu-btn" type="button" aria-label="Toggle menu" aria-expanded="false" aria-controls="nav">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M3 7h18M3 12h18M3 17h18"/></svg>
      </button>
    </div>
  </div>
</header>"""


CTA = f"""<section class="cta section">
  <div class="wrap cta__inner">
    <div>
      <p class="eyebrow">Next step</p>
      <h2 class="h-sec">Tell us what's breaking, stalling, or unstaffed.</h2>
      <p>One call. We'll tell you honestly whether this is a consulting problem, a staffing problem, or something you can fix without us.</p>
    </div>
    <div class="btn-row">
      <a class="btn btn--primary" href="contact.html">Start a conversation {ARROW}</a>
      <a class="btn btn--on-ink" href="mailto:{EMAIL}">{EMAIL}</a>
    </div>
  </div>
</section>"""


FOOTER = f"""</main>
<footer class="footer">
  <div class="wrap">
    <div class="footer__grid">
      <div>
        <a class="brand" href="index.html" aria-label="ThabTech home">{LOGO}<span class="brand__name">Thab<em>Tech</em></span></a>
        <p class="footer__tag">An IT consulting and staffing firm. The right technology and the right talent, at the right time.</p>
      </div>
      <div>
        <h3>Services</h3>
        <ul>
          <li><a href="services.html#cloud">Cloud &amp; Infrastructure</a></li>
          <li><a href="services.html#security">Cybersecurity &amp; Compliance</a></li>
          <li><a href="services.html#apps">Applications</a></li>
          <li><a href="services.html#advisory">IT Strategy &amp; Advisory</a></li>
        </ul>
      </div>
      <div>
        <h3>Staffing</h3>
        <ul>
          <li><a href="staffing.html#models">Engagement models</a></li>
          <li><a href="staffing.html#roles">Roles we fill</a></li>
          <li><a href="staffing.html#vetting">How we vet</a></li>
          <li><a href="staffing.html#candidates">For candidates</a></li>
        </ul>
      </div>
      <div>
        <h3>Company</h3>
        <ul>
          <li><a href="about.html">About ThabTech</a></li>
          <li><a href="about.html#capability">Capability statement</a></li>
          <li><a href="contact.html">Contact</a></li>
          <li><a href="{PHONE_H}">{PHONE_D}</a></li>
        </ul>
      </div>
    </div>
    <div class="footer__bar">
      <span>&copy; 2026 ThabTech LLC. All rights reserved.</span>
      <span>Mon&ndash;Fri, 9:00 am &ndash; 5:00 pm &middot; <a href="mailto:{EMAIL}">{EMAIL}</a></span>
    </div>
  </div>
</footer>
<script>
(function () {{
  var root = document.documentElement;
  var mq = window.matchMedia('(prefers-color-scheme: dark)');
  var theme = mq.matches ? 'dark' : 'light';
  root.setAttribute('data-theme', theme);
  document.getElementById('theme-toggle').addEventListener('click', function () {{
    theme = theme === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-theme', theme);
  }});

  var nav = document.getElementById('nav');
  var mb = document.getElementById('menu-btn');
  mb.addEventListener('click', function () {{
    var open = nav.getAttribute('data-open') === 'true';
    nav.setAttribute('data-open', String(!open));
    mb.setAttribute('aria-expanded', String(!open));
  }});

  var io = new IntersectionObserver(function (entries) {{
    entries.forEach(function (e) {{ if (e.isIntersecting) {{ e.target.classList.add('is-in'); io.unobserve(e.target); }} }});
  }}, {{ rootMargin: '0px 0px -8% 0px', threshold: 0.05 }});
  document.querySelectorAll('.reveal').forEach(function (el, i) {{
    el.style.transitionDelay = (Math.min(i % 4, 3) * 70) + 'ms';
    io.observe(el);
  }});
}})();
</script>
</body>
</html>"""


# ---------------------------------------------------------------- pages

INDEX = f"""<section class="hero">
  <div class="hero__media"><img src="assets/hero.webp" alt="A data center corridor lit by a single warm light along ranks of server cabinets." fetchpriority="high"></div>
  <div class="hero__inner">
    <p class="eyebrow">IT Consulting &amp; Staffing</p>
    <h1 class="h-hero">Your systems are only as strong as the people behind them.</h1>
    <p class="hero__lede">ThabTech modernizes the infrastructure your business runs on &mdash; and places the engineers who keep it running. One firm, both halves of the problem.</p>
    <div class="btn-row">
      <a class="btn btn--primary" href="contact.html">Start a conversation {ARROW}</a>
      <a class="btn btn--on-ink" href="about.html#capability">View capability statement</a>
    </div>
  </div>
  <dl class="statbar">
    <div><dt>Consulting</dt><dd>Cloud, infrastructure, security, and application modernization</dd></div>
    <div><dt>Staffing</dt><dd>Contract, contract-to-hire, and direct placement</dd></div>
    <div><dt>Coverage</dt><dd>US-based engagements, remote and on-site</dd></div>
    <div><dt>Response</dt><dd>Every inquiry answered within one business day</dd></div>
  </dl>
</section>

<section class="section">
  <div class="wrap split">
    <div class="sticky-head reveal">
      <p class="eyebrow">What we do</p>
      <h2 class="h-sec">Two disciplines, one accountability.</h2>
      <p class="lede mt-6">Most firms sell you a roadmap or sell you a resume. We do both, which means we can't hand off the hard part and walk away.</p>
    </div>
    <ol class="caplist reveal">
      <li><span class="num">01</span>
        <div><h3 class="h-card">Assess what you actually have</h3>
        <p>Before recommending anything, we document the current state &mdash; systems, dependencies, licensing, risk, and the institutional knowledge that lives in one person's head.</p></div>
      </li>
      <li><span class="num">02</span>
        <div><h3 class="h-card">Design for the budget in front of you</h3>
        <p>Architecture that fits your constraints, not a vendor's product catalog. We tell you which problems are worth solving now and which can wait a fiscal year.</p></div>
      </li>
      <li><span class="num">03</span>
        <div><h3 class="h-card">Deliver with people who stay accountable</h3>
        <p>Our consultants execute the work. When you need capacity beyond the engagement, our staffing practice places vetted engineers into the same environment.</p></div>
      </li>
      <li><span class="num">04</span>
        <div><h3 class="h-card">Hand over something maintainable</h3>
        <p>Documentation, runbooks, and knowledge transfer are part of the scope &mdash; not an upsell. You should be able to fire us and still be fine.</p></div>
      </li>
    </ol>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap cards">
    <article class="card card--feature reveal">
      <img src="assets/consulting.webp" alt="Graphite blocks and copper rods arranged in a precise modular grid." loading="lazy">
      <div class="card__body">
        <p class="eyebrow eyebrow--plain">Practice 01</p>
        <h3 class="h-sub">IT Consulting</h3>
        <p>Cloud migration, infrastructure optimization, cybersecurity and compliance, and application development &mdash; scoped as fixed engagements with defined deliverables.</p>
        <div class="card__foot"><a class="arrow-link" href="services.html">Explore consulting services {ARROW}</a></div>
      </div>
    </article>
    <article class="card card--feature reveal">
      <img src="assets/staffing.webp" alt="Two colleagues reviewing work together at a monitor in a bright office." loading="lazy">
      <div class="card__body">
        <p class="eyebrow eyebrow--plain">Practice 02</p>
        <h3 class="h-sub">IT Staffing</h3>
        <p>Contract, contract-to-hire, and direct placement for technical roles. Screened by people who have done the job, not by keyword match.</p>
        <div class="card__foot"><a class="arrow-link" href="staffing.html">Explore staffing services {ARROW}</a></div>
      </div>
    </article>
  </div>
</section>

<section class="band section">
  <div class="wrap">
    <div style="max-width:52ch">
      <p class="eyebrow">How engagements run</p>
      <h2 class="h-sec">A predictable sequence, every time.</h2>
    </div>
    <div class="steps mt-12">
      <div class="reveal"><span class="num">Step 01</span><h3 class="h-card">Discovery call</h3><p>30 minutes. We learn the problem, the deadline, and the constraint. No pitch deck.</p></div>
      <div class="reveal"><span class="num">Step 02</span><h3 class="h-card">Written scope</h3><p>Deliverables, timeline, roles, and price in writing before any work begins.</p></div>
      <div class="reveal"><span class="num">Step 03</span><h3 class="h-card">Execution</h3><p>A named lead, a weekly status, and a single escalation path. You always know where things stand.</p></div>
      <div class="reveal"><span class="num">Step 04</span><h3 class="h-card">Handover</h3><p>Documentation, runbooks, and a transition plan. Ongoing support only if you want it.</p></div>
    </div>
  </div>
</section>

<div class="strip"><img src="assets/texture.webp" alt="" role="presentation" loading="lazy"></div>

<section class="section">
  <div class="wrap split">
    <div class="sticky-head reveal">
      <p class="eyebrow">Why ThabTech</p>
      <h2 class="h-sec">Built to be easy to buy from.</h2>
    </div>
    <div class="cards reveal" style="grid-template-columns:repeat(auto-fit,minmax(min(100%,260px),1fr))">
      <div class="card"><h3 class="h-card">Senior people on the work</h3><p>The person who scopes your engagement is the person accountable for delivering it. No bait-and-switch staffing after signature.</p></div>
      <div class="card"><h3 class="h-card">Procurement-ready</h3><p>Registered US entity, standard MSA and SOW templates, W-9, and insurance documentation available on request &mdash; so vendor onboarding isn't the bottleneck.</p></div>
      <div class="card"><h3 class="h-card">Right-sized for mid-market</h3><p>Large enough to staff a real project, small enough that your account isn't rounding error. You get a direct line, not a ticket queue.</p></div>
      <div class="card"><h3 class="h-card">Consulting and staffing under one contract</h3><p>When a project needs both a design and a body to run it, you don't manage two vendors or two invoices.</p></div>
    </div>
  </div>
</section>

{CTA}"""


SERVICES = f"""<section class="hero hero--sub">
  <div class="hero__media"><img src="assets/consulting.webp" alt=""></div>
  <div class="hero__inner">
    <p class="eyebrow">Consulting</p>
    <h1 class="h-hero">Fix the infrastructure. Then make it boring.</h1>
    <p class="hero__lede">Four practice areas, scoped as defined engagements with written deliverables. We work on fixed scope wherever the problem allows it.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="cards">
      <article class="card reveal" id="cloud">
        <p class="eyebrow eyebrow--plain">01 &mdash; Cloud &amp; Infrastructure</p>
        <h2 class="h-sub">Migration, optimization, and the bill that follows</h2>
        <p>Moving to cloud is the easy half. Running it at a defensible cost is the half that gets skipped.</p>
        <ul>
          <li>Migration assessment and wave planning</li>
          <li>Azure, AWS, and hybrid landing zones</li>
          <li>Cost optimization and rightsizing reviews</li>
          <li>Network, identity, and directory modernization</li>
          <li>Backup, recovery, and business continuity design</li>
        </ul>
      </article>
      <article class="card reveal" id="security">
        <p class="eyebrow eyebrow--plain">02 &mdash; Cybersecurity &amp; Compliance</p>
        <h2 class="h-sub">Controls that survive an audit and a Tuesday</h2>
        <p>Security work that maps to a framework, gets documented, and can actually be operated by your team.</p>
        <ul>
          <li>Security posture and gap assessments</li>
          <li>Identity and access management, MFA, least privilege</li>
          <li>Endpoint, email, and network hardening</li>
          <li>Policy, control documentation, and audit support</li>
          <li>Incident response planning and tabletop exercises</li>
        </ul>
      </article>
      <article class="card reveal" id="apps">
        <p class="eyebrow eyebrow--plain">03 &mdash; Application Development</p>
        <h2 class="h-sub">Build, integrate, or retire</h2>
        <p>Custom software and integration work, plus the harder conversation about which systems should stop existing.</p>
        <ul>
          <li>Custom web and internal business applications</li>
          <li>Legacy application assessment and modernization</li>
          <li>API and system-to-system integration</li>
          <li>Data migration and reporting pipelines</li>
          <li>Workflow automation across existing platforms</li>
        </ul>
      </article>
      <article class="card reveal" id="advisory">
        <p class="eyebrow eyebrow--plain">04 &mdash; IT Strategy &amp; Advisory</p>
        <h2 class="h-sub">A plan your CFO will approve</h2>
        <p>Roadmaps tied to budget cycles and business outcomes, written so non-technical stakeholders can sign off.</p>
        <ul>
          <li>Current-state assessment and technology roadmap</li>
          <li>Vendor selection and licensing review</li>
          <li>IT budget planning and total cost analysis</li>
          <li>Fractional IT leadership for growing teams</li>
          <li>Project and program delivery oversight</li>
        </ul>
      </article>
    </div>
  </div>
</section>

<section class="band section">
  <div class="wrap">
    <div style="max-width:52ch">
      <p class="eyebrow">Engagement types</p>
      <h2 class="h-sec">Three ways to buy consulting from us.</h2>
    </div>
    <div class="steps mt-12">
      <div class="reveal"><span class="num">Type 01</span><h3 class="h-card">Assessment</h3><p>A time-boxed review producing findings, prioritized risks, and a costed recommendation. Fixed fee, fixed duration.</p></div>
      <div class="reveal"><span class="num">Type 02</span><h3 class="h-card">Project delivery</h3><p>Defined scope, milestones, and acceptance criteria. Priced as a fixed engagement wherever the work allows it.</p></div>
      <div class="reveal"><span class="num">Type 03</span><h3 class="h-card">Ongoing advisory</h3><p>A retained block of senior hours each month for roadmap, escalation, and vendor decisions. Cancel with notice.</p></div>
    </div>
  </div>
</section>

{CTA}"""


STAFFING = f"""<section class="hero hero--sub">
  <div class="hero__media"><img src="assets/staffing.webp" alt=""></div>
  <div class="hero__inner">
    <p class="eyebrow">Staffing</p>
    <h1 class="h-hero">Screened by people who have done the job.</h1>
    <p class="hero__lede">Technical staffing for teams that are tired of receiving five résumés that all match the keywords and none of the requirement.</p>
  </div>
</section>

<section class="section" id="models">
  <div class="wrap split">
    <div class="sticky-head reveal">
      <p class="eyebrow">Engagement models</p>
      <h2 class="h-sec">Hire the way the work actually needs.</h2>
      <p class="lede mt-6">Same vetting standard across all three. The difference is who carries the employment risk and for how long.</p>
    </div>
    <ol class="caplist reveal">
      <li><span class="num">01</span><div><h3 class="h-card">Contract</h3><p>Short- or long-term engagements for a defined project, a backfill, or a surge in workload. We handle employment, payroll, and compliance; you direct the work.</p></div></li>
      <li><span class="num">02</span><div><h3 class="h-card">Contract-to-hire</h3><p>A trial period on our payroll before conversion. The lowest-risk way to fill a role you can't afford to get wrong twice.</p></div></li>
      <li><span class="num">03</span><div><h3 class="h-card">Direct placement</h3><p>Permanent hires sourced, screened, and presented for your own offer process. Fee on placement, with a replacement guarantee in writing.</p></div></li>
      <li><span class="num">04</span><div><h3 class="h-card">Statement-of-work teams</h3><p>When you'd rather buy an outcome than manage contractors, we deliver the work under our own SOW with a named lead.</p></div></li>
    </ol>
  </div>
</section>

<section class="band section" id="vetting">
  <div class="wrap">
    <div style="max-width:52ch">
      <p class="eyebrow">How we vet</p>
      <h2 class="h-sec">Four filters before you ever see a résumé.</h2>
    </div>
    <div class="steps mt-12">
      <div class="reveal"><span class="num">Filter 01</span><h3 class="h-card">Requirement intake</h3><p>We sit with the hiring manager to separate the must-haves from the wish list before sourcing starts.</p></div>
      <div class="reveal"><span class="num">Filter 02</span><h3 class="h-card">Technical screen</h3><p>A working conversation about the actual stack &mdash; conducted by someone who can tell a real answer from a rehearsed one.</p></div>
      <div class="reveal"><span class="num">Filter 03</span><h3 class="h-card">Verification</h3><p>Work authorization, references, and background checks completed before submission, not after you've made an offer.</p></div>
      <div class="reveal"><span class="num">Filter 04</span><h3 class="h-card">Shortlist, not a stack</h3><p>You get a small number of qualified candidates with written notes on fit &mdash; including the reservations.</p></div>
    </div>
  </div>
</section>

<section class="section" id="roles">
  <div class="wrap split">
    <div class="sticky-head reveal">
      <p class="eyebrow">Roles we fill</p>
      <h2 class="h-sec">Technical and technical-adjacent.</h2>
      <p class="lede mt-6">If the role sits between the business and the system, it's in scope. If we can't staff it well, we'll say so rather than take the requisition.</p>
    </div>
    <div class="reveal">
      <ul class="chips">
        <li>Cloud Engineer</li><li>DevOps / SRE</li><li>Systems Administrator</li><li>Network Engineer</li>
        <li>Security Analyst</li><li>GRC / Compliance Analyst</li><li>Identity &amp; Access Engineer</li>
        <li>Software Engineer</li><li>Front-End Developer</li><li>Backend / API Developer</li>
        <li>Data Engineer</li><li>Data / BI Analyst</li><li>Database Administrator</li>
        <li>Business Analyst</li><li>Systems Analyst</li><li>Product Owner</li>
        <li>Project Manager</li><li>Program Manager</li><li>Scrum Master</li>
        <li>ERP / HRIS Analyst</li><li>Workday Analyst</li><li>Salesforce Administrator</li>
        <li>QA Engineer</li><li>Service Desk / Desktop Support</li><li>IT Manager</li>
      </ul>
    </div>
  </div>
</section>

<section class="section" id="candidates" style="padding-top:0">
  <div class="wrap">
    <div class="cards">
      <div class="card reveal">
        <p class="eyebrow eyebrow--plain">For hiring managers</p>
        <h3 class="h-sub">Send us the requirement</h3>
        <p>Share the role, the must-haves, and the deadline. We'll come back with a sourcing plan and a realistic timeline &mdash; or tell you the market rate makes the role unfillable as written.</p>
        <div class="card__foot"><a class="arrow-link" href="contact.html">Submit a role {ARROW}</a></div>
      </div>
      <div class="card reveal">
        <p class="eyebrow eyebrow--plain">For candidates</p>
        <h3 class="h-sub">We won't waste your time</h3>
        <p>We tell you the client, the rate range, and the interview process up front. We don't submit your résumé anywhere without asking first, and we tell you when you're out.</p>
        <div class="card__foot"><a class="arrow-link" href="contact.html">Send your résumé {ARROW}</a></div>
      </div>
    </div>
  </div>
</section>

{CTA}"""


ABOUT = f"""<section class="hero hero--sub">
  <div class="hero__media"><img src="assets/texture.webp" alt=""></div>
  <div class="hero__inner">
    <p class="eyebrow">About</p>
    <h1 class="h-hero">A small firm that behaves like a large one on paper.</h1>
    <p class="hero__lede">ThabTech LLC is a US-based IT consulting and staffing firm serving mid-market and enterprise clients.</p>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div class="sticky-head reveal">
      <p class="eyebrow">Why we exist</p>
      <h2 class="h-sec">The gap between the plan and the people.</h2>
    </div>
    <div class="measure reveal">
      <p class="lede" style="max-width:none">Technology projects rarely fail because the architecture was wrong. They fail because the plan was handed to a team that didn't have the capacity, the skills, or the context to run it.</p>
      <p class="mt-6 body-muted">ThabTech was built around that gap. We consult on the systems &mdash; cloud, infrastructure, security, applications &mdash; and we staff the roles that keep those systems alive after the engagement ends. Because we do both, we can't recommend something we're unwilling to help you operate.</p>
      <p class="mt-6 body-muted">We stay deliberately right-sized. Our clients get senior people, a direct phone number, and an honest answer about what a project will actually cost. Our mission is unchanged since day one: the right technology and the right talent, at the right time.</p>
    </div>
  </div>
</section>

<section class="band section">
  <div class="wrap">
    <div style="max-width:52ch">
      <p class="eyebrow">How we operate</p>
      <h2 class="h-sec">Four commitments we'll hold ourselves to.</h2>
    </div>
    <div class="steps mt-12">
      <div class="reveal"><span class="num">01</span><h3 class="h-card">Scope in writing</h3><p>Deliverables, exclusions, and price documented before work starts. Changes go through a change order, not a surprise invoice.</p></div>
      <div class="reveal"><span class="num">02</span><h3 class="h-card">No unnecessary work</h3><p>If a problem doesn't need our help, we'll say so. Long-term clients are worth more than a padded statement of work.</p></div>
      <div class="reveal"><span class="num">03</span><h3 class="h-card">Documented handover</h3><p>Every engagement ends with material your team can operate from. Dependency on us is not our business model.</p></div>
      <div class="reveal"><span class="num">04</span><h3 class="h-card">One business day</h3><p>Every inquiry gets a human response within one business day, including the ones we have to decline.</p></div>
    </div>
  </div>
</section>

<section class="section" id="capability">
  <div class="wrap split">
    <div class="sticky-head reveal">
      <p class="eyebrow">Capability statement</p>
      <h2 class="h-sec">Everything procurement asks for, in one place.</h2>
      <p class="lede mt-6">Vendor onboarding shouldn't take three weeks of email. Additional documentation is available on request.</p>
      <div class="btn-row mt-8">
        <a class="btn btn--primary" href="mailto:{EMAIL}?subject=Capability%20statement%20request">Request full documentation {ARROW}</a>
      </div>
    </div>
    <dl class="deftable reveal">
      <div><dt>Legal name</dt><dd>ThabTech LLC</dd></div>
      <div><dt>Entity type</dt><dd>Limited Liability Company, United States</dd></div>
      <div><dt>Core competencies</dt><dd>IT consulting &mdash; cloud and infrastructure, cybersecurity and compliance, application development and modernization, IT strategy and advisory. Technical staffing &mdash; contract, contract-to-hire, and direct placement.</dd></div>
      <div><dt>Service delivery</dt><dd>Remote and on-site across the United States</dd></div>
      <div><dt>Primary NAICS</dt><dd>541512 Computer Systems Design Services &middot; 541511 Custom Computer Programming Services &middot; 541519 Other Computer Related Services &middot; 561320 Temporary Help Services &middot; 541612 Human Resources Consulting</dd></div>
      <div><dt>Contract vehicles</dt><dd>Master Service Agreement, Statement of Work, staffing agreement, and time-and-materials. Client paper accepted for review.</dd></div>
      <div><dt>Documentation</dt><dd>W-9, certificate of insurance, and references available on request</dd></div>
      <div><dt>Point of contact</dt><dd><a href="mailto:{EMAIL}" style="color:var(--accent);text-decoration:none">{EMAIL}</a> &middot; <a href="{PHONE_H}" style="color:var(--accent);text-decoration:none">{PHONE_D}</a></dd></div>
      <div><dt>Business hours</dt><dd>Monday&ndash;Friday, 9:00 am &ndash; 5:00 pm</dd></div>
    </dl>
  </div>
</section>

{CTA}"""


CONTACT = f"""<section class="hero hero--sub">
  <div class="hero__media"><img src="assets/hero.webp" alt=""></div>
  <div class="hero__inner">
    <p class="eyebrow">Contact</p>
    <h1 class="h-hero">Start a conversation.</h1>
    <p class="hero__lede">Tell us what you're trying to solve. Every inquiry gets a human response within one business day.</p>
  </div>
</section>

<section class="section">
  <div class="wrap contact-grid">
    <div class="reveal">
      <h2 class="h-sub">Send us a note</h2>
      <form class="mt-8" method="post" action="#" novalidate>
        <div class="field">
          <label for="name">Full name</label>
          <input id="name" name="name" type="text" autocomplete="name" required>
        </div>
        <div class="field">
          <label for="company">Company</label>
          <input id="company" name="company" type="text" autocomplete="organization">
        </div>
        <div class="field">
          <label for="email">Work email</label>
          <input id="email" name="email" type="email" autocomplete="email" required>
        </div>
        <div class="field">
          <label for="reason">What do you need?</label>
          <select id="reason" name="reason">
            <option>IT consulting engagement</option>
            <option>Technical staffing &mdash; contract</option>
            <option>Technical staffing &mdash; direct hire</option>
            <option>I'm a candidate looking for work</option>
            <option>Vendor onboarding / documentation</option>
            <option>Something else</option>
          </select>
        </div>
        <div class="field">
          <label for="message">Details</label>
          <textarea id="message" name="message" placeholder="The problem, the deadline, and the constraint."></textarea>
        </div>
        <button class="btn btn--primary" type="submit">Send message {ARROW}</button>
        <p class="note mt-8">This is a design preview &mdash; the live form on thabtech.com is handled by the site's built-in contact form and delivers to {EMAIL}.</p>
      </form>
    </div>

    <div class="reveal">
      <h2 class="h-sub">Reach us directly</h2>
      <ul class="contact-list mt-8">
        <li><span class="k">Email</span><a class="v" href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li><span class="k">Phone</span><a class="v" href="{PHONE_H}">{PHONE_D}</a></li>
        <li><span class="k">Business hours</span><span class="v">Mon&ndash;Fri, 9:00 am &ndash; 5:00 pm</span></li>
        <li><span class="k">Entity</span><span class="v">ThabTech LLC</span></li>
      </ul>
      <div class="cards mt-12" style="grid-template-columns:1fr">
        <div class="card">
          <h3 class="h-card">Hiring managers</h3>
          <p>Send the role description and the deadline. You'll get a sourcing plan and a realistic timeline before we start.</p>
        </div>
        <div class="card">
          <h3 class="h-card">Candidates</h3>
          <p>Attach your résumé and tell us the kind of work you want. We'll only submit you somewhere after we've asked.</p>
        </div>
        <div class="card">
          <h3 class="h-card">Procurement</h3>
          <p>Need a W-9, COI, MSA, or capability statement? Ask and it goes out the same day.</p>
        </div>
      </div>
    </div>
  </div>
</section>"""


PAGES = [
    ("index.html", "ThabTech &mdash; IT Consulting &amp; Technical Staffing",
     "ThabTech LLC modernizes the infrastructure your business runs on and places the engineers who keep it running. IT consulting and technical staffing under one contract.", INDEX),
    ("services.html", "IT Consulting Services &mdash; ThabTech",
     "Cloud and infrastructure, cybersecurity and compliance, application development, and IT strategy consulting from ThabTech LLC.", SERVICES),
    ("staffing.html", "IT Staffing &mdash; ThabTech",
     "Contract, contract-to-hire, and direct placement technical staffing. Candidates screened by people who have done the job.", STAFFING),
    ("about.html", "About ThabTech &mdash; Capability Statement",
     "ThabTech LLC is a US-based IT consulting and staffing firm. Capability statement, NAICS codes, and vendor documentation in one place.", ABOUT),
    ("contact.html", "Contact ThabTech",
     "Contact ThabTech LLC. Every inquiry gets a human response within one business day.", CONTACT),
]

for filename, title, desc, body in PAGES:
    html = head(title, desc, filename) + body + FOOTER
    (OUT / filename).write_text(html, encoding="utf-8")
    print("wrote", filename)
