"""Generate References / Referenzen / Referenze pages (de/en/it)."""
from __future__ import annotations

import json
import re
from pathlib import Path

from site_chrome import ASSETS, SCRIPT, footer_html, nav_login, refs_nav_item

ROOT = Path(__file__).parent
DATA = json.loads((ROOT / "references_copy.json").read_text(encoding="utf-8"))

AUDIENCE = {
    "de": {"inv": "/de/fuer-investoren/", "ent": "/de/fuer-unternehmer/", "inv_l": "Für Investoren", "ent_l": "Für Unternehmer"},
    "en": {"inv": "/en/for-investors/", "ent": "/en/for-entrepreneurs/", "inv_l": "For investors", "ent_l": "For entrepreneurs"},
    "it": {"inv": "/it/per-investitori/", "ent": "/it/per-imprenditori/", "inv_l": "Per investitori", "ent_l": "Per imprenditori"},
}

LANG_HREFS = {
    "de": "/de/referenzen/",
    "en": "/en/references/",
    "it": "/it/referenze/",
}

EXTRA_CSS = """
    body.page-refs { padding-top: var(--nav-height); background: var(--white); }
    body.page-refs nav {
      background: rgba(249, 248, 245, 0.96) !important;
      border-bottom-color: var(--border);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
    }
    body.page-refs nav .logo img { filter: none; }
    body.page-refs .nav-links a,
    body.page-refs .nav-lang-link { color: var(--gray-text); }
    body.page-refs .nav-links a:hover { color: var(--black); }
    body.page-refs .nav-links a[aria-current="page"] { color: var(--black); font-weight: 500; }
    body.page-refs .nav-lang-link.is-active { color: var(--black); font-weight: 500; }

    .refs-hero {
      padding: 5rem 3.5rem 4.5rem;
      border-bottom: 0.5px solid var(--border);
      background: var(--white);
    }
    .refs-hero-grid {
      display: grid;
      grid-template-columns: minmax(0, 1.05fr) minmax(0, 0.95fr);
      gap: 3rem 4rem;
      align-items: center;
      max-width: 1180px;
      margin: 0 auto;
    }
    .refs-hero-title {
      font-family: var(--serif);
      font-size: clamp(32px, 4.2vw, 48px);
      font-weight: 300;
      line-height: 1.15;
      letter-spacing: -0.02em;
      margin-bottom: 1.35rem;
    }
    .refs-hero-body {
      font-size: 15px;
      line-height: 1.85;
      font-weight: 300;
      color: var(--gray-text);
      max-width: 34rem;
    }
    .refs-feature {
      position: relative;
      display: block;
      aspect-ratio: 1 / 1;
      overflow: hidden;
      color: var(--white);
      text-decoration: none;
      max-height: 420px;
      width: 100%;
      max-width: 420px;
      justify-self: end;
    }
    .refs-feature img {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center;
    }
    .refs-feature::after {
      content: '';
      position: absolute;
      inset: 0;
      background: linear-gradient(to top, rgba(8, 8, 7, 0.72) 0%, rgba(8, 8, 7, 0.18) 55%, rgba(8, 8, 7, 0.28) 100%);
    }
    .refs-feature-copy {
      position: absolute;
      left: 1.35rem;
      right: 1.35rem;
      bottom: 1.35rem;
      z-index: 1;
    }
    .refs-feature-label {
      display: inline-block;
      font-size: 10px;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      margin-bottom: 0.75rem;
      color: rgba(255, 255, 255, 0.78);
    }
    .refs-feature-title {
      font-family: var(--serif);
      font-size: clamp(22px, 2.4vw, 30px);
      font-weight: 300;
      line-height: 1.2;
      margin-bottom: 0.85rem;
    }
    .refs-feature-link {
      font-size: 13px;
      letter-spacing: 0.02em;
      color: var(--white);
      text-decoration: none;
      border-bottom: 0.5px solid rgba(255, 255, 255, 0.45);
      padding-bottom: 2px;
    }
    .refs-feature:hover .refs-feature-link {
      border-bottom-color: var(--white);
    }

    .refs-deals {
      padding: 5rem 3.5rem 5.5rem;
      background: var(--off-white);
    }
    .refs-deals-inner {
      max-width: 1180px;
      margin: 0 auto;
    }
    .refs-deals-title {
      font-family: var(--serif);
      font-size: clamp(28px, 3.4vw, 40px);
      font-weight: 300;
      line-height: 1.2;
      margin-bottom: 0.75rem;
    }
    .refs-deals-hint {
      font-size: 13px;
      line-height: 1.6;
      font-weight: 300;
      color: var(--gray-text);
      margin-bottom: 1.75rem;
    }
    .refs-filters {
      display: flex;
      flex-wrap: wrap;
      gap: 0.55rem 0.35rem;
      margin-bottom: 2.25rem;
    }
    .refs-deals-toolbar {
      display: flex;
      flex-wrap: wrap;
      gap: 0.75rem 1rem;
      margin-bottom: 1.5rem;
      align-items: flex-end;
    }
    .refs-select-field {
      display: flex;
      flex-direction: column;
      gap: 0.35rem;
      min-width: 9.5rem;
    }
    .refs-select-label {
      font-size: 10px;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      color: var(--gray-mid);
    }
    .refs-select {
      appearance: none;
      font-family: inherit;
      font-size: 13px;
      font-weight: 300;
      color: var(--black);
      background: #fff url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8' viewBox='0 0 12 8'%3E%3Cpath fill='%23666' d='M1 1l5 5 5-5'/%3E%3C/svg%3E") no-repeat right 0.7rem center;
      border: 0.5px solid var(--border);
      border-radius: 1px;
      padding: 0.55rem 2rem 0.55rem 0.75rem;
      cursor: pointer;
      min-width: 9.5rem;
    }
    .refs-select:hover,
    .refs-select:focus {
      border-color: var(--gray-mid);
      outline: none;
    }
    .refs-filter {
      appearance: none;
      border: 0.5px solid var(--border);
      background: transparent;
      color: var(--gray-text);
      font-family: inherit;
      font-size: 12px;
      letter-spacing: 0.04em;
      padding: 0.45rem 0.85rem;
      cursor: pointer;
      border-radius: 1px;
    }
    .refs-filter:hover { color: var(--black); border-color: var(--gray-mid); }
    .refs-filter.is-active {
      color: var(--black);
      border-color: var(--black);
      background: var(--white);
    }

    .refs-tombstones {
      display: grid;
      grid-template-columns: repeat(6, minmax(0, 1fr));
      gap: 0.65rem;
      justify-content: start;
      max-width: 100%;
    }
    .refs-tombstone {
      appearance: none;
      width: 100%;
      margin: 0;
      padding: 0;
      border: 0.5px solid var(--border);
      background: #fff;
      cursor: pointer;
      text-align: left;
      font: inherit;
      color: inherit;
      display: flex;
      flex-direction: column;
      min-height: 228px;
      max-width: none;
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.06), 0 1px 3px rgba(0, 0, 0, 0.04);
      transition: border-color 0.2s, box-shadow 0.25s ease;
    }
    .refs-tombstone:hover,
    .refs-tombstone:focus-visible {
      border-color: rgba(0, 0, 0, 0.22);
      outline: none;
      box-shadow: 0 10px 28px rgba(0, 0, 0, 0.1), 0 2px 6px rgba(0, 0, 0, 0.05);
    }
    .refs-tombstone.is-selected {
      border-color: var(--black);
      box-shadow: 0 10px 28px rgba(0, 0, 0, 0.1), 0 2px 6px rgba(0, 0, 0, 0.05);
    }
    .refs-tombstone[hidden] { display: none !important; }
    .refs-tombstone-face {
      display: flex;
      flex-direction: column;
      flex: 1;
      min-height: 0;
      background: #fff;
    }
    .refs-tombstone-logos {
      flex: 1;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 0.45rem;
      padding: 1.15rem 0.85rem 1rem;
      text-align: center;
      background: #fff;
    }
    .refs-logo-slot {
      width: 100%;
      height: 2.35rem;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .refs-logo-slot--buyer {
      height: 2rem;
    }
    .refs-logo {
      display: block;
      width: auto;
      height: auto;
      max-width: 7.25rem;
      max-height: 2.15rem;
      object-fit: contain;
      object-position: center;
    }
    .refs-logo--buyer {
      max-width: 6.75rem;
      max-height: 1.85rem;
    }
    .refs-logo[src*="gustav-wolf"],
    .refs-logo[src*="/cmp."] {
      max-width: 10.5rem;
      max-height: 3.65rem;
    }
    .refs-logo-slot:has(.refs-logo[src*="gustav-wolf"]),
    .refs-logo-slot:has(.refs-logo[src*="/cmp."]) {
      height: 3.85rem;
    }
    .refs-overlay-visual .refs-logo[src*="gustav-wolf"],
    .refs-overlay-visual .refs-logo[src*="/cmp."] {
      max-width: 280px;
      max-height: 4.5rem;
    }
    .refs-overlay-visual .refs-logo-slot:has(.refs-logo[src*="gustav-wolf"]),
    .refs-overlay-visual .refs-logo-slot:has(.refs-logo[src*="/cmp."]) {
      height: 4.75rem;
    }
    .refs-tombstone-rule {
      width: 1.75rem;
      height: 0.5px;
      background: rgba(0, 0, 0, 0.18);
      margin: 0.1rem 0;
    }
    .refs-tombstone-acquired {
      font-size: 9px;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--gray-mid);
      margin: 0;
    }
    .refs-tombstone-badges {
      display: flex;
      flex-direction: column;
      margin-top: auto;
    }
    .refs-badge {
      display: block;
      width: 100%;
      text-align: center;
      font-size: 9px;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      padding: 0.42rem 0.4rem;
    }
    .refs-badge--sector {
      background: var(--black);
      color: var(--white);
    }
    .refs-badge--type {
      background: #e8e6e0;
      color: var(--black);
    }
    .refs-footnote {
      margin-top: 1.75rem;
      font-size: 12px;
      line-height: 1.65;
      font-weight: 300;
      color: var(--gray-text);
      max-width: 40rem;
    }

    body.refs-overlay-open { overflow: hidden; }
    .refs-overlay {
      position: fixed;
      inset: 0;
      z-index: 400;
      background: var(--white);
      opacity: 0;
      visibility: hidden;
      pointer-events: none;
      transition: opacity 0.35s ease, visibility 0.35s ease;
    }
    .refs-overlay.is-open {
      opacity: 1;
      visibility: visible;
      pointer-events: auto;
    }
    .refs-overlay[hidden] { display: block; }
    .refs-overlay:not(.is-open)[hidden] { display: none; }
    .refs-overlay-close {
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
    .refs-overlay-close:hover {
      background: var(--black);
      color: var(--white);
      border-color: var(--black);
    }
    .refs-overlay-detail {
      position: absolute;
      inset: 0;
      display: grid;
      grid-template-columns: minmax(0, 0.9fr) minmax(0, 1.1fr);
      align-items: stretch;
      min-height: 100dvh;
    }
    .refs-overlay-detail[hidden] { display: none; }
    .refs-overlay-visual {
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      gap: 0.85rem;
      padding: 4rem 3rem;
      background: var(--off-white);
      border-right: 0.5px solid var(--border);
      text-align: center;
    }
    .refs-overlay-visual .refs-logo {
      max-width: 200px;
      max-height: 2.75rem;
    }
    .refs-overlay-visual .refs-logo--buyer {
      max-height: 2.35rem;
    }
    .refs-overlay-visual .refs-logo-slot {
      width: 100%;
      max-width: 220px;
      height: 3rem;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .refs-overlay-visual .refs-logo-slot--buyer {
      height: 2.5rem;
    }
    .refs-overlay-badges {
      display: flex;
      flex-wrap: wrap;
      gap: 0.4rem;
      justify-content: center;
      margin-top: 1.25rem;
    }
    .refs-overlay-badges .refs-badge {
      width: auto;
      padding: 0.4rem 0.7rem;
    }
    .refs-overlay-content {
      padding: calc(var(--nav-height) + 2.5rem) 3.5rem 3rem 3rem;
      overflow-y: auto;
      align-self: stretch;
      max-height: 100dvh;
    }
    .refs-overlay-title {
      font-family: var(--serif);
      font-size: clamp(1.6rem, 3vw, 2.2rem);
      font-weight: 300;
      line-height: 1.2;
      margin-bottom: 0.5rem;
    }
    .refs-overlay-sub {
      font-size: 13px;
      color: var(--gray-text);
      margin-bottom: 1.75rem;
    }
    .refs-overlay-body {
      font-family: var(--serif);
      font-size: 16px;
      line-height: 1.75;
      font-weight: 300;
      color: var(--black);
      max-width: 36rem;
      margin-bottom: 1.75rem;
    }
    .refs-overlay-meta {
      display: flex;
      flex-wrap: wrap;
      gap: 0.45rem 0.85rem;
      margin: 0 0 1.5rem;
      font-size: 11px;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--gray-mid);
    }
    .refs-overlay-facts-label,
    .refs-overlay-sources-label {
      font-size: 10px;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      color: var(--gray-mid);
      margin: 0 0 0.75rem;
    }
    .refs-overlay-facts {
      list-style: none;
      margin: 0 0 2rem;
      padding: 0;
      max-width: 36rem;
      border-top: 0.5px solid var(--border);
    }
    .refs-overlay-facts li {
      padding: 0.7rem 0;
      border-bottom: 0.5px solid var(--border);
      font-size: 13px;
      line-height: 1.55;
      font-weight: 300;
      color: var(--black);
      padding-left: 1rem;
      position: relative;
    }
    .refs-overlay-facts li::before {
      content: "";
      position: absolute;
      left: 0;
      top: 1.15rem;
      width: 0.35rem;
      height: 0.35rem;
      background: var(--black);
    }
    .refs-overlay-sources {
      list-style: none;
      margin: 0;
      padding: 0;
      max-width: 36rem;
    }
    .refs-overlay-sources li {
      margin: 0 0 0.55rem;
    }
    .refs-overlay-sources a {
      font-size: 13px;
      font-weight: 300;
      color: var(--gray-text);
      text-decoration: none;
      border-bottom: 0.5px solid var(--border);
    }
    .refs-overlay-sources a:hover {
      color: var(--black);
      border-bottom-color: var(--black);
    }

    .refs-cases {
      padding: 5rem 3.5rem 4.5rem;
      background: var(--white);
      border-bottom: 0.5px solid var(--border);
    }
    .refs-cases-inner {
      max-width: 1180px;
      margin: 0 auto;
    }
    .refs-cases-title {
      font-family: var(--serif);
      font-size: clamp(28px, 3.4vw, 40px);
      font-weight: 300;
      line-height: 1.2;
      margin-bottom: 1.75rem;
    }
    .refs-cases-grid {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 1.25rem;
    }
    .refs-case {
      display: flex;
      flex-direction: column;
      color: inherit;
      text-decoration: none;
      background: var(--off-white);
      border: 0.5px solid var(--border);
      min-height: 100%;
    }
    .refs-case[hidden] { display: none !important; }
    .refs-case-media {
      position: relative;
      aspect-ratio: 16 / 10;
      overflow: hidden;
      background: var(--gray-light);
    }
    .refs-case-media img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }
    .refs-case-body {
      padding: 1.25rem 1.2rem 1.35rem;
      display: flex;
      flex-direction: column;
      flex: 1;
      gap: 0.65rem;
    }
    .refs-case-title {
      font-size: 16px;
      font-weight: 500;
      line-height: 1.35;
    }
    .refs-case-excerpt {
      font-size: 13px;
      line-height: 1.7;
      font-weight: 300;
      color: var(--gray-text);
      flex: 1;
    }
    .refs-case-meta {
      font-size: 11px;
      letter-spacing: 0.04em;
      color: var(--gray-mid);
      margin-top: 0.35rem;
    }
    .refs-case:hover .refs-case-title { text-decoration: underline; text-underline-offset: 3px; }

    @media (max-width: 1100px) {
      .refs-tombstones { grid-template-columns: repeat(3, minmax(0, 1fr)); }
      .refs-cases-grid { grid-template-columns: 1fr 1fr; }
    }
    @media (max-width: 800px) {
      .refs-hero { padding: 3.5rem 1.75rem 3rem; }
      .refs-hero-grid { grid-template-columns: 1fr; gap: 2rem; }
      .refs-feature { max-width: 100%; margin: 0; aspect-ratio: 1 / 1; max-height: none; justify-self: stretch; }
      .refs-cases { padding: 3.5rem 1.75rem 3rem; }
      .refs-cases-grid { grid-template-columns: 1fr; }
      .refs-deals { padding: 3.5rem 1.75rem 4rem; }
      .refs-deals-toolbar { gap: 0.65rem; }
      .refs-select-field,
      .refs-select { min-width: 0; width: 100%; flex: 1 1 calc(50% - 0.5rem); }
      .refs-tombstones { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 0.55rem; }
      .refs-tombstone { min-height: 210px; }
      .refs-overlay-detail { grid-template-columns: 1fr; }
      .refs-overlay-visual {
        min-height: auto;
        padding: 5rem 1.75rem 2rem;
        border-right: none;
        border-bottom: 0.5px solid var(--border);
      }
      .refs-overlay-content {
        padding: 2rem 1.75rem 3rem;
        max-height: none;
      }
    }
"""


def extract_style(html: str) -> str:
    m = re.search(r"<style>(.*?)</style>", html, re.S)
    return m.group(1) if m else ""


def build_nav(lang: str, ui: dict) -> str:
    a = AUDIENCE[lang]

    def lang_link(code: str) -> str:
        active = " is-active" if lang == code else ""
        current = ' aria-current="true"' if lang == code else ""
        return f'<a href="{LANG_HREFS[code]}" class="nav-lang-link{active}" hreflang="{code}" lang="{code}"{current}>{code.upper()}</a>'

    return f"""  <nav>
    <a href="{ui['home']}" class="logo"><img src="/image.png" alt="Finstant Advisory" width="160" height="40" decoding="async" /></a>
    <ul class="nav-links">
      <li><a href="{a['inv']}">{a['inv_l']}</a></li>
      <li><a href="{a['ent']}">{a['ent_l']}</a></li>
{refs_nav_item(lang, current="refs")}
      <li><a href="{ui['about']}">{ui['about_label']}</a></li>
      <li><a href="{ui['contact']}">{ui['contact_label']}</a></li>
    </ul>
    <div class="nav-right">
      <div class="nav-lang" role="navigation" aria-label="Language">
        {lang_link('en')}
        <span class="nav-lang-sep">/</span>
        {lang_link('de')}
        <span class="nav-lang-sep">/</span>
        {lang_link('it')}
      </div>
      {nav_login(lang)}
    </div>
  </nav>"""


def build_deal_filters(ui: dict) -> str:
    sectors_used = {d["sector"] for d in DATA["deals"]}
    types_used = {d["type"] for d in DATA["deals"]}
    years = sorted({d.get("year") for d in DATA["deals"] if d.get("year")}, reverse=True)

    def select(dim: str, label: str, options: list[tuple[str, str]]) -> str:
        opts = [f'        <option value="all">{ui["filter_all"]}</option>']
        for key, text in options:
            opts.append(f'        <option value="{key}">{text}</option>')
        return f"""      <label class="refs-select-field">
        <span class="refs-select-label">{label}</span>
        <select class="refs-select" data-dim="{dim}" aria-label="{label}">
{chr(10).join(opts)}
        </select>
      </label>"""

    sector_opts = [(k, v) for k, v in ui["sectors"].items() if k in sectors_used]
    type_opts = [(k, v) for k, v in ui["types"].items() if k in types_used]
    year_opts = [(y, y) for y in years]
    return "\n".join(
        [
            select("sector", ui["filter_industry"], sector_opts),
            select("year", ui["filter_year"], year_opts),
            select("type", ui["filter_type"], type_opts),
        ]
    )


def build_case_filters(ui: dict) -> str:
    buttons = [
        f'      <button type="button" class="refs-filter is-active" data-filter="all">{ui["filter_all"]}</button>'
    ]
    for key, label in ui["cases_topics"].items():
        buttons.append(
            f'      <button type="button" class="refs-filter" data-filter="topic:{key}">{label}</button>'
        )
    return "\n".join(buttons)


def build_cases(lang: str) -> str:
    cards = []
    for case in DATA["cases"]:
        c = case[lang]
        cards.append(
            f"""      <a class="refs-case reveal" href="{case['href']}" data-topic="{case['topic']}">
        <div class="refs-case-media">
          <img src="{case['image']}" alt="" width="800" height="500" decoding="async">
        </div>
        <div class="refs-case-body">
          <div class="refs-case-title">{c['title']}</div>
          <p class="refs-case-excerpt">{c['excerpt']}</p>
          <div class="refs-case-meta">{c['meta']}</div>
        </div>
      </a>"""
        )
    return "\n".join(cards)


def build_tombstones(lang: str, ui: dict) -> str:
    cards = []
    for deal in DATA["deals"]:
        sector_label = ui["sectors"][deal["sector"]]
        type_label = ui["types"][deal["type"]]
        cards.append(
            f"""      <button type="button" class="refs-tombstone reveal" data-deal="{deal['id']}" data-sector="{deal['sector']}" data-type="{deal['type']}" data-year="{deal.get('year', '')}" aria-haspopup="dialog">
        <span class="refs-tombstone-face">
          <span class="refs-tombstone-logos">
            <span class="refs-logo-slot">
              <img class="refs-logo refs-logo--target" src="{deal['target_logo']}" alt="{deal['target']}" width="180" height="48" decoding="async" />
            </span>
            <span class="refs-tombstone-rule" aria-hidden="true"></span>
            <span class="refs-tombstone-acquired">{ui['acquired_by']}</span>
            <span class="refs-logo-slot refs-logo-slot--buyer">
              <img class="refs-logo refs-logo--buyer" src="{deal['buyer_logo']}" alt="{deal['buyer']}" width="180" height="40" decoding="async" />
            </span>
          </span>
          <span class="refs-tombstone-badges">
            <span class="refs-badge refs-badge--sector">{sector_label}</span>
            <span class="refs-badge refs-badge--type">{type_label}</span>
          </span>
        </span>
      </button>"""
        )
    return "\n".join(cards)


def build_deal_overlay(lang: str, ui: dict) -> str:
    panels = []
    for deal in DATA["deals"]:
        copy = deal[lang]
        body = copy["body"]
        sector_label = ui["sectors"][deal["sector"]]
        type_label = ui["types"][deal["type"]]
        year = deal.get("year", "")
        highlights = copy.get("highlights") or []
        facts_html = ""
        if highlights:
            items = "\n".join(f"          <li>{item}</li>" for item in highlights)
            facts_html = f"""        <div class="refs-overlay-facts-label">{ui['facts_label']}</div>
        <ul class="refs-overlay-facts">
{items}
        </ul>"""
        sources = deal.get("sources") or []
        sources_html = ""
        if sources:
            links = []
            for src in sources:
                label = src.get(lang) or src.get("en") or src["url"]
                links.append(
                    f'          <li><a href="{src["url"]}" target="_blank" rel="noopener noreferrer">{label}</a></li>'
                )
            sources_html = f"""        <div class="refs-overlay-sources-label">{ui['sources_label']}</div>
        <ul class="refs-overlay-sources">
{chr(10).join(links)}
        </ul>"""
        meta_bits = []
        if year:
            meta_bits.append(f"<span>{year}</span>")
        meta_bits.append(f"<span>{type_label}</span>")
        meta_bits.append(f"<span>{sector_label}</span>")
        meta_html = f'        <div class="refs-overlay-meta">{"".join(meta_bits)}</div>'
        panels.append(
            f"""    <article class="refs-overlay-detail" data-deal="{deal['id']}" hidden>
      <div class="refs-overlay-visual">
        <span class="refs-logo-slot">
          <img class="refs-logo refs-logo--target" src="{deal['target_logo']}" alt="" width="220" height="52" decoding="async" />
        </span>
        <div class="refs-tombstone-rule" aria-hidden="true"></div>
        <div class="refs-tombstone-acquired">{ui['acquired_by']}</div>
        <span class="refs-logo-slot refs-logo-slot--buyer">
          <img class="refs-logo refs-logo--buyer" src="{deal['buyer_logo']}" alt="" width="220" height="48" decoding="async" />
        </span>
        <div class="refs-overlay-badges">
          <span class="refs-badge refs-badge--sector">{sector_label}</span>
          <span class="refs-badge refs-badge--type">{type_label}</span>
        </div>
      </div>
      <div class="refs-overlay-content">
        <h2 class="refs-overlay-title" id="refs-detail-title-{deal['id']}">{deal['target']}</h2>
        <p class="refs-overlay-sub">{ui['acquired_by']} {deal['buyer']}</p>
{meta_html}
        <p class="refs-overlay-body">{body}</p>
{facts_html}
{sources_html}
      </div>
    </article>"""
        )
    return f"""  <div class="refs-overlay" id="refs-overlay" hidden role="dialog" aria-modal="true" aria-label="{ui['deals_title']}">
    <button type="button" class="refs-overlay-close" aria-label="{ui['overlay_close']}">×</button>
{chr(10).join(panels)}
  </div>"""


def build_page(lang: str, base_style: str) -> str:
    ui = DATA["ui"][lang]
    hrefs = "\n".join(
        f'  <link rel="alternate" hreflang="{code}" href="https://www.finstantadvisory.com{LANG_HREFS[code]}" />'
        for code in ("de", "en", "it")
    )
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{ui['title']}</title>
  <meta name="description" content="{ui['description']}" />
  <meta name="robots" content="index, follow" />
  <link rel="canonical" href="{ui['canonical']}" />
{hrefs}
  <link rel="alternate" hreflang="x-default" href="https://www.finstantadvisory.com/de/referenzen/" />
  <link rel="icon" href="/favi.png" type="image/png" />
  <link rel="apple-touch-icon" href="/favi.png" />
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet" />
  <style>
{base_style}
{EXTRA_CSS}
  </style>
{ASSETS}
</head>
<body class="page-refs">

{build_nav(lang, ui)}

  <section class="refs-hero">
    <div class="refs-hero-grid">
      <div class="refs-hero-copy">
        <h1 class="refs-hero-title reveal">{ui['hero_title']}</h1>
        <p class="refs-hero-body reveal">{ui['hero_body']}</p>
      </div>
      <a class="refs-feature reveal reveal-delay-1" href="{ui['feature_href']}">
        <img src="{ui['feature_image']}" alt="{ui['feature_alt']}" width="960" height="600" decoding="async">
        <div class="refs-feature-copy">
          <div class="refs-feature-label">{ui['feature_label']}</div>
          <div class="refs-feature-title">{ui['feature_title']}</div>
          <span class="refs-feature-link">{ui['feature_link']} →</span>
        </div>
      </a>
    </div>
  </section>

  <section class="refs-cases" id="case-studies">
    <div class="refs-cases-inner">
      <h2 class="refs-cases-title reveal">{ui['cases_title']}</h2>
      <div class="refs-filters reveal" role="group" aria-label="{ui['cases_filter_aria']}" data-filter-group="cases">
{build_case_filters(ui)}
      </div>
      <div class="refs-cases-grid">
{build_cases(lang)}
      </div>
    </div>
  </section>

  <section class="refs-deals" id="transactions">
    <div class="refs-deals-inner">
      <h2 class="refs-deals-title reveal">{ui['deals_title']}</h2>
      <p class="refs-deals-hint reveal">{ui['deals_hint']}</p>
      <div class="refs-deals-toolbar reveal" data-filter-group="deals" aria-label="{ui['filter_aria']}">
{build_deal_filters(ui)}
      </div>
      <div class="refs-tombstones" role="list">
{build_tombstones(lang, ui)}
      </div>
      <p class="refs-footnote reveal">{ui['footnote']}</p>
    </div>
  </section>

{build_deal_overlay(lang, ui)}

{footer_html(lang)}

  <script>

    (function () {{
      function wireCaseFilters() {{
        const root = document.querySelector('[data-filter-group="cases"]');
        if (!root) return;
        const filters = root.querySelectorAll('.refs-filter');
        const items = document.querySelectorAll('.refs-case');
        if (!filters.length || !items.length) return;
        filters.forEach((btn) => {{
          btn.addEventListener('click', () => {{
            filters.forEach((b) => b.classList.remove('is-active'));
            btn.classList.add('is-active');
            const value = btn.getAttribute('data-filter') || 'all';
            items.forEach((item) => {{
              if (value === 'all') {{
                item.hidden = false;
                return;
              }}
              const [kind, key] = value.split(':');
              item.hidden = !(kind === 'topic' && item.getAttribute('data-topic') === key);
            }});
          }});
        }});
      }}

      function wireDealFilters() {{
        const root = document.querySelector('[data-filter-group="deals"]');
        if (!root) return;
        const items = document.querySelectorAll('.refs-tombstone');
        const selects = root.querySelectorAll('.refs-select');
        if (!items.length || !selects.length) return;

        function apply() {{
          const state = {{ sector: 'all', year: 'all', type: 'all' }};
          selects.forEach((sel) => {{
            const dim = sel.getAttribute('data-dim');
            if (dim) state[dim] = sel.value || 'all';
          }});
          items.forEach((item) => {{
            const sectorOk = state.sector === 'all' || item.getAttribute('data-sector') === state.sector;
            const yearOk = state.year === 'all' || item.getAttribute('data-year') === state.year;
            const typeOk = state.type === 'all' || item.getAttribute('data-type') === state.type;
            item.hidden = !(sectorOk && yearOk && typeOk);
          }});
        }}

        selects.forEach((sel) => sel.addEventListener('change', apply));
      }}

      wireDealFilters();
      wireCaseFilters();
    }})();

    (function () {{
      const overlay = document.getElementById('refs-overlay');
      const closeBtn = overlay && overlay.querySelector('.refs-overlay-close');
      const picks = document.querySelectorAll('.refs-tombstone');
      const details = overlay ? overlay.querySelectorAll('.refs-overlay-detail') : [];
      if (!overlay || !picks.length || !details.length) return;

      let isOpen = false;
      let activeId = null;

      function showPanel(dealId) {{
        details.forEach((panel) => {{
          const show = panel.dataset.deal === dealId;
          panel.hidden = !show;
          if (show) {{
            overlay.setAttribute('aria-labelledby', 'refs-detail-title-' + dealId);
          }}
        }});
      }}

      function setPickState(dealId) {{
        picks.forEach((btn) => {{
          const on = btn.dataset.deal === dealId;
          btn.classList.toggle('is-selected', on);
        }});
      }}

      function openOverlay(dealId) {{
        activeId = dealId;
        showPanel(dealId);
        setPickState(dealId);
        overlay.hidden = false;
        requestAnimationFrame(() => overlay.classList.add('is-open'));
        document.body.classList.add('refs-overlay-open');
        isOpen = true;
        if (closeBtn) closeBtn.focus();
      }}

      function closeOverlay() {{
        overlay.classList.remove('is-open');
        document.body.classList.remove('refs-overlay-open');
        picks.forEach((btn) => btn.classList.remove('is-selected'));
        const restore = activeId;
        activeId = null;
        isOpen = false;
        window.setTimeout(() => {{
          if (!isOpen) {{
            overlay.hidden = true;
            details.forEach((panel) => {{ panel.hidden = true; }});
            const btn = restore && document.querySelector('.refs-tombstone[data-deal="' + restore + '"]');
            if (btn) btn.focus();
          }}
        }}, 360);
      }}

      picks.forEach((btn) => {{
        btn.addEventListener('click', () => openOverlay(btn.dataset.deal));
      }});
      if (closeBtn) closeBtn.addEventListener('click', closeOverlay);
      document.addEventListener('keydown', (e) => {{
        if (!isOpen) return;
        if (e.key === 'Escape') closeOverlay();
      }});
    }})();
  </script>
{SCRIPT}
</body>
</html>
"""


def patch_home_nav() -> None:
    """Insert References link on hand-edited homepages if missing."""
    inserts = {
        "de": (
            '<li><a href="/de/fuer-unternehmer/">Für Unternehmer</a></li>',
            '<li><a href="/de/fuer-unternehmer/">Für Unternehmer</a></li>\n      <li><a href="/de/referenzen/">Referenzen</a></li>',
        ),
        "en": (
            '<li><a href="/en/for-entrepreneurs/">For entrepreneurs</a></li>',
            '<li><a href="/en/for-entrepreneurs/">For entrepreneurs</a></li>\n      <li><a href="/en/references/">References</a></li>',
        ),
        "it": (
            '<li><a href="/it/per-imprenditori/">Per imprenditori</a></li>',
            '<li><a href="/it/per-imprenditori/">Per imprenditori</a></li>\n      <li><a href="/it/referenze/">Referenze</a></li>',
        ),
    }
    for lang, (needle, replacement) in inserts.items():
        path = ROOT / lang / "index.html"
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        href = LANG_HREFS[lang]
        if href in text:
            continue
        if needle in text:
            text = text.replace(needle, replacement)
            path.write_text(text, encoding="utf-8")
            print(f"Patched home nav: {lang}/index.html")


def main() -> None:
    base_style = extract_style((ROOT / "de" / "index.html").read_text(encoding="utf-8"))
    for lang, ui in DATA["ui"].items():
        out_dir = ROOT / ui["dir"]
        out_dir.mkdir(parents=True, exist_ok=True)
        page = build_page(lang, base_style)
        (out_dir / "index.html").write_text(page, encoding="utf-8")
        print(f"Built {ui['dir']}/index.html")
    patch_home_nav()


if __name__ == "__main__":
    main()
