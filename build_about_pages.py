"""Generate About Us pages (de/en/it) and patch nav links."""
from pathlib import Path
import re

ROOT = Path(__file__).parent

LANGS = {
    "de": {
        "dir": "de/ueber-uns",
        "home": "/de/",
        "about_url": "/de/ueber-uns/",
        "contact_url": "/de/kontakt/",
        "impressum_url": "/de/impressum/",
        "footer_label": "Impressum",
        "lang_hrefs": {"de": "/de/ueber-uns/", "en": "/en/about/", "it": "/it/chi-siamo/"},
        "title": "Über uns — Finstant Advisory",
        "description": "Über Finstant Advisory — Werte, Ansatz und Team. M&A-Beratung mit Private-Equity-Erfahrung, verwurzelt in Zürich.",
        "canonical": "https://www.finstantadvisory.com/de/ueber-uns/",
        "nav": {
            "home": "Home",
            "services": ("Leistungen", "/de/#leistungen"),
            "about": "Über uns",
            "contact": "Kontakt",
            "cta": "Kontakt",
        },
        "hero_label": "Über uns",
        "hero_title": "Wer wir sind",
        "hero_intro": (
            "Finstant Advisory ist eine unabhängige M&A-Beratung für den europäischen Mittelstand. "
            "Wir verbinden über 12 Jahre Erfahrung in Private Equity und M&A mit einem tiefgreifenden "
            "Netzwerk bei Europas führenden Finanzinvestoren — verwurzelt in Zürich, aktiv in DACH, Italien und Europa."
        ),
        "values_label": "Unsere Werte",
        "values_title": "Was uns leitet",
        "values": [
            ("Diskretion", "Vertraulichkeit ist keine Floskel — sie prägt jeden Schritt, vom ersten Gespräch bis zum Closing."),
            ("Unternehmernähe", "Klare Ansagen, kein Berater-Jargon. Wir sprechen auf Augenhöhe mit Gründern, Familien und Management."),
            ("Investorenperspektive", "Wir denken wie Käufer — weil wir es waren. Wir wissen, was institutionelle Investoren suchen."),
            ("Lokale Expertise", "Tiefe Marktkenntnis in der Schweiz, Italien und Europa — mit direkten Beziehungen zu Eigentümern und Investoren."),
        ],
        "approach_label": "Unser Ansatz",
        "approach_title": "Wie wir arbeiten",
        "approach_paragraphs": [
            "Aufgrund unserer langjährigen Erfahrung als Berater und auf der Käuferseite verstehen wir beide Seiten des Tisches aus eigener Praxis und können diese Expertise für unsere Mandanten direkt nutzbar machen. Unser Ziel ist es, Sie in jeder Phase des Prozesses umfassend zu unterstützen und nachhaltigen Mehrwert für Ihr Unternehmen zu schaffen.",
            "Wir verstehen Ihre Bedürfnisse und entwickeln maßgeschneiderte und langfristig erfolgreiche Lösungen. Unsere Kommunikation ist dabei stets offen, klar und zielorientiert.",
            "Jedes Mandat wird von unseren erfahrenen Partnern geleitet, die über tiefgehende Branchenkenntnisse und starke Verbindungen zu Käufern verfügen. Wir managen alle Aspekte eines Deals und garantieren Exzellenz in der Ausführung und erfolgreiche Ergebnisse für unsere Kunden.",
            "Durch unser Netzwerk von Senior Advisors bringen wir umfassende operative Erfahrung in jedes Projekt ein. Mit umfangreichem strategischem Know-how erweitern sie unsere Beratungsleistungen, um branchenspezifische Lösungen zu erzielen und bestmögliche Ergebnisse zu ermöglichen.",
            "Wir sehen uns nicht nur als Berater, sondern als Ihren Partner, der mit vollem Einsatz und Herzblut an Ihrer Seite steht — von Unternehmer zu Unternehmer.",
        ],
        "team_label": "Team",
        "team_title": "Unser Team",
        "team_intro": (
            "In allem, was wir tun, spiegelt sich unsere Leidenschaft für Qualität und Kundenzufriedenheit wider. "
            "Unser Team ist die treibende Kraft hinter unserem Erfolg. Wir sind stolz darauf, gemeinsam mit "
            "unseren Mandanten Großes zu erreichen."
        ),
        "team_click_hint": "Klicken Sie auf ein Porträt, um mehr zu erfahren.",
        "close_label": "Schließen",
        "linkedin": "LinkedIn",
        "email": "E-Mail",
        "members": [
            {
                "id": "johannes",
                "name": "Johannes Kirchmayr, CFA",
                "role": "Gründer & Partner",
                "photo": "/jkirchmayr.png",
                "photo_class": "",
                "email": "jkirchmayr@finstantadvisory.com",
                "linkedin": "https://www.linkedin.com/in/johanneskirchmayr/",
                "bio": (
                    "Johannes Kirchmayr begann seine Karriere im Turnaround Private Equity, bevor er zu einem der "
                    "führenden institutionellen Asset Manager der Schweiz wechselte. Dort verantwortete er über mehrere "
                    "Jahre Mid-Market-Transaktionen in der Schweiz und Europa und erlernte das Handwerk von Grund auf — "
                    "von der ersten Ansprache bis zum Closing. Die eigene unternehmerische Energie und der Wunsch nach "
                    "einem direkten, vertrauensvollen Austausch mit Unternehmern und Mandanten führten zur Gründung von "
                    "Finstant Advisory. Bei Finstant Advisory liegt sein Schwerpunkt auf dem DACH-Markt."
                ),
            },
            {
                "id": "riccardo",
                "name": "Riccardo Cunego",
                "role": "Gründer & Partner",
                "photo": "/rici-thumb.jpg",
                "photo_large": "/rici-portrait.jpg",
                "photo_class": "team-photo--riccardo",
                "email": "riccardo@finstantadvisory.com",
                "linkedin": "https://www.linkedin.com/in/riccardocunego/",
                "bio": (
                    "Riccardo bringt über 6 Jahre Erfahrung in Private Equity und M&A mit — in der Private-Equity-Sparte "
                    "von Schroders Capital sowie in M&A bei BNP Paribas, Rabobank und Promethiem. Er war über den "
                    "gesamten Deal-Lebenszyklus hinweg tätig — von Origination und Target-Screening bis zur Umsetzung — "
                    "und hat ein umfassendes Netzwerk bei Europas führenden Finanzinvestoren aufgebaut."
                ),
            },
        ],
    },
    "en": {
        "dir": "en/about",
        "home": "/en/",
        "about_url": "/en/about/",
        "contact_url": "/en/contact/",
        "impressum_url": "/en/impressum/",
        "footer_label": "Legal notice",
        "lang_hrefs": {"de": "/de/ueber-uns/", "en": "/en/about/", "it": "/it/chi-siamo/"},
        "title": "About us — Finstant Advisory",
        "description": "About Finstant Advisory — our values, approach, and team. M&A advisory rooted in Zurich with private equity experience.",
        "canonical": "https://www.finstantadvisory.com/en/about/",
        "nav": {
            "home": "Home",
            "services": ("Services", "/en/#leistungen"),
            "about": "About us",
            "contact": "Contact",
            "cta": "Contact",
        },
        "hero_label": "About us",
        "hero_title": "Who we are",
        "hero_intro": (
            "Finstant Advisory is an independent M&A advisory firm focused on the European mid-market. "
            "We combine over 12 years of private equity and M&A experience with a deep network among "
            "Europe's leading financial investors — based in Zurich, active across DACH, Italy, and Europe."
        ),
        "values_label": "Our values",
        "values_title": "What guides us",
        "values": [
            ("Discretion", "Confidentiality is not a slogan — it shapes every step, from the first conversation to closing."),
            ("Founder proximity", "Clear answers, no consultant jargon. We speak at eye level with founders, families, and management."),
            ("Investor mindset", "We think like buyers — because we were buyers. We know what institutional investors look for."),
            ("Local expertise", "Deep market knowledge across Switzerland, Italy, and Europe — with direct relationships to owners and investors."),
        ],
        "approach_label": "Our approach",
        "approach_title": "How we work",
        "approach_paragraphs": [
            "Drawing on years of experience as advisors and on the buy side, we understand both sides of the table from firsthand practice — and put that expertise to work directly for our clients. Our goal is to support you comprehensively at every stage of the process and create lasting value for your business.",
            "We understand your needs and develop tailored solutions built for long-term success. Our communication is always open, clear, and focused on outcomes.",
            "Every mandate is led by our experienced partners, who bring deep sector knowledge and strong connections to buyers. We manage all aspects of a deal and are committed to excellence in execution and successful results for our clients.",
            "Through our network of senior advisors, we bring extensive operational experience into every project. With substantial strategic know-how, they extend our advisory capabilities to deliver sector-specific solutions and the best possible outcomes.",
            "We see ourselves not only as advisors, but as your partner — committed with full dedication from entrepreneur to entrepreneur.",
        ],
        "team_label": "Team",
        "team_title": "Our team",
        "team_intro": (
            "In everything we do, our passion for quality and client satisfaction shines through. "
            "Our team is the driving force behind our success. We are proud to achieve great things "
            "together with our clients."
        ),
        "team_click_hint": "Click a portrait to learn more.",
        "close_label": "Close",
        "linkedin": "LinkedIn",
        "email": "Email",
        "members": [
            {
                "id": "johannes",
                "name": "Johannes Kirchmayr, CFA",
                "role": "Founder & Partner",
                "photo": "/jkirchmayr.png",
                "photo_class": "",
                "email": "jkirchmayr@finstantadvisory.com",
                "linkedin": "https://www.linkedin.com/in/johanneskirchmayr/",
                "bio": (
                    "Johannes Kirchmayr began his career in turnaround private equity before joining one of "
                    "Switzerland's leading institutional asset managers. There he led mid-market transactions "
                    "across Switzerland and Europe for several years and learned the craft end to end — from "
                    "first approach to closing. His entrepreneurial drive and desire for a direct, trusted "
                    "dialogue with founders and clients led him to found Finstant Advisory. At Finstant Advisory, "
                    "his focus is the DACH market."
                ),
            },
            {
                "id": "riccardo",
                "name": "Riccardo Cunego",
                "role": "Founder & Partner",
                "photo": "/rici-thumb.jpg",
                "photo_large": "/rici-portrait.jpg",
                "photo_class": "team-photo--riccardo",
                "email": "riccardo@finstantadvisory.com",
                "linkedin": "https://www.linkedin.com/in/riccardocunego/",
                "bio": (
                    "Riccardo brings over 6 years of private equity and M&A experience — at Schroders Capital's "
                    "private equity division and in M&A at BNP Paribas, Rabobank, and Promethiem. He has worked "
                    "across the full deal lifecycle — from origination and target screening through execution — "
                    "and has built a broad network among Europe's leading financial investors."
                ),
            },
        ],
    },
    "it": {
        "dir": "it/chi-siamo",
        "home": "/it/",
        "about_url": "/it/chi-siamo/",
        "contact_url": "/it/contatto/",
        "impressum_url": "/it/impressum/",
        "footer_label": "Note legali",
        "lang_hrefs": {"de": "/de/ueber-uns/", "en": "/en/about/", "it": "/it/chi-siamo/"},
        "title": "Chi siamo — Finstant Advisory",
        "description": "Chi siamo — valori, approccio e team di Finstant Advisory. Consulenza M&A con esperienza in private equity, con sede a Zurigo.",
        "canonical": "https://www.finstantadvisory.com/it/chi-siamo/",
        "nav": {
            "home": "Home",
            "services": ("Servizi", "/it/#leistungen"),
            "about": "Chi siamo",
            "contact": "Contatto",
            "cta": "Contatto",
        },
        "hero_label": "Chi siamo",
        "hero_title": "Chi siamo",
        "hero_intro": (
            "Finstant Advisory è una boutique di consulenza M&A indipendente per il mid-market europeo. "
            "Uniamo oltre 12 anni di esperienza in private equity e M&A a una rete consolidata tra i "
            "principali investitori finanziari europei — con sede a Zurigo, attivi in DACH, Italia ed Europa."
        ),
        "values_label": "I nostri valori",
        "values_title": "Cosa ci guida",
        "values": [
            ("Discrezione", "La riservatezza non è uno slogan — guida ogni fase, dal primo colloquio al closing."),
            ("Vicinanza agli imprenditori", "Risposte chiare, niente gergo da consulenza. Dialogo alla pari con imprenditori, famiglie e management."),
            ("Mentalità da investitori", "Pensiamo come acquirenti — perché lo siamo stati. Sappiamo cosa cercano gli investitori istituzionali."),
            ("Competenza locale", "Conoscenza profonda di Svizzera, Italia ed Europa — con relazioni dirette verso titolari e investitori."),
        ],
        "approach_label": "Il nostro approccio",
        "approach_title": "Come lavoriamo",
        "approach_paragraphs": [
            "Grazie alla nostra lunga esperienza come consulenti e dal lato dell'acquirente, conosciamo entrambi i lati del tavolo in prima persona e rendiamo questa competenza direttamente utile ai nostri clienti. Il nostro obiettivo è supportarvi in ogni fase del processo e creare valore duraturo per la vostra azienda.",
            "Comprendiamo le vostre esigenze e sviluppiamo soluzioni su misura, orientate al successo nel lungo periodo. La nostra comunicazione è sempre aperta, chiara e focalizzata sugli obiettivi.",
            "Ogni mandato è guidato dai nostri partner esperti, con una conoscenza approfondita del settore e solide relazioni con gli acquirenti. Gestiamo tutti gli aspetti di un deal e garantiamo eccellenza nell'esecuzione e risultati di successo per i nostri clienti.",
            "Attraverso la nostra rete di senior advisor portiamo un'ampia esperienza operativa in ogni progetto. Con un forte know-how strategico, estendono le nostre capacità di consulenza per offrire soluzioni settoriali e i migliori risultati possibili.",
            "Non ci vediamo solo come consulenti, ma come vostro partner — al vostro fianco con pieno impegno, da imprenditore a imprenditore.",
        ],
        "team_label": "Team",
        "team_title": "Il nostro team",
        "team_intro": (
            "In tutto ciò che facciamo si riflette la nostra passione per la qualità e la soddisfazione dei clienti. "
            "Il nostro team è la forza trainante del nostro successo. Siamo orgogliosi di raggiungere grandi "
            "risultati insieme ai nostri mandanti."
        ),
        "team_click_hint": "Cliccate su un ritratto per saperne di più.",
        "close_label": "Chiudi",
        "linkedin": "LinkedIn",
        "email": "Email",
        "members": [
            {
                "id": "johannes",
                "name": "Johannes Kirchmayr, CFA",
                "role": "Fondatore & Partner",
                "photo": "/jkirchmayr.png",
                "photo_class": "",
                "email": "jkirchmayr@finstantadvisory.com",
                "linkedin": "https://www.linkedin.com/in/johanneskirchmayr/",
                "bio": (
                    "Johannes Kirchmayr ha iniziato nel turnaround private equity prima di entrare in uno dei "
                    "principali asset manager istituzionali della Svizzera. Per diversi anni ha guidato transazioni "
                    "mid-market in Svizzera ed Europa e ha imparato il mestiere dall'inizio alla fine — dal primo "
                    "contatto al closing. L'energia imprenditoriale e il desiderio di un dialogo diretto e fidato "
                    "con imprenditori e clienti lo hanno portato a fondare Finstant Advisory. Il suo focus è il mercato DACH."
                ),
            },
            {
                "id": "riccardo",
                "name": "Riccardo Cunego",
                "role": "Fondatore & Partner",
                "photo": "/rici-thumb.jpg",
                "photo_large": "/rici-portrait.jpg",
                "photo_class": "team-photo--riccardo",
                "email": "riccardo@finstantadvisory.com",
                "linkedin": "https://www.linkedin.com/in/riccardocunego/",
                "bio": (
                    "Riccardo porta oltre 6 anni di esperienza in private equity e M&A — nella divisione private equity "
                    "di Schroders Capital e in M&A presso BNP Paribas, Rabobank e Promethiem. Ha lavorato sull'intero "
                    "ciclo del deal — dall'origination e screening fino all'esecuzione — costruendo una rete tra i "
                    "principali investitori finanziari europei."
                ),
            },
        ],
    },
}

EXTRA_CSS = """
    body.page-about { padding-top: var(--nav-height); background: var(--white); }
    body.page-about nav {
      background: rgba(249, 248, 245, 0.96) !important;
      border-bottom-color: var(--border);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
    }
    body.page-about nav .logo img { filter: none; }
    body.page-about .nav-links a,
    body.page-about .nav-lang-link { color: var(--gray-text); }
    body.page-about .nav-links a:hover { color: var(--black); }
    body.page-about .nav-links a[aria-current="page"] { color: var(--black); font-weight: 500; }
    body.page-about .nav-lang-link.is-active { color: var(--black); font-weight: 500; }
    body.page-about .nav-cta {
      color: var(--black);
      border-color: var(--black);
      background: transparent;
    }
    body.page-about .nav-cta:hover {
      background: var(--black);
      color: var(--white);
    }

    .about-section {
      padding: 4.5rem 3.5rem;
      border-bottom: 0.5px solid var(--border);
      background: var(--white);
    }

    .about-section:nth-child(even) {
      background: var(--off-white);
    }

    .about-hero {
      padding-top: 5.5rem;
      padding-bottom: 5rem;
      text-align: center;
    }

    .about-hero .section-title {
      max-width: none;
      margin: 0 auto 1.5rem;
    }

    .about-lead {
      font-size: 15px;
      line-height: 1.9;
      font-weight: 300;
      color: var(--gray-text);
      max-width: 40rem;
      margin-left: auto;
      margin-right: auto;
    }

    #values {
      text-align: center;
    }

    #approach {
      text-align: center;
    }

    #approach .approach-body {
      text-align: center;
    }

    .values-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 0;
      margin: 2.5rem auto 0;
      max-width: 920px;
      border: 0.5px solid var(--border);
      background: var(--white);
      text-align: left;
    }

    .value-card {
      padding: 2rem 2.25rem;
      border-right: 0.5px solid var(--border);
      border-bottom: 0.5px solid var(--border);
    }

    .value-card:nth-child(2n) { border-right: none; }
    .value-card:nth-last-child(-n+2) { border-bottom: none; }

    .value-card-title {
      font-size: 13px;
      font-weight: 500;
      margin-bottom: 0.65rem;
      letter-spacing: 0.02em;
    }

    .value-card-body {
      font-size: 13px;
      line-height: 1.8;
      font-weight: 300;
      color: var(--gray-text);
    }

    .approach-body {
      margin: 2rem auto 0;
      max-width: 44rem;
    }

    .approach-body p {
      font-size: 14px;
      line-height: 1.9;
      font-weight: 300;
      color: var(--gray-text);
      margin-bottom: 1.35rem;
    }

    .approach-body p:last-child {
      margin-bottom: 0;
    }

    #team {
      text-align: center;
    }

    #team .about-team-intro {
      font-size: 14px;
      color: var(--gray-text);
      line-height: 1.85;
      font-weight: 300;
      max-width: 42rem;
      margin: -1rem auto 1rem;
    }

    .about-team-hint {
      font-size: 13px;
      color: var(--gray-mid);
      line-height: 1.6;
      font-weight: 300;
      margin: 0 auto 2.5rem;
    }

    .team-about-picks {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 1.25rem 1.5rem;
      max-width: 920px;
      margin: 0 auto;
      width: 100%;
    }

    .team-about-pick {
      display: block;
      width: 100%;
      margin: 0;
      padding: 0;
      border: none;
      background: none;
      font: inherit;
      color: inherit;
      text-align: center;
      cursor: pointer;
      -webkit-tap-highlight-color: transparent;
    }

    .team-about-pick:focus-visible .team-about-pick-photo {
      outline: 2px solid var(--black);
      outline-offset: 4px;
    }

    .team-about-pick-photo {
      position: relative;
      display: block;
      width: 100%;
      aspect-ratio: 4 / 5;
      overflow: hidden;
      background: var(--off-white);
    }

    .team-about-pick-photo .team-photo {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center center;
      filter: none;
      transition: transform 0.35s ease, opacity 0.25s ease;
    }

    .team-about-pick-photo .team-photo--riccardo {
      object-position: center 8%;
      transform: scale(1.08);
      transform-origin: center center;
    }

    .team-about-pick:hover .team-photo:not(.team-photo--riccardo),
    .team-about-pick.is-selected .team-photo:not(.team-photo--riccardo) {
      transform: scale(1.03);
    }

    .team-about-pick:hover .team-photo--riccardo,
    .team-about-pick.is-selected .team-photo--riccardo {
      transform: scale(1.11);
    }

    .team-about-pick:not(.is-selected) .team-photo {
      opacity: 0.92;
    }

    .team-about-pick-caption {
      position: absolute;
      left: 50%;
      bottom: 0.85rem;
      transform: translateX(-50%);
      width: calc(100% - 1.25rem);
      max-width: 13.5rem;
      background: var(--white);
      padding: 0.7rem 0.85rem 0.65rem;
      box-shadow: 0 10px 28px rgba(0, 0, 0, 0.1);
      text-align: center;
      pointer-events: none;
    }

    .team-about-pick-name {
      display: block;
      font-family: var(--serif);
      font-size: clamp(0.95rem, 1.6vw, 1.05rem);
      font-weight: 400;
      line-height: 1.25;
      color: var(--black);
      margin-bottom: 0.2rem;
    }

    .team-about-pick-role {
      display: block;
      font-size: 9px;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--gray-text);
      line-height: 1.35;
    }

  /* Center pairs when fewer than three members */
    .team-about-picks:has(.team-about-pick:nth-child(2):last-child) {
      grid-template-columns: repeat(6, minmax(0, 1fr));
    }

    .team-about-picks:has(.team-about-pick:nth-child(2):last-child) .team-about-pick:nth-child(1) {
      grid-column: 2 / span 2;
    }

    .team-about-picks:has(.team-about-pick:nth-child(2):last-child) .team-about-pick:nth-child(2) {
      grid-column: 4 / span 2;
    }

    body.team-overlay-open {
      overflow: hidden;
    }

    .team-about-overlay {
      position: fixed;
      inset: 0;
      z-index: 400;
      background: var(--white);
      opacity: 0;
      visibility: hidden;
      pointer-events: none;
      transition: opacity 0.35s ease, visibility 0.35s ease;
    }

    .team-about-overlay.is-open {
      opacity: 1;
      visibility: visible;
      pointer-events: auto;
    }

    .team-about-overlay[hidden] {
      display: block;
    }

    .team-about-overlay:not(.is-open)[hidden] {
      display: none;
    }

    .team-about-overlay-close {
      position: fixed;
      top: 1.25rem;
      right: 1.5rem;
      z-index: 420;
      width: 2.75rem;
      height: 2.75rem;
      margin: 0;
      padding: 0;
      border: 0.5px solid var(--border);
      border-radius: 50%;
      background: var(--white);
      color: var(--black);
      font-size: 1.5rem;
      line-height: 1;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: background 0.2s, color 0.2s, border-color 0.2s;
    }

    .team-about-overlay-close:hover {
      background: var(--black);
      color: var(--white);
      border-color: var(--black);
    }

    .team-about-detail {
      position: absolute;
      inset: 0;
      display: grid;
      grid-template-columns: minmax(0, 1.12fr) minmax(0, 1fr);
      align-items: stretch;
      min-height: 100dvh;
    }

    .team-about-detail[hidden] {
      display: none;
    }

    .team-about-detail-photo {
      position: relative;
      min-height: 100dvh;
      background: var(--off-white);
      overflow: hidden;
    }

    .team-about-detail-photo .team-photo {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center center;
      filter: none;
    }

    .team-about-detail-photo .team-photo--riccardo {
      object-position: center 8%;
      transform: none;
      transform-origin: center center;
    }

    .team-about-detail-content {
      padding: calc(var(--nav-height) + 2.5rem) 3.5rem 3rem 3rem;
      overflow-y: auto;
      align-self: stretch;
      max-height: 100dvh;
    }

    .team-about-detail-name {
      font-size: clamp(1.5rem, 3vw, 2rem);
      font-weight: 500;
      margin-bottom: 0.25rem;
      font-family: var(--serif);
      font-weight: 300;
    }

    .team-about-detail-role {
      font-size: 12px;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--gray-text);
      margin-bottom: 1.25rem;
    }

    .team-about-detail-bio {
      font-size: 14px;
      line-height: 1.9;
      font-weight: 300;
      color: var(--gray-text);
      max-width: 36rem;
      margin-bottom: 1.75rem;
    }

    .team-about-actions {
      display: flex;
      flex-wrap: wrap;
      gap: 0.75rem 1rem;
    }

    .team-about-btn {
      display: inline-block;
      font-size: 11px;
      font-weight: 500;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      text-decoration: none;
      padding: 10px 18px;
      border: 0.5px solid var(--black);
      color: var(--black);
      transition: background 0.25s, color 0.25s;
    }

    .team-about-btn:hover {
      background: var(--black);
      color: var(--white);
    }

    .team-about-btn--ghost {
      background: transparent;
    }

    .footer-links {
      font-size: 11px;
      color: var(--gray-text);
      letter-spacing: 0.04em;
    }
    .footer-links a {
      color: var(--gray-text);
      text-decoration: none;
    }
    .footer-links a:hover { color: var(--black); }
    .footer-sep { margin: 0 0.35rem; }

    @media (max-width: 800px) {
      .about-section { padding: 3.5rem 1.75rem; }
      .values-grid { grid-template-columns: 1fr; }
      .value-card { border-right: none; }
      .value-card:last-child { border-bottom: none; }
      .team-about-detail {
        grid-template-columns: 1fr;
        grid-template-rows: min(42vh, 380px) 1fr;
      }
      .team-about-detail-photo {
        min-height: 0;
      }
      .team-about-detail-content {
        padding: 2rem 1.75rem 2.5rem;
        max-height: none;
      }
      .team-about-overlay-close {
        top: 1rem;
        right: 1rem;
      }
      .team-about-picks {
        grid-template-columns: repeat(2, minmax(0, 1fr));
        max-width: 520px;
      }
      .team-about-picks:has(.team-about-pick:nth-child(2):last-child) .team-about-pick:nth-child(1),
      .team-about-picks:has(.team-about-pick:nth-child(2):last-child) .team-about-pick:nth-child(2) {
        grid-column: auto;
      }
    }

    @media (max-width: 520px) {
      .team-about-picks {
        grid-template-columns: 1fr;
        max-width: 280px;
      }
    }
"""

TEAM_PHOTO_CSS = """
    .team-photo-wrap {
      flex-shrink: 0;
      background: var(--off-white);
      border: 1px solid var(--border);
      padding: 8px;
      box-shadow: 0 18px 48px rgba(0, 0, 0, 0.06);
      transition: opacity 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease;
      border-radius: 2px;
    }
    .team-photo-frame {
      position: relative;
      display: block;
      aspect-ratio: 4 / 5;
      overflow: hidden;
      border-radius: 2px;
    }
    .team-photo {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center center;
      filter: grayscale(1) contrast(1.06);
    }
    .team-photo--riccardo {
      object-position: center 16%;
      transform: scale(1.1);
      transform-origin: center center;
    }
"""


def extract_style(html: str) -> str:
    m = re.search(r"<style>(.*?)</style>", html, re.S)
    return m.group(1) if m else ""


def build_nav(lang: str, cfg: dict) -> str:
    n = cfg["nav"]
    home = cfg["home"]

    def lang_link(code: str) -> str:
        active = " is-active" if lang == code else ""
        current = ' aria-current="true"' if lang == code else ""
        return f'<a href="{cfg["lang_hrefs"][code]}" class="nav-lang-link{active}" hreflang="{code}" lang="{code}"{current}>{code.upper()}</a>'

    return f"""  <nav>
    <a href="{home}" class="logo"><img src="/image.png" alt="Finstant Advisory" width="160" height="40" decoding="async" /></a>
    <ul class="nav-links">
      <li><a href="{home}">{n['home']}</a></li>
      <li><a href="{cfg['about_url']}" aria-current="page">{n['about']}</a></li>
      <li><a href="{cfg['contact_url']}">{n['contact']}</a></li>
    </ul>
    <div class="nav-right">
      <div class="nav-lang" role="navigation" aria-label="Language">
        {lang_link('en')}
        <span class="nav-lang-sep">/</span>
        {lang_link('de')}
        <span class="nav-lang-sep">/</span>
        {lang_link('it')}
      </div>
    </div>
  </nav>"""


def build_values(cfg: dict) -> str:
    cards = []
    for title, body in cfg["values"]:
        cards.append(
            f"""      <div class="value-card reveal">
        <div class="value-card-title">{title}</div>
        <p class="value-card-body">{body}</p>
      </div>"""
        )
    return "\n".join(cards)


def build_approach(cfg: dict) -> str:
    paras = []
    for text in cfg["approach_paragraphs"]:
        paras.append(f"      <p class=\"reveal\">{text}</p>")
    return "\n".join(paras)


def build_team_picks(cfg: dict) -> str:
    picks = []
    for m in cfg["members"]:
        pc = f"team-photo {m['photo_class']}".strip()
        picks.append(
            f"""      <button type="button" class="team-about-pick" data-member="{m['id']}" aria-selected="false" tabindex="0">
        <span class="team-about-pick-photo">
          <img class="{pc}" src="{m['photo']}" alt="" width="640" height="800" decoding="async" aria-hidden="true">
          <span class="team-about-pick-caption">
            <span class="team-about-pick-name">{m['name']}</span>
            <span class="team-about-pick-role">{m['role']}</span>
          </span>
        </span>
      </button>"""
        )
    return "\n".join(picks)


def build_team_details(cfg: dict) -> str:
    panels = []
    for m in cfg["members"]:
        pc = f"team-photo {m['photo_class']}".strip()
        photo_src = m.get("photo_large", m["photo"])
        panels.append(
            f"""    <div class="team-about-detail" id="about-detail-{m['id']}" data-member="{m['id']}" role="document" hidden>
      <div class="team-about-detail-photo">
        <img class="{pc}" src="{photo_src}" alt="{m['name']}" width="1600" height="2000" decoding="async">
      </div>
      <div class="team-about-detail-content">
        <h3 class="team-about-detail-name" id="about-detail-title-{m['id']}">{m['name']}</h3>
        <div class="team-about-detail-role">{m['role']}</div>
        <p class="team-about-detail-bio">{m['bio']}</p>
        <div class="team-about-actions">
          <a href="{m['linkedin']}" class="team-about-btn" target="_blank" rel="noopener noreferrer">{cfg['linkedin']}</a>
          <a href="mailto:{m['email']}" class="team-about-btn team-about-btn--ghost">{cfg['email']}</a>
        </div>
      </div>
    </div>"""
        )
    return "\n".join(panels)


def build_team_overlay(cfg: dict) -> str:
    return f"""  <div class="team-about-overlay" id="team-overlay" hidden aria-modal="true" role="dialog" aria-label="{cfg['team_title']}">
    <button type="button" class="team-about-overlay-close" aria-label="{cfg['close_label']}">×</button>
{build_team_details(cfg)}
  </div>"""


def build_page(lang: str, cfg: dict, style: str) -> str:
    approach_heading = ""
    if cfg.get("approach_title"):
        approach_heading = f'    <h2 class="section-title reveal">{cfg["approach_title"]}</h2>\n'

    hrefs = "\n".join(
        f'  <link rel="alternate" hreflang="{code}" href="https://www.finstantadvisory.com{cfg["lang_hrefs"][code]}" />'
        for code in ("de", "en", "it")
    )
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{cfg['title']}</title>
  <meta name="description" content="{cfg['description']}" />
  <meta name="robots" content="index, follow" />
  <link rel="canonical" href="{cfg['canonical']}" />
{hrefs}
  <link rel="alternate" hreflang="x-default" href="https://www.finstantadvisory.com/de/ueber-uns/" />
  <link rel="icon" href="/favi.png" type="image/png" />
  <link rel="apple-touch-icon" href="/favi.png" />
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet" />
  <style>
{style}
{TEAM_PHOTO_CSS}
{EXTRA_CSS}
  </style>
</head>
<body class="page-about">

{build_nav(lang, cfg)}

  <section class="about-section about-hero" id="about">
    <div class="label reveal">{cfg['hero_label']}</div>
    <h1 class="section-title reveal">{cfg['hero_title']}</h1>
    <p class="about-lead reveal">{cfg['hero_intro']}</p>
  </section>

  <section class="about-section" id="values">
    <div class="label reveal">{cfg['values_label']}</div>
    <h2 class="section-title reveal">{cfg['values_title']}</h2>
    <div class="values-grid">
{build_values(cfg)}
    </div>
  </section>

  <section class="about-section" id="approach">
    <div class="label reveal">{cfg['approach_label']}</div>
{approach_heading}    <div class="approach-body">
{build_approach(cfg)}
    </div>
  </section>

  <section class="about-section" id="team">
    <div class="label reveal">{cfg['team_label']}</div>
    <h2 class="section-title reveal">{cfg['team_title']}</h2>
    <p class="about-team-intro reveal">{cfg['team_intro']}</p>
    <p class="about-team-hint reveal">{cfg['team_click_hint']}</p>
    <div class="team-about-picks reveal" role="tablist" aria-label="{cfg['team_title']}">
{build_team_picks(cfg)}
    </div>
  </section>

{build_team_overlay(cfg)}

  <footer>
    <div class="footer-logo"><img src="/image.png" alt="Finstant Advisory" width="160" height="40" decoding="async" /></div>
    <div class="footer-text">© 2026 Finstant Advisory · Zurich</div>
    <div class="footer-links"><a href="{cfg['impressum_url']}">{cfg['footer_label']}</a><span class="footer-sep">·</span><a href="mailto:kontakt@finstantadvisory.com">kontakt@finstantadvisory.com</a></div>
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

    (function() {{
      const overlay = document.getElementById('team-overlay');
      const closeBtn = overlay && overlay.querySelector('.team-about-overlay-close');
      const picks = document.querySelectorAll('.team-about-pick');
      const details = overlay ? overlay.querySelectorAll('.team-about-detail') : [];
      if (!overlay || !picks.length || !details.length) return;

      let isOpen = false;
      let activeId = null;

      function showPanel(memberId) {{
        details.forEach((panel) => {{
          const show = panel.dataset.member === memberId;
          panel.hidden = !show;
          if (show) {{
            overlay.setAttribute('aria-labelledby', 'about-detail-title-' + memberId);
          }}
        }});
      }}

      function setPickState(memberId) {{
        picks.forEach((btn) => {{
          const on = btn.dataset.member === memberId;
          btn.classList.toggle('is-selected', on);
          btn.setAttribute('aria-selected', on ? 'true' : 'false');
        }});
      }}

      function openOverlay(memberId) {{
        activeId = memberId;
        showPanel(memberId);
        setPickState(memberId);
        overlay.hidden = false;
        requestAnimationFrame(() => overlay.classList.add('is-open'));
        document.body.classList.add('team-overlay-open');
        isOpen = true;
        if (closeBtn) closeBtn.focus();
      }}

      function closeOverlay() {{
        overlay.classList.remove('is-open');
        document.body.classList.remove('team-overlay-open');
        picks.forEach((btn) => {{
          btn.classList.remove('is-selected');
          btn.setAttribute('aria-selected', 'false');
        }});
        activeId = null;
        isOpen = false;
        window.setTimeout(() => {{
          if (!isOpen) {{
            overlay.hidden = true;
            details.forEach((panel) => {{ panel.hidden = true; }});
          }}
        }}, 360);
      }}

      picks.forEach((btn) => {{
        btn.addEventListener('click', () => openOverlay(btn.dataset.member));
      }});

      if (closeBtn) closeBtn.addEventListener('click', closeOverlay);

      document.addEventListener('keydown', (e) => {{
        if (!isOpen) return;
        if (e.key === 'Escape') {{
          closeOverlay();
          return;
        }}
        if (e.key === 'ArrowLeft' || e.key === 'ArrowRight') {{
          const order = Array.from(picks).map((b) => b.dataset.member);
          const i = order.indexOf(activeId);
          if (i < 0) return;
          const step = e.key === 'ArrowRight' ? 1 : -1;
          const next = order[(i + step + order.length) % order.length];
          e.preventDefault();
          openOverlay(next);
        }}
      }});

      const tablist = document.querySelector('.team-about-picks');
      if (tablist) {{
        tablist.addEventListener('keydown', (e) => {{
          const keys = ['ArrowLeft', 'ArrowRight', 'Home', 'End'];
          if (!keys.includes(e.key)) return;
          const order = Array.from(picks);
          const i = order.findIndex((b) => b === document.activeElement);
          const start = i >= 0 ? i : 0;
          let next = start;
          if (e.key === 'ArrowRight') next = (start + 1) % order.length;
          else if (e.key === 'ArrowLeft') next = (start - 1 + order.length) % order.length;
          else if (e.key === 'Home') next = 0;
          else if (e.key === 'End') next = order.length - 1;
          e.preventDefault();
          order[next].focus();
          if (isOpen) openOverlay(order[next].dataset.member);
        }});
      }}
    }})();
  </script>

</body>
</html>
"""


def patch_nav_links():
    for path in ROOT.rglob("*.html"):
        rel = path.relative_to(ROOT).as_posix()
        if rel == "index.html" or "/ueber-uns/" in rel or "/about/" in rel or "/chi-siamo/" in rel:
            continue
        text = path.read_text(encoding="utf-8")
        original = text
        if rel.startswith("de/") or rel == "de/index.html":
            text = text.replace('href="/de/#team"', 'href="/de/ueber-uns/"')
            text = text.replace(">Wer wir sind</a>", ">Über uns</a>")
        elif rel.startswith("en/"):
            text = text.replace('href="/en/#team"', 'href="/en/about/"')
            text = text.replace(">Who We Are</a>", ">About us</a>")
        elif rel.startswith("it/"):
            text = text.replace('href="/it/#team"', 'href="/it/chi-siamo/"')
        if text != original:
            path.write_text(text, encoding="utf-8")
            print(f"Patched nav: {rel}")


def patch_home_nav():
    for lang, cfg in LANGS.items():
        path = ROOT / lang / "index.html"
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        n = cfg["nav"]
        old_team = f'<li><a href="#team">{n.get("about_old", "")}</a></li>'
        # DE uses Wer wir sind, EN Who We Are, IT Chi siamo in nav - check actual
        patterns = [
            ('<li><a href="#team">Wer wir sind</a></li>', f'<li><a href="{cfg["about_url"]}">{n["about"]}</a></li>'),
            ('<li><a href="#team">Who We Are</a></li>', f'<li><a href="{cfg["about_url"]}">{n["about"]}</a></li>'),
            ('<li><a href="#team">Chi siamo</a></li>', f'<li><a href="{cfg["about_url"]}">{n["about"]}</a></li>'),
        ]
        for old, new in patterns:
            if old in text:
                text = text.replace(old, new)
        path.write_text(text, encoding="utf-8")
        print(f"Patched home nav: {lang}/index.html")


def main():
    base_style = extract_style((ROOT / "de" / "index.html").read_text(encoding="utf-8"))
    for lang, cfg in LANGS.items():
        out_dir = ROOT / cfg["dir"]
        out_dir.mkdir(parents=True, exist_ok=True)
        page = build_page(lang, cfg, base_style)
        (out_dir / "index.html").write_text(page, encoding="utf-8")
        print(f"Built {cfg['dir']}/index.html")
    patch_home_nav()
    patch_nav_links()


if __name__ == "__main__":
    main()
