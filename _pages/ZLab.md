---
permalink: /zlab/
title: "Zhang Computational Social Science Lab"
excerpt: "People, projects, and placements from the Zhang CSS Lab at Stony Brook University."
author_profile: true
---

<style>
.zl-lead { font-size: 1.05em; line-height: 1.6; }
.zl-cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 1rem; margin: 1.5em 0; }
.zl-card { border: 1px solid #e2e2e2; border-radius: 10px; padding: 1.05em 1.15em; background: #fafafa; transition: box-shadow .15s ease, border-color .15s ease, transform .15s ease; }
.zl-card:hover { box-shadow: 0 4px 14px rgba(0,0,0,.10); border-color: #a84a22; transform: translateY(-2px); }
.zl-card h3 { margin: .1em 0 .3em; font-size: 1.12em; line-height: 1.25; }
.zl-card .zl-role { font-size: .72em; letter-spacing: .07em; text-transform: uppercase; color: #a84a22; font-weight: 700; }
.zl-card p { margin: 0; font-size: .87em; color: #555; line-height: 1.45; }
.zl-place { display: flex; gap: 1.1em; align-items: flex-start; border: 1px solid #e7d9c9; border-left: 5px solid #a84a22; border-radius: 12px; background: linear-gradient(100deg, #f7ece2 0%, #fdfaf6 62%); padding: 1.1em 1.3em; margin: 1.1em 0; box-shadow: 0 1px 2px rgba(80,50,20,.06); }
.zl-place img { width: 86px; height: 86px; object-fit: cover; border-radius: 50%; border: 2px solid #fff; box-shadow: 0 2px 8px rgba(80,50,20,.18); flex-shrink: 0; }
.zl-place-body { flex: 1; min-width: 0; }
.zl-place h3 { margin: .05em 0 .28em; font-size: 1.14em; color: #7a3b1c; line-height: 1.25; }
.zl-place .zl-dest { font-weight: 700; color: #a84a22; font-size: .93em; }
.zl-place p { margin: .3em 0 0; font-size: .89em; color: #5a5048; line-height: 1.5; }
.zl-note { border-left: 3px solid #a84a22; background: #f7ece2; padding: .7em 1em; border-radius: 0 6px 6px 0; font-size: .92em; }
.zl-figure { margin: 1.5em 0; }
.zl-figure img { width: 100%; height: auto; display: block; border-radius: 12px; border: 1px solid #e7d9c9; box-shadow: 0 6px 20px rgba(40,25,12,.14); }
.zl-figure figcaption { font-size: .87em; color: #6a6058; margin-top: .6em; line-height: 1.5; }
.zl-projects { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1.05rem; margin: 1.5em 0; }
.zl-proj { border: 1px solid #e7d9c9; border-top: 4px solid #a84a22; border-radius: 12px; background: linear-gradient(170deg, #fdfaf6 0%, #f9f2ea 100%); padding: 1.15em 1.25em 1.05em; display: flex; flex-direction: column; transition: box-shadow .16s ease, transform .16s ease; }
.zl-proj:hover { box-shadow: 0 8px 22px rgba(168,74,34,.16); transform: translateY(-2px); }
.zl-proj .zl-num { font-size: .7em; letter-spacing: .1em; text-transform: uppercase; color: #a84a22; font-weight: 700; }
.zl-proj h3 { margin: .25em 0 .4em; font-size: 1.1em; color: #7a3b1c; line-height: 1.3; }
.zl-proj p { margin: 0 0 .7em; font-size: .88em; color: #55504a; line-height: 1.5; flex-grow: 1; }
.zl-proj .zl-tags { font-size: .78em; color: #8a7f74; border-top: 1px solid #ecdfd2; padding-top: .55em; line-height: 1.5; }
.zl-proj .zl-tags a { color: #a84a22; }
.zl-btn { display: inline-block; font-weight: 700; font-size: .92em; text-decoration: none !important; padding: .55em 1em; border-radius: 8px; background: #a84a22; color: #fff; transition: background .15s ease; }
.zl-btn:hover { background: #8a5a34; color: #fff; }
@media (max-width: 480px) {
  .zl-place { flex-direction: column; align-items: center; text-align: center; }
}
</style>

<p class="zl-lead">The <strong>Zhang Computational Social Science Lab</strong> at Stony Brook University studies social and human behavior with computational, statistical, and network methods — natural language processing and computer vision applied to data large enough that reading it by hand is no longer an option. Our current work centers on the relationship between <strong>AI and society</strong>, alongside long-running interests in mobility, segregation, and polarization in the United States.</p>

## What we work on

Three lines of research run in parallel. All three share a method — large-scale digital trace data, read with language and vision models — and a commitment to verifying what those models tell us.

<div class="zl-projects">

  <div class="zl-proj">
    <div class="zl-num">Project 01</div>
    <h3>AI and society, in both directions</h3>
    <p>How AI reshapes social life, and how social life reshapes AI. One strand measures societal impact — chatbots and adolescent mental health, generative AI in election campaigns, the spread of machine-written text. The other asks what agentic AI does to knowledge production itself: if an agent can run a study end to end, what is left for the social scientist to do, and which checks have to stay human?</p>
    <div class="zl-tags">Related: <a href="/vibe-researching/">Vibe Researching</a> · <a href="https://github.com/joshzyj/open-scholar-skill"><code>open-scholar-skill</code></a> · <a href="https://doi.org/10.1177/08944393251366243">the risks of LLM text annotation</a></div>
  </div>

  <div class="zl-proj">
    <div class="zl-num">Project 02</div>
    <h3>Community resilience and the geography of daily life</h3>
    <p>GPS mobility traces joined to administrative and voter records, used to study how communities absorb shocks and how inequality is built into the places people actually move through. Recent work traces activity-space segregation across U.S. metro areas and public response to Hurricane Helene — where segregation is measured not by where people sleep but by where they spend their days.</p>
    <div class="zl-tags">Related: <a href="https://doi.org/10.1215/00703370-12193739">mobility-based segregation (<em>Demography</em>)</a> · <a href="https://doi.org/10.7758/RSF.2025.11.1.07">activity-space segregation (<em>RSF</em>)</a></div>
  </div>

  <div class="zl-proj">
    <div class="zl-num">Project 03</div>
    <h3>Video as social data</h3>
    <p>YouTube at scale, read with large language and vision models. The lab studies how China is framed and argued about online, and how video circulates around polarization, protest, and voting — including the discourse that legitimizes undocumented immigration, and visual framing in global news coverage. Video is still mostly unread by social scientists; the methods to read it are a research problem in their own right.</p>
    <div class="zl-tags">Related: large language and vision models for global social protests; visual framing in global news media</div>
  </div>

</div>

## Current members

<div class="zl-cards">
  <div class="zl-card">
    <div class="zl-role">PhD Student · Sociology</div>
    <h3><a href="https://www.stonybrook.edu/sociology/people/bulin-li.html">Bulin Li</a></h3>
    <p>Immigration, politics, and computational social science. Applies NLP to large social media datasets to trace how people legitimize immigration in public discourse. BA from Anhui University; master's degrees in sociology and statistics from American University and George Washington University.</p>
  </div>
  <div class="zl-card">
    <div class="zl-role">PhD Student · Sociology</div>
    <h3>Zoey Zhang</h3>
    <p>Computational social science.</p>
  </div>
  <div class="zl-card">
    <div class="zl-role">PhD Student · Sociology</div>
    <h3><a href="https://www.stonybrook.edu/sociology/people/kaizhe-wang.html">Kaizhe Wang</a></h3>
    <p>Social stratification and demography through causal inference and computational methods, with an active interest in gender and LGBTQ+ issues. BA from East China University of Science and Technology; MS in social policy from Peking University.</p>
  </div>
</div>

## The lab's first PhD

<figure class="zl-figure">
  <img src="/images/haolin-defense.jpeg" alt="Illustration of Hao Lin's doctoral dissertation defense, holding flowers with her committee, in front of a slide reading &quot;Mapping the Social Turn in Artificial Intelligence Research as a Scientific/Intellectual Movement&quot;">
  <figcaption>Hao Lin defends <em>Mapping the &ldquo;Social Turn&rdquo; in Artificial Intelligence Research as a Scientific/Intellectual Movement</em> — the lab's first doctoral dissertation.</figcaption>
</figure>

## Placements

<div class="zl-place">
  <img src="/images/haolin.png" alt="Hao Lin">
  <div class="zl-place-body">
    <h3>Hao Lin</h3>
    <div class="zl-dest">Senior Data Scientist, Apple</div>
    <p>The lab's first PhD graduate. Hao studies racial inequality, social contagion, and social networks, applying computational methods to social behavior; our paper on <a href="https://doi.org/10.48550/arXiv.2503.22040">the risks of using LLMs for text annotation</a> appeared in <em>Social Science Computer Review</em>. BA from Central University of Finance and Economics (2017); MSc in sociology from Utrecht University (2019).</p>
  </div>
</div>

<div class="zl-place">
  <div class="zl-place-body">
    <h3>Danial Vahabli</h3>
    <div class="zl-dest">Postdoctoral Researcher, WZB Berlin Social Science Center</div>
    <p>A political sociologist working at the intersection of resistance, culture, and globalization, and a former graduate fellow of Stony Brook's Institute for Advanced Computational Science. His dissertation asks how and why domestic dissidents seek international support, how their concerns get represented in international media, and what that support does to the movements receiving it.</p>
  </div>
</div>

## Join the lab

The lab hires graduate and undergraduate research assistants in computational social science. If that is you, [apply through this form](https://docs.google.com/forms/d/e/1FAIpQLSdcAjGlDqmyHAAqn4bh2UzsUi9zHOE3xZhO-5eKtItJl7ldSA/viewform?usp=sf_link).

<div class="zl-note">
<strong>On recommendation letters.</strong> I write letters for students who have worked in the lab. Please come talk to me about it at least six months before your application is due.
</div>
