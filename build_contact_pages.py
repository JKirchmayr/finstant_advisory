from pathlib import Path
import re

ROOT = Path(__file__).parent

LANGS = {
    "en": {
        "dir": "en/contact",
        "home": "/en/",
        "contact_url": "/en/contact/",
        "title": "Contact — Finstant Advisory",
        "description": "Get in touch with Finstant Advisory for a discreet introductory conversation about M&A advisory and buy-side origination.",
        "canonical": "https://www.finstantadvisory.com/en/contact/",
        "nav": {
            "home": "Home",
            "services": ("Services", "#leistungen"),
            "who": ("Who We Are", "#team"),
            "contact": "Contact",
            "cta": "Contact us",
        },
        "lang_hrefs": {"en": "/en/contact/", "de": "/de/kontakt/", "it": "/it/contatto/"},
        "contact_bg": "Contact",
        "impressum_url": "/en/impressum/",
        "footer_label": "Legal notice",
    },
    "de": {
        "dir": "de/kontakt",
        "home": "/de/",
        "contact_url": "/de/kontakt/",
        "title": "Kontakt — Finstant Advisory",
        "description": "Kontaktieren Sie Finstant Advisory für ein diskretes Erstgespräch zu M&A-Beratung und Buy-side Origination.",
        "canonical": "https://www.finstantadvisory.com/de/kontakt/",
        "nav": {
            "home": "Home",
            "services": ("Leistungen", "#leistungen"),
            "who": ("Wer wir sind", "#team"),
            "contact": "Kontakt",
            "cta": "Kontakt",
        },
        "lang_hrefs": {"en": "/en/contact/", "de": "/de/kontakt/", "it": "/it/contatto/"},
        "contact_bg": "Kontakt",
        "impressum_url": "/de/impressum/",
        "footer_label": "Impressum",
    },
    "it": {
        "dir": "it/contatto",
        "home": "/it/",
        "contact_url": "/it/contatto/",
        "title": "Contatto — Finstant Advisory",
        "description": "Contattate Finstant Advisory per un primo colloquio discreto su consulenza M&A e origination buy-side.",
        "canonical": "https://www.finstantadvisory.com/it/contatto/",
        "nav": {
            "home": "Home",
            "services": ("Servizi", "#leistungen"),
            "who": ("Chi siamo", "#team"),
            "contact": "Contatto",
            "cta": "Contattaci",
        },
        "lang_hrefs": {"en": "/en/contact/", "de": "/de/kontakt/", "it": "/it/contatto/"},
        "contact_bg": "Contatto",
        "impressum_url": "/it/impressum/",
        "footer_label": "Note legali",
    },
}

EXTRA_CSS = """
    body.page-contact { padding-top: var(--nav-height); }
    body.page-contact nav {
      background: rgba(249, 248, 245, 0.96) !important;
      border-bottom-color: var(--border);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
    }
    body.page-contact nav .logo img { filter: none; }
    body.page-contact .nav-links a,
    body.page-contact .nav-lang-link { color: var(--gray-text); }
    body.page-contact .nav-links a:hover { color: var(--black); }
    body.page-contact .nav-lang-link.is-active { color: var(--black); font-weight: 500; }
    body.page-contact .nav-cta {
      color: var(--black);
      border-color: var(--black);
      background: transparent;
    }
    body.page-contact .nav-cta:hover {
      background: var(--black);
      color: var(--white);
    }
    body.page-contact .contact {
      min-height: calc(100vh - var(--nav-height) - 80px);
      min-height: calc(100dvh - var(--nav-height) - 80px);
      padding-top: 5rem;
      border-bottom: none;
    }
    body.page-contact .nav-links a[aria-current="page"] {
      color: var(--black);
    }
"""


def extract_style(html: str) -> str:
    m = re.search(r"<style>(.*?)</style>", html, re.S)
    return m.group(1) if m else ""


def extract_contact_section(html: str) -> str:
    m = re.search(r"<!-- CONTACT -->(.*?)<!-- FOOTER -->", html, re.S)
    if not m:
        raise ValueError("Contact section not found")
    section = m.group(1).strip()
    section = re.sub(r'\s*id="kontakt"', "", section, count=1)
    return section


def build_nav(lang: str, cfg: dict) -> str:
    n = cfg["nav"]
    home = cfg["home"]
    lh = cfg["lang_hrefs"]

    def lang_link(code: str) -> str:
        active = " is-active" if lang == code else ""
        current = ' aria-current="true"' if lang == code else ""
        return f'<a href="{lh[code]}" class="nav-lang-link{active}" hreflang="{code}" lang="{code}"{current}>{code.upper()}</a>'

    return f"""  <nav>
    <a href="{home}" class="logo"><img src="/image.png" alt="Finstant Advisory" width="160" height="40" decoding="async" /></a>
    <ul class="nav-links">
      <li><a href="{home}">{n['home']}</a></li>
      <li><a href="{home}{n['services'][1]}">{n['services'][0]}</a></li>
      <li><a href="{home}{n['who'][1]}">{n['who'][0]}</a></li>
      <li><a href="{cfg['contact_url']}" aria-current="page">{n['contact']}</a></li>
    </ul>
    <div class="nav-right">
      <div class="nav-lang" role="navigation" aria-label="Language">
        {lang_link('en')}
        <span class="nav-lang-sep">/</span>
        {lang_link('de')}
        <span class="nav-lang-sep">/</span>
        {lang_link('it')}
      </div>
      <a href="{cfg['contact_url']}" class="nav-cta">{n['cta']}</a>
    </div>
  </nav>"""


def build_contact_page(lang: str, cfg: dict, html: str) -> str:
    style = extract_style(html)
    contact = extract_contact_section(html)
    contact = re.sub(
        r"<div class=\"contact-bg\">[^<]*</motion.div>",
        f'<div class="contact-bg">{cfg["contact_bg"]}</div>',
        contact,
    )
    contact = re.sub(
        r"<div class=\"contact-bg\">[^<]*</div>",
        f'<div class="contact-bg">{cfg["contact_bg"]}</div>',
        contact,
        count=1,
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
  <link rel="alternate" hreflang="de" href="https://www.finstantadvisory.com/de/kontakt/" />
  <link rel="alternate" hreflang="en" href="https://www.finstantadvisory.com/en/contact/" />
  <link rel="alternate" hreflang="it" href="https://www.finstantadvisory.com/it/contatto/" />
  <link rel="alternate" hreflang="x-default" href="https://www.finstantadvisory.com/de/kontakt/" />
  <link rel="icon" href="/favi.png" type="image/png" />
  <link rel="apple-touch-icon" href="/favi.png" />
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet" />
  <style>
{style}
{EXTRA_CSS}
  </style>
</head>
<body class="page-contact">

{build_nav(lang, cfg)}

{contact}

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
  </script>
  <script src="/contact-form.js"></script>

</body>
</html>
"""


def patch_home(html: str, contact_url: str) -> str:
    html = re.sub(
        r"\n  <!-- CONTACT -->.*?\n  <!-- FOOTER -->",
        "\n  <!-- FOOTER -->",
        html,
        count=1,
        flags=re.S,
    )
    html = html.replace('href="#kontakt"', f'href="{contact_url}"')
    html = html.replace('  <script src="/contact-form.js"></script>\n', "")
    return html


for lang, cfg in LANGS.items():
    src = (ROOT / lang / "index.html").read_text(encoding="utf-8")
    out_dir = ROOT / cfg["dir"]
    out_dir.mkdir(parents=True, exist_ok=True)
    page = build_contact_page(lang, cfg, src)
    (out_dir / "index.html").write_text(page, encoding="utf-8")
    patched = patch_home(src, cfg["contact_url"])
    (ROOT / lang / "index.html").write_text(patched, encoding="utf-8")
    print(f"Built {cfg['dir']}/index.html and updated {lang}/index.html")
