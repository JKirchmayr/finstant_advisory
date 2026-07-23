from pathlib import Path
import re

ROOT = Path(__file__).parent

LANGS = {
    "de": {
        "dir": "de/impressum",
        "home": "/de/",
        "contact_url": "/de/kontakt/",
        "impressum_url": "/de/impressum/",
        "title": "Impressum — Finstant Advisory",
        "description": "Impressum und Kontaktdaten von Finstant Advisory, Zürich.",
        "canonical": "https://www.finstantadvisory.com/de/impressum/",
        "heading": "Impressum",
        "country": "Schweiz",
        "email_label": "E-Mail",
        "tel_label": "Tel",
        "footer_label": "Impressum",
        "nav": {
            "home": "Home",
            "services": ("Leistungen", "/de/#leistungen"),
            "who": ("Über uns", "/de/ueber-uns/"),
            "contact": "Kontakt",
            "cta": "Kontakt",
        },
    },
    "en": {
        "dir": "en/impressum",
        "home": "/en/",
        "contact_url": "/en/contact/",
        "impressum_url": "/en/impressum/",
        "title": "Legal notice — Finstant Advisory",
        "description": "Legal notice and contact details for Finstant Advisory, Zurich.",
        "canonical": "https://www.finstantadvisory.com/en/impressum/",
        "heading": "Legal notice",
        "country": "Switzerland",
        "email_label": "Email",
        "tel_label": "Tel",
        "footer_label": "Legal notice",
        "nav": {
            "home": "Home",
            "services": ("Services", "/en/#leistungen"),
            "who": ("About us", "/en/about/"),
            "contact": "Contact",
            "cta": "Contact",
        },
    },
    "it": {
        "dir": "it/impressum",
        "home": "/it/",
        "contact_url": "/it/contatto/",
        "impressum_url": "/it/impressum/",
        "title": "Note legali — Finstant Advisory",
        "description": "Note legali e dati di contatto di Finstant Advisory, Zurigo.",
        "canonical": "https://www.finstantadvisory.com/it/impressum/",
        "heading": "Note legali",
        "country": "Svizzera",
        "email_label": "Email",
        "tel_label": "Tel",
        "footer_label": "Note legali",
        "nav": {
            "home": "Home",
            "services": ("Servizi", "/it/#leistungen"),
            "who": ("Chi siamo", "/it/chi-siamo/"),
            "contact": "Contatto",
            "cta": "Contatto",
        },
    },
}

IMPRESSUM_HREFS = {
    "de": "https://www.finstantadvisory.com/de/impressum/",
    "en": "https://www.finstantadvisory.com/en/impressum/",
    "it": "https://www.finstantadvisory.com/it/impressum/",
}

EXTRA_CSS = """
    body.page-legal { padding-top: var(--nav-height); }
    body.page-legal nav {
      background: rgba(249, 248, 245, 0.96) !important;
      border-bottom-color: var(--border);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
    }
    body.page-legal nav .logo img { filter: none; }
    body.page-legal .nav-links a,
    body.page-legal .nav-lang-link { color: var(--gray-text); }
    body.page-legal .nav-links a:hover { color: var(--black); }
    body.page-legal .nav-lang-link.is-active { color: var(--black); font-weight: 500; }
    body.page-legal .nav-cta {
      color: var(--black);
      border-color: var(--black);
      background: transparent;
    }
    body.page-legal .nav-cta:hover {
      background: var(--black);
      color: var(--white);
    }
    .legal {
      padding: 5rem 3.5rem 6rem;
      max-width: 36rem;
    }
    .legal-title {
      font-family: var(--serif);
      font-size: 38px;
      font-weight: 300;
      line-height: 1.2;
      margin-bottom: 2rem;
    }
    .legal-body {
      font-size: 14px;
      line-height: 1.85;
      font-weight: 300;
      color: var(--black);
    }
    .legal-body p { margin-bottom: 0.35rem; }
    .legal-body a {
      color: var(--black);
      text-decoration: none;
      border-bottom: 0.5px solid var(--gray-mid);
    }
    .legal-body a:hover { opacity: 0.6; }
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
      .legal { padding: 3.5rem 1.75rem 4rem; }
    }
"""

FOOTER_CSS = """
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
        href = LANGS[code]["impressum_url"]
        return f'<a href="{href}" class="nav-lang-link{active}" hreflang="{code}" lang="{code}"{current}>{code.upper()}</a>'

    return f"""  <nav>
    <a href="{home}" class="logo"><img src="/image.png" alt="Finstant Advisory" width="160" height="40" decoding="async" /></a>
    <ul class="nav-links">
      <li><a href="{home}">{n['home']}</a></li>
      <li><a href="{n['who'][1] if str(n['who'][1]).startswith('/') else home + n['who'][1]}">{n['who'][0]}</a></li>
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


def build_legal_section(cfg: dict) -> str:
    return f"""  <main class="legal">
    <h1 class="legal-title reveal">{cfg['heading']}</h1>
    <div class="legal-body reveal">
      <p>Johannes Kirchmayr</p>
      <p>Langgrütstrasse 61</p>
      <p>8047 Zürich</p>
      <p>{cfg['country']}</p>
      <p>{cfg['email_label']}: <a href="mailto:jkirchmayr@finstantadvisory.com">jkirchmayr@finstantadvisory.com</a></p>
      <p>{cfg['tel_label']}: <a href="tel:+41764970496">+41 76 497 04 96</a></p>
    </div>
  </main>"""


def build_footer(cfg: dict) -> str:
    return f"""  <footer>
    <div class="footer-logo"><img src="/image.png" alt="Finstant Advisory" width="160" height="40" decoding="async" /></div>
    <div class="footer-text">© 2026 Finstant Advisory · Zurich</div>
    <div class="footer-links"><a href="{cfg['impressum_url']}">{cfg['footer_label']}</a><span class="footer-sep">·</span><a href="mailto:contact@finstantadvisory.com">contact@finstantadvisory.com</a></div>
  </footer>"""


def build_page(lang: str, cfg: dict, style: str) -> str:
    hrefs = "\n".join(
        f'  <link rel="alternate" hreflang="{code}" href="{IMPRESSUM_HREFS[code]}" />'
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
  <link rel="alternate" hreflang="x-default" href="https://www.finstantadvisory.com/de/impressum/" />
  <link rel="icon" href="/favi.png" type="image/png" />
  <link rel="apple-touch-icon" href="/favi.png" />
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet" />
  <style>
{style}
{EXTRA_CSS}
  </style>
</head>
<body class="page-legal">

{build_nav(lang, cfg)}

{build_legal_section(cfg)}

{build_footer(cfg)}

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


def patch_footer(html: str, cfg: dict) -> str:
    old = '    <div class="footer-text">jkirchmayr@finstant.ai</div>'
    new = (
        f'    <div class="footer-links"><a href="{cfg["impressum_url"]}">{cfg["footer_label"]}</a>'
        f'<span class="footer-sep">·</span><a href="mailto:contact@finstantadvisory.com">contact@finstantadvisory.com</a></div>'
    )
    if old not in html:
        return html
    html = html.replace(old, new, 1)
    if ".footer-links" not in html:
        html = html.replace(
            "    .footer-text {",
            FOOTER_CSS + "\n    .footer-text {",
            1,
        )
    return html


def patch_all_footers():
    html_files = list(ROOT.rglob("*.html"))
    for path in html_files:
        if path.name != "index.html" and path.parent.name not in (
            "de", "en", "it", "kontakt", "contact", "contatto",
            "impressum", "buy-side-origination", "sell-side-advisory",
        ):
            continue
        rel = path.relative_to(ROOT).as_posix()
        lang = rel.split("/")[0] if rel.split("/")[0] in LANGS else None
        if not lang:
            continue
        text = path.read_text(encoding="utf-8")
        patched = patch_footer(text, LANGS[lang])
        if patched != text:
            path.write_text(patched, encoding="utf-8")
            print(f"Patched footer: {rel}")


def main():
    base_style = extract_style((ROOT / "de" / "index.html").read_text(encoding="utf-8"))
    for lang, cfg in LANGS.items():
        out_dir = ROOT / cfg["dir"]
        out_dir.mkdir(parents=True, exist_ok=True)
        page = build_page(lang, cfg, base_style)
        (out_dir / "index.html").write_text(page, encoding="utf-8")
        print(f"Built {cfg['dir']}/index.html")
    patch_all_footers()


if __name__ == "__main__":
    main()
