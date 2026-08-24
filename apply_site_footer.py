"""Create privacy policy pages and replace site footers."""
from __future__ import annotations

import re
from pathlib import Path

from site_chrome import ASSETS, SCRIPT, footer_html

ROOT = Path(__file__).parent

PRIVACY = {
    "de": {
        "dir": "de/datenschutz",
        "title": "Datenschutzerklärung — Finstant Advisory",
        "desc": "Datenschutzerklärung von Finstant Advisory, Zürich.",
        "canonical": "https://www.finstantadvisory.com/de/datenschutz/",
        "hreflang": {
            "de": "https://www.finstantadvisory.com/de/datenschutz/",
            "en": "https://www.finstantadvisory.com/en/privacy/",
            "it": "https://www.finstantadvisory.com/it/privacy/",
        },
        "lang_href": {"de": "/de/datenschutz/", "en": "/en/privacy/", "it": "/it/privacy/"},
        "h1": "Datenschutzerklärung",
        "body": """
      <p>Verantwortlich für die Datenbearbeitung auf dieser Website ist Johannes Kirchmayr, Langgrütstrasse 61, 8047 Zürich, Schweiz, E-Mail: <a href="mailto:contact@finstantadvisory.com">contact@finstantadvisory.com</a>.</p>
      <h2>1. Umfang</h2>
      <p>Diese Erklärung erläutert, welche Personendaten wir bearbeiten, wenn Sie unsere Website nutzen oder uns kontaktieren. Massgeblich ist das Schweizer Datenschutzgesetz (DSG). Soweit die DSGVO Anwendung findet, gelten ergänzend deren Grundsätze.</p>
      <h2>2. Hosting</h2>
      <p>Die Website wird über einen Hosting-Anbieter in der EU bzw. im EWR bereitgestellt. Dabei können technische Protokolldaten (z.&nbsp;B. IP-Adresse, Zeitpunkt, aufgerufene Seite, Browser) anfallen, soweit dies für Betrieb, Sicherheit und Fehlerbehebung erforderlich ist.</p>
      <h2>3. Kontaktformular und E-Mail</h2>
      <p>Wenn Sie uns über das Formular oder per E-Mail schreiben, bearbeiten wir die von Ihnen angegebenen Daten (Name, E-Mail, Nachricht und allfällige weitere Angaben), um Ihre Anfrage zu beantworten. Die Bearbeitung erfolgt zur Durchführung vorvertraglicher Massnahmen bzw. aufgrund unseres berechtigten Interesses an der Kommunikation mit Interessenten.</p>
      <h2>4. Cookies</h2>
      <p>Notwendige Cookies speichern Ihre Auswahl in den Cookie-Einstellungen. Optionale Analyse-Cookies setzen wir nur, wenn Sie zustimmen. Sie können Ihre Einwilligung jederzeit über «Cookie-Einstellungen» im Footer anpassen.</p>
      <h2>5. Weitergabe</h2>
      <p>Eine Weitergabe erfolgt nur, soweit dies für den Betrieb der Website, die Beantwortung Ihrer Anfrage oder eine gesetzliche Pflicht erforderlich ist (z.&nbsp;B. Hosting, E-Mail-Zustellung). Eine Weitergabe zu Werbezwecken findet nicht statt.</p>
      <h2>6. Speicherdauer</h2>
      <p>Anfragen speichern wir so lange, wie es für die Bearbeitung und allfällige Nachfragen nötig ist, längstens jedoch im Rahmen gesetzlicher Aufbewahrungspflichten.</p>
      <h2>7. Ihre Rechte</h2>
      <p>Sie haben das Recht auf Auskunft, Berichtigung, Löschung, Einschränkung der Bearbeitung sowie auf Herausgabe Ihrer Daten. Wenden Sie sich dazu an die oben genannte Adresse. Sie können sich zudem an den Eidgenössischen Datenschutz- und Öffentlichkeitsbeauftragten (EDÖB) wenden.</p>
      <h2>8. Änderungen</h2>
      <p>Wir können diese Erklärung anpassen, wenn sich unsere Bearbeitung oder die Rechtslage ändert. Es gilt die jeweils auf dieser Seite veröffentlichte Fassung.</p>
""",
    },
    "en": {
        "dir": "en/privacy",
        "title": "Privacy policy — Finstant Advisory",
        "desc": "Privacy policy of Finstant Advisory, Zurich.",
        "canonical": "https://www.finstantadvisory.com/en/privacy/",
        "hreflang": {
            "de": "https://www.finstantadvisory.com/de/datenschutz/",
            "en": "https://www.finstantadvisory.com/en/privacy/",
            "it": "https://www.finstantadvisory.com/it/privacy/",
        },
        "lang_href": {"de": "/de/datenschutz/", "en": "/en/privacy/", "it": "/it/privacy/"},
        "h1": "Privacy policy",
        "body": """
      <p>The controller for personal data processed on this website is Johannes Kirchmayr, Langgrütstrasse 61, 8047 Zurich, Switzerland, email: <a href="mailto:contact@finstantadvisory.com">contact@finstantadvisory.com</a>.</p>
      <h2>1. Scope</h2>
      <p>This notice explains which personal data we process when you use our website or contact us. Swiss data protection law (FADP) applies. Where the GDPR applies, its principles apply in addition.</p>
      <h2>2. Hosting</h2>
      <p>The website is hosted by a provider in the EU/EEA. Technical log data (for example IP address, time, page requested, browser) may be processed as needed for operation, security, and troubleshooting.</p>
      <h2>3. Contact form and email</h2>
      <p>If you write to us via the form or email, we process the data you provide (name, email, message and any other details) to respond. This is done to take pre-contractual steps or based on our legitimate interest in communicating with prospective clients.</p>
      <h2>4. Cookies</h2>
      <p>Necessary cookies store your cookie-settings choice. Optional analytics cookies are used only with your consent. You can change your consent at any time via “Cookie settings” in the footer.</p>
      <h2>5. Sharing</h2>
      <p>We share data only as required to operate the website, answer your enquiry, or comply with the law (for example hosting or email delivery). We do not share data for advertising.</p>
      <h2>6. Retention</h2>
      <p>We keep enquiries for as long as needed to handle them and any follow-up, and otherwise only as required by law.</p>
      <h2>7. Your rights</h2>
      <p>You have the right to access, rectification, erasure, restriction of processing, and to receive your data. Contact us at the address above. You may also contact the Swiss Federal Data Protection and Information Commissioner (FDPIC).</p>
      <h2>8. Changes</h2>
      <p>We may update this notice if our processing or the law changes. The version published on this page applies.</p>
""",
    },
    "it": {
        "dir": "it/privacy",
        "title": "Informativa sulla privacy — Finstant Advisory",
        "desc": "Informativa sulla privacy di Finstant Advisory, Zurigo.",
        "canonical": "https://www.finstantadvisory.com/it/privacy/",
        "hreflang": {
            "de": "https://www.finstantadvisory.com/de/datenschutz/",
            "en": "https://www.finstantadvisory.com/en/privacy/",
            "it": "https://www.finstantadvisory.com/it/privacy/",
        },
        "lang_href": {"de": "/de/datenschutz/", "en": "/en/privacy/", "it": "/it/privacy/"},
        "h1": "Informativa sulla privacy",
        "body": """
      <p>Il titolare del trattamento dei dati su questo sito è Johannes Kirchmayr, Langgrütstrasse 61, 8047 Zurigo, Svizzera, e-mail: <a href="mailto:contact@finstantadvisory.com">contact@finstantadvisory.com</a>.</p>
      <h2>1. Ambito</h2>
      <p>Questa informativa spiega quali dati personali trattiamo quando utilizzate il sito o ci contattate. Si applica la legge svizzera sulla protezione dei dati (LPD). Ove applicabile, valgono inoltre i principi del GDPR.</p>
      <h2>2. Hosting</h2>
      <p>Il sito è ospitato da un provider nell’UE/SEE. Possono essere trattati dati di log tecnici (ad es. indirizzo IP, orario, pagina richiesta, browser) se necessari per esercizio, sicurezza e risoluzione di errori.</p>
      <h2>3. Modulo di contatto e e-mail</h2>
      <p>Se ci scrivete tramite modulo o e-mail, trattiamo i dati indicati (nome, e-mail, messaggio ed eventuali altri dati) per rispondere. Il trattamento avviene per misure precontrattuali o per il nostro legittimo interesse alla comunicazione con potenziali clienti.</p>
      <h2>4. Cookie</h2>
      <p>I cookie necessari memorizzano la vostra scelta nelle impostazioni. I cookie di analisi opzionali sono usati solo con il consenso. Potete modificare il consenso in qualsiasi momento tramite «Impostazioni cookie» nel footer.</p>
      <h2>5. Comunicazione a terzi</h2>
      <p>I dati sono comunicati solo se necessario per il funzionamento del sito, per rispondere alla richiesta o per un obbligo di legge (ad es. hosting o invio e-mail). Non avviene alcuna cessione a fini pubblicitari.</p>
      <h2>6. Conservazione</h2>
      <p>Conserviamo le richieste per il tempo necessario alla gestione e a eventuali follow-up, e comunque nei limiti degli obblighi di legge.</p>
      <h2>7. Diritti</h2>
      <p>Avete diritto di accesso, rettifica, cancellazione, limitazione del trattamento e di ottenere i vostri dati. Contattateci all’indirizzo sopra. Potete inoltre rivolgervi all’Incaricato federale della protezione dei dati e della trasparenza (IFPDT).</p>
      <h2>8. Modifiche</h2>
      <p>Possiamo aggiornare questa informativa se cambiano il trattamento o il quadro normativo. Vale la versione pubblicata su questa pagina.</p>
""",
    },
}


def inject_assets(html: str) -> str:
    if "/site-footer.css" not in html:
        html = html.replace("</head>", ASSETS + "</head>", 1)
    if "/cookie-consent.js" not in html:
        html = html.replace("</body>", SCRIPT + "</body>", 1)
    elif "/site-nav.js" not in html:
        html = html.replace("</body>", '  <script src="/site-nav.js" defer></script>\n</body>', 1)
    return html


def replace_footer(html: str, lang: str) -> str:
    html = re.sub(r"<footer\b[\s\S]*?</footer>", footer_html(lang).rstrip(), html, count=1)
    return inject_assets(html)


def extra_legal_css() -> str:
    return """
    .legal { max-width: 42rem; }
    .legal-prose h2 {
      font-family: var(--serif);
      font-size: 1.2rem;
      font-weight: 400;
      margin: 2rem 0 0.7rem;
    }
    .legal-prose p { margin-bottom: 1rem; }
"""


def build_privacy_pages() -> None:
    template = (ROOT / "de" / "impressum" / "index.html").read_text(encoding="utf-8")
    for lang, cfg in PRIVACY.items():
        html = template
        html = html.replace('lang="de"', f'lang="{lang}"', 1)
        html = re.sub(r"<title>.*?</title>", f"<title>{cfg['title']}</title>", html, count=1)
        html = re.sub(
            r'<meta name="description" content=".*?" />',
            f'<meta name="description" content="{cfg["desc"]}" />',
            html,
            count=1,
        )
        html = re.sub(
            r'<link rel="canonical" href=".*?" />',
            f'<link rel="canonical" href="{cfg["canonical"]}" />',
            html,
            count=1,
        )
        for code, href in cfg["hreflang"].items():
            html = re.sub(
                rf'<link rel="alternate" hreflang="{code}" href=".*?" />',
                f'<link rel="alternate" hreflang="{code}" href="{href}" />',
                html,
                count=1,
            )
        html = re.sub(
            r'<link rel="alternate" hreflang="x-default" href=".*?" />',
            f'<link rel="alternate" hreflang="x-default" href="{cfg["hreflang"]["de"]}" />',
            html,
            count=1,
        )
        # language switcher targets
        html = html.replace('href="/en/impressum/"', f'href="{cfg["lang_href"]["en"]}"')
        html = html.replace('href="/de/impressum/"', f'href="{cfg["lang_href"]["de"]}"')
        html = html.replace('href="/it/impressum/"', f'href="{cfg["lang_href"]["it"]}"')
        html = html.replace("nav-lang-link is-active", "nav-lang-link")
        html = re.sub(
            rf'(href="{cfg["lang_href"][lang]}" class="nav-lang-link)(")',
            rf'\1 is-active" aria-current="true',
            html,
            count=1,
        )
        html = re.sub(
            r"<main class=\"legal\">[\s\S]*?</main>",
            f'<main class="legal">\n    <h1 class="legal-title reveal">{cfg["h1"]}</h1>\n    <div class="legal-body legal-prose reveal">{cfg["body"]}\n    </div>\n  </main>',
            html,
            count=1,
        )
        if extra_legal_css() not in html:
            html = html.replace("    .legal {", extra_legal_css() + "    .legal {", 1)
        html = replace_footer(html, lang)
        out = ROOT / cfg["dir"] / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html, encoding="utf-8")
        print("privacy", out.relative_to(ROOT))


def patch_all_html() -> None:
    for path in ROOT.rglob("index.html"):
        rel = str(path.relative_to(ROOT)).replace("\\", "/")
        if rel.startswith("de/"):
            lang = "de"
        elif rel.startswith("en/"):
            lang = "en"
        elif rel.startswith("it/"):
            lang = "it"
        else:
            continue
        html = path.read_text(encoding="utf-8")
        if "<footer" not in html:
            continue
        path.write_text(replace_footer(html, lang), encoding="utf-8")
        print("footer", rel)


if __name__ == "__main__":
    patch_all_html()
    build_privacy_pages()
