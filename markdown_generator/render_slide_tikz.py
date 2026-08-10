#!/usr/bin/env python3
r"""Render every \begin{tikzpicture} in a Beamer slide-deck source to a PNG.

Extracts the deck's \definecolor lines and \usetikzlibrary set from the YAML
header-includes, wraps each picture in a standalone xelatex document (with an
\alert shim and CJK support), compiles, and converts the cropped PDF to a
high-density PNG. Pictures are numbered in document order so the companion
converter can drop <img> placeholders that line up 1:1.

Usage: python3 render_slide_tikz.py <deck.md> <deck-slug> <out-dir>
Writes <out-dir>/tikz-NN.png and prints one JSON line: {"n": N, "ok": [...], "failed": [...]}.
"""
import json
import os
import re
import subprocess
import sys
import tempfile

TEMPLATE = r"""\documentclass[border=6pt]{standalone}
\usepackage{tikz}
\usetikzlibrary{%(libs)s}
\usepackage{xcolor}
%(colors)s
\usepackage{csquotes}
\usepackage{amsmath,amssymb}
\usepackage{fontawesome5}
\usepackage[hidelinks]{hyperref}
\providecommand{\faGithub}{}\providecommand{\faGlobe}{}
\usepackage{xeCJK}
\IfFontExistsTF{PingFang SC}{\setCJKmainfont{PingFang SC}}{%%
  \IfFontExistsTF{Heiti SC}{\setCJKmainfont{Heiti SC}}{\setCJKmainfont{Hiragino Sans GB}}}
\newcommand{\alert}[1]{\textcolor{accent}{#1}}
\setlength{\textwidth}{15cm}
\begin{document}
%(body)s
\end{document}
"""


def extract(src):
    colors = re.findall(r"\\definecolor\{[^}]*\}\{[^}]*\}\{[^}]*\}", src)
    m = re.search(r"usetikzlibrary\{([^}]*)\}", src)
    libs = m.group(1) if m else "arrows.meta,positioning,shapes.geometric,calc,fit,backgrounds,matrix"
    pics = re.findall(r"\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}", src, re.S)
    return "\n".join(colors), libs, pics


def render(src_path, slug, out_dir):
    src = open(src_path, encoding="utf-8").read()
    colors, libs, pics = extract(src)
    os.makedirs(out_dir, exist_ok=True)
    ok, failed = [], []
    with tempfile.TemporaryDirectory() as td:
        for i, pic in enumerate(pics, 1):
            tag = f"{i:02d}"
            tex = os.path.join(td, f"t{tag}.tex")
            with open(tex, "w", encoding="utf-8") as f:
                f.write(TEMPLATE % {"libs": libs, "colors": colors, "body": pic})
            r = subprocess.run(
                ["xelatex", "-interaction=nonstopmode", "-halt-on-error", f"t{tag}.tex"],
                cwd=td, capture_output=True, text=True,
            )
            pdf = os.path.join(td, f"t{tag}.pdf")
            if r.returncode != 0 or not os.path.exists(pdf):
                failed.append(i)
                continue
            png = os.path.join(out_dir, f"tikz-{tag}.png")
            m = subprocess.run(
                ["magick", "-density", "220", pdf, "-background", "white",
                 "-flatten", "-quality", "92", "-strip", png],
                capture_output=True, text=True,
            )
            (ok if m.returncode == 0 and os.path.exists(png) else failed).append(i)
    return {"slug": slug, "n": len(pics), "ok": ok, "failed": failed}


if __name__ == "__main__":
    src_path, slug, out_dir = sys.argv[1], sys.argv[2], sys.argv[3]
    print(json.dumps(render(src_path, slug, out_dir)))
