"""Shared dark site footer HTML."""

AUDIENCE = {
    "de": {"inv": "/de/fuer-investoren/", "ent": "/de/fuer-unternehmer/", "inv_l": "Für Investoren", "ent_l": "Für Unternehmer"},
    "en": {"inv": "/en/for-investors/", "ent": "/en/for-entrepreneurs/", "inv_l": "For investors", "ent_l": "For entrepreneurs"},
    "it": {"inv": "/it/per-investitori/", "ent": "/it/per-imprenditori/", "inv_l": "Per investitori", "ent_l": "Per imprenditori"},
}

FOOTER_COPY = {
    "de": {
        "blurb": "Finstant Advisory ist eine unabhängige M&amp;A-Boutique für Private Equity und inhabergeführte Unternehmen in DACH, Italien und Europa.",
        "nav": "Navigation",
        "services": "Leistungen",
        "home": ("Startseite", "/de/"),
        "about": ("Über uns", "/de/ueber-uns/"),
        "contact": ("Kontakt", "/de/kontakt/"),
        "svc1": ("Off-Market Deal Origination", "/de/buy-side-origination/"),
        "svc2": ("M&amp;A Advisory beim Verkauf", "/de/sell-side-advisory/"),
        "svc3": ("Unternehmensnachfolge", "/de/fuer-unternehmer/"),
        "impressum": ("Impressum", "/de/impressum/"),
        "privacy": ("Datenschutzerklärung", "/de/datenschutz/"),
        "cookies": "Cookie-Einstellungen",
        "copy": "Copyright ©2026 FINSTANT ADVISORY",
    },
    "en": {
        "blurb": "Finstant Advisory is an independent M&amp;A boutique for private equity and owner-managed companies in DACH, Italy, and Europe.",
        "nav": "Navigation",
        "services": "Services",
        "home": ("Home", "/en/"),
        "about": ("About us", "/en/about/"),
        "contact": ("Contact", "/en/contact/"),
        "svc1": ("Off-market deal origination", "/en/buy-side-origination/"),
        "svc2": ("M&amp;A advisory on a sale", "/en/sell-side-advisory/"),
        "svc3": ("Business succession", "/en/for-entrepreneurs/"),
        "impressum": ("Legal notice", "/en/impressum/"),
        "privacy": ("Privacy policy", "/en/privacy/"),
        "cookies": "Cookie settings",
        "copy": "Copyright ©2026 FINSTANT ADVISORY",
    },
    "it": {
        "blurb": "Finstant Advisory è una boutique M&amp;A indipendente per private equity e imprese a conduzione familiare in DACH, Italia ed Europa.",
        "nav": "Navigazione",
        "services": "Servizi",
        "home": ("Home", "/it/"),
        "about": ("Chi siamo", "/it/chi-siamo/"),
        "contact": ("Contatto", "/it/contatto/"),
        "svc1": ("Origination off-market", "/it/buy-side-origination/"),
        "svc2": ("Advisory M&amp;A nella vendita", "/it/sell-side-advisory/"),
        "svc3": ("Successione aziendale", "/it/per-imprenditori/"),
        "impressum": ("Note legali", "/it/impressum/"),
        "privacy": ("Informativa sulla privacy", "/it/privacy/"),
        "cookies": "Impostazioni cookie",
        "copy": "Copyright ©2026 FINSTANT ADVISORY",
    },
}

LINKEDIN = "https://www.linkedin.com/company/finstantadvisory"
ASSETS = """  <link rel="stylesheet" href="/site-footer.css?v=4" />
"""
SCRIPT = """  <script src="/cookie-consent.js" defer></script>
  <script src="/site-nav.js" defer></script>
  <script src="/site-reveal.js" defer></script>
"""

REFS_NAV = {
    "de": {
        "label": "Referenzen",
        "href": "/de/referenzen/",
    },
    "en": {
        "label": "References",
        "href": "/en/references/",
    },
    "it": {
        "label": "Referenze",
        "href": "/it/referenze/",
    },
}


def refs_nav_item(lang: str, current: str | None = None) -> str:
    item = REFS_NAV[lang]
    href = item["href"]
    label = item["label"]
    is_current = current == "refs" or current == href
    attrs = ' aria-current="page"' if is_current else ""
    return f'      <li><a href="{href}"{attrs}>{label}</a></li>\n'


LOGIN_URL = "https://dev.finstant.ai/"
LOGIN_LABEL = {"de": "Login", "en": "Login", "it": "Accedi"}


def nav_login(lang: str) -> str:
    label = LOGIN_LABEL.get(lang, "Login")
    return (
        f'<a class="nav-login" href="{LOGIN_URL}" target="_blank" '
        f'rel="noopener noreferrer">{label}</a>'
    )


def footer_html(lang: str) -> str:
    c = FOOTER_COPY[lang]
    a = AUDIENCE[lang]
    return f"""  <footer class="site-footer">
    <div class="site-footer-grid">
      <div>
        <a class="site-footer-logo" href="{c['home'][1]}"><img src="/image.png" alt="Finstant Advisory" width="160" height="40" decoding="async" /></a>
        <p class="site-footer-blurb">{c['blurb']}</p>
        <div class="site-footer-address">Langgrütstrasse 61<br>8047 Zürich<br>Schweiz</div>
        <div class="site-footer-contact">
          <a href="mailto:contact@finstantadvisory.com">contact@finstantadvisory.com</a>
          <a href="tel:+41764970496">+41 76 497 04 96</a>
        </div>
        <a class="site-footer-social" href="{LINKEDIN}" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn">
          <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4.98 3.5C4.98 4.88 3.88 6 2.5 6S0 4.88 0 3.5 1.12 1 2.5 1s2.48 1.12 2.48 2.5zM.22 8.5h4.56V24H.22V8.5zM8.34 8.5h4.37v2.11h.06c.61-1.16 2.1-2.38 4.32-2.38 4.62 0 5.47 3.04 5.47 7v8.77h-4.56v-7.78c0-1.86-.03-4.25-2.59-4.25-2.59 0-2.99 2.02-2.99 4.11V24H8.34V8.5z"/></svg>
        </a>
      </div>
      <div>
        <div class="site-footer-heading">{c['nav']}</div>
        <ul class="site-footer-list">
          <li><a href="{c['home'][1]}">{c['home'][0]}</a></li>
          <li><a href="{a['inv']}">{a['inv_l']}</a></li>
          <li><a href="{a['ent']}">{a['ent_l']}</a></li>
          <li><a href="{REFS_NAV[lang]['href']}">{REFS_NAV[lang]['label']}</a></li>
          <li><a href="{c['about'][1]}">{c['about'][0]}</a></li>
          <li><a href="{c['contact'][1]}">{c['contact'][0]}</a></li>
        </ul>
      </div>
      <div>
        <div class="site-footer-heading">{c['services']}</div>
        <ul class="site-footer-list">
          <li><a href="{c['svc1'][1]}">{c['svc1'][0]}</a></li>
          <li><a href="{c['svc2'][1]}">{c['svc2'][0]}</a></li>
          <li><a href="{c['svc3'][1]}">{c['svc3'][0]}</a></li>
        </ul>
      </div>
    </div>
    <div class="site-footer-bar">
      <div>{c['copy']}</div>
      <div class="site-footer-legal">
        <a href="{c['privacy'][1]}">{c['privacy'][0]}</a><span class="site-footer-dot">·</span>
        <a href="{c['impressum'][1]}">{c['impressum'][0]}</a><span class="site-footer-dot">·</span>
        <button type="button" class="js-cookie-settings" data-cookie-settings>{c['cookies']}</button>
      </div>
    </div>
  </footer>
"""
