#!/usr/bin/env python3
r"""Convert a Beamer/metropolis slide-deck (.md, pandoc-flavoured) into a
handbook-style Jekyll book page.

Structure:  '#' section dividers -> H1 (sidebar part groups)
            '##' slides          -> H2 (walkable sections)
Beamer environments become HTML/markdown:
   columns/column        -> <div class="s-cols"><div class="s-col" markdown="1">
   block/alertblock/..    -> callout <div class="s-box ...">
   itemize/enumerate      -> markdown lists
   tabular                -> <table> (hb-table-wrap)
   tikzpicture            -> <img> (rendered separately by render_slide_tikz.py)
Inline LaTeX (\textbf,\emph,\texttt,\alert,\enquote,\href,math,...) is converted.
CUHK branding is stripped.

Usage: python3 convert_slides_book.py <deck.md> <slug> <dest.md> [failed_idx_csv]
"""
import re
import sys

# ---------------------------------------------------------------- front matter
FRONT = """---
title: {title}
excerpt: {excerpt}
permalink: /course/{prefix}{slug}/
author_profile: false
handbook: true
course: true
lang: {lang}
---
"""

# Per-language: slug -> (short heading, next slug, next label).
# A slug missing here falls back to the deck's own title, which is what day5
# has always done in English; do not "fix" that without rebuilding EN.
NAV = {
    "en": {
        "day1": ("The Model", "day2", "Day 2 · Agents"),
        "day2": ("Agents", "day3", "Day 3 · Claude Code"),
        "day3": ("Claude Code", "day4", "Day 4 · The Pipeline"),
        "day4": ("The Pipeline", None, None),
    },
    "zh": {
        "day1": ("模型", "day2", "第 2 天 · 智能体"),
        "day2": ("智能体", "day3", "第 3 天 · Claude Code"),
        "day3": ("Claude Code", "day4", "第 4 天 · 流水线"),
        "day4": ("流水线", None, None),
        "day5": ("汉语项目", None, None),
    },
}

# Everything that differs between the English and Chinese page chrome.
# `prefix` lands in the permalink: EN stays at /course/dayN/ so no existing
# URL moves; ZH gets /course/zh/dayN/ -> /vibe-researching-lecture/zh/dayN/.
LANG = {
    "en": {
        "prefix": "",
        "home": "&larr; Course home",
        "other_href": "/course/zh/{slug}/",
        "other_label": "中文版",
        "excerpt": '"Agentic AI for Social Science Research — {short}."',
    },
    "zh": {
        "prefix": "zh/",
        "home": "&larr; 课程主页",
        "other_href": "/course/{slug}/",
        "other_label": "English version",
        "excerpt": '"面向社会科学研究的智能体 AI —— {short}。"',
    },
}

# ---------------------------------------------------------------- helpers

def strip_front_matter(text):
    assert text.startswith("---")
    m = re.search(r"\n---[ \t]*\n", text)
    fm = text[:m.start()]
    body = text[m.end():]
    def field(name):
        mm = re.search(r'^' + name + r':\s*"?(.*?)"?\s*$', fm, re.M)
        return mm.group(1).strip() if mm else ""
    return body, field("title"), field("subtitle")


MATH = [
    (r"\\leftrightarrow", "↔"), (r"\\rightarrow", "→"), (r"\\Rightarrow", "⇒"),
    (r"\\leftarrow", "←"), (r"\\to\b", "→"), (r"\\times", "×"), (r"\\cdot", "·"),
    (r"\\leq", "≤"), (r"\\geq", "≥"), (r"\\le\b", "≤"), (r"\\ge\b", "≥"),
    (r"\\approx", "≈"), (r"\\sim\b", "~"), (r"\\neq", "≠"), (r"\\pm", "±"),
    (r"\\ldots", "…"), (r"\\dots", "…"), (r"\\cdots", "⋯"),
    (r"\\kappa", "κ"), (r"\\alpha", "α"), (r"\\beta", "β"), (r"\\delta", "δ"),
    (r"\\Delta", "Δ"), (r"\\mu\b", "μ"), (r"\\sigma", "σ"), (r"\\lambda", "λ"),
    (r"\\eta\b", "η"), (r"\\rho\b", "ρ"), (r"\\tau\b", "τ"), (r"\\phi\b", "φ"),
    (r"\\epsilon", "ε"), (r"\\gamma", "γ"), (r"\\omega", "ω"), (r"\\Sigma", "Σ"),
    (r"\\theta", "θ"), (r"\\pi\b", "π"), (r"\\infty", "∞"), (r"\\subset", "⊂"),
    (r"\\in\b", "∈"), (r"\\forall", "∀"), (r"\\exists", "∃"), (r"\\sum\b", "∑"),
    (r"\\gg\b", "≫"), (r"\\ll\b", "≪"), (r"\\uparrow", "↑"), (r"\\downarrow", "↓"),
    (r"\\neg\b", "¬"), (r"\\land\b", "∧"), (r"\\lor\b", "∨"), (r"\\Pr\b", "Pr"),
    (r"\\mid\b", "|"), (r"\\perp", "⊥"), (r"\\cup\b", "∪"), (r"\\cap\b", "∩"),
    (r"\\\|", "‖"), (r"\\textdollar(?:\{\})?", "$"),
    (r"\\max\b", "max"), (r"\\min\b", "min"), (r"\\log\b", "log"),
    (r"\\exp\b", "exp"), (r"\\arg\b", "arg"),
]

# LaTeX accents ( \`a -> à, \'e -> é, \"o -> ö, \^e -> ê, \~n -> ñ )
ACCENTS = {
    "`": dict(a="à", e="è", i="ì", o="ò", u="ù", A="À", E="È", O="Ò"),
    "'": dict(a="á", e="é", i="í", o="ó", u="ú", c="ć", n="ń", s="ś", A="Á", E="É"),
    '"': dict(a="ä", e="ë", i="ï", o="ö", u="ü", A="Ä", O="Ö", U="Ü"),
    "^": dict(a="â", e="ê", i="î", o="ô", u="û"),
    "~": dict(a="ã", n="ñ", o="õ"),
}


def apply_accents(s):
    def rep(m):
        return ACCENTS.get(m.group(1), {}).get(m.group(2), m.group(2))
    return re.sub(r"\\([`'\"^~])\{?([a-zA-Z])\}?", rep, s)


def clean_math_syms(s):
    for pat, rep in MATH:
        s = re.sub(pat, rep, s)
    return s


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


COLORMAP = {}


def build_colormap(src):
    r"""Populate COLORMAP from the deck's \definecolor lines (HTML/RGB/rgb/gray)."""
    COLORMAP.clear()
    for m in re.finditer(r"\\definecolor\{([^}]+)\}\{(HTML|RGB|rgb|gray)\}\{([^}]+)\}", src):
        name, mode, val = m.group(1), m.group(2), m.group(3).strip()
        try:
            if mode == "HTML":
                COLORMAP[name] = "#" + val
            elif mode == "RGB":
                r, g, b = [int(x) for x in val.split(",")]
                COLORMAP[name] = "#%02x%02x%02x" % (r, g, b)
            elif mode == "rgb":
                r, g, b = [float(x) for x in val.split(",")]
                COLORMAP[name] = "#%02x%02x%02x" % (int(r * 255), int(g * 255), int(b * 255))
            elif mode == "gray":
                v = int(float(val) * 255)
                COLORMAP[name] = "#%02x%02x%02x" % (v, v, v)
        except Exception:
            pass


def color_hex(name):
    return COLORMAP.get((name or "").strip().split("!")[0])


def _textcolor(c, x):
    hx = color_hex(c)
    return ('<span style="color:%s">%s</span>' % (hx, x)) if hx else ("<strong>%s</strong>" % x)


def _match(s, brace):
    """Index of the '}' matching the '{' at `brace`, ignoring escaped \\{ \\}."""
    depth, i, n = 0, brace, len(s)
    while i < n:
        c = s[i]
        if c == "\\":
            i += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return i
        i += 1
    return -1


def bcmd(s, name, fmt):
    r"""Replace every balanced \name{...} with fmt(inner). Handles nested braces."""
    pat = "\\" + name + "{"
    out, i = [], 0
    while True:
        j = s.find(pat, i)
        if j < 0:
            out.append(s[i:])
            return "".join(out)
        out.append(s[i:j])
        brace = j + len(pat) - 1
        k = _match(s, brace)
        if k < 0:
            out.append(s[j:j + len(pat)])
            i = j + len(pat)
            continue
        out.append(fmt(s[brace + 1:k]))
        i = k + 1


def bcmd2(s, name, fmt):
    r"""Replace balanced two-arg \name{a}{b} with fmt(a, b) (e.g. \href)."""
    pat = "\\" + name + "{"
    out, i = [], 0
    while True:
        j = s.find(pat, i)
        if j < 0:
            out.append(s[i:])
            return "".join(out)
        b1 = j + len(pat) - 1
        k1 = _match(s, b1)
        if k1 < 0 or k1 + 1 >= len(s) or s[k1 + 1] != "{":
            out.append(s[i:j + len(pat)])
            i = j + len(pat)
            continue
        k2 = _match(s, k1 + 1)
        if k2 < 0:
            out.append(s[i:j + len(pat)])
            i = j + len(pat)
            continue
        out.append(s[i:j])
        out.append(fmt(s[b1 + 1:k1], s[k1 + 2:k2]))
        i = k2 + 1


def drop_cmd(s, name):
    r"""Remove \name{...} keeping the inner text (balanced)."""
    return bcmd(s, name, lambda x: x)


# font/size/style switches that appear as {\switch ...} groups
SWITCH = {
    "tiny": "", "scriptsize": "", "footnotesize": "", "small": "", "normalsize": "",
    "large": "", "Large": "", "LARGE": "", "huge": "", "Huge": "",
    "bfseries": "b", "bf": "b", "itshape": "i", "it": "i", "em": "i", "slshape": "i",
    "sffamily": "", "ttfamily": "", "rmfamily": "", "upshape": "", "normalfont": "",
    "centering": "", "raggedright": "", "raggedleft": "", "color": "c",
}


def conv_switch_groups(s):
    r"""Turn {\scriptsize text} / {\bfseries text} / {\color{c} text} groups into
    plain text (bold/italic where the switch implies it). Handles nesting."""
    out, i, n = [], 0, len(s)
    while i < n:
        if s[i] == "{":
            k = _match(s, i)
            if k > 0:
                inner = s[i + 1:k]
                m = re.match(r"\s*\\([a-zA-Z]+)\b(\{[^}]*\})?[ \t]*", inner)
                if m and m.group(1) in SWITCH:
                    kind = SWITCH[m.group(1)]
                    body = conv_switch_groups(inner[m.end():]).strip()
                    if kind == "b" and body:
                        body = f"**{body}**"
                    elif kind == "i" and body:
                        body = f"*{body}*"
                    out.append(body)
                    i = k + 1
                    continue
        out.append(s[i])
        i += 1
    return "".join(out)


def math_subsup(x):
    r"""Inside math: convert ^{..}/_{..}/^x/_x to <sup>/<sub>, then drop $."""
    x = re.sub(r"\^\{([^{}]*)\}", r"<sup>\1</sup>", x)
    x = re.sub(r"\^([A-Za-z0-9])", r"<sup>\1</sup>", x)
    x = re.sub(r"_\{([^{}]*)\}", r"<sub>\1</sub>", x)
    x = re.sub(r"_([A-Za-z0-9])", r"<sub>\1</sub>", x)
    return x


# ---------------------------------------------------------------- tabular -> HTML

def tabular_to_html(m):
    inner = m.group("body")
    inner = re.sub(r"\\(?:toprule|midrule|bottomrule|hline)\b", "", inner)
    inner = re.sub(r"\\addlinespace(?:\[[^\]]*\])?", "", inner)   # optional [dim]; no trailing \b (fails after ']')
    inner = re.sub(r"\\rowcolor\{[^}]*\}", "", inner)
    # \multicolumn{n}{spec}{content} -> content (balanced)
    while "\\multicolumn{" in inner:
        j = inner.find("\\multicolumn{")
        b1 = j + len("\\multicolumn")
        k1 = _match(inner, b1)
        k2 = _match(inner, k1 + 1) if k1 > 0 and inner[k1 + 1:k1 + 2] == "{" else -1
        k3 = _match(inner, k2 + 1) if k2 > 0 and inner[k2 + 1:k2 + 2] == "{" else -1
        if k3 < 0:
            break
        inner = inner[:j] + inner[k2 + 2:k3] + inner[k3 + 1:]
    rows = [r.strip() for r in re.split(r"\\\\(?:\[[^\]]*\])?", inner) if r.strip()]
    out = ['<div class="hb-table-wrap" markdown="0">', "<table>"]
    for i, row in enumerate(rows):
        cells = [clean_cell(c) for c in re.split(r"(?<!\\)&", row)]
        if i == 0:
            out.append("<thead><tr>" + "".join(f"<th>{c}</th>" for c in cells) + "</tr></thead><tbody>")
        else:
            out.append("<tr>" + "".join(f"<td>{c}</td>" for c in cells) + "</tr>")
    out.append("</tbody></table></div>")
    return "\n\n" + "\n".join(out) + "\n\n"


# $...$ inside a code span, but never shell: $( , ${ , $VAR and $1 are excluded
# by the lookahead, and a body with ASCII letters is left alone.
CODE_MATH_RE = re.compile(r"\$(?![({]|[A-Za-z0-9_])([^$\n(){}]{1,30})\$")


def _code_math(m):
    inner = m.group(1)
    return m.group(0) if re.search(r"[A-Za-z]", inner) else math_subsup(inner)


def _unesc_code(x):
    r"""Normalise the literal contents of a code span/line: drop styling and
    size switches (\textbf/\scriptsize/\ttfamily used only for looks), resolve
    tilde/backslash/enquote macros, convert stray math symbols, unescape."""
    for name in ("textbf", "emph", "textit", "alert", "textsc", "underline", "mathbf", "mathrm", "texttt"):
        x = drop_cmd(x, name)
    x = bcmd2(x, "textcolor", lambda c, t: t)
    x = bcmd(x, "enquote", lambda t: f"“{t}”")
    x = x.replace("{,}", ",").replace("{.}", ".")
    x = re.sub(r"\\(tiny|scriptsize|footnotesize|small|normalsize|large|Large|LARGE|huge|"
               r"ttfamily|sffamily|rmfamily|bfseries|itshape|slshape|scshape|upshape|mdseries|normalfont)\b", "", x)
    x = x.replace(r"\textasciitilde{}", "~").replace(r"\textasciitilde", "~")
    x = x.replace(r"\textbackslash{}", "\\").replace(r"\textbackslash", "\\")
    x = x.replace(r"\ldots", "…").replace(r"\dots", "…")
    x = apply_accents(x)
    x = clean_math_syms(x)
    x = CODE_MATH_RE.sub(_code_math, x)                # $\times$ -> ×, but keep $(( ))
    x = re.sub(r"\\(quad|qquad|,|;|:|!)", " ", x)
    x = re.sub(r"\\ ", " ", x)
    x = re.sub(r"\\([_%&#${}~^])", r"\1", x)
    return x


def clean_cell(raw):
    s = raw.strip()
    s = strip_parbox(s)
    s = re.sub(r"\\texttt\{\\href\{([^}]*)\}\{([^}]*)\}\}", r'<a href="\1"><code>\2</code></a>', s)
    s = bcmd2(s, "colorbox", lambda c, x: f'<mark class="s-hl">{x}</mark>')
    s = bcmd2(s, "href", lambda a, b: f'<a href="{a}">{b}</a>')
    code = []
    s = bcmd(s, "texttt", lambda x: (code.append(_unesc_code(x)), f"\x01C{len(code)-1}\x01")[1])
    for _ in range(4):
        s = bcmd(s, "textbf", lambda x: f"<strong>{x}</strong>")
        s = bcmd(s, "alert", lambda x: f'<span class="s-al">{x}</span>')
        s = bcmd(s, "emph", lambda x: f"<em>{x}</em>")
        s = bcmd(s, "textit", lambda x: f"<em>{x}</em>")
        s = bcmd2(s, "textcolor", _textcolor)
        s = bcmd(s, "enquote", lambda x: f"“{x}”")
    s = conv_switch_groups(s)
    s = strip_inline(s)
    s = re.sub(r"\s*\\\\(\[[^\]]*\])?\s*", "<br>", s)
    s = s.replace("---", "—").replace("--", "–")   # smart dashes (raw <td>, no kramdown)
    s = re.sub(r"\s+", " ", s).strip()
    s = re.sub(r"\x01C(\d+)\x01", lambda m: f"<code>{esc(code[int(m.group(1))])}</code>", s)
    return s


TABULAR_RE = re.compile(
    r"\\begin\{tabular\}\{[^\n]*\}[ \t]*\n?(?P<body>.*?)\\end\{tabular\}", re.DOTALL)


# ---------------------------------------------------------------- inline cleanup

def strip_inline(s):
    """Remove formatting-only LaTeX and convert math symbols. Idempotent-ish."""
    # math wrappers -> keep inner (balanced)
    for name in ("mathbf", "mathrm", "mathit", "mathsf", "text", "bm", "boldsymbol", "phantom", "mbox", "textnormal"):
        s = drop_cmd(s, name)
    # fractions
    s = bcmd2(s, "dfrac", lambda a, b: f"{a}/{b}")
    s = bcmd2(s, "frac", lambda a, b: f"{a}/{b}")
    s = bcmd2(s, "sfrac", lambda a, b: f"{a}/{b}")
    # size / spacing / layout directives -> drop
    s = re.sub(r"\\(tiny|scriptsize|footnotesize|small|normalsize|large|Large|LARGE|huge|Huge)\b", "", s)
    s = re.sub(r"\\(vspace|hspace)\*?\s*\{[^}]*\}", "", s)
    s = re.sub(r"\\(vfill|hfill|smallskip|medskip|bigskip|enspace|thinspace|noindent|centering|raggedright|raggedleft|par|itshape|bfseries|upshape|normalfont|columnbreak|leavevmode|ttfamily|sffamily|rmfamily|slshape|scshape|mdseries|em)\b", "", s)
    s = re.sub(r"\\(quad|qquad)\b", " ", s)
    s = re.sub(r"\\newline\b", "  \n", s)
    s = re.sub(r"\\(Big|big|Bigg|bigg|bigl|bigr|Bigl|Bigr|left|right)\b", "", s)
    s = re.sub(r"\\cellcolor\{[^}]*\}", "", s)
    s = re.sub(r"\\setlength\s*\{[^}]*\}\s*\{[^}]*\}", "", s)
    s = re.sub(r"\\setlength\\\w+\{[^}]*\}", "", s)
    s = re.sub(r"\\renewcommand\s*\{[^}]*\}\s*\{[^}]*\}", "", s)
    s = re.sub(r"\\(arraybackslash|arraystretch)\b", "", s)
    s = re.sub(r"\\(faArrowRight|faCheck|faTimes|faLightbulb|faEye|faDumbbell|faGlobe|checkmark|blacksquare)\b",
               lambda m: {"\\checkmark": "✓", "\\blacksquare": "■"}.get(m.group(0), ""), s)
    s = re.sub(r"\\fa[A-Za-z]+\b", "", s)           # any other FontAwesome icon -> drop
    s = re.sub(r"\\vdots\b", "⋮", s)
    s = drop_cmd(s, "sqrt")
    for pat, rep in ((r"\\top\b", "⊤"), (r"\\div\b", "÷"), (r"\\S\b", "§"),
                     (r"\\P\b", "¶"), (r"\\dagger\b", "†"), (r"\\star\b", "★"),
                     (r"\\bullet\b", "•"), (r"\\circ\b", "∘"), (r"\\mapsto\b", "↦"),
                     (r"\\emptyset\b", "∅"), (r"\\equiv\b", "≡"), (r"\\propto\b", "∝")):
        s = re.sub(pat, rep, s)
    # escaped chars. \# becomes the entity, not a bare "#": the decks quote sample
    # markdown inside \ttfamily blocks (day4's my-four-layer-blueprint.md), and a
    # line reading "## ..." after unescaping is a heading to kramdown — four lines
    # of sample text became four walkable sections in day4's sidebar. &#35; renders
    # identically and cannot open an ATX heading. Code spans and fences never reach
    # this function; they are stashed before inline conversion runs.
    s = s.replace(r"\%", "%").replace(r"\&", "&amp;").replace(r"\#", "&#35;")
    s = s.replace(r"\_", "_").replace(r"\$", "$").replace(r"\{", "{").replace(r"\}", "}")
    s = s.replace(r"\textasciitilde", "~").replace("~", " ")
    s = s.replace("{,}", ",").replace("{.}", ".")   # math digit separators
    s = re.sub(r"\\S(?![a-zA-Z])", "§", s)
    s = re.sub(r"\\P(?![a-zA-Z])", "¶", s)
    s = re.sub(r"\\ph\{([^}]*)\}", r"[\1]", s)      # \ph{...} placeholder macro -> [ ... ]
    s = apply_accents(s)
    s = re.sub(r"\\color\{[^}]*\}", "", s)          # bare \color switch -> drop
    s = re.sub(r"\\[,;:!> ]", " ", s)   # thin spaces / \  / \>
    s = clean_math_syms(s)
    # math: sub/sup, drop $. Never span a line: a lone $ (a shell prompt, cfps$var)
    # would otherwise pair with a $ further down and shift every pair after it.
    s = re.sub(r"\$([^$\n]*)\$", lambda m: math_subsup(m.group(1)), s)
    s = re.sub(r"\{\s*\}", "", s)                    # empty braces
    s = re.sub(r"\{([+\-=*/×·→⇒≤≥])\}", r"\1", s)   # braced single operators
    return s


def strip_parbox(s):
    r"""\parbox[pos]{width}{content} -> content (balanced)."""
    while True:
        m = re.search(r"\\parbox(\[[^\]]*\])?\{", s)
        if not m:
            return s
        wb = m.end() - 1
        wk = _match(s, wb)
        if wk < 0 or s[wk + 1:wk + 2] != "{":
            s = s[:m.start()] + s[(wk + 1 if wk > 0 else m.end()):]
            continue
        ck = _match(s, wk + 1)
        if ck < 0:
            return s
        s = s[:m.start()] + s[wk + 2:ck] + s[ck + 1:]


def strip_resizebox(s):
    r"""\resizebox{w}{h}{body} -> body (balanced)."""
    while True:
        m = re.search(r"\\resizebox\*?\{", s)
        if not m:
            return s
        b1 = m.end() - 1
        k1 = _match(s, b1)
        if k1 < 0 or s[k1 + 1:k1 + 2] != "{":
            return s
        k2 = _match(s, k1 + 1)
        if k2 < 0 or s[k2 + 1:k2 + 2] != "{":
            return s
        k3 = _match(s, k2 + 1)
        if k3 < 0:
            return s
        s = s[:m.start()] + s[k2 + 2:k3] + s[k3 + 1:]


def convert_inline(s):
    """Full inline conversion for prose segments (outside code fences).

    Emphasis is emitted as HTML (<strong>/<em>/<code>) so nested LaTeX emphasis
    can't break markdown's * / ** nesting; inline code is stashed literally so
    later cleanup never mangles its contents (e.g. ~ or $ inside code)."""
    s = strip_parbox(s)
    s = re.sub(r"\\texttt\{\\href\{([^}]*)\}\{([^}]*)\}\}", r'<a href="\1"><code>\2</code></a>', s)
    s = bcmd2(s, "colorbox", lambda c, x: f'<mark class="s-hl">{x}</mark>')
    s = bcmd2(s, "href", lambda a, b: f"[{b}]({a})")
    s = bcmd(s, "url", lambda a: f"<{a}>")
    code = []
    s = bcmd(s, "texttt", lambda x: (code.append(_unesc_code(x)), f"\x01C{len(code)-1}\x01")[1])
    for _ in range(4):
        s = bcmd(s, "alert", lambda x: f'<span class="s-al">{x}</span>')
        s = bcmd(s, "textbf", lambda x: f"<strong>{x}</strong>")
        s = bcmd(s, "emph", lambda x: f"<em>{x}</em>")
        s = bcmd(s, "textit", lambda x: f"<em>{x}</em>")
        s = bcmd(s, "textsc", lambda x: x)
        s = bcmd2(s, "textcolor", _textcolor)
        s = bcmd(s, "enquote", lambda x: f"“{x}”")
    s = conv_switch_groups(s)
    s = strip_inline(s)
    s = re.sub(r"\s*\\\\(\[[^\]]*\])?\s*", "  \n", s)   # \\ or \\[dim] -> hard break

    def restore(m):
        c = code[int(m.group(1))]
        # a lone backtick fence breaks on a trailing "\" (kramdown reads \` as an
        # escaped backtick, so the span never closes and the leak cascades)
        n = max((len(r) for r in re.findall(r"`+", c)), default=0) + 1
        if c.endswith("\\") or "`" in c or c.startswith(" ") or c.endswith(" "):
            f = "`" * max(n, 2)
            return f"{f} {c} {f}"        # kramdown strips one pad space per side
        return f"{'`' * n}{c}{'`' * n}"
    s = re.sub(r"\x01C(\d+)\x01", restore, s)
    return s


# ---------------------------------------------------------------- environments

def conv_list(m):
    kind = m.group(1)
    body = m.group(2)
    body = re.sub(r"\\setlength\\?\w*\{[^}]*\}(\{[^}]*\})?", "", body)
    items = re.split(r"\\item(?:\[[^\]]*\])?", body)
    marker_for = "1." if kind == "enumerate" else "-"
    out = []
    for it in items[1:]:
        txt = it.strip()
        if not txt:
            continue
        txt = re.sub(r"\s+", " ", txt).strip()
        out.append(f"{marker_for} {txt}")
    return "\n\n" + "\n".join(out) + "\n\n"


LIST_RE = re.compile(r"\\begin\{(itemize|enumerate)\}(.*?)\\end\{(?:itemize|enumerate)\}", re.DOTALL)

BOX_TYPES = {"block": "note", "alertblock": "alert", "exampleblock": "tip"}


def conv_box(m):
    env = m.group(1)
    title = m.group(2).strip()
    body = m.group(3).strip()
    cls = BOX_TYPES.get(env, "note")
    t = f'<div class="s-box-t" markdown="1">\n{title}\n</div>\n\n' if title else ""
    return ('\n\n<div class="s-box s-' + cls + '" markdown="1">\n\n' + t + body + "\n\n</div>\n\n")


BOX_RE = re.compile(
    r"\\begin\{(block|alertblock|exampleblock)\}"
    r"\{((?:[^{}]|\{[^{}]*\})*)\}"          # title (allows one level of nested braces)
    r"(.*?)\\end\{(?:block|alertblock|exampleblock)\}", re.DOTALL)


def conv_column(m):
    body = m.group(2).strip()
    return '\n\n<div class="s-col" markdown="1">\n\n' + body + "\n\n</div>\n\n"


COLUMN_RE = re.compile(r"\\begin\{column\}\{([^}]*)\}(.*?)\\end\{column\}", re.DOTALL)


def conv_columns(m):
    body = m.group(1)
    return '\n\n<div class="s-cols" markdown="1">\n' + body + "\n</div>\n\n"


COLUMNS_RE = re.compile(r"\\begin\{columns\}(?:\[[^\]]*\])?(.*?)\\end\{columns\}", re.DOTALL)

QUOTE_RE = re.compile(r"\\begin\{quote\}(.*?)\\end\{quote\}", re.DOTALL)


def conv_quote(m):
    lines = [l.strip() for l in m.group(1).strip().split("\n")]
    return "\n\n" + "\n".join("> " + l for l in lines if l) + "\n\n"


# ------------------------------------------------ multi-line \texttt code blocks

def _code_line(x):
    r"""Literal text of one \texttt{...} config line."""
    return _unesc_code(x)


def _texttt_only(ln):
    r"""If `ln` is exactly one \texttt{...} (optionally + \\), return its inner
    content; else None. Uses balanced matching so table rows (\texttt{x} & y)
    and other lines with trailing content are rejected."""
    s = re.sub(r"\\\\[ \t]*$", "", ln.rstrip()).rstrip()
    m = re.match(r"^[ \t]*\\texttt\{", s)
    if not m:
        return None
    brace = m.end() - 1
    k = _match(s, brace)
    if k != len(s) - 1:
        return None
    return s[brace + 1:k]


def texttt_line_blocks(body):
    r"""Turn a run of 2+ consecutive pure \texttt{...}\\ lines (config listings)
    into a fenced code block."""
    lines = body.split("\n")
    out, i, n = [], 0, len(lines)
    while i < n:
        c = _texttt_only(lines[i])
        if c is not None:
            block, j = [c], i + 1
            while j < n:
                cj = _texttt_only(lines[j])
                if cj is None:
                    break
                block.append(cj)
                j += 1
            if len(block) >= 2:
                out.append("\n```text\n" + "\n".join(_code_line(x) for x in block) + "\n```\n")
                i = j
                continue
        out.append(lines[i])
        i += 1
    return "\n".join(out)


FLUSHLEFT_TT_RE = re.compile(
    r"\\begin\{flushleft\}(?=[^\n]*\\ttfamily)[^\n]*\n(?P<inner>.*?)\\end\{flushleft\}",
    re.DOTALL)


def flushleft_ttfamily_blocks(body):
    r"""Turn \begin{flushleft}\ttfamily ... \end{flushleft} monospace listings
    (CLI/code/config, \\-separated lines, sometimes with a leading size switch)
    into fenced code blocks. Otherwise the wrapper is stripped later and the
    lines leak as raw markdown (a leading `# comment` becomes an <h1>)."""
    def repl(m):
        inner = m.group("inner").replace("\r", "")
        lines = []
        for ln in inner.split("\n"):                       # one code line per row
            ln = re.sub(r"\\\\(?:\[[^\]]*\])?[ \t]*$", "", ln)   # drop trailing \\
            out = _unesc_code(ln).rstrip()
            if not out.strip() and lines and not lines[-1].strip():
                continue                                    # collapse blank runs
            lines.append(out)
        while lines and not lines[0].strip():
            lines.pop(0)
        while lines and not lines[-1].strip():
            lines.pop()
        if not lines:
            return ""
        return "\n\n```text\n" + "\n".join(lines) + "\n```\n\n"
    return FLUSHLEFT_TT_RE.sub(repl, body)


# ---------------------------------------------------------------- main

def convert(src_path, slug, failed, lang="en"):
    text = open(src_path, encoding="utf-8").read()
    build_colormap(text)
    body, title, subtitle = strip_front_matter(text)

    # Diagrams are per-language: 84 of the 97 tikz pictures carry translated
    # labels, so ZH renders its own set under images/course/zh/<slug>/.
    img_dir = LANG[lang]["prefix"] + slug

    # strip build/tag comments and section-divider decoration
    body = re.sub(r"<!--.*?-->", "", body, flags=re.DOTALL)

    # strip LaTeX line comments (unescaped % to end of line) — e.g. the trailing
    # `%` in \resizebox{..}{..}{%. A literal percent in the deck is \% (kept).
    body = re.sub(r"(?<!\\)%[^\n]*", "", body)

    # \begin{flushleft}\ttfamily ... \end{flushleft} listings -> fenced code
    body = flushleft_ttfamily_blocks(body)

    # runs of \texttt{...}\\ config lines -> fenced code blocks
    body = texttt_line_blocks(body)

    # protect fenced code blocks
    fences = []
    def stash(m):
        fences.append(m.group(0))
        return f"\x00FENCE{len(fences)-1}\x00"
    body = re.sub(r"```.*?\n.*?```", stash, body, flags=re.DOTALL)

    # tikzpicture -> img (document order)
    counter = {"i": 0}
    def tikz_img(m):
        counter["i"] += 1
        n = counter["i"]
        if n in failed:
            return ""
        cap = ""
        urls = []
        for u in re.findall(r"\\href\{([^}]*)\}", m.group(0)):
            if u not in urls:
                urls.append(u)
        if urls:
            parts = ['<a href="%s">%s</a>' % (u, esc(re.sub(r"^https?://", "", u).rstrip("/"))) for u in urls]
            cap = '<figcaption class="s-fig-links">&#8599; ' + " &middot; ".join(parts) + "</figcaption>"
        return (f'\n\n<figure class="s-fig" markdown="0"><img loading="lazy" '
                f'src="/images/course/{img_dir}/tikz-{n:02d}.png" alt="Diagram {n}">{cap}</figure>\n\n')
    body = re.sub(r"\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}", tikz_img, body, flags=re.DOTALL)

    # \includegraphics{...figures/foo.png} -> embedded raster figure
    def img_repl(m):
        base = re.split(r"[\\/]", m.group("p").strip())[-1]
        return (f'\n\n<figure class="s-fig" markdown="0"><img loading="lazy" '
                f'src="/images/course/figures/{base}" alt="Figure"></figure>\n\n')
    body = re.sub(r"\\includegraphics(\[[^\]]*\])?\{(?P<p>[^}]*)\}", img_repl, body)

    # unwrap \resizebox{..}{..}{body} and drop \begingroup/\endgroup
    body = strip_resizebox(body)
    body = re.sub(r"\\(begingroup|endgroup)\b", "", body)

    # drop standalone latex layout lines
    body = re.sub(r"^[ \t]*\\(vspace|hspace)\*?\{[^}]*\}[ \t]*$", "", body, flags=re.M)
    body = re.sub(r"^[ \t]*\\(centering|vfill|hfill|smallskip|medskip|bigskip|noindent|par|columnbreak|bigskip)[ \t]*$", "", body, flags=re.M)
    body = re.sub(r"^[ \t]*\\(tiny|scriptsize|footnotesize|small|normalsize|large|Large|LARGE)[ \t]*$", "", body, flags=re.M)

    # tables first (innermost structural)
    body = TABULAR_RE.sub(tabular_to_html, body)
    # lists (repeat for nesting)
    for _ in range(3):
        body, n = LIST_RE.subn(conv_list, body)
        if not n:
            break
    # boxes, then columns
    body = BOX_RE.sub(conv_box, body)
    body = COLUMN_RE.sub(conv_column, body)
    body = COLUMNS_RE.sub(conv_columns, body)
    body = QUOTE_RE.sub(conv_quote, body)

    # drop remaining structural wrappers
    body = re.sub(r"\\(begin|end)\{(center|flushleft|flushright|minipage|scope)\}(\{[^}]*\})?(\[[^\]]*\])?", "", body)

    # inline conversion outside fences
    body = convert_inline(body)

    # de-brand CUHK
    body = re.sub(r"CUHK[- ]?(Workshop|2026)?", "the workshop", body)
    body = body.replace("the workshop the workshop", "the workshop")

    # restore fences
    def unstash(m):
        return fences[int(m.group(1))]
    body = re.sub(r"\x00FENCE(\d+)\x00", unstash, body)

    # collapse blank lines
    body = re.sub(r"\n{3,}", "\n\n", body).strip("\n")

    L = LANG[lang]
    short, nxt, nxt_label = NAV[lang].get(slug, (title, None, None))
    excerpt = L["excerpt"].format(short=short)
    fm = FRONT.format(title='"Agentic AI for Social Science Research"',
                      excerpt=excerpt, slug=slug, prefix=L["prefix"], lang=lang)

    # data-hb-lang drives the viewer's own localisation (目录 / 搜索 / 复制 / 上一节)
    # in _includes/handbook-assets.html — not decorative.
    back = (f'<p class="hb-backlink" data-hb-lang="{lang}">'
            + f'<a href="/course/">{L["home"]}</a>'
            + f' &nbsp;·&nbsp; <a href="{L["other_href"].format(slug=slug)}">{L["other_label"]}</a>'
            + (f' &nbsp;·&nbsp; <a href="/course/{L["prefix"]}{nxt}/">{nxt_label} &rarr;</a>' if nxt else "")
            + "</p>\n\n")

    lead = f"# {short}\n\n*{convert_inline(subtitle)}*\n\n" if subtitle else f"# {short}\n\n"

    out = (fm + "\n{% include handbook-assets.html %}\n{% include course-assets.html %}\n\n"
           + back + "{% raw %}\n" + lead + body + "\n{% endraw %}\n")
    return out


if __name__ == "__main__":
    src, slug, dst = sys.argv[1], sys.argv[2], sys.argv[3]
    failed = set()
    if len(sys.argv) > 4 and sys.argv[4]:
        failed = set(int(x) for x in sys.argv[4].split(",") if x.strip())
    lang = sys.argv[5] if len(sys.argv) > 5 and sys.argv[5] else "en"
    if lang not in LANG:
        sys.exit(f"convert_slides_book: unknown lang {lang!r} (want one of {sorted(LANG)})")
    result = convert(src, slug, failed, lang)
    open(dst, "w", encoding="utf-8").write(result)
    sys.stderr.write(f"[{slug}/{lang}] wrote {dst} ({len(result)} chars)\n")
