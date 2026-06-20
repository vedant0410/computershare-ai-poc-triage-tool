import json
from pathlib import Path

import pandas as pd
import streamlit as st

from scoring_engine import UseCase, score_use_case


st.set_page_config(
    page_title="AI PoC Triage and Adoption Planner",
    page_icon="AI",
    layout="wide",
)

ROOT = Path(__file__).parent


def load_samples():
    with open(ROOT / "sample_use_cases.json", "r", encoding="utf-8") as handle:
        return json.load(handle)


def score_colour(value, inverse=False):
    if inverse:
        if value >= 70:
            return "#b42318"
        if value >= 45:
            return "#b54708"
        return "#067647"
    if value >= 70:
        return "#067647"
    if value >= 45:
        return "#b54708"
    return "#b42318"


def metric_card(label, value, help_text, inverse=False):
    colour = score_colour(value, inverse=inverse)
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">{label}</div>
            <div class="metric-value" style="color:{colour};">{value}/100</div>
            <div class="metric-help">{help_text}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def build_case_from_state(data):
    return UseCase(
        title=data["title"],
        business_area=data["business_area"],
        problem=data["problem"],
        current_workflow=data["current_workflow"],
        ai_approach=data["ai_approach"],
        stakeholders=data["stakeholders"],
        data_types=data["data_types"],
        frequency=data["frequency"],
        time_saved=data["time_saved"],
        quality_uplift=data["quality_uplift"],
        strategic_alignment=data["strategic_alignment"],
        data_readiness=data["data_readiness"],
        process_clarity=data["process_clarity"],
        tool_fit=data["tool_fit"],
        stakeholder_readiness=data["stakeholder_readiness"],
        integration_complexity=data["integration_complexity"],
        sensitive_data=data["sensitive_data"],
        regulatory_exposure=data["regulatory_exposure"],
        hallucination_risk=data["hallucination_risk"],
        human_judgement=data["human_judgement"],
        audit_need=data["audit_need"],
        training_need=data["training_need"],
        change_complexity=data["change_complexity"],
        feedback_channels=data["feedback_channels"],
    )


st.markdown(
    """
    <style>
    :root {
      --ink: #111827;
      --muted: #667085;
      --line: #d0d5dd;
      --soft: #f8fafc;
      --panel: #ffffff;
      --accent: #215a6d;
    }
    .block-container { padding-top: 1.2rem; padding-bottom: 2rem; }
    h1, h2, h3 { letter-spacing: 0 !important; color: var(--ink); }
    .hero {
      border: 1px solid var(--line);
      background: linear-gradient(180deg, #ffffff, #f8fafc);
      border-radius: 8px;
      padding: 20px 22px;
      margin-bottom: 18px;
    }
    .hero-title {
      font-size: 30px;
      font-weight: 760;
      color: var(--ink);
      margin-bottom: 6px;
    }
    .hero-subtitle {
      font-size: 15px;
      line-height: 1.45;
      color: var(--muted);
      max-width: 980px;
    }
    .tag-row { margin-top: 12px; display: flex; gap: 8px; flex-wrap: wrap; }
    .tag {
      border: 1px solid #c9d7df;
      color: #215a6d;
      background: #f3f8fa;
      border-radius: 999px;
      padding: 4px 10px;
      font-size: 12px;
      font-weight: 650;
    }
    .metric-card {
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 14px 14px;
      background: var(--panel);
      min-height: 132px;
    }
    .metric-label {
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: .04em;
      color: var(--muted);
      font-weight: 760;
    }
    .metric-value {
      font-size: 34px;
      line-height: 1.1;
      font-weight: 780;
      margin-top: 6px;
    }
    .metric-help {
      color: var(--muted);
      font-size: 13px;
      line-height: 1.35;
      margin-top: 8px;
    }
    .decision {
      border-left: 4px solid var(--accent);
      background: #f3f8fa;
      padding: 14px 16px;
      border-radius: 6px;
      margin: 8px 0 16px;
    }
    .decision b { color: #174457; }
    .small-note { color: var(--muted); font-size: 13px; line-height: 1.4; }
    .plan-row {
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 12px 14px;
      margin-bottom: 10px;
      background: #fff;
    }
    .plan-phase {
      color: var(--ink);
      font-weight: 760;
      margin-bottom: 4px;
    }
    .copy-box {
      border: 1px solid var(--line);
      background: #f8fafc;
      border-radius: 8px;
      padding: 12px 14px;
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      font-size: 12.5px;
      line-height: 1.45;
      white-space: pre-wrap;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero">
      <div class="hero-title">AI PoC Triage and Adoption Planner</div>
      <div class="hero-subtitle">
        A practical tool for AI transformation teams: assess an internal AI idea, understand its impact,
        feasibility, risk and adoption readiness, then generate a controlled PoC plan with metrics,
        guardrails and stakeholder-facing prompts.
      </div>
      <div class="tag-row">
        <span class="tag">AI experimentation</span>
        <span class="tag">PoC stage-gates</span>
        <span class="tag">Copilot rollout</span>
        <span class="tag">Risk controls</span>
        <span class="tag">Adoption metrics</span>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

samples = load_samples()
sample_names = [item["title"] for item in samples]

with st.sidebar:
    st.header("Use-case setup")
    selected = st.selectbox("Load a sample", sample_names)
    base = next(item for item in samples if item["title"] == selected)
    st.caption("Adjust the sliders to test a different assumption set.")

    with st.expander("Business context", expanded=True):
        title = st.text_input("Use-case title", base["title"])
        business_area = st.text_input("Business area", base["business_area"])
        problem = st.text_area("Problem", base["problem"], height=90)
        current_workflow = st.text_area("Current workflow", base["current_workflow"], height=90)
        ai_approach = st.text_area("Proposed AI approach", base["ai_approach"], height=90)
        stakeholders = st.text_area("Stakeholders", base["stakeholders"], height=70)
        data_types = st.text_area("Data types", base["data_types"], height=70)

    with st.expander("Business impact", expanded=True):
        frequency = st.slider("Workflow frequency / volume", 1, 10, base["frequency"])
        time_saved = st.slider("Expected time saving", 1, 10, base["time_saved"])
        quality_uplift = st.slider("Quality or consistency uplift", 1, 10, base["quality_uplift"])
        strategic_alignment = st.slider("Strategic alignment", 1, 10, base["strategic_alignment"])

    with st.expander("Delivery feasibility", expanded=False):
        data_readiness = st.slider("Data readiness", 1, 10, base["data_readiness"])
        process_clarity = st.slider("Process clarity", 1, 10, base["process_clarity"])
        tool_fit = st.slider("Tool fit", 1, 10, base["tool_fit"])
        stakeholder_readiness = st.slider("Stakeholder readiness", 1, 10, base["stakeholder_readiness"])
        integration_complexity = st.slider("Integration complexity", 1, 10, base["integration_complexity"])

    with st.expander("Risk and adoption", expanded=False):
        sensitive_data = st.slider("Sensitive data exposure", 1, 10, base["sensitive_data"])
        regulatory_exposure = st.slider("Regulatory / client exposure", 1, 10, base["regulatory_exposure"])
        hallucination_risk = st.slider("Hallucination or unsupported-claim risk", 1, 10, base["hallucination_risk"])
        human_judgement = st.slider("Human judgement required", 1, 10, base["human_judgement"])
        audit_need = st.slider("Audit trail requirement", 1, 10, base["audit_need"])
        training_need = st.slider("Training need", 1, 10, base["training_need"])
        change_complexity = st.slider("Change complexity", 1, 10, base["change_complexity"])
        feedback_channels = st.slider("Feedback channels available", 1, 10, base["feedback_channels"])

case = build_case_from_state(locals())
result = score_use_case(case)

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    metric_card("Readiness", result["readiness"], "Composite score for whether this should move toward PoC.")
with col2:
    metric_card("Impact", result["impact"], "Potential value from time saved, quality and strategic fit.")
with col3:
    metric_card("Feasibility", result["feasibility"], "Data, process, tool and stakeholder readiness.")
with col4:
    metric_card("Risk", result["risk"], "Sensitivity, regulatory exposure, hallucination and audit burden.", inverse=True)
with col5:
    metric_card("Adoption", result["adoption"], "Whether users can understand, trust and repeatedly use it.")

st.markdown(
    f"""
    <div class="decision">
      <b>Stage-gate recommendation: {result["decision"]}</b><br>
      {result["decision_detail"]}
    </div>
    """,
    unsafe_allow_html=True,
)

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["Use-case brief", "PoC plan", "Adoption kit", "Prompt pack", "Export summary"]
)

with tab1:
    left, right = st.columns([1.2, 1])
    with left:
        st.subheader("Business brief")
        st.write(f"**Business area:** {case.business_area}")
        st.write(f"**Problem:** {case.problem}")
        st.write(f"**Current workflow:** {case.current_workflow}")
        st.write(f"**AI approach:** {case.ai_approach}")
        st.write(f"**Stakeholders:** {case.stakeholders}")
        st.write(f"**Data types:** {case.data_types}")
    with right:
        st.subheader("Scoring profile")
        profile = pd.DataFrame(
            {
                "Dimension": ["Readiness", "Impact", "Feasibility", "Risk", "Adoption"],
                "Score": [
                    result["readiness"],
                    result["impact"],
                    result["feasibility"],
                    result["risk"],
                    result["adoption"],
                ],
            }
        )
        st.bar_chart(profile, x="Dimension", y="Score", height=300)
        st.caption("Risk is intentionally separate: high value does not mean low control burden.")

with tab2:
    st.subheader("Four-week PoC plan")
    for row in result["plan"]:
        st.markdown(
            f"""
            <div class="plan-row">
              <div class="plan-phase">{row["phase"]}</div>
              <div><b>Work:</b> {row["work"]}</div>
              <div><b>Output:</b> {row["output"]}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    st.subheader("Success metrics")
    for metric in result["metrics"]:
        st.write(f"- {metric}")

with tab3:
    st.subheader("Controls and adoption requirements")
    control_col, adoption_col = st.columns(2)
    with control_col:
        st.markdown("**Required controls**")
        for control in result["controls"]:
            st.write(f"- {control}")
    with adoption_col:
        st.markdown("**Adoption materials to create**")
        st.write("- One-page use-case explainer")
        st.write("- Short walkthrough or demo script")
        st.write("- FAQ covering scope, limits, escalation, and data handling")
        st.write("- User feedback form with quality and confidence questions")
        st.write("- Leadership update showing adoption, impact, risks, and next decision")

with tab4:
    st.subheader("Prompt pack")
    st.markdown(
        "<p class='small-note'>These prompts are designed to use an LLM as an analyst assistant, not as an unchecked decision-maker.</p>",
        unsafe_allow_html=True,
    )
    for label, prompt in result["prompt_pack"].items():
        st.markdown(f"**{label.replace('_', ' ').title()}**")
        st.code(prompt, language="text")

with tab5:
    st.subheader("Executive-ready summary")
    st.write(result["executive_summary"])
    export = {
        "use_case": case.to_dict(),
        "scores": {k: result[k] for k in ["readiness", "impact", "feasibility", "risk", "adoption"]},
        "decision": result["decision"],
        "decision_detail": result["decision_detail"],
        "metrics": result["metrics"],
        "controls": result["controls"],
        "plan": result["plan"],
        "executive_summary": result["executive_summary"],
    }
    st.download_button(
        "Download JSON evidence pack",
        data=json.dumps(export, indent=2),
        file_name="ai_poc_triage_evidence_pack.json",
        mime="application/json",
    )

