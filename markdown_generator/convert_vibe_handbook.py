#!/usr/bin/env python3
r"""Convert a Pandoc/LaTeX-flavored handbook .md into a Jekyll page .md.

Handles exactly the artifacts present in the vibe-researching handbooks:
  - strips the Pandoc YAML front matter (replaced with Jekyll front matter)
  - removes \newpage / \pagebreak
  - converts the two \begin{tabular} blocks to HTML tables
  - replaces the Coleman's-boat \includegraphics figure with an inline SVG
  - strips stray LaTeX wrapper lines (\begingroup, \footnotesize, ...)
  - converts inline LaTeX (\texttt, \emph, \textbf, $\times$, ...) OUTSIDE code fences
  - drops the CUHK subtitle
"""
import re
import sys

# ---------------------------------------------------------------- inline cleaners

def esc_html(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def clean_math(s: str) -> str:
    s = s.replace(r"$\leftrightarrow$", "↔").replace(r"$\rightarrow$", "→")
    s = s.replace(r"$\leftarrow$", "←").replace(r"$\times$", "×")
    s = s.replace(r"$\Rightarrow$", "⇒").replace(r"$\leq$", "≤").replace(r"$\geq$", "≥")
    s = s.replace(r"\times", "×")
    return s

def clean_cell(raw: str) -> str:
    """Clean one LaTeX table cell into inline HTML."""
    s = raw.strip()
    s = esc_html(s)                      # escape first so <project> survives inside <code>
    s = s.replace(r"\newline", "<br>")
    s = re.sub(r"\\textbf\{([^{}]*)\}", r"<strong>\1</strong>", s)
    s = re.sub(r"\\emph\{([^{}]*)\}", r"<em>\1</em>", s)
    s = re.sub(r"\\texttt\{([^{}]*)\}", r"<code>\1</code>", s)
    s = clean_math(s)
    s = s.replace(r"\textasciitilde", "~").replace(r"\_", "_").replace(r"\&", "&amp;")
    s = re.sub(r"\s*\n\s*", " ", s).strip()
    return s

def clean_inline_prose(s: str) -> str:
    """Inline LaTeX -> Markdown, for non-code segments only."""
    s = re.sub(r"\\texttt\{([^{}]*)\}", r"`\1`", s)
    s = re.sub(r"\\emph\{([^{}]*)\}", r"*\1*", s)
    s = re.sub(r"\\textit\{([^{}]*)\}", r"*\1*", s)
    s = re.sub(r"\\textbf\{([^{}]*)\}", r"**\1**", s)
    s = clean_math(s)
    s = s.replace(r"\textasciitilde", "~")
    # strip LaTeX spacing / line-break directives that leak into prose
    # (\medskip, \vfill, \allowbreak{}, \vspace{..}, ...) — they have no HTML meaning
    s = re.sub(r"\\[vh]space\*?\s*\{[^}]*\}", "", s)
    s = re.sub(
        r"\\(?:medskip|smallskip|bigskip|vfill|hfill|noindent|allowbreak"
        r"|clearpage|centering|raggedright|raggedleft)\b(?:\{\})?",
        "", s,
    )
    return s

# ---------------------------------------------------------------- tabular -> HTML

def tabular_to_html(m: re.Match) -> str:
    inner = m.group("body")
    # drop rule/spacing commands
    inner = re.sub(r"\\(toprule|midrule|bottomrule|addlinespace|hline)\b", "", inner)
    rows = [r.strip() for r in re.split(r"\\\\", inner) if r.strip()]
    html = ['<div class="hb-table-wrap">', "<table>"]
    for i, row in enumerate(rows):
        cells = re.split(r"(?<!\\)&", row)
        cells = [clean_cell(c) for c in cells]
        tag = "th" if i == 0 else "td"
        if i == 0:
            html.append("<thead><tr>")
        elif i == 1:
            html.append("</thead><tbody>")
        html.append("<tr>" if i > 0 else "")
        html.append("".join(f"<{tag}>{c}</{tag}>" for c in cells))
        html.append("</tr>")
    html.append("</tbody></table></div>")
    # collapse the little bookkeeping so we don't emit empty <tr></tr>
    out = "\n".join(x for x in html if x != "")
    out = out.replace("<thead><tr>\n<tr>", "<thead><tr>")
    return "\n\n" + out + "\n\n"

TABULAR_RE = re.compile(
    r"(?:\\begingroup\s*\n)?(?:\\footnotesize\s*\n)?"
    r"\\begin\{tabular\}\{[^\n]*\}[ \t]*\n(?P<body>.*?)\\end\{tabular\}"
    r"(?:\s*\n\\endgroup)?",
    re.DOTALL,
)

# ---------------------------------------------------------------- figure -> SVG

SVG = {}
SVG["en"] = r"""<figure class="hb-figure">
<svg viewBox="0 0 720 300" role="img" aria-label="Coleman's boat mechanism diagram for the rural-urban digital use-intensity gap" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="ah" markerWidth="9" markerHeight="9" refX="7" refY="3.2" orient="auto">
      <path d="M0,0 L7,3.2 L0,6.4 Z" fill="#c05a1e"/>
    </marker>
    <marker id="ahb" markerWidth="10" markerHeight="10" refX="8" refY="3.6" orient="auto">
      <path d="M0,0 L8,3.6 L0,7.2 Z" fill="#2f5c8f"/>
    </marker>
  </defs>
  <text x="10" y="52" font-size="11" fill="#8a8a8a" font-style="italic">MACRO</text>
  <text x="10" y="246" font-size="11" fill="#8a8a8a" font-style="italic">MICRO</text>
  <!-- macro-macro observed association -->
  <line x1="276" y1="51" x2="450" y2="51" stroke="#2f5c8f" stroke-width="3" marker-end="url(#ahb)"/>
  <text x="363" y="40" font-size="11" fill="#2f5c8f" font-style="italic" text-anchor="middle">Observed gap (descriptive)</text>
  <!-- micro legs -->
  <line x1="140" y1="82" x2="172" y2="208" stroke="#c05a1e" stroke-width="2" marker-end="url(#ah)"/>
  <text x="128" y="150" font-size="11" fill="#c05a1e" font-style="italic" text-anchor="end">(1) Situational</text>
  <line x1="292" y1="240" x2="406" y2="240" stroke="#c05a1e" stroke-width="2" marker-end="url(#ah)"/>
  <text x="349" y="264" font-size="11" fill="#c05a1e" font-style="italic" text-anchor="middle">(2) Action-formation</text>
  <line x1="528" y1="208" x2="576" y2="82" stroke="#c05a1e" stroke-width="2" marker-end="url(#ah)"/>
  <text x="590" y="150" font-size="11" fill="#c05a1e" font-style="italic" text-anchor="start">(3) Transformational</text>
  <!-- macro boxes -->
  <rect x="20" y="22" width="252" height="58" rx="5" fill="#eaf0f7" stroke="#2f5c8f" stroke-width="1.5"/>
  <text x="146" y="46" font-size="13" fill="#16324f" text-anchor="middle" font-weight="600">Hukou system</text>
  <text x="146" y="64" font-size="12" fill="#16324f" text-anchor="middle">(institutional sorting)</text>
  <rect x="450" y="22" width="252" height="58" rx="5" fill="#eaf0f7" stroke="#2f5c8f" stroke-width="1.5"/>
  <text x="576" y="46" font-size="13" fill="#16324f" text-anchor="middle" font-weight="600">Population-level</text>
  <text x="576" y="64" font-size="12" fill="#16324f" text-anchor="middle">use-intensity gap (Y2)</text>
  <!-- micro boxes -->
  <rect x="58" y="212" width="234" height="56" rx="5" fill="#ffffff" stroke="#2f5c8f" stroke-width="1.5"/>
  <text x="175" y="236" font-size="12.5" fill="#1a1a1a" text-anchor="middle">Differential digital</text>
  <text x="175" y="253" font-size="12.5" fill="#1a1a1a" text-anchor="middle">infrastructure exposure</text>
  <rect x="408" y="212" width="234" height="56" rx="5" fill="#ffffff" stroke="#2f5c8f" stroke-width="1.5"/>
  <text x="525" y="244" font-size="12.5" fill="#1a1a1a" text-anchor="middle">Differential skill conversion</text>
</svg>
<figcaption>%%CAPTION%%</figcaption>
</figure>"""

SVG["zh"] = r"""<figure class="hb-figure">
<svg viewBox="0 0 720 300" role="img" aria-label="城乡数字使用强度差距的 Coleman's boat 机制图" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="ah" markerWidth="9" markerHeight="9" refX="7" refY="3.2" orient="auto">
      <path d="M0,0 L7,3.2 L0,6.4 Z" fill="#c05a1e"/>
    </marker>
    <marker id="ahb" markerWidth="10" markerHeight="10" refX="8" refY="3.6" orient="auto">
      <path d="M0,0 L8,3.6 L0,7.2 Z" fill="#2f5c8f"/>
    </marker>
  </defs>
  <text x="8" y="52" font-size="11" fill="#8a8a8a" font-style="italic">宏观</text>
  <text x="8" y="246" font-size="11" fill="#8a8a8a" font-style="italic">微观</text>
  <line x1="276" y1="51" x2="450" y2="51" stroke="#2f5c8f" stroke-width="3" marker-end="url(#ahb)"/>
  <text x="363" y="40" font-size="11" fill="#2f5c8f" font-style="italic" text-anchor="middle">观察到的差距（描述性）</text>
  <line x1="140" y1="82" x2="172" y2="208" stroke="#c05a1e" stroke-width="2" marker-end="url(#ah)"/>
  <text x="128" y="150" font-size="11" fill="#c05a1e" font-style="italic" text-anchor="end">(1) 情境机制</text>
  <line x1="292" y1="240" x2="406" y2="240" stroke="#c05a1e" stroke-width="2" marker-end="url(#ah)"/>
  <text x="349" y="264" font-size="11" fill="#c05a1e" font-style="italic" text-anchor="middle">(2) 行动生成</text>
  <line x1="528" y1="208" x2="576" y2="82" stroke="#c05a1e" stroke-width="2" marker-end="url(#ah)"/>
  <text x="590" y="150" font-size="11" fill="#c05a1e" font-style="italic" text-anchor="start">(3) 转化机制</text>
  <rect x="20" y="22" width="252" height="58" rx="5" fill="#eaf0f7" stroke="#2f5c8f" stroke-width="1.5"/>
  <text x="146" y="46" font-size="13" fill="#16324f" text-anchor="middle" font-weight="600">户籍制度</text>
  <text x="146" y="64" font-size="12" fill="#16324f" text-anchor="middle">（制度分层）</text>
  <rect x="450" y="22" width="252" height="58" rx="5" fill="#eaf0f7" stroke="#2f5c8f" stroke-width="1.5"/>
  <text x="576" y="46" font-size="13" fill="#16324f" text-anchor="middle" font-weight="600">总体层面</text>
  <text x="576" y="64" font-size="12" fill="#16324f" text-anchor="middle">使用强度差距（Y2）</text>
  <rect x="58" y="212" width="234" height="56" rx="5" fill="#ffffff" stroke="#2f5c8f" stroke-width="1.5"/>
  <text x="175" y="244" font-size="12.5" fill="#1a1a1a" text-anchor="middle">数字基础设施暴露差异</text>
  <rect x="408" y="212" width="234" height="56" rx="5" fill="#ffffff" stroke="#2f5c8f" stroke-width="1.5"/>
  <text x="525" y="244" font-size="12.5" fill="#1a1a1a" text-anchor="middle">技能转化差异</text>
</svg>
<figcaption>%%CAPTION%%</figcaption>
</figure>"""

FIGURE_RE = re.compile(
    r"\\begin\{center\}\s*\n\\includegraphics[^\n]*\n\\end\{center\}\s*\n\s*\n?"
    r"\\begin\{center\}\s*\n\\footnotesize\\itshape\s*(?P<cap>.*?)\n\\end\{center\}",
    re.DOTALL,
)

# ---------------------------------------------------------------- front matter

FRONT = {
    "en": """---
title: "Vibe Researching with Coding Agents"
excerpt: "A hands-on participant handbook: from a blank machine to a verified, journal-ready paper built with coding agents."
permalink: /vibe-researching/en/
author_profile: false
handbook: true
lang: en
---
""",
    "zh": """---
title: "Vibe Researching with Coding Agents（中文手册）"
excerpt: "学员实操手册：从一台空白电脑，到一份用编码智能体写成、经过验证、可投稿的论文草稿。"
permalink: /vibe-researching/zh/
author_profile: false
handbook: true
lang: zh
---
""",
}

HUB_LINK = {
    "en": '<p class="hb-backlink" data-hb-lang="en"><a href="/vibe-researching/">&larr; Vibe Researching hub</a> &nbsp;·&nbsp; <a href="/vibe-researching/zh/">中文版</a></p>\n\n',
    "zh": '<p class="hb-backlink" data-hb-lang="zh"><a href="/vibe-researching/">&larr; Vibe Researching 主页</a> &nbsp;·&nbsp; <a href="/vibe-researching/en/">English version</a></p>\n\n',
}

# ---------------------------------------------------------------- main

def strip_front_matter(text: str) -> str:
    assert text.startswith("---"), "expected leading front matter"
    # find the closing '---' on its own line
    m = re.search(r"\n---\s*\n", text)
    return text[m.end():]

def protect_and_clean_inline(body: str) -> str:
    """Apply inline prose cleaning outside fenced code blocks."""
    parts = re.split(r"(```.*?\n.*?```)", body, flags=re.DOTALL)
    out = []
    for i, p in enumerate(parts):
        if p.startswith("```"):
            out.append(p)          # code fence: leave untouched
        else:
            out.append(clean_inline_prose(p))
    return "".join(out)

def convert(src_path: str, lang: str) -> str:
    with open(src_path, encoding="utf-8") as f:
        text = f.read()
    body = strip_front_matter(text)

    counts = {}

    # figure — embed the real compiled figure (same image the source references
    # in both EN and CN), with the per-language caption.
    FIG_IMG = (
        '<figure class="hb-figure">\n'
        '<img src="/images/fig-mechanism-coleman.png" loading="lazy"'
        ' alt="Coleman\'s boat mechanism: the Hukou system (macro) links to the'
        ' population-level use-intensity gap (macro) via differential digital'
        ' infrastructure exposure and differential skill conversion (micro),'
        ' with rival explanations listed as falsifiers.">\n'
        '<figcaption>%%CAPTION%%</figcaption>\n'
        '</figure>'
    )
    def fig_repl(m):
        cap = clean_math(m.group("cap")).replace("--", "–").strip()
        counts["figure"] = counts.get("figure", 0) + 1
        return "\n\n" + FIG_IMG.replace("%%CAPTION%%", cap) + "\n\n"
    body = FIGURE_RE.sub(fig_repl, body)

    # tabulars
    def tab_repl(m):
        counts["tabular"] = counts.get("tabular", 0) + 1
        return tabular_to_html(m)
    body = TABULAR_RE.sub(tab_repl, body)

    # remove page breaks
    n = len(re.findall(r"^\\(?:newpage|pagebreak|clearpage)\s*$", body, flags=re.MULTILINE))
    counts["newpage"] = n
    body = re.sub(r"^\\(?:newpage|pagebreak|clearpage)\s*$\n?", "", body, flags=re.MULTILINE)

    # remove stray latex wrapper lines
    body = re.sub(
        r"^\\(?:begingroup|endgroup|footnotesize|small|normalsize|itshape|bfseries|centering|begin\{center\}|end\{center\})\s*$\n?",
        "", body, flags=re.MULTILINE,
    )

    # inline prose LaTeX (outside code fences)
    body = protect_and_clean_inline(body)

    # collapse 3+ blank lines
    body = re.sub(r"\n{3,}", "\n\n", body).strip("\n")

    sys.stderr.write(f"[{lang}] {src_path}\n  replacements: {counts}\n")

    # residual raw-LaTeX sanity check (outside code fences)
    residual = []
    for seg in re.split(r"(```.*?\n.*?```)", body, flags=re.DOTALL):
        if seg.startswith("```"):
            continue
        for mm in re.finditer(r"\\(newpage|begin\{|end\{|includegraphics|texttt|textbf|emph|footnotesize|itshape|tabular)", seg):
            residual.append(mm.group(0))
    if residual:
        sys.stderr.write(f"  WARNING residual LaTeX outside code: {sorted(set(residual))}\n")

    # Guard against Jekyll/Liquid interpreting {{ }} or {% %} inside the handbook
    # body (e.g. GitHub Actions "${{ secrets.* }}" samples). The include stays
    # outside the raw block so it still runs.
    assert "{% endraw %}" not in body and "{% raw %}" not in body, "body contains raw tags"
    out = (FRONT[lang]
           + "\n{% include handbook-assets.html %}\n\n"
           + HUB_LINK[lang]
           + "{% raw %}\n" + body + "\n{% endraw %}\n")
    return out


if __name__ == "__main__":
    src, lang, dst = sys.argv[1], sys.argv[2], sys.argv[3]
    result = convert(src, lang)
    with open(dst, "w", encoding="utf-8") as f:
        f.write(result)
    sys.stderr.write(f"  wrote {dst} ({len(result)} bytes)\n")
