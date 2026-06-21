# Application note: AI PoC Triage and Adoption Planner

For the "Show us how you use AI" prompt, I built a small AI PoC Triage and Adoption Planner. I wanted to create something close to the work of an AI transformation team rather than a generic chatbot demo.

Live demo: https://vedant0410.github.io/computershare-ai-poc-triage-tool/  
Code repository: https://github.com/vedant0410/computershare-ai-poc-triage-tool

## Motivation and how I used AI

I chose this artefact because I think the hard part of enterprise AI is no longer simply getting access to powerful tools. The harder question is how an organisation decides which AI ideas are worth testing, how it keeps them safe enough to pilot, how it measures whether they actually improve work, and how it helps people adopt them without creating shadow AI or ungoverned workflows.

That is why I built a triage and adoption planner rather than a generic chatbot. The prototype reflects my view that useful AI work sits between capability and judgement: AI can help generate options, structure analysis, challenge assumptions, summarise evidence, and accelerate prototyping, but humans still need to define the business problem, set constraints, review risks, decide what evidence is enough, and own the final deployment decision.

I used AI as a thinking and building partner in that spirit. It helped me move faster from problem framing to interface structure, scoring logic, sample use cases, prompt-pack design, and documentation. But I deliberately constrained the work around a clear enterprise workflow: transparent scoring, human review checkpoints, risk controls, adoption metrics, and stage-gate decisions. In other words, I tried to use AI not as an answer machine, but as a way to build a more disciplined decision tool.

The problem I wanted to solve is one that an AI transformation team faces often: many AI ideas sound promising, but not all are ready to pilot. Some have high business value but weak data readiness; others are easy to prototype but carry sensitive-data, regulatory, auditability, or adoption risks.

I made the tool specifically relevant to Computershare after reading more about the business. Computershare's own AI insights from its 2025 Industry Conference emphasise alignment before algorithms, regulation as design, attention to shadow AI, different adoption speeds across teams, clear measures of success, training, and a "test, measure, analyze and repeat" approach. The prototype reflects exactly that logic: it does not just ask whether an AI idea is exciting, but whether it has business value, feasible data/process conditions, responsible controls, human review, adoption support, and measurable outcomes.

It also fits Computershare's wider context as a global financial administration and transfer agency business where technology is used to deliver secure data management, reporting, shareholder services, employee share-plan support, and compliant client solutions. Recent initiatives such as Computershare's issuer-sponsored tokenized shares work show the company is modernising financial infrastructure while preserving regulation, trust, investor rights, and operational control. I tried to build with that same mindset: innovation is useful only when it can be tested, governed, adopted, and trusted.

The tool takes an internal AI use case and scores it across business impact, delivery feasibility, responsible AI / operational risk, and adoption readiness. It then produces a stage-gate recommendation, a four-week PoC plan, required controls, success metrics, adoption materials, and a prompt pack for deeper LLM-assisted analysis.

I designed it to be relevant to a financial-administration environment rather than a generic chatbot demo. The sample use cases include a Copilot assistant for shareholder query summaries, a corporate actions document obligation extractor, an employee share-plan FAQ assistant, and an internal AI adoption reporting assistant. These examples show how AI can support productivity while still requiring human review, approved tooling, audit trails, escalation routes, and clear measurement.

What this demonstrates:

- I can use AI-assisted development to move from concept to working prototype quickly, while still making deliberate product, workflow, and risk-design choices.
- I understand that enterprise AI adoption is not just about prompting; it needs workflow design, risk controls, stakeholder engagement, training, and adoption metrics.
- I can translate AI capability into a structured business tool for non-technical stakeholders.
- I can think about PoCs from idea through to outcome: scope, build, test, measure, and decide whether to scale.

Files included:

- `index.html`: standalone browser version.
- `app.py`: optional Streamlit version.
- `scoring_engine.py`: Python scoring logic.
- `sample_use_cases.json`: realistic use-case examples.

If I had enterprise access, the next step would be to connect this to approved Copilot/LLM tooling, maintain a live AI use-case register, log reviewer decisions, and connect adoption metrics to an internal reporting dashboard.

Computershare context I considered:

- Computershare's public AI approach, especially its Global AI Working Group, AI risk framework, data-security posture, document-processing use cases, service-support examples, and GEMS AI.
- Computershare's 2025 Industry Conference AI insights around reusable frameworks, responsible AI, alignment before algorithms, sandbox-style experimentation, clear measures of success, training, and "test, measure, analyze and repeat".
- Computershare's 2026 issuer-sponsored tokenized shares work with Securitize, which reinforced the importance of modernising financial infrastructure while preserving issuer control, regulatory oversight, shareholder trust, and operational interoperability.
