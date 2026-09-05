#!/usr/bin/env python3
"""Compile the tutorial's Markdown into a static site for GitHub Pages.

The Markdown in tutorial/ is the single source of truth. This script is the
only thing that produces HTML, and the HTML is never committed — the workflow
in .github/workflows/pages.yml runs this and publishes the result.

Usage:  python3 scripts/build_site.py [output_dir]
"""
from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "_site"

SITE_TITLE = "Maintainable Vibecoding"
SITE_BLURB = (
    "Build a real web app with an AI assistant, and still understand it "
    "six months later. A complete course for someone who has never opened a terminal."
)

# Order matters: it drives the sidebar and the prev/next links.
CHAPTERS = [
    ("01-what-youre-making", "What you're making"),
    ("02-the-stack-and-why", "The stack, and why"),
    ("03-your-macs-control-room", "Your Mac's control room"),
    ("04-the-toolbox", "The toolbox"),
    ("05-github", "GitHub"),
    ("06-talking-to-claude", "Talking to Claude Code"),
    ("07-build-the-calendar", "Build the calendar"),
    ("08-vercel", "Put it on the internet"),
    ("09-holidays", "Add the holidays"),
    ("10-appointments-and-a-database", "Add a database"),
    ("11-staying-maintainable", "Staying maintainable"),
]

APPENDICES = [
    ("appendix-a-when-it-breaks", "A · When it breaks"),
    ("appendix-b-glossary", "B · Glossary"),
    ("appendix-c-what-it-costs", "C · What it costs"),
]

CSS = """
:root {
  --paper: #f4f1e8;
  --paper-raised: #faf7f0;
  --ink: #26211c;
  --ink-soft: #6b6157;
  --red-ink: #a8322a;
  --blue-ink: #33455f;
  --rule: #d8d0be;
}
@media (prefers-color-scheme: dark) {
  :root {
    --paper: #211d19;
    --paper-raised: #2a2521;
    --ink: #ece5da;
    --red-ink: #d9705f;
    --blue-ink: #9fb4d4;
    --ink-soft: #a89d90;
    --rule: #3c3630;
  }
}
* { box-sizing: border-box; }
html { -webkit-text-size-adjust: 100%; }
body {
  margin: 0;
  background: var(--paper);
  color: var(--ink);
  font-family: Newsreader, Georgia, "Times New Roman", serif;
  font-size: 18px;
  line-height: 1.65;
  font-optical-sizing: auto;
}
/* Paper is never perfectly flat. One SVG filter, no image to download. */
body::before {
  content: "";
  position: fixed; inset: 0; z-index: 50;
  pointer-events: none; opacity: .26; mix-blend-mode: multiply;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='g'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.82' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23g)'/%3E%3C/svg%3E");
}
@media (prefers-color-scheme: dark) {
  body::before { mix-blend-mode: screen; opacity: .12; }
}
.shell { display: flex; gap: 3rem; max-width: 1180px; margin: 0 auto; padding: 0 1.5rem; }
nav.side {
  width: 15rem; flex: none; padding: 2.5rem 0 4rem;
  position: sticky; top: 0; align-self: flex-start; max-height: 100vh; overflow-y: auto;
}
nav.side .brand {
  font-family: "Instrument Serif", Georgia, serif;
  font-size: 1.6rem; line-height: 1.05; display: block;
  color: var(--ink); text-decoration: none; margin-bottom: .3rem;
}
nav.side .brand em { color: var(--red-ink); font-style: normal; }
nav.side h2 {
  font-size: .62rem; letter-spacing: .2em; text-transform: uppercase;
  color: var(--ink-soft); margin: 1.8rem 0 .5rem; font-weight: 400;
}
nav.side ol { list-style: none; margin: 0; padding: 0; counter-reset: ch; }
nav.side li { margin: 0 0 .12rem; }
nav.side a {
  display: block; padding: .22rem .5rem .22rem .55rem;
  color: var(--ink-soft); text-decoration: none;
  font-size: .88rem; line-height: 1.3; border-left: 2px solid transparent;
}
nav.side a:hover { color: var(--ink); background: rgba(0,0,0,.03); }
nav.side a.current { color: var(--red-ink); border-left-color: var(--red-ink); }
main { flex: 1 1 auto; min-width: 0; padding: 2.5rem 0 5rem; max-width: 46rem; }
h1, h2, h3 { font-family: "Instrument Serif", Georgia, serif; font-weight: 400; letter-spacing: -.01em; }
h1 { font-size: clamp(2.4rem, 6vw, 3.6rem); line-height: 1; margin: 0 0 1.6rem; }
h2 { font-size: 1.9rem; margin: 2.8rem 0 .8rem; padding-top: .9rem; border-top: 1px solid var(--rule); }
h3 { font-size: 1.35rem; margin: 2rem 0 .5rem; }
p, ul, ol { margin: 0 0 1.05rem; }
li { margin-bottom: .3rem; }
a { color: var(--blue-ink); text-underline-offset: 2px; }
a:hover { color: var(--red-ink); }
strong { font-weight: 600; }
hr { border: 0; border-top: 1px solid var(--rule); margin: 2.4rem 0; }
/* Sections are written as `---` then a heading, and the heading carries its own
   rule. Without this the two stack up into a double line and a large gap. */
hr + h2 { border-top: 0; padding-top: 0; margin-top: 1.5rem; }
hr:has(+ h2) { margin-bottom: 0; }
blockquote {
  margin: 1.4rem 0; padding: .1rem 0 .1rem 1.1rem;
  border-left: 2px solid var(--red-ink); color: var(--ink-soft);
}
blockquote strong { color: var(--ink); }
code {
  font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
  font-size: .86em; background: rgba(120,100,70,.11);
  padding: .12em .38em; border-radius: 2px;
}
pre {
  background: var(--paper-raised); border: 1px solid var(--rule);
  padding: .9rem 1.1rem; overflow-x: auto; border-radius: 2px;
  font-size: .82rem; line-height: 1.55;
}
pre code { background: none; padding: 0; font-size: inherit; }
table { border-collapse: collapse; width: 100%; margin: 1.3rem 0; font-size: .93rem; }
th, td { border: 1px solid var(--rule); padding: .5rem .7rem; text-align: left; vertical-align: top; }
th { background: rgba(120,100,70,.07); font-weight: 600; }
img { max-width: 100%; height: auto; border: 1px solid var(--rule); border-radius: 2px; display: block; margin: 1.4rem 0; }
.pager { display: flex; justify-content: space-between; gap: 1rem; margin-top: 3rem; padding-top: 1.2rem; border-top: 1px solid var(--rule); font-size: .92rem; }
.pager a { text-decoration: none; }
footer.site { max-width: 1180px; margin: 0 auto; padding: 2rem 1.5rem 3rem; color: var(--ink-soft); font-size: .8rem; border-top: 1px solid var(--rule); }
.menu-toggle { display: none; }
@media (max-width: 860px) {
  .shell { flex-direction: column; gap: 0; padding: 0 1.1rem; }
  nav.side { width: auto; position: static; max-height: none; padding: 1.6rem 0 .5rem; border-bottom: 1px solid var(--rule); }
  nav.side ol { columns: 2; column-gap: 1.2rem; }
  main { padding-top: 1.6rem; }
  body { font-size: 17px; }
}
"""

FONTS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?'
    "family=Instrument+Serif:ital@0;1&"
    'family=Newsreader:opsz,wght@6..72,300;6..72,400;6..72,600&display=swap" rel="stylesheet">'
)


def nav_html(current: str, depth: int) -> str:
    """Sidebar. `depth` is how many directories deep the page is."""
    up = "../" * depth
    parts = [
        f'<nav class="side"><a class="brand" href="{up}index.html">'
        f"Maintainable<br><em>Vibecoding</em></a>",
        '<h2>Chapters</h2><ol>',
    ]
    for i, (slug, title) in enumerate(CHAPTERS, 1):
        cls = ' class="current"' if slug == current else ""
        parts.append(
            f'<li><a{cls} href="{up}tutorial/{slug}.html">'
            f"<span>{i}.</span> {title}</a></li>"
        )
    parts.append("</ol><h2>Appendices</h2><ol>")
    for slug, title in APPENDICES:
        cls = ' class="current"' if slug == current else ""
        parts.append(f'<li><a{cls} href="{up}tutorial/{slug}.html">{title}</a></li>')
    parts.append("</ol></nav>")
    return "".join(parts)


def page(body: str, title: str, current: str, depth: int, description: str) -> str:
    up = "../" * depth
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="article">
{FONTS}
<link rel="stylesheet" href="{up}assets/style.css">
</head>
<body>
<div class="shell">
{nav_html(current, depth)}
<main>
{body}
</main>
</div>
<footer class="site">
Every command in this course was run on a real Mac on 5 September 2026, and every
screenshot is of the real thing. Prices and versions are facts about that date —
check the vendor's page before relying on them.
<br>© 2026 Albert Hui.
</footer>
</body>
</html>
"""


MD_LINK = re.compile(r'(href=")([^"]+?)\.md((?:#[^"]*)?")')


def convert(md_text: str) -> str:
    html = markdown.markdown(
        md_text,
        extensions=["extra", "sane_lists", "smarty"],
        output_format="html5",
    )
    # Every internal .md link becomes .html; the folder layout is mirrored, so
    # nothing else about the path needs to change.
    return MD_LINK.sub(r"\1\2.html\3", html)


def first_paragraph(md_text: str) -> str:
    for line in md_text.splitlines():
        line = line.strip()
        if line and not line.startswith(("#", "!", ">", "|", "-", "*", "`")):
            return re.sub(r"[*`\[\]]|\(https?://[^)]+\)", "", line)[:180]
    return SITE_BLURB


def build() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "tutorial").mkdir(parents=True)
    (OUT / "assets").mkdir(parents=True)

    (OUT / "assets" / "style.css").write_text(CSS, encoding="utf-8")

    # Screenshots, with the repo's layout preserved so relative links survive.
    src_shots = ROOT / "screenshots"
    if src_shots.exists():
        shutil.copytree(src_shots, OUT / "screenshots")

    # Home page, from the README.
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    (OUT / "index.html").write_text(
        page(convert(readme), SITE_TITLE, "", 0, SITE_BLURB), encoding="utf-8"
    )

    ordered = CHAPTERS + APPENDICES
    written = 0
    for index, (slug, title) in enumerate(ordered):
        source = ROOT / "tutorial" / f"{slug}.md"
        if not source.exists():
            raise SystemExit(f"missing chapter source: {source}")

        md_text = source.read_text(encoding="utf-8")
        body = convert(md_text)

        # Prev/next, so the sidebar is not the only way through.
        links = []
        if index > 0:
            prev_slug, prev_title = ordered[index - 1]
            links.append(f'<a href="{prev_slug}.html">← {prev_title}</a>')
        else:
            links.append("<span></span>")
        if index < len(ordered) - 1:
            next_slug, next_title = ordered[index + 1]
            links.append(f'<a href="{next_slug}.html">{next_title} →</a>')
        else:
            links.append('<a href="../index.html">Back to the start</a>')
        body += f'<div class="pager">{links[0]}{links[1]}</div>'

        (OUT / "tutorial" / f"{slug}.html").write_text(
            page(body, f"{title} · {SITE_TITLE}", slug, 1, first_paragraph(md_text)),
            encoding="utf-8",
        )
        written += 1

    # Tell GitHub Pages not to run Jekyll over the output.
    (OUT / ".nojekyll").write_text("", encoding="utf-8")

    print(f"built {written} chapter pages + index -> {OUT}")


if __name__ == "__main__":
    build()
