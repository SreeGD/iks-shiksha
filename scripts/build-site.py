#!/usr/bin/env python3
"""Build a static HTML site for navigating the IKS curriculum.

Generates:
  exports/site/index.html                                 — landing page
  exports/site/<band>/index.html                          — band overview
  exports/site/<band>/<module>/index.html                 — pack overview
  exports/site/<band>/<module>/<filename>.html            — rendered MD
  exports/site/exports.html                               — downloads index

Uses pandoc to convert each .md to HTML; wraps in a consistent template.
"""

import os
import re
import shutil
import subprocess
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "exports" / "site"
CURR = ROOT / "curriculum"
EXPORTS = ROOT / "exports"

# Per-band palette (matches the PPTX decks)
PALETTES = {
    "primary": {"accent1": "#87A96B", "accent2": "#E07A5F", "bg": "#FAF7F2", "name": "Primary"},
    "middle":  {"accent1": "#277884", "accent2": "#FE4447", "bg": "#FFFFFF", "name": "Middle"},
    "senior":  {"accent1": "#5D1D2E", "accent2": "#997929", "bg": "#FAF7F2", "name": "Senior"},
}
GRADES = {"primary": "Grades 3–5", "middle": "Grades 6–8", "senior": "Grades 9–12"}
MODULES = [
    "module-01-what-is-iks",
    "module-02-panchabhuta",
    "module-03-ayurveda-good-health",
    "module-05-dot-addition",
    "module-08-yoga",
]
MODULE_TITLES = {
    "module-01-what-is-iks": "What is IKS?",
    "module-02-panchabhuta": "Panchabhūta (Five Elements)",
    "module-03-ayurveda-good-health": "Ayurveda and Good Health",
    "module-05-dot-addition": "Bindu Paddhati (Dot Method)",
    "module-08-yoga": "Yoga and the Body",
}

# ----- HTML template ------------------------------------------------------

BASE_CSS = """
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; font-family: Georgia, serif;
             background: var(--bg); color: #1a1a1a; line-height: 1.55; }
body { display: grid; grid-template-columns: 1fr; grid-template-rows: auto 1fr;
       min-height: 100vh; }
header.top { background: var(--accent1); color: #fff; padding: 14px 24px;
             display: flex; justify-content: space-between; align-items: center;
             gap: 16px; flex-wrap: wrap; }
header.top a { color: #fff; text-decoration: none; }
header.top h1 { margin: 0; font-size: 18px; font-weight: 700; }
header.top .nav-toggle-cb { display: none; }
header.top .mobile-toggle { display: none; cursor: pointer;
                            padding: 4px 10px; border-radius: 4px;
                            background: rgba(255,255,255,0.12); color: #fff;
                            font-size: 22px; line-height: 1; user-select: none; }
header.top .nav-toggle-cb:checked + .mobile-toggle { background: rgba(255,255,255,0.25); }
header.top nav { display: flex; gap: 16px; font-size: 14px; flex-wrap: wrap; }
header.top nav a { padding: 4px 0; }
header.top nav a:hover { text-decoration: underline; }
.layout { display: grid; grid-template-columns: 240px 1fr; min-height: 100%; }
.layout.no-sidebar { grid-template-columns: 1fr; }
aside.sidebar { background: #fff; border-right: 1px solid #e0d8d0;
                padding: 20px 16px; font-size: 13.5px; }
.sidebar-drawer-toggle { display: none; }
aside.sidebar h3 { font-size: 13px; text-transform: uppercase;
                   letter-spacing: 1.5px; color: var(--accent2);
                   margin: 20px 0 8px 0; font-family: Verdana, sans-serif; }
aside.sidebar h3:first-child { margin-top: 0; }
aside.sidebar ul { list-style: none; padding: 0; margin: 0 0 12px 0; }
aside.sidebar li { margin: 3px 0; }
aside.sidebar a { color: #2a2a2a; text-decoration: none; display: block;
                  padding: 4px 8px; border-radius: 4px; }
aside.sidebar a:hover { background: var(--bg); color: var(--accent1); }
aside.sidebar a.active { background: var(--accent1); color: #fff; }
main { padding: 28px 44px 60px 44px; max-width: 880px; }
main h1, main h2 { font-family: Georgia, serif; color: var(--accent1);
                   margin-top: 1.4em; line-height: 1.2; }
main h1 { font-size: 30px; margin-top: 0; border-bottom: 3px solid var(--accent2);
          padding-bottom: 8px; }
main h2 { font-size: 22px; }
main h3 { font-size: 17px; color: #444; }
main p, main li { font-size: 15.5px; }
main code { background: #f4f1de; padding: 1px 5px; border-radius: 3px;
            font-size: 14px; }
main pre { background: #f4f1de; padding: 12px 16px; border-radius: 6px;
           overflow-x: auto; border-left: 4px solid var(--accent1); }
main pre code { background: none; padding: 0; }
main blockquote { border-left: 5px solid var(--accent2); margin: 16px 0;
                  padding: 8px 16px; background: #fff; font-style: italic;
                  color: #444; }
main table { border-collapse: collapse; margin: 12px 0; width: 100%; }
main th, main td { border: 1px solid #ddd; padding: 8px 10px; text-align: left;
                   vertical-align: top; font-size: 14.5px; }
main th { background: var(--accent1); color: #fff; }
main hr { border: none; border-top: 1px solid #ccc; margin: 32px 0; }
main a { color: var(--accent1); }
.crumbs { font-size: 13px; color: #666; margin-bottom: 12px; }
.crumbs a { color: var(--accent2); text-decoration: none; }
.cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
         gap: 18px; margin: 18px 0; }
.card { background: #fff; padding: 20px; border-radius: 8px;
        border-left: 5px solid var(--accent2); text-decoration: none;
        color: #1a1a1a; box-shadow: 0 1px 3px rgba(0,0,0,0.05); }
.card:hover { transform: translateY(-2px); box-shadow: 0 4px 10px rgba(0,0,0,0.08); }
.card h3 { margin: 0 0 6px 0; color: var(--accent1); }
.card p { margin: 0; font-size: 13.5px; color: #555; }
.kicker { font-size: 11px; letter-spacing: 2px; color: var(--accent2);
          text-transform: uppercase; font-weight: bold; font-family: Verdana; }
.downloads { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
             gap: 12px; margin: 20px 0; }
.dlcard { background: #fff; padding: 14px 18px; border-radius: 6px;
          border: 1px solid #e0d8d0; text-decoration: none; color: #1a1a1a;
          display: flex; align-items: center; gap: 10px; font-size: 14px; }
.dlcard:hover { border-color: var(--accent1); }
.dlcard .badge { background: var(--accent1); color: #fff; padding: 2px 8px;
                 border-radius: 3px; font-size: 11px; font-weight: bold; }
footer.bottom { font-size: 12px; color: #888; text-align: center; padding: 24px;
                background: #fff; border-top: 1px solid #e0d8d0; }

/* ----- Mobile (< 800px) ----- */
@media (max-width: 800px) {
  .layout { grid-template-columns: 1fr; }
  main { padding: 20px; }
  /* Header nav -> hamburger */
  header.top { padding: 12px 16px; flex-wrap: nowrap; position: relative; }
  header.top .mobile-toggle { display: inline-block; }
  header.top nav { display: none; }
  header.top .nav-toggle-cb:checked ~ nav { display: flex; flex-direction: column;
       position: absolute; top: 52px; right: 0; left: 0;
       background: var(--accent1); padding: 12px 20px; gap: 12px;
       box-shadow: 0 6px 12px rgba(0,0,0,0.15); z-index: 1000; }
  /* Sidebar -> collapsible drawer */
  aside.sidebar { padding: 0; border-right: none; border-bottom: 1px solid #e0d8d0;
                  background: #fff; }
  .sidebar-drawer-toggle { display: block; cursor: pointer; padding: 14px 20px;
                           background: var(--bg); border: none; width: 100%;
                           text-align: left; font-family: Verdana, sans-serif;
                           font-size: 14px; font-weight: bold; color: var(--accent1);
                           list-style: none; user-select: none; }
  .sidebar-drawer-toggle::-webkit-details-marker { display: none; }
  .sidebar-drawer-toggle::after { content: " ▾"; font-size: 12px; color: var(--accent2); }
  details.sidebar-drawer[open] .sidebar-drawer-toggle::after { content: " ▴"; }
  .sidebar-drawer .sidebar-inner { padding: 16px 20px 24px 20px; }
}

/* ----- Print ----- */
@media print {
  html, body { background: #fff; color: #000; }
  header.top, aside.sidebar, footer.bottom,
  .crumbs, .downloads, .sidebar-drawer-toggle { display: none !important; }
  /* Hide the "Download guides" + "Daily lessons" sections (they're noise on paper).
     They are flagged by their preceding h2 with emoji prefix. */
  main h2:has(+ p + table) + p + table { display: none; }
  main h2:has(+ p + .downloads) + p + .downloads { display: none; }
  .layout { display: block; }
  main { max-width: 100%; padding: 0; margin: 0; font-size: 11pt; }
  main h1 { font-size: 18pt; }
  main h2 { font-size: 14pt; page-break-after: avoid; }
  main h3 { font-size: 12pt; page-break-after: avoid; }
  main a { color: #000; text-decoration: none; }
  main pre, main blockquote { break-inside: avoid; }
}
"""

def page_template(title, body, palette, crumbs_html="", sidebar_html=None, depth=0):
    accent1 = palette["accent1"]
    accent2 = palette["accent2"]
    bg = palette["bg"]
    rel = "../" * depth
    layout_cls = "" if sidebar_html else "no-sidebar"
    if sidebar_html:
        # Wrap sidebar in a <details> drawer for mobile; open by default on desktop.
        sidebar = (
            f'<aside class="sidebar">'
            f'  <details class="sidebar-drawer" open>'
            f'    <summary class="sidebar-drawer-toggle">📚 In this pack</summary>'
            f'    <div class="sidebar-inner">{sidebar_html}</div>'
            f'  </details>'
            f'</aside>'
        )
    else:
        sidebar = ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)} — IKS Curriculum</title>
<style>
:root {{ --accent1: {accent1}; --accent2: {accent2}; --bg: {bg}; }}
{BASE_CSS}
</style>
</head>
<body>
<header class="top">
  <h1><a href="{rel}index.html">IKS Curriculum</a></h1>
  <input type="checkbox" id="nav-toggle" class="nav-toggle-cb" aria-label="Open menu">
  <label for="nav-toggle" class="mobile-toggle" aria-hidden="true">☰</label>
  <nav>
    <a href="{rel}primary/index.html">Primary</a>
    <a href="{rel}middle/index.html">Middle</a>
    <a href="{rel}senior/index.html">Senior</a>
    <a href="{rel}exports.html">Downloads</a>
    <a href="{rel}backlog.html">Backlog</a>
    <a href="{rel}attribution.html">Attribution</a>
  </nav>
</header>
<div class="layout {layout_cls}">
{sidebar}
<main>
{crumbs_html}
{body}
</main>
</div>
<footer class="bottom">
  IKS Curriculum · static site · see <a href="{rel}attribution.html">Attribution</a>
</footer>
</body>
</html>
"""

# ----- pandoc helper ------------------------------------------------------

def md_to_html_body(md_path: Path) -> str:
    """Convert a markdown file to an HTML body fragment via pandoc.

    Post-processes link targets to rewrite *.md → *.html and ATTRIBUTION.md →
    attribution.html so cross-document links work in the built site.
    """
    result = subprocess.run(
        ["pandoc", str(md_path), "--from=markdown+raw_html", "--to=html",
         "--no-highlight"],
        capture_output=True, text=True, check=True
    )
    out = result.stdout
    # Rewrite top-level uppercase doc names to their site equivalents
    out = re.sub(r'href="ATTRIBUTION\.md"', 'href="attribution.html"', out)
    out = re.sub(r'href="BACKLOG\.md"', 'href="backlog.html"', out)
    out = re.sub(r'href="README\.md"', 'href="README.html"', out)
    # Generic: rewrite href="...path/file.md" to href="...path/file.html"
    out = re.sub(r'(href="[^"]+?)\.md"', r'\1.html"', out)
    return out

def md_text_to_html(md: str) -> str:
    result = subprocess.run(
        ["pandoc", "--from=markdown", "--to=html", "--no-highlight"],
        input=md, capture_output=True, text=True, check=True
    )
    return result.stdout

# ----- file naming --------------------------------------------------------

def pretty_name(filename: str) -> str:
    stem = Path(filename).stem
    label = {
        "README": "Overview",
        "lesson-plan": "10-Day Lesson Plan",
        "teacher-notes": "Teacher Notes",
        "sources": "Sources",
        "parent-guide": "Parent Guide",
        "writing-prompts": "Writing Prompts",
        "homework": "Homework",
        "student-workbook": "Student Workbook",
        "rubric": "Rubric",
        "project-brief": "Project Brief",
        "formative": "Formative Quiz",
        "summative": "Summative Quiz",
        "oral-recall": "Oral Recall",
        "deck": "Slide Deck (source)",
    }.get(stem, None)
    if label:
        return label
    # Day file?
    m = re.match(r"day-(\d+)-(.+)", stem)
    if m:
        n, slug = m.group(1), m.group(2)
        return f"Day {int(n)} — {slug.replace('-', ' ').title()}"
    # Activity file?
    m = re.match(r"activity-(\d+)-(.+)", stem)
    if m:
        n, slug = m.group(1), m.group(2)
        return f"Activity {int(n)} — {slug.replace('-', ' ').title()}"
    return stem.replace('-', ' ').title()

# ----- sidebar builder ----------------------------------------------------

def build_pack_sidebar(band: str, module: str, current_file: str | None = None,
                       depth_in_pack: int = 0) -> str:
    """Build the sidebar HTML.

    `depth_in_pack` is how many folders deep the current page sits inside
    the pack (0 = pack root index.html; 1 = days/day-01.html, etc.).
    Links are prefixed with `../` × depth_in_pack so they resolve correctly
    no matter where they're embedded.
    """
    pack_dir = CURR / module if False else CURR / band / module
    prefix = "../" * depth_in_pack
    sections = []

    sections.append(("Pack", [("index.html", "Pack overview")]))

    core = []
    for fname in ["README.md", "lesson-plan.md", "teacher-notes.md",
                  "sources.md", "parent-guide.md"]:
        if (pack_dir / fname).exists():
            core.append((Path(fname).stem + ".html", pretty_name(fname)))
    if core:
        sections.append(("Core", core))

    days = []
    if (pack_dir / "days").is_dir():
        for f in sorted((pack_dir / "days").glob("day-*.md")):
            days.append((f"days/{f.stem}.html", pretty_name(f.name)))
    if days:
        sections.append(("Daily lessons", days))

    quizzes = []
    if (pack_dir / "quizzes").is_dir():
        for f in sorted((pack_dir / "quizzes").glob("*.md")):
            quizzes.append((f"quizzes/{f.stem}.html", pretty_name(f.name)))
    if quizzes:
        sections.append(("Quizzes", quizzes))

    activities = []
    if (pack_dir / "activities").is_dir():
        for f in sorted((pack_dir / "activities").glob("*.md")):
            activities.append((f"activities/{f.stem}.html", pretty_name(f.name)))
    if activities:
        sections.append(("Activities", activities))

    assessments = []
    if (pack_dir / "assessments").is_dir():
        for f in sorted((pack_dir / "assessments").glob("*.md")):
            assessments.append((f"assessments/{f.stem}.html", pretty_name(f.name)))
    if assessments:
        sections.append(("Assessments", assessments))

    other = []
    for fname in ["writing-prompts.md", "homework.md", "student-workbook.md"]:
        if (pack_dir / fname).exists():
            other.append((Path(fname).stem + ".html", pretty_name(fname)))
    if other:
        sections.append(("Other", other))

    if (pack_dir / "slides" / "deck.md").exists():
        sections.append(("Slides", [("slides/deck.html", "Deck (markdown source)")]))

    html = []
    for sect_name, items in sections:
        html.append(f'<h3>{escape(sect_name)}</h3><ul>')
        for href, label in items:
            cls = " class='active'" if current_file == href else ""
            html.append(f'<li><a href="{prefix}{href}"{cls}>{escape(label)}</a></li>')
        html.append('</ul>')
    return "\n".join(html)

# ----- page generators ----------------------------------------------------

def write_landing():
    body = """<p class="kicker">IKS Curriculum · Pilot</p>
<h1>Indian Knowledge Systems Curriculum</h1>
<p>A three-age-band school curriculum covering 15 modules on Indian Knowledge Systems — adapted across primary, middle, and senior school years. See the <a href="attribution.html">attribution page</a> for sources and inspirations.</p>
<p>This pilot covers <strong>5 modules across 3 age bands — 15 module packs</strong> in total. The full curriculum continues in <a href="backlog.html">the backlog</a>.</p>

<h2>Pick a band</h2>
<div class="cards">
  <a class="card" href="primary/index.html" style="border-left-color: #87A96B;">
    <span class="kicker" style="color:#87A96B;">Primary</span>
    <h3 style="color:#87A96B;">Grades 3–5</h3>
    <p>Story-led, drawing-heavy, 30-minute sessions. Sticker-based assessment.</p>
  </a>
  <a class="card" href="middle/index.html">
    <span class="kicker">Middle</span>
    <h3>Grades 6–8</h3>
    <p>Original audience. Balanced text + activity, 45-minute sessions, mixed quizzes, projects.</p>
  </a>
  <a class="card" href="senior/index.html" style="border-left-color: #997929;">
    <span class="kicker" style="color:#997929;">Senior</span>
    <h3 style="color:#5D1D2E;">Grades 9–12</h3>
    <p>Primary-source reading, research-paper projects, structured debate.</p>
  </a>
</div>

<h2>The five pilot modules</h2>
<div class="cards">
  <div class="card">
    <span class="kicker">Module 1</span>
    <h3>What is IKS?</h3>
    <p>The map of Indian Knowledge Systems — Vedas, Vedangas, Upavedas, named achievements with dates.</p>
  </div>
  <div class="card">
    <span class="kicker">Module 2</span>
    <h3>Panchabhūta — Five Elements</h3>
    <p>The Sāṅkhya cosmology of earth, water, fire, air, space — taught alongside states of matter.</p>
  </div>
  <div class="card">
    <span class="kicker">Module 3</span>
    <h3>Ayurveda and Good Health</h3>
    <p>Tridosha, dinacharya, ahāra. Lifestyle medicine + honest modern evidence framing.</p>
  </div>
  <div class="card">
    <span class="kicker">Module 5</span>
    <h3>Bindu Paddhati — Dot Addition</h3>
    <p>The 20th-century mental-arithmetic technique for fast column addition.</p>
  </div>
  <div class="card">
    <span class="kicker">Module 8</span>
    <h3>Yoga and the Body</h3>
    <p>Patañjali's eight limbs + safe āsana practice + breath physiology.</p>
  </div>
</div>

<h2>How to use</h2>
<p>Read the <strong>Overview</strong> first, then pick a band, then a module. Inside each pack the sidebar lists day files, quizzes, activities, project brief, and rubric.</p>
<p>For downloads (PPTX decks, PDF guides, DOCX workbooks), see <a href="exports.html">the downloads page</a>.</p>

<h2>Source-of-truth retrieval</h2>
<p>Citations come from two upstream systems:</p>
<ul>
  <li><strong>vidya-karana-kg RAG</strong> — Bhāgavatam, Bhagavad-gītā, Caitanya-caritāmṛta, Prabhupāda works (~89k chunks)</li>
  <li><strong>SutraGanita corpus</strong> — Bharati Krishna Tirthaji's <em>Vedic Mathematics</em> + Vedic Cultural Center materials</li>
</ul>
<p>Every scripture verse cited in a lesson has a matching cached RAG retrieval — see each pack's <code>.rag-cache/</code> folder.</p>
"""
    html = page_template("IKS Curriculum", body, PALETTES["middle"], depth=0)
    (SITE / "index.html").write_text(html, encoding="utf-8")

def write_band_page(band: str):
    pal = PALETTES[band]
    name = pal["name"]
    grades = GRADES[band]
    crumbs = f'<div class="crumbs"><a href="../index.html">Home</a> › {name}</div>'
    cards = []
    for mod in MODULES:
        if not (CURR / band / mod).is_dir():
            continue
        title = MODULE_TITLES[mod]
        cards.append(f'''
<a class="card" href="{mod}/index.html">
  <span class="kicker">{escape(mod)}</span>
  <h3>{escape(title)}</h3>
  <p>10-day lesson plan, quizzes, activities, project, slide deck.</p>
</a>''')
    band_descriptions = {
        "primary": "Grades 3–5. Story-led, sensory, lots of drawing. 30-minute sessions. Sticker assessments. Sanskrit terms learned through a daily chant.",
        "middle": "Grades 6–8 — the original audience for the source program. 45-minute sessions. Balanced text + hands-on activity. Project-based assessment with rubric. Sanskrit terms with transliteration and meaning; verses cited from primary sources.",
        "senior": "Grades 9–12. Primary-source reading in IAST. Argumentative writing. Structured debate. Research-synthesis papers. Engagement with scholarly debates about IKS labelling and history.",
    }
    body = f'''{crumbs}
<p class="kicker">{escape(name)} · {escape(grades)}</p>
<h1>{escape(name)} Band</h1>
<p>{escape(band_descriptions[band])}</p>

<h2>Modules in this band</h2>
<div class="cards">
{''.join(cards)}
</div>
'''
    html = page_template(name, body, pal, depth=1)
    (SITE / band / "index.html").write_text(html, encoding="utf-8")

def write_pack_overview(band: str, mod: str):
    pal = PALETTES[band]
    pack_dir = CURR / band / mod
    title = MODULE_TITLES[mod]
    crumbs = f'<div class="crumbs"><a href="../../index.html">Home</a> › <a href="../index.html">{pal["name"]}</a> › {escape(mod)}</div>'

    sidebar = build_pack_sidebar(band, mod, current_file="index.html")
    readme_html = md_to_html_body(pack_dir / "README.md") if (pack_dir / "README.md").exists() else "<p>(no overview)</p>"

    # Build the 4-guide download grid (Teacher / Parent / Student / Activities)
    stem = f"{band}-{mod}"
    guide_cards = []
    guide_meta = [
        ("teacher", "Teacher Guide", "Full pack — lesson plan, day files, teacher notes, quizzes, rubric"),
        ("parent", "Parent Guide", "What your child is learning, how to support at home"),
        ("student", "Student Guide", "Workbook + day-by-day reading + writing prompts"),
        ("activities", "Activity Pack", "Printable activity sheets + project brief"),
    ]
    for kind, label, desc in guide_meta:
        pdf_rel = f"../../pdf/{stem}-{kind}.pdf"
        pdf_path = EXPORTS / "pdf" / f"{stem}-{kind}.pdf"
        if pdf_path.exists():
            size_kb = pdf_path.stat().st_size // 1024
            guide_cards.append(f'''
<a class="dlcard" href="{pdf_rel}" download>
  <span class="badge">PDF</span>
  <span><strong>{escape(label)}</strong><br><small style="color:#666;">{escape(desc)} · {size_kb} KB</small></span>
</a>''')

    # Slide deck + workbook if available
    pptx_path = EXPORTS / "pptx" / f"{stem}.pptx"
    if pptx_path.exists():
        size_kb = pptx_path.stat().st_size // 1024
        guide_cards.append(f'''
<a class="dlcard" href="../../pptx/{stem}.pptx" download>
  <span class="badge" style="background:var(--accent2);">PPTX</span>
  <span><strong>Slide Deck</strong><br><small style="color:#666;">~20-slide classroom deck · {size_kb} KB</small></span>
</a>''')

    docx_path = EXPORTS / "docx" / f"iks-curriculum-{band}.docx"
    if docx_path.exists():
        size_kb = docx_path.stat().st_size // 1024
        guide_cards.append(f'''
<a class="dlcard" href="../../docx/iks-curriculum-{band}.docx" download>
  <span class="badge" style="background:#666;">DOCX</span>
  <span><strong>Full {escape(pal["name"])} Workbook</strong><br><small style="color:#666;">All 5 modules combined · {size_kb} KB</small></span>
</a>''')

    downloads_html = f'''
<h2 style="margin-top: 36px;">📥 Download guides</h2>
<p style="font-size: 14px; color: #555;">Four audience-specific PDFs plus the slide deck and combined workbook for this band.</p>
<div class="downloads">{''.join(guide_cards)}</div>
''' if guide_cards else ''

    # Build the per-day "Daily Lessons" table (10 days each with PDF + PPTX + HTML view)
    daily_rows = []
    pack_pdf_dir = EXPORTS / "pdf" / "lessons" / stem
    pack_pptx_dir = EXPORTS / "pptx" / "lessons" / stem
    if (pack_dir / "days").is_dir():
        for f in sorted((pack_dir / "days").glob("day-*.md")):
            day_stem = f.stem
            label = pretty_name(f.name)
            html_link = f'days/{day_stem}.html'
            pdf_file = pack_pdf_dir / f"{day_stem}.pdf"
            pptx_file = pack_pptx_dir / f"{day_stem}.pptx"
            pdf_cell = (f'<a href="../../pdf/lessons/{stem}/{day_stem}.pdf" download>📄 PDF</a>'
                        if pdf_file.exists() else '<span style="color:#aaa;">—</span>')
            pptx_cell = (f'<a href="../../pptx/lessons/{stem}/{day_stem}.pptx" download>📊 PPTX</a>'
                         if pptx_file.exists() else '<span style="color:#aaa;">—</span>')
            daily_rows.append(
                f'<tr><td><a href="{html_link}"><strong>{escape(label)}</strong></a></td>'
                f'<td style="text-align:center;">{pdf_cell}</td>'
                f'<td style="text-align:center;">{pptx_cell}</td></tr>'
            )

    daily_html = ''
    if daily_rows:
        daily_html = f'''
<h2 style="margin-top: 36px;">📚 Daily lessons</h2>
<p style="font-size: 14px; color: #555;">Click the lesson title to read it online, or download a printable PDF / projector-ready PPTX for any day.</p>
<table style="margin-top: 12px;">
  <tr><th style="width: 60%;">Lesson</th><th style="text-align:center; width:20%;">Printable handout</th><th style="text-align:center; width:20%;">Slide deck</th></tr>
  {''.join(daily_rows)}
</table>
'''

    body = f'''{crumbs}
<p class="kicker">{escape(pal["name"])} · {escape(GRADES[band])}</p>
{readme_html}
{daily_html}
{downloads_html}
'''
    html = page_template(f"{title} — {pal['name']}", body, pal,
                         sidebar_html=sidebar, depth=2)
    out_dir = SITE / band / mod
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "index.html").write_text(html, encoding="utf-8")

def write_pack_file(band: str, mod: str, rel_md: Path):
    """Render one .md file from a pack as an HTML page."""
    pal = PALETTES[band]
    pack_dir = CURR / band / mod

    # Compute relative location for current_file marker
    rel_str = rel_md.as_posix()
    if rel_str.endswith(".md"):
        rel_html = rel_str[:-3] + ".html"
    else:
        rel_html = rel_str

    # Depth from the file's directory back to site root
    depth = 2 + len(rel_md.parent.parts)  # band/mod + subdir(s)
    # Band index lives at depth-1 ups + index.html (no extra band/ prefix).
    crumbs = (f'<div class="crumbs"><a href="{"../" * depth}index.html">Home</a>'
              f' › <a href="{"../" * (depth - 1)}index.html">{pal["name"]}</a>'
              f' › <a href="{"../" * len(rel_md.parent.parts)}index.html">{escape(mod)}</a>'
              f' › {escape(pretty_name(rel_md.name))}</div>')

    md_path = pack_dir / rel_md
    html_body = md_to_html_body(md_path)
    sidebar = build_pack_sidebar(band, mod, current_file=rel_html,
                                 depth_in_pack=len(rel_md.parent.parts))
    body = f"{crumbs}{html_body}"

    out_path = SITE / band / mod / rel_html
    out_path.parent.mkdir(parents=True, exist_ok=True)
    title = pretty_name(rel_md.name)
    html = page_template(title, body, pal, sidebar_html=sidebar, depth=depth)
    out_path.write_text(html, encoding="utf-8")

def write_pack(band: str, mod: str):
    pack_dir = CURR / band / mod
    if not pack_dir.is_dir():
        return
    write_pack_overview(band, mod)
    # Render each .md (skip .rag-cache and .sutraganita-cache)
    for md_path in pack_dir.rglob("*.md"):
        if any(p.startswith(".") for p in md_path.relative_to(pack_dir).parts):
            continue
        rel = md_path.relative_to(pack_dir)
        write_pack_file(band, mod, rel)

def write_exports_page():
    pal = PALETTES["middle"]
    crumbs = '<div class="crumbs"><a href="index.html">Home</a> › Downloads</div>'

    pptx_files = sorted((EXPORTS / "pptx").glob("*.pptx")) if (EXPORTS / "pptx").is_dir() else []
    pdf_files = sorted((EXPORTS / "pdf").glob("*.pdf")) if (EXPORTS / "pdf").is_dir() else []
    docx_files = sorted((EXPORTS / "docx").glob("*.docx")) if (EXPORTS / "docx").is_dir() else []

    def section(title, files, badge):
        if not files:
            return ""
        cards = []
        for f in files:
            size = f.stat().st_size
            kb = size // 1024
            label = f.stem.replace('-', ' ').title()
            cards.append(f'''
<a class="dlcard" href="../{f.relative_to(EXPORTS).as_posix()}" download>
  <span class="badge">{escape(badge)}</span>
  <span>{escape(label)} <small style="color:#888;">({kb} KB)</small></span>
</a>''')
        return f"<h2>{escape(title)}</h2><div class='downloads'>{''.join(cards)}</div>"

    body = f'''{crumbs}
<h1>Downloads</h1>
<p>All exports are regenerated from the markdown source. The markdown is the source of truth.</p>

{section("PPTX Slide Decks (9 decks)", pptx_files, "PPTX")}

<h2>PDF Audience Guides (36 PDFs)</h2>
<p>Each pack has 4 audience-specific PDFs: <strong>teacher</strong>, <strong>parent</strong>, <strong>student</strong>, <strong>activity</strong>.</p>
{section("PDF guides", pdf_files, "PDF")}

{section("DOCX Combined Workbooks (3 workbooks)", docx_files, "DOCX")}
'''
    html = page_template("Downloads", body, pal, depth=0)
    (SITE / "exports.html").write_text(html, encoding="utf-8")

def write_backlog_page():
    pal = PALETTES["middle"]
    crumbs = '<div class="crumbs"><a href="index.html">Home</a> › Backlog</div>'
    backlog_path = ROOT / "BACKLOG.md"
    if backlog_path.exists():
        html_body = md_to_html_body(backlog_path)
    else:
        html_body = "<p>No BACKLOG.md found.</p>"
    body = f"{crumbs}{html_body}"
    html = page_template("Backlog", body, pal, depth=0)
    (SITE / "backlog.html").write_text(html, encoding="utf-8")

def write_attribution_page():
    pal = PALETTES["middle"]
    crumbs = '<div class="crumbs"><a href="index.html">Home</a> › Attribution</div>'
    attr_path = ROOT / "ATTRIBUTION.md"
    if attr_path.exists():
        html_body = md_to_html_body(attr_path)
    else:
        html_body = "<p>No ATTRIBUTION.md found.</p>"
    body = f"{crumbs}{html_body}"
    html = page_template("Attribution", body, pal, depth=0)
    (SITE / "attribution.html").write_text(html, encoding="utf-8")

# ----- Main ---------------------------------------------------------------

def main():
    # Clean previous site
    if SITE.exists():
        shutil.rmtree(SITE)
    SITE.mkdir(parents=True)
    (SITE / "primary").mkdir()
    (SITE / "middle").mkdir()
    (SITE / "senior").mkdir()

    # Landing + band pages
    write_landing()
    for band in ["primary", "middle", "senior"]:
        write_band_page(band)
        for mod in MODULES:
            write_pack(band, mod)
    write_exports_page()
    write_backlog_page()
    write_attribution_page()

    # Symlink exports/{pdf,pptx,docx} into the site dir so relative download
    # links inside HTML pages work without escaping the site root.
    for sub in ("pdf", "pptx", "docx"):
        target = EXPORTS / sub
        link = SITE / sub
        if target.exists():
            if link.is_symlink() or link.exists():
                link.unlink() if link.is_symlink() else shutil.rmtree(link)
            link.symlink_to(target.resolve())

    # Count pages
    pages = list(SITE.rglob("*.html"))
    print(f"Generated {len(pages)} HTML pages")
    print(f"Site root: {SITE}")
    print(f"Open: open {SITE}/index.html")

if __name__ == "__main__":
    main()
