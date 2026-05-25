"""Generate buy-side and sell-side service detail pages (en/de/it)."""
from pathlib import Path
import re

ROOT = Path(__file__).parent

NAV = {
    "en": {
        "home": "/en/",
        "contact": "/en/contact/",
        "impressum_url": "/en/impressum/",
        "footer_label": "Legal notice",
        "home_label": "Home",
        "services": ("Services", "#leistungen"),
        "who": ("Who We Are", "#team"),
        "contact_label": "Contact",
        "cta": "Contact us",
        "back": "All services",
        "cta_section": "Ready to talk?",
        "cta_body": "Discreet introductory conversations — no obligation.",
        "cta_btn": "Get in touch",
    },
    "de": {
        "home": "/de/",
        "contact": "/de/kontakt/",
        "impressum_url": "/de/impressum/",
        "footer_label": "Impressum",
        "home_label": "Home",
        "services": ("Leistungen", "#leistungen"),
        "who": ("Wer wir sind", "#team"),
        "contact_label": "Kontakt",
        "cta": "Kontakt",
        "back": "Alle Leistungen",
        "cta_section": "Bereit für ein Gespräch?",
        "cta_body": "Diskrete Erstgespräche — unverbindlich.",
        "cta_btn": "Kontakt aufnehmen",
    },
    "it": {
        "home": "/it/",
        "contact": "/it/contatto/",
        "impressum_url": "/it/impressum/",
        "footer_label": "Note legali",
        "home_label": "Home",
        "services": ("Servizi", "#leistungen"),
        "who": ("Chi siamo", "#team"),
        "contact_label": "Contatto",
        "cta": "Contattaci",
        "back": "Tutti i servizi",
        "cta_section": "Pronti a parlarne?",
        "cta_body": "Primi colloqui discreti — senza impegno.",
        "cta_btn": "Contattaci",
    },
}

SERVICES = {
    "buy-side": {
        "slug": "buy-side-origination",
        "en": {
            "title": "Buy-Side Origination — Finstant Advisory",
            "description": "Proprietary off-market deal origination for private equity platforms — sector-driven sourcing across Switzerland, Italy, and Europe.",
            "label": "Services",
            "heading": "Buy-Side Origination",
            "subtitle": "Proprietary deal flow for private equity platforms.",
            "intro": (
                "We support private equity firms and their portfolio companies in building "
                "buy-and-build strategies through systematic, off-market origination. Our approach "
                "is sector-driven and relationship-led — every conversation begins long before a transaction."
            ),
            "steps": [
                (
                    "Sector & Market Analysis",
                    "We begin with an in-depth evaluation of the vertical you want to build in. We map the competitive landscape, identify white spaces, profile the most relevant targets, and define the criteria that make a company a true fit for your platform thesis.",
                ),
                (
                    "Target Engagement",
                    "We engage owners directly — through our existing network and through proprietary outreach to new leads. Conversations are private, patient, and built on credibility. We don't run auctions; we build the relationships that lead to the right introduction at the right time.",
                ),
                (
                    "Deal Phase & Transaction Support",
                    "Once a conversation matures, we facilitate the deal phase end-to-end — coordinating both sides, supporting due diligence, and managing the dynamics that move a transaction from intent to close.",
                ),
            ],
        },
        "de": {
            "title": "Buy-Side Origination — Finstant Advisory",
            "description": "Proprietäre Off-Market-Origination für Private-Equity-Plattformen — branchenorientiertes Sourcing in der Schweiz, Italien und Europa.",
            "label": "Leistungen",
            "heading": "Buy-Side Origination",
            "subtitle": "Proprietäre Deal-Pipeline für Private-Equity-Plattformen.",
            "intro": (
                "Wir unterstützen Private-Equity-Gesellschaften und ihre Portfoliounternehmen beim Aufbau "
                "von Buy-and-Build-Strategien durch systematische Off-Market-Origination. Unser Ansatz ist "
                "branchenorientiert und beziehungsgeführt — jedes Gespräch beginnt lange vor einer Transaktion."
            ),
            "steps": [
                (
                    "Sektor- & Marktanalyse",
                    "Wir beginnen mit einer vertieften Bewertung der Branche, in der Sie aufbauen möchten. Wir kartieren das Wettbewerbsumfeld, identifizieren White Spots, profilieren die relevantesten Targets und definieren die Kriterien, die ein Unternehmen wirklich zur Plattform-These passt.",
                ),
                (
                    "Target-Ansprache",
                    "Wir sprechen Inhaber direkt an — über unser bestehendes Netzwerk und durch proprietäre Ansprache neuer Leads. Gespräche sind vertraulich, geduldig und auf Glaubwürdigkeit aufgebaut. Wir führen keine Auktionen; wir bauen die Beziehungen, die zur richtigen Einführung zum richtigen Zeitpunkt führen.",
                ),
                (
                    "Deal-Phase & Transaktionsbegleitung",
                    "Sobald ein Gespräch reift, begleiten wir die Deal-Phase End-to-End — koordinieren beide Seiten, unterstützen die Due Diligence und steuern die Dynamiken, die eine Transaktion von der Absicht bis zum Abschluss voranbringen.",
                ),
            ],
        },
        "it": {
            "title": "Origination Buy-Side — Finstant Advisory",
            "description": "Origination off-market proprietaria per piattaforme di private equity — sourcing settoriale in Svizzera, Italia ed Europa.",
            "label": "Servizi",
            "heading": "Origination Buy-Side",
            "subtitle": "Flusso di deal proprietario per piattaforme di private equity.",
            "intro": (
                "Supportiamo società di private equity e le loro portfolio company nella costruzione di "
                "strategie buy-and-build attraverso origination sistematica off-market. Il nostro approccio "
                "è guidato dal settore e dalle relazioni — ogni conversazione inizia molto prima di una transazione."
            ),
            "steps": [
                (
                    "Analisi di settore e mercato",
                    "Partiamo da una valutazione approfondita del verticale in cui volete crescere. Mappiamo il panorama competitivo, individuiamo gli spazi bianchi, profiliamo i target più rilevanti e definiamo i criteri che rendono un'azienda davvero adatta alla vostra tesi di piattaforma.",
                ),
                (
                    "Coinvolgimento dei target",
                    "Contattiamo i titolari direttamente — attraverso la nostra rete esistente e con outreach proprietario verso nuovi lead. Le conversazioni sono riservate, pazienti e basate sulla credibilità. Non gestiamo aste; costruiamo le relazioni che portano alla giusta introduzione al momento giusto.",
                ),
                (
                    "Fase deal e supporto alla transazione",
                    "Quando una conversazione matura, facilitiamo la fase deal end-to-end — coordinando entrambe le parti, supportando la due diligence e gestendo le dinamiche che portano una transazione dall'intenzione alla chiusura.",
                ),
            ],
        },
    },
    "sell-side": {
        "slug": "sell-side-advisory",
        "en": {
            "title": "Sell-Side Advisory — Finstant Advisory",
            "description": "Discreet sell-side M&A advisory for founders and family-owned businesses — from strategic assessment through closing.",
            "label": "Services",
            "heading": "Sell-Side Advisory",
            "subtitle": "When founders are ready for what comes next.",
            "intro": (
                "Selling a business — or bringing in a strategic partner — is one of the most important "
                "decisions an owner will ever make. We work privately with entrepreneurs and family-owned "
                "companies to ensure the right partner is found, the right process is run, and the right outcome is achieved."
            ),
            "steps": [
                (
                    "Strategic Assessment",
                    "We start by understanding you: your business, your timeline, your motivations, and what \"the next chapter\" really looks like for you and your family. From there, we evaluate the options on the table — full sale, partial sale, capital raise, recapitalization — and recommend the path that best serves your goals.",
                ),
                (
                    "Buyer Universe Mapping",
                    "We build a curated map of the most suitable acquirers — strategic, financial, and hybrid — and prioritize the ones most aligned with your vision for the business. Quality of fit always comes before quantity of names.",
                ),
                (
                    "Materials Preparation",
                    "We prepare the full set of documents needed to engage the market with confidence: teaser, information memorandum, financial model, and management presentation. Every page is built to position your business at its best.",
                ),
                (
                    "Due Diligence & Negotiation",
                    "We stand alongside you through the most intense phase of the process — managing the data room, coordinating buyer Q&A, leading negotiations, and protecting your interests through to signing and closing.",
                ),
            ],
        },
        "de": {
            "title": "Sell-Side Advisory — Finstant Advisory",
            "description": "Diskrete Sell-Side-M&A-Beratung für Gründer und Familienunternehmen — von der strategischen Bestandsaufnahme bis zum Closing.",
            "label": "Leistungen",
            "heading": "Sell-Side Advisory",
            "subtitle": "Wenn Gründer bereit sind für das Nächste.",
            "intro": (
                "Der Verkauf eines Unternehmens — oder die Aufnahme eines strategischen Partners — gehört zu den "
                "wichtigsten Entscheidungen eines Eigentümers. Wir arbeiten vertraulich mit Unternehmern und "
                "Familienunternehmen, damit der richtige Partner gefunden wird, der richtige Prozess geführt wird "
                "und das richtige Ergebnis erzielt wird."
            ),
            "steps": [
                (
                    "Strategische Bestandsaufnahme",
                    "Wir beginnen damit, Sie zu verstehen: Ihr Unternehmen, Ihren Zeitplan, Ihre Motivation und wie «das nächste Kapitel» für Sie und Ihre Familie wirklich aussieht. Anschliessend bewerten wir die Optionen — Vollverkauf, Teilverkauf, Kapitalaufnahme, Rekapitalisierung — und empfehlen den Weg, der Ihren Zielen am besten dient.",
                ),
                (
                    "Käuferuniversum",
                    "Wir erstellen eine kuratierte Landkarte der passendsten Erwerber — strategisch, finanziell und hybrid — und priorisieren diejenigen, die am besten zu Ihrer Vision für das Unternehmen passen. Qualität des Fits steht immer vor Quantität der Namen.",
                ),
                (
                    "Materialerstellung",
                    "Wir bereiten den vollständigen Dokumentensatz vor, um den Markt mit Überzeugung anzusprechen: Teaser, Information Memorandum, Finanzmodell und Management-Präsentation. Jede Seite positioniert Ihr Unternehmen optimal.",
                ),
                (
                    "Due Diligence & Verhandlung",
                    "Wir stehen Ihnen in der intensivsten Phase des Prozesses zur Seite — verwalten den Data Room, koordinieren Käufer-Q&A, führen Verhandlungen und schützen Ihre Interessen bis zur Unterzeichnung und zum Closing.",
                ),
            ],
        },
        "it": {
            "title": "Sell-Side Advisory — Finstant Advisory",
            "description": "Consulenza sell-side M&A discreta per fondatori e aziende familiari — dalla valutazione strategica alla chiusura.",
            "label": "Servizi",
            "heading": "Sell-Side Advisory",
            "subtitle": "Quando i fondatori sono pronti per ciò che viene dopo.",
            "intro": (
                "Vendere un'azienda — o accogliere un partner strategico — è una delle decisioni più importanti "
                "che un titolare possa prendere. Lavoriamo in privato con imprenditori e aziende familiari per "
                "garantire il partner giusto, il processo giusto e l'esito giusto."
            ),
            "steps": [
                (
                    "Valutazione strategica",
                    "Partiamo dalla comprensione di voi: la vostra azienda, i tempi, le motivazioni e come appare davvero «il prossimo capitolo» per voi e la vostra famiglia. Da lì valutiamo le opzioni — vendita totale, parziale, raccolta di capitale, recapitalizzazione — e raccomandiamo il percorso che meglio serve i vostri obiettivi.",
                ),
                (
                    "Mappatura dell'universo acquirenti",
                    "Costruiamo una mappa curata degli acquirenti più adatti — strategici, finanziari e ibridi — e diamo priorità a chi è più allineato alla vostra visione per l'azienda. La qualità dell'affinità viene sempre prima della quantità di nomi.",
                ),
                (
                    "Preparazione dei materiali",
                    "Prepariamo l'intero set di documenti per affrontare il mercato con fiducia: teaser, information memorandum, modello finanziario e presentazione del management. Ogni pagina è costruita per posizionare al meglio la vostra azienda.",
                ),
                (
                    "Due diligence e negoziazione",
                    "Vi affianchiamo nella fase più intensa del processo — gestendo la data room, coordinando le Q&A degli acquirenti, guidando le negoziazioni e proteggendo i vostri interessi fino alla firma e alla chiusura.",
                ),
            ],
        },
    },
}

EXTRA_CSS = """
    body.page-service { padding-top: var(--nav-height); }
    body.page-service nav {
      background: rgba(249, 248, 245, 0.96) !important;
      border-bottom-color: var(--border);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
    }
    body.page-service nav .logo img { filter: none; }
    body.page-service .nav-links a,
    body.page-service .nav-lang-link { color: var(--gray-text); }
    body.page-service .nav-links a:hover { color: var(--black); }
    body.page-service .nav-lang-link.is-active { color: var(--black); font-weight: 500; }
    body.page-service .nav-cta {
      color: var(--black);
      border-color: var(--black);
      background: transparent;
    }
    body.page-service .nav-cta:hover {
      background: var(--black);
      color: var(--white);
    }
    .service-detail {
      max-width: 52rem;
      margin: 0 auto;
      padding: 4.5rem 3.5rem 5rem;
    }
    .service-detail-back {
      display: inline-block;
      font-size: 12px;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      color: var(--gray-text);
      text-decoration: none;
      margin-bottom: 2.5rem;
      transition: color 0.25s;
    }
    .service-detail-back:hover { color: var(--black); }
    .service-detail-heading {
      font-family: var(--serif);
      font-size: clamp(2.5rem, 5vw, 3.75rem);
      font-weight: 400;
      line-height: 1.08;
      letter-spacing: -0.02em;
      margin-bottom: 1.25rem;
    }
    .service-detail-subtitle {
      font-size: 1.125rem;
      font-weight: 500;
      line-height: 1.45;
      margin-bottom: 1.75rem;
      max-width: 36rem;
    }
    .service-detail-intro {
      font-size: 1.05rem;
      font-weight: 300;
      line-height: 1.75;
      color: var(--gray-text);
      margin-bottom: 3.5rem;
      max-width: 40rem;
    }
    .service-steps {
      list-style: none;
      border-top: 0.5px solid var(--border);
    }
    .service-step {
      padding: 2.25rem 0;
      border-bottom: 0.5px solid var(--border);
    }
    .service-step-title {
      font-size: 1rem;
      font-weight: 500;
      letter-spacing: 0.02em;
      margin-bottom: 0.85rem;
    }
    .service-step-num { color: var(--gray-text); font-weight: 400; }
    .service-step-body {
      font-size: 0.95rem;
      font-weight: 300;
      line-height: 1.75;
      color: var(--gray-text);
      max-width: 40rem;
    }
    .service-cta {
      margin-top: 4rem;
      padding-top: 3rem;
      border-top: 0.5px solid var(--border);
    }
    .service-cta-title {
      font-family: var(--serif);
      font-size: 2rem;
      font-weight: 400;
      margin-bottom: 0.75rem;
    }
    .service-cta-body {
      font-size: 0.95rem;
      font-weight: 300;
      color: var(--gray-text);
      margin-bottom: 1.5rem;
    }
    @media (max-width: 768px) {
      .service-detail { padding: 3rem 1.75rem 4rem; }
    }
"""


def extract_style(html: str) -> str:
    m = re.search(r"<style>(.*?)</style>", html, re.S)
    if not m:
        return ""
    style = m.group(1)
    return re.sub(r"\s*body\.page-contact.*", "", style, flags=re.S)


def lang_urls(service_key: str) -> dict[str, str]:
    slug = SERVICES[service_key]["slug"]
    return {lang: f"/{lang}/{slug}/" for lang in ("en", "de", "it")}


def build_nav_html(lang: str, service_key: str) -> str:
    n = NAV[lang]
    home = n["home"]
    lh = lang_urls(service_key)

    def lang_link(code: str) -> str:
        active = " is-active" if lang == code else ""
        current = ' aria-current="true"' if lang == code else ""
        return f'<a href="{lh[code]}" class="nav-lang-link{active}" hreflang="{code}" lang="{code}"{current}>{code.upper()}</a>'

    return f"""  <nav>
    <a href="{home}" class="logo"><img src="/image.png" alt="Finstant Advisory" width="160" height="40" decoding="async" /></a>
    <ul class="nav-links">
      <li><a href="{home}">{n['home_label']}</a></li>
      <li><a href="{home}{n['services'][1]}">{n['services'][0]}</a></li>
      <li><a href="{home}{n['who'][1]}">{n['who'][0]}</a></li>
      <li><a href="{n['contact']}">{n['contact_label']}</a></li>
    </ul>
    <div class="nav-right">
      <div class="nav-lang" role="navigation" aria-label="Language">
        {lang_link('en')}
        <span class="nav-lang-sep">/</span>
        {lang_link('de')}
        <span class="nav-lang-sep">/</span>
        {lang_link('it')}
      </div>
      <a href="{n['contact']}" class="nav-cta">{n['cta']}</a>
    </div>
  </nav>"""


def build_steps_html(steps: list[tuple[str, str]]) -> str:
    items = []
    for i, (title, body) in enumerate(steps, start=1):
        num = f"{i:02d}"
        items.append(
            f"""      <li class="service-step reveal">
        <h3 class="service-step-title"><span class="service-step-num">{num} —</span> {title}</h3>
        <p class="service-step-body">{body}</p>
      </li>"""
        )
    return "\n".join(items)


def build_page(lang: str, service_key: str, style: str) -> str:
    svc = SERVICES[service_key]
    c = svc[lang]
    n = NAV[lang]
    slug = svc["slug"]
    canonical = f"https://www.finstantadvisory.com/{lang}/{slug}/"
    urls = lang_urls(service_key)
    hreflang = "\n".join(
        f'  <link rel="alternate" hreflang="{code}" href="https://www.finstantadvisory.com{urls[code]}" />'
        for code in ("de", "en", "it")
    )
    steps_html = build_steps_html(c["steps"])

    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{c['title']}</title>
  <meta name="description" content="{c['description']}" />
  <meta name="robots" content="index, follow" />
  <link rel="canonical" href="{canonical}" />
{hreflang}
  <link rel="alternate" hreflang="x-default" href="https://www.finstantadvisory.com/de/{slug}/" />
  <link rel="icon" href="/favi.png" type="image/png" />
  <link rel="apple-touch-icon" href="/favi.png" />
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet" />
  <style>
{style}
{EXTRA_CSS}
  </style>
</head>
<body class="page-service">

{build_nav_html(lang, service_key)}

<main class="service-detail">
  <a href="{n['home']}{n['services'][1]}" class="service-detail-back reveal">← {n['back']}</a>
  <div class="label reveal">{c['label']}</div>
  <h1 class="service-detail-heading reveal">{c['heading']}</h1>
  <p class="service-detail-subtitle reveal">{c['subtitle']}</p>
  <p class="service-detail-intro reveal">{c['intro']}</p>
  <ol class="service-steps">
{steps_html}
  </ol>
  <div class="service-cta reveal">
    <h2 class="service-cta-title">{n['cta_section']}</h2>
    <p class="service-cta-body">{n['cta_body']}</p>
    <a href="{n['contact']}" class="btn-primary">{n['cta_btn']}</a>
  </div>
</main>

  <footer>
    <div class="footer-logo"><img src="/image.png" alt="Finstant Advisory" width="160" height="40" decoding="async" /></div>
    <div class="footer-text">© 2026 Finstant Advisory · Zurich</div>
    <div class="footer-links"><a href="{n['impressum_url']}">{n['footer_label']}</a><span class="footer-sep">·</span><a href="mailto:kontakt@finstantadvisory.com">kontakt@finstantadvisory.com</a></div>
  </footer>

  <script>
    const observer = new IntersectionObserver((entries) => {{
      entries.forEach(e => {{
        if (e.isIntersecting) {{
          e.target.classList.add('visible');
          observer.unobserve(e.target);
        }}
      }});
    }}, {{ threshold: 0.1 }});
    document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
  </script>
</body>
</html>
"""


def patch_home(html: str, lang: str) -> str:
    buy_url = f"/{lang}/buy-side-origination/"
    sell_url = f"/{lang}/sell-side-advisory/"
    html = re.sub(
        r'(<div class="service-num">01</div>[\s\S]*?<p class="service-body">[\s\S]*?</p>\s*)<a href="#markt"',
        rf'\1<a href="{buy_url}"',
        html,
        count=1,
    )
    html = re.sub(
        r'(<div class="service reveal reveal-delay-1">[\s\S]*?<p class="service-body">[\s\S]*?</p>\s*)<a href="#unternehmer"',
        rf'\1<a href="{sell_url}"',
        html,
        count=1,
    )
    return html


def main():
    style = extract_style((ROOT / "en" / "contact" / "index.html").read_text(encoding="utf-8"))

    for service_key in ("buy-side", "sell-side"):
        slug = SERVICES[service_key]["slug"]
        for lang in ("en", "de", "it"):
            out_dir = ROOT / lang / slug
            out_dir.mkdir(parents=True, exist_ok=True)
            page = build_page(lang, service_key, style)
            (out_dir / "index.html").write_text(page, encoding="utf-8")
            print(f"Built {lang}/{slug}/index.html")

    for lang in ("en", "de", "it"):
        path = ROOT / lang / "index.html"
        path.write_text(patch_home(path.read_text(encoding="utf-8"), lang), encoding="utf-8")
        print(f"Updated {lang}/index.html")


if __name__ == "__main__":
    main()
