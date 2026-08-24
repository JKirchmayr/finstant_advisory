"""Generate investor / entrepreneur pages and retarget navigation."""
from __future__ import annotations

import json
import re
from pathlib import Path

from site_chrome import refs_nav_item

ROOT = Path(__file__).parent
COPY = json.loads((ROOT / "audience_copy.json").read_text(encoding="utf-8"))
CALENDLY = "https://calendly.com/finstant/new-meeting?month=2026-08"

PATHS = {
    "de": {
        "home": "/de/",
        "inv": "/de/fuer-investoren/",
        "ent": "/de/fuer-unternehmer/",
        "inv_label": "Für Investoren",
        "ent_label": "Für Unternehmer",
        "about": "/de/ueber-uns/",
        "about_label": "Über uns",
        "contact": "/de/kontakt/",
        "contact_label": "Kontakt",
        "home_label": "Home",
        "lang_inv": {"de": "/de/fuer-investoren/", "en": "/en/for-investors/", "it": "/it/per-investitori/"},
        "lang_ent": {"de": "/de/fuer-unternehmer/", "en": "/en/for-entrepreneurs/", "it": "/it/per-imprenditori/"},
    },
    "en": {
        "home": "/en/",
        "inv": "/en/for-investors/",
        "ent": "/en/for-entrepreneurs/",
        "inv_label": "For investors",
        "ent_label": "For entrepreneurs",
        "about": "/en/about/",
        "about_label": "About us",
        "contact": "/en/contact/",
        "contact_label": "Contact",
        "home_label": "Home",
        "lang_inv": {"de": "/de/fuer-investoren/", "en": "/en/for-investors/", "it": "/it/per-investitori/"},
        "lang_ent": {"de": "/de/fuer-unternehmer/", "en": "/en/for-entrepreneurs/", "it": "/it/per-imprenditori/"},
    },
    "it": {
        "home": "/it/",
        "inv": "/it/per-investitori/",
        "ent": "/it/per-imprenditori/",
        "inv_label": "Per investitori",
        "ent_label": "Per imprenditori",
        "about": "/it/chi-siamo/",
        "about_label": "Chi siamo",
        "contact": "/it/contatto/",
        "contact_label": "Contatto",
        "home_label": "Home",
        "lang_inv": {"de": "/de/fuer-investoren/", "en": "/en/for-investors/", "it": "/it/per-investitori/"},
        "lang_ent": {"de": "/de/fuer-unternehmer/", "en": "/en/for-entrepreneurs/", "it": "/it/per-imprenditori/"},
    },
}

EXTRA_CSS = """
    .hero-title--long { max-width: 920px; font-size: clamp(32px, 4.8vw, 58px); }
    .services-grid--split { grid-template-columns: 1fr 1fr; }
    a.service { text-decoration: none; color: inherit; transition: background 0.2s; }
    a.service:hover { background: var(--off-white); }
    .engine { padding: 5rem 3.5rem; border-bottom: 0.5px solid var(--border); background: var(--off-white); }
    .engine-label { font-size: 10px; letter-spacing: 0.2em; text-transform: uppercase; color: var(--gray-mid); margin-bottom: 1rem; }
    .engine-title { font-family: var(--serif); font-size: clamp(28px, 3.5vw, 40px); font-weight: 300; line-height: 1.2; margin-bottom: 2.5rem; max-width: 18em; }
    .engine-title--single { max-width: none; white-space: nowrap; }
    @media (max-width: 900px) {
      .engine-title--single { white-space: normal; max-width: 18em; }
    }
    .engine-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem; }
    .engine-grid--4 { grid-template-columns: repeat(4, 1fr); }
    .engine-label + .engine-grid { margin-top: 1.5rem; }
    @media (max-width: 1100px) {
      .engine-grid--4 { grid-template-columns: 1fr 1fr; }
    }
    .engine-num { font-size: 12px; letter-spacing: 0.08em; color: var(--gray-mid); margin-bottom: 1rem; }
    .engine-item-title { font-size: 16px; font-weight: 500; margin-bottom: 0.75rem; }
    .engine-item-body { font-size: 14px; line-height: 1.75; font-weight: 300; color: var(--gray-text); }
    body.page-audience nav,
    body.page-audience nav.is-blurred:not(.is-scrolled) {
      background: rgba(249, 248, 245, 0.96) !important;
      border-bottom-color: var(--border);
      backdrop-filter: blur(16px) saturate(1.15);
      -webkit-backdrop-filter: blur(16px) saturate(1.15);
    }
    body.page-audience nav:not(.is-scrolled) .logo img { filter: none; }
    body.page-audience nav:not(.is-scrolled) .nav-links a { color: var(--gray-text); }
    body.page-audience nav:not(.is-scrolled) .nav-links a:hover { color: var(--black); }
    body.page-audience nav:not(.is-scrolled) .nav-lang-link { color: var(--gray-text); }
    body.page-audience nav:not(.is-scrolled) .nav-lang-link:hover,
    body.page-audience nav:not(.is-scrolled) .nav-lang-link.is-active { color: var(--black); }
    body.page-audience nav:not(.is-scrolled) .nav-lang-sep { color: var(--gray-mid); }
    .hero.hero--plain {
      background: var(--white) !important;
      background-image: none !important;
      min-height: 0 !important;
      padding: calc(5.5rem + var(--nav-height)) 3.5rem 4.5rem;
      justify-content: flex-start;
      align-items: center;
      text-align: center;
    }
    .hero--plain::before,
    .hero--plain::after { display: none; }
    .hero--plain .label { color: var(--gray-text); }
    .hero--plain .hero-title { color: var(--black); margin-left: auto; margin-right: auto; }
    .hero--plain .hero-sub { color: var(--gray-text); margin-left: auto; margin-right: auto; }
    .hero--plain .hero-actions { justify-content: center; }
    .hero--plain .btn-primary {
      background: var(--black);
      color: var(--white);
      box-shadow: none;
    }
    @media (max-width: 800px) {
      .engine { padding: 3.5rem 1.75rem; }
      .engine-grid { grid-template-columns: 1fr; }
      .services-grid--split { grid-template-columns: 1fr; }
      .hero.hero--plain { padding: calc(4.5rem + var(--nav-height)) 1.75rem 3rem; min-height: 0 !important; }
    }
"""

AUDIENCE_SNIPPET = '''
AUDIENCE = {
    "de": {"inv_url": "/de/fuer-investoren/", "ent_url": "/de/fuer-unternehmer/", "inv_label": "Für Investoren", "ent_label": "Für Unternehmer"},
    "en": {"inv_url": "/en/for-investors/", "ent_url": "/en/for-entrepreneurs/", "inv_label": "For investors", "ent_label": "For entrepreneurs"},
    "it": {"inv_url": "/it/per-investitori/", "ent_url": "/it/per-imprenditori/", "inv_label": "Per investitori", "ent_label": "Per imprenditori"},
}
'''


def slice_between(html: str, start: str, end: str) -> str:
    i = html.find(start)
    j = html.find(end, i)
    if i < 0 or j < 0:
        raise SystemExit(f"markers missing: {start!r} -> {end!r}")
    return html[i:j]


def clean_panel(html: str) -> str:
    html = html.replace(" audience-panel", "")
    html = re.sub(r'\s*data-audience-panel="[^"]*"', "", html)
    html = html.replace(" hidden>", ">")
    return html.replace(" hidden", "")


def nav_html(lang: str, current: str) -> str:
    p = PATHS[lang]
    langs = p["lang_inv"] if current == "inv" else p["lang_ent"]

    def lang_link(code: str) -> str:
        active = " is-active" if lang == code else ""
        curr = ' aria-current="true"' if lang == code else ""
        return f'<a href="{langs[code]}" class="nav-lang-link{active}" hreflang="{code}" lang="{code}"{curr}>{code.upper()}</a>'

    inv_cur = ' aria-current="page"' if current == "inv" else ""
    ent_cur = ' aria-current="page"' if current == "ent" else ""
    return f"""    <nav class="is-scrolled">
      <a href="{p['home']}" class="logo"><img src="/image.png" alt="Finstant Advisory" width="160" height="40" decoding="async" /></a>
    <ul class="nav-links">
      <li><a href="{p['inv']}"{inv_cur}>{p['inv_label']}</a></li>
      <li><a href="{p['ent']}"{ent_cur}>{p['ent_label']}</a></li>
{refs_nav_item(lang)}
      <li><a href="{p['about']}">{p['about_label']}</a></li>
      <li><a href="{p['contact']}">{p['contact_label']}</a></li>
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


def page_shell(lang: str, title: str, desc: str, canonical: str, hreflangs: dict, body: str, css: str) -> str:
    alts = "\n".join(
        f'  <link rel="alternate" hreflang="{code}" href="https://www.finstantadvisory.com{href}" />'
        for code, href in hreflangs.items()
    )
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <meta name="robots" content="index, follow" />
  <link rel="canonical" href="{canonical}" />
{alts}
  <link rel="alternate" hreflang="x-default" href="https://www.finstantadvisory.com{hreflangs['de']}" />
  <link rel="icon" href="/favi.png" type="image/png" />
  <link rel="apple-touch-icon" href="/favi.png" />
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=DM+Sans:wght@300;400;500;600&display=swap" rel="stylesheet" />
  <style>
{css}
{EXTRA_CSS}
  </style>
</head>
<body class="page-audience">
{body}
</body>
</html>
"""


def engine_html(c: dict) -> str:
    items = []
    for i, (title, body) in enumerate(c["inv_steps"], start=1):
        delay = "" if i == 1 else f" reveal-delay-{i-1}"
        items.append(
            f"""      <div class="engine-item reveal{delay}">
        <div class="engine-num">0{i}</div>
        <div class="engine-item-title">{title}</div>
        <p class="engine-item-body">{body}</p>
      </div>"""
        )
    return f"""  <section class="engine" id="engine">
    <div class="engine-label reveal">{c['inv_engine_label']}</div>
    <h2 class="engine-title engine-title--single reveal">{c['inv_engine_title']}</h2>
    <div class="engine-grid">
{chr(10).join(items)}
    </div>
  </section>
"""


def scripts() -> str:
    return """  <script>
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(e => {
        if (e.isIntersecting) {
          e.target.classList.add('visible');
          observer.unobserve(e.target);
        }
      });
    }, { threshold: 0.1 });
    document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
    (function() {
      const nav = document.querySelector('nav');
      const afterHero = document.querySelector('.succession, .engine, .market');
      if (!nav) return;
      function updateNav() {
        const navHeight = nav.getBoundingClientRect().height;
        const atWhite = afterHero ? afterHero.getBoundingClientRect().top <= navHeight : window.scrollY > 80;
        nav.classList.toggle('is-scrolled', atWhite);
        nav.classList.toggle('is-blurred', window.scrollY > 24 && !atWhite);
      }
      updateNav();
      window.addEventListener('scroll', updateNav, { passive: true });
      window.addEventListener('resize', updateNav);
    })();
  </script>
"""


def write_rel(rel: str, text: str) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    print("wrote", rel)


def build_pages() -> None:
    home = (ROOT / "de" / "index.html").read_text(encoding="utf-8")
    css = re.search(r"<style>([\s\S]*?)</style>", home).group(1)
    blocks = {}
    for lang in ("de", "en", "it"):
        html = (ROOT / lang / "index.html").read_text(encoding="utf-8")
        succ_start = next(s for s in ("<!-- NACHFOLGE -->", "<!-- SUCCESSION -->", "<!-- SUCCESSIONE -->") if s in html)
        fokus = "<!-- FOKUS -->" if "<!-- FOKUS -->" in html else "<!-- FOCUS -->"
        blocks[lang] = {
            "team": slice_between(html, "<!-- TEAM -->", '<section class="deal-cta"'),
            "deal": slice_between(html, '<section class="deal-cta"', "<!-- FOOTER -->"),
            "foot": slice_between(html, "<!-- FOOTER -->", "  <script>"),
            "succ": clean_panel(slice_between(html, succ_start, "<!-- FÜR UNTERNEHMER -->")),
            "ent_m": slice_between(html, "<!-- FÜR UNTERNEHMER -->", "<!-- FÜR INVESTOREN -->"),
            "inv_m": slice_between(html, "<!-- FÜR INVESTOREN -->", "<!-- CTA -->"),
            "cta": clean_panel(slice_between(html, "<!-- CTA -->", fokus)),
        }

    for lang, p in PATHS.items():
        c = COPY[lang]
        b = blocks[lang]
        ent_body = f"""
  <section class="hero hero--plain">
{nav_html(lang, "ent")}
    <div class="label reveal">{c['label']}</div>
    <h1 class="hero-title hero-title--long reveal reveal-delay-1">{c['ent_h1']}</h1>
    <p class="hero-sub reveal reveal-delay-2">{c['ent_sub']}</p>
    <div class="hero-actions reveal reveal-delay-3">
      <a href="{CALENDLY}" class="btn-primary" target="_blank" rel="noopener noreferrer">{c['ent_cta']}</a>
    </div>
  </section>
{b['succ']}
{b['ent_m']}
{b['cta']}
{b['foot']}
{scripts()}
"""
        write_rel(
            p["ent"].strip("/") + "/index.html",
            page_shell(lang, c["ent_title"], c["ent_desc"], f"https://www.finstantadvisory.com{p['ent']}", p["lang_ent"], ent_body, css),
        )
        inv_body = f"""
  <section class="hero hero--plain">
{nav_html(lang, "inv")}
    <div class="label reveal">{c['label']}</div>
    <h1 class="hero-title hero-title--long reveal reveal-delay-1">{c['inv_h1']}</h1>
    <p class="hero-sub reveal reveal-delay-2">{c['inv_sub']}</p>
    <div class="hero-actions reveal reveal-delay-3">
      <a href="{CALENDLY}" class="btn-primary" target="_blank" rel="noopener noreferrer">{c['inv_cta']}</a>
    </div>
  </section>
{engine_html(c)}
{b['inv_m']}
  <section class="page-cta" id="kontakt-cta">
    <h2 class="page-cta-title reveal">{c['inv_page_cta_title']}</h2>
    <a href="{CALENDLY}" class="btn-primary reveal" target="_blank" rel="noopener noreferrer">{c['inv_page_cta']}</a>
  </section>
{b['foot']}
{scripts()}
"""
        write_rel(
            p["inv"].strip("/") + "/index.html",
            page_shell(lang, c["inv_title"], c["inv_desc"], f"https://www.finstantadvisory.com{p['inv']}", p["lang_inv"], inv_body, css),
        )


def patch_homepage(lang: str) -> None:
    path = ROOT / lang / "index.html"
    html = path.read_text(encoding="utf-8")
    p = PATHS[lang]
    for old, new in (
        (f'href="{p["home"]}#investoren"', f'href="{p["inv"]}"'),
        (f'href="{p["home"]}#unternehmer"', f'href="{p["ent"]}"'),
        (f'href="{p["home"]}#investors"', f'href="{p["inv"]}"'),
        (f'href="{p["home"]}#entrepreneurs"', f'href="{p["ent"]}"'),
        (f'href="{p["home"]}#investitori"', f'href="{p["inv"]}"'),
        (f'href="{p["home"]}#imprenditori"', f'href="{p["ent"]}"'),
    ):
        html = html.replace(old, new)

    if "services-grid--split" not in html:
        html = html.replace(
            "    .services-grid {",
            "    a.service { text-decoration: none; color: inherit; }\n    a.service:hover { background: var(--off-white); }\n    .services-grid--split { grid-template-columns: 1fr 1fr; }\n    .services-grid {",
            1,
        )
        html = html.replace(
            "      .services-grid { grid-template-columns: 1fr 1fr; }",
            "      .services-grid, .services-grid--split { grid-template-columns: 1fr; }",
            1,
        )

    html = re.sub(
        r"  <!-- LEISTUNGEN -->\s*<section class=\"section\" id=\"leistungen\">[\s\S]*?</section>\s*",
        "",
        html,
        count=1,
    )
    html = re.sub(
        r"  <!-- (UNSERE LEISTUNGEN|OUR SERVICES|I NOSTRI SERVIZI) -->\s*<section class=\"offer\"[\s\S]*?</section>\s*",
        "",
        html,
        count=1,
    )
    succ_start = next(s for s in ("<!-- NACHFOLGE -->", "<!-- SUCCESSION -->", "<!-- SUCCESSIONE -->") if s in html)
    fokus = "<!-- FOKUS -->" if "<!-- FOKUS -->" in html else "<!-- FOCUS -->"
    html = html[: html.find(succ_start)] + html[html.find(fokus) :]
    html = re.sub(
        r"\n    \(function \(\) \{\n      var tabs = Array\.from[\s\S]*?\n    \}\)\(\);\n",
        "\n",
        html,
        count=1,
    )
    path.write_text(html, encoding="utf-8")
    print("patched home", lang)


def patch_navs() -> None:
    mapping = [
        ('href="/de/#investoren"', 'href="/de/fuer-investoren/"'),
        ('href="/de/#unternehmer"', 'href="/de/fuer-unternehmer/"'),
        ('href="/en/#investors"', 'href="/en/for-investors/"'),
        ('href="/en/#entrepreneurs"', 'href="/en/for-entrepreneurs/"'),
        ('href="/it/#investitori"', 'href="/it/per-investitori/"'),
        ('href="/it/#imprenditori"', 'href="/it/per-imprenditori/"'),
    ]
    for path in ROOT.rglob("*.html"):
        text = path.read_text(encoding="utf-8")
        orig = text
        for a, b in mapping:
            text = text.replace(a, b)
        if text != orig:
            path.write_text(text, encoding="utf-8")
            print("nav", path.relative_to(ROOT))

    py_nav = (
        '      <li><a href="{home}#investoren">Für Investoren</a></li>\n'
        '      <li><a href="{home}#unternehmer">Für Unternehmer</a></li>'
    )
    py_new = (
        '      <li><a href="{inv_url}">{inv_label}</a></li>\n'
        '      <li><a href="{ent_url}">{ent_label}</a></li>'
    )
    unpack = (
        '    inv_url = AUDIENCE[lang]["inv_url"]\n'
        '    ent_url = AUDIENCE[lang]["ent_url"]\n'
        '    inv_label = AUDIENCE[lang]["inv_label"]\n'
        '    ent_label = AUDIENCE[lang]["ent_label"]\n'
    )
    for name in (
        "build_about_pages.py",
        "build_contact_pages.py",
        "build_impressum_pages.py",
        "build_service_pages.py",
    ):
        p = ROOT / name
        t = p.read_text(encoding="utf-8")
        if "AUDIENCE =" not in t:
            t = t.replace("ROOT = Path(__file__).parent\n", "ROOT = Path(__file__).parent\n" + AUDIENCE_SNIPPET, 1)
        t = t.replace(py_nav, py_new)
        if 'inv_url = AUDIENCE[lang]' not in t:
            if 'n = cfg["nav"]' in t:
                t = t.replace('    n = cfg["nav"]\n', '    n = cfg["nav"]\n' + unpack, 1)
            if "n = NAV[lang]" in t and "inv_url = AUDIENCE[lang]" not in t:
                t = t.replace("    n = NAV[lang]\n", "    n = NAV[lang]\n" + unpack, 1)
        p.write_text(t, encoding="utf-8")
        print("py", name)


if __name__ == "__main__":
    build_pages()
    for lang in PATHS:
        patch_homepage(lang)
    patch_navs()
