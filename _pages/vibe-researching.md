---
permalink: /vibe-researching/
title: "Vibe Researching"
excerpt: "A hands-on handbook for doing real social-science research with coding agents."
author_profile: true
---

<style>
.vr-lead { font-size: 1.05em; line-height: 1.6; }
.vr-cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1rem; margin: 1.6em 0; }
.vr-card { display: block; border: 1px solid #e2e2e2; border-radius: 10px; padding: 1.1em 1.2em; text-decoration: none !important; color: inherit; background: #fafafa; transition: box-shadow .15s ease, border-color .15s ease, transform .15s ease; }
.vr-card:hover { box-shadow: 0 4px 14px rgba(0,0,0,.10); border-color: #a84a22; transform: translateY(-2px); }
.vr-card .vr-eyebrow { font-size: .72em; letter-spacing: .08em; text-transform: uppercase; color: #a84a22; font-weight: 700; }
.vr-card h3 { margin: .25em 0 .35em; font-size: 1.15em; }
.vr-card p { margin: 0; font-size: .88em; color: #555; line-height: 1.45; }
.vr-parts { margin: 1em 0; }
.vr-parts li { margin-bottom: .35em; }
.vr-meta { font-size: .85em; color: #666; }
.vr-note { border-left: 3px solid #a84a22; background: #f7ece2; padding: .7em 1em; border-radius: 0 6px 6px 0; font-size: .92em; }
.vr-video { margin: 1.6em 0; }
.vr-video video { width: 100%; height: auto; aspect-ratio: 16 / 9; display: block; border-radius: 10px; border: 1px solid #e2d6c8; background: #241f1b; box-shadow: 0 6px 20px rgba(40,25,12,.14); }
.vr-video figcaption { font-size: .85em; color: #6a6058; margin-top: .55em; }
.vr-paper { border: 1px solid #e7d9c9; border-left: 5px solid #a84a22; border-radius: 12px; background: linear-gradient(100deg, #f7ece2 0%, #fdfaf6 62%); padding: 1.15em 1.35em; margin: 1.4em 0; box-shadow: 0 1px 2px rgba(80,50,20,.06); }
.vr-paper .vr-eyebrow { font-size: .72em; letter-spacing: .08em; text-transform: uppercase; color: #a84a22; font-weight: 700; }
.vr-paper h3 { margin: .18em 0 .3em; font-size: 1.18em; color: #7a3b1c; line-height: 1.25; }
.vr-cite { font-size: .9em; color: #5a5048; line-height: 1.5; margin: 0 0 .85em; }
.vr-cite a { word-break: break-word; }
.vr-btns { display: flex; gap: .6em; flex-wrap: wrap; }
.vr-btn { display: inline-block; font-weight: 700; font-size: .9em; text-decoration: none !important; padding: .5em .95em; border-radius: 8px; transition: background .15s ease, border-color .15s ease; }
.vr-btn-primary { background: #a84a22; color: #fff; }
.vr-btn-primary:hover { background: #8a5a34; }
.vr-btn-ghost { border: 1px solid #d8c4ae; color: #7a3b1c; background: #fff; }
.vr-btn-ghost:hover { border-color: #a84a22; }
</style>

<p class="vr-lead"><strong>Vibe researching</strong> is doing real empirical social science by <em>directing coding agents</em> — Claude Code and Codex — rather than writing every line yourself. You describe the study; the agent runs the brainstorm, the design, the analysis, the draft, and the checks. The discipline that separates it from careless automation is <strong>verification</strong>: nothing is trusted until an independent pass confirms it.</p>

This is the home of my **participant handbook**, written for a two-hour hands-on workshop. It is not a slide transcript — it is a tutorial you can work through at your own pace, on your own machine, from *"Claude is not yet installed"* all the way to a complete, verified, journal-ready paper draft built on real [CFPS](http://www.isss.pku.edu.cn/cfps/en/) data. Every command, figure, table, and verification finding in it came from an actual run — including the **seven critical errors** that verification caught before the manuscript went anywhere.

<div class="vr-cards">
  <a class="vr-card" href="/vibe-researching/en/">
    <div class="vr-eyebrow">Read online · English</div>
    <h3>The Handbook &rarr;</h3>
    <p>Read section by section with a searchable sidebar and one-click copy on every code block.</p>
  </a>
  <a class="vr-card" href="/vibe-researching/zh/">
    <div class="vr-eyebrow">在线阅读 · 中文</div>
    <h3>学员实操手册 &rarr;</h3>
    <p>侧边栏可搜索、逐节阅读，代码块一键复制，适合边读边操作。</p>
  </a>
</div>

## See a full run

Here is the whole idea in one take. Watch Open Scholar Skills run end to end on a real study — [`scholar-full-paper`](https://github.com/joshzyj/open-scholar-skill) orchestrating the pipeline from project setup and a safety scan, through literature review and analysis, into a **multi-agent code review that catches real, results-changing defects**, and on to drafting and verification. The agent does the execution; the verification gates decide what survives.

<figure class="vr-video">
  <video controls preload="none" playsinline poster="/images/scholar-full-paper-demo-poster.jpg" width="1280" height="720">
    <source src="/files/scholar-full-paper-demo.mp4" type="video/mp4">
    Your browser can’t play this embedded video — <a href="/files/scholar-full-paper-demo.mp4">open the MP4 directly</a>.
  </video>
  <figcaption>About 11 minutes · <code>scholar-full-paper</code> on a China digital-divide study (CFPS) — a multi-hour run, condensed.</figcaption>
</figure>

## What's inside

The handbook is built around one running example — a *Social Forces*-style paper on the Chinese digital divide, built from six waves of CFPS (2010–2020) using only Claude Code, Codex CLI, and the [`open-scholar-skill`](https://github.com/joshzyj/open-scholar-skill) suite.

<ul class="vr-parts">
  <li><strong>Part I — Foundations.</strong> Install the agents, open your first session, learn the safe project layout, and write an agent-quality prompt.</li>
  <li><strong>Part II — Open Scholar Skills, end to end.</strong> Every major skill in the order you actually use them: brainstorm → idea → design → EDA → analysis → write → <em>verify</em> → citations → polish.</li>
  <li><strong>Part III — Orchestrators.</strong> When one paper deserves the full pipeline (<code>scholar-full-paper</code>, <code>scholar-auto-research</code>), plus Codex as an external reviewer.</li>
  <li><strong>Part IV — Responsible practice.</strong> The first-20-minutes protocol, common mistakes, the take-home checklist, and five principles for responsible use.</li>
  <li><strong>Appendices.</strong> The real artifacts in full — brainstorm reports, design blueprint, code-review and verification reports, and a Windows setup walkthrough.</li>
</ul>

<div class="vr-note">
<strong>Built for copy-and-paste.</strong> Commands prefixed with <code>$</code> go in your terminal (without the <code>$</code>); commands prefixed with <code>&gt;</code> go inside a running Claude Code session. Hover any code block and hit <strong>Copy</strong>.
</div>

## The paper

The peer-reviewed study behind these workshops and the talk is now published in *Chinese Sociological Review* — read the full text free below.

<div class="vr-paper">
  <div class="vr-eyebrow">Peer-reviewed article · Chinese Sociological Review</div>
  <h3>Vibe Researching: Can AI Agents with Skills Replace or Augment Social Scientists?</h3>
  <p class="vr-cite">Zhang, Y. (2026). Vibe researching: can AI agents with skills replace or augment social scientists? <em>Chinese Sociological Review</em>, 1–36. <a href="https://doi.org/10.1080/21620555.2026.2707167">https://doi.org/10.1080/21620555.2026.2707167</a></p>
  <div class="vr-btns">
    <a class="vr-btn vr-btn-primary" href="https://www.tandfonline.com/eprint/A7U8VWGZ9GD3ESISGS9U/full?target=10.1080/21620555.2026.2707167">Read the full text (free) &rarr;</a>
    <a class="vr-btn vr-btn-ghost" href="https://doi.org/10.1080/21620555.2026.2707167">View via DOI</a>
  </div>
</div>

## The talk

The workshops are paired with a research talk — *Vibe Researching as Wolf Coming: Can AI Agents with Skills Replace or Augment Social Scientists?* Walk through it slide by slide right in your browser — arrow keys to move, an overview grid, and fullscreen.

<div class="vr-cards">
  <a class="vr-card" href="/vibe-researching/slides-en/">
    <div class="vr-eyebrow">Slides · English</div>
    <h3>Vibe Researching as Wolf Coming &rarr;</h3>
    <p>The full talk, slide by slide: arrow-key navigation, an overview grid, and fullscreen.</p>
  </a>
  <a class="vr-card" href="/vibe-researching/slides-zh/">
    <div class="vr-eyebrow">幻灯片 · 中文</div>
    <h3>狼来了 &rarr;</h3>
    <p>逐张浏览完整演讲，支持方向键翻页、缩略图总览与全屏。</p>
  </a>
</div>

## The lecture

The workshops grew out of a four-day lecture series — *Agentic AI for Social Science Research* — that moves from how a language model actually works to a full research pipeline. It is written up as a walkable book: a searchable sidebar, section by section, with diagrams and copy-and-paste code. It is shared with workshop participants and opens with a passcode.

<div class="vr-cards">
  <a class="vr-card" href="/vibe-researching-lecture/">
    <div class="vr-eyebrow">Lecture · Day 1–4 · Passcode</div>
    <h3>Agentic AI for Social Science Research &rarr;</h3>
    <p>The Model · Agents · Claude Code · The Pipeline — a four-day book for participants. Ask me for the passcode.</p>
  </a>
</div>

## Resources

- **The paper (free full text):** [*Vibe Researching* in *Chinese Sociological Review*](https://www.tandfonline.com/eprint/A7U8VWGZ9GD3ESISGS9U/full?target=10.1080/21620555.2026.2707167) · [DOI](https://doi.org/10.1080/21620555.2026.2707167)
- **Read the handbook:** [English](/vibe-researching/en/) · [中文](/vibe-researching/zh/)
- **Talk slides (read online):** [English](/vibe-researching/slides-en/) · [中文](/vibe-researching/slides-zh/)
- **The skill suite:** [`open-scholar-skill` on GitHub](https://github.com/joshzyj/open-scholar-skill)

<p class="vr-meta">Author: Yongjun Zhang (Stony Brook University). If you would like this workshop run for your department or program, feel free to <a href="mailto:yongjun.zhang@stonybrook.edu">reach out</a>.</p>
