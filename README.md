# AI PoC Triage and Adoption Planner

This is a compact AI transformation prototype built for a Graduate AI Analyst style role. It helps an internal AI team move from "interesting idea" to a structured proof-of-concept decision.

The tool evaluates an AI use case across four dimensions:

- Business impact
- Delivery feasibility
- Responsible AI / operational risk
- Adoption readiness

It then produces:

- a stage-gate recommendation
- a four-week PoC plan
- adoption and training requirements
- suggested success metrics
- practical controls and human-review checkpoints
- an LLM prompt pack for deeper analysis
- an executive-ready summary

## Why this is relevant

The role asks for practical evidence of using AI to solve a problem, create something new, or improve productivity. This prototype is designed around the real work of AI adoption: triaging use cases, testing AI tools, supporting PoCs, tracking adoption, and communicating between technical and non-technical stakeholders.

It is intentionally not a generic chatbot. The focus is on structured AI enablement inside a regulated financial-administration environment, where AI ideas need business value, human oversight, auditability, data-sensitivity checks, and measurable adoption.

## Files

- `index.html` - polished standalone web app; open directly in a browser.
- `scoring_engine.py` - Python scoring logic and reusable data model.
- `sample_use_cases.json` - realistic sample use cases.
- `app.py` - optional Streamlit implementation for deployment.
- `requirements.txt` - dependencies for the Streamlit version.
- `APPLICATION_NOTE.md` - short explanation suitable for an application upload or text box.

## How to run

### Fastest preview

Open `index.html` in a browser.

### Python scoring check

```bash
python3 scoring_engine.py
```

### Optional Streamlit version

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Design choices

- Transparent scoring instead of hidden black-box output.
- Risk and adoption treated as first-class factors, not afterthoughts.
- Sample use cases are relevant to financial administration, but generic enough to avoid claiming any internal Computershare information.
- The prompt pack demonstrates deliberate AI use: task framing, structured outputs, challenge prompts, and adoption messaging.

