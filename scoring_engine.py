from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Dict, List


def clamp(value: float, lower: float = 0, upper: float = 100) -> float:
    return max(lower, min(upper, value))


@dataclass
class UseCase:
    title: str
    business_area: str
    problem: str
    current_workflow: str
    ai_approach: str
    stakeholders: str
    data_types: str
    frequency: int = 5
    time_saved: int = 5
    quality_uplift: int = 5
    strategic_alignment: int = 5
    data_readiness: int = 5
    process_clarity: int = 5
    tool_fit: int = 5
    stakeholder_readiness: int = 5
    integration_complexity: int = 5
    sensitive_data: int = 5
    regulatory_exposure: int = 5
    hallucination_risk: int = 5
    human_judgement: int = 5
    audit_need: int = 5
    training_need: int = 5
    change_complexity: int = 5
    feedback_channels: int = 5

    def to_dict(self) -> Dict[str, object]:
        return asdict(self)


def weighted_average(values: Dict[str, int], weights: Dict[str, float]) -> float:
    total_weight = sum(weights.values())
    return sum(values[k] * weights[k] for k in weights) / total_weight * 10


def score_use_case(case: UseCase) -> Dict[str, object]:
    impact = weighted_average(
        {
            "frequency": case.frequency,
            "time_saved": case.time_saved,
            "quality_uplift": case.quality_uplift,
            "strategic_alignment": case.strategic_alignment,
        },
        {
            "frequency": 0.24,
            "time_saved": 0.30,
            "quality_uplift": 0.22,
            "strategic_alignment": 0.24,
        },
    )

    feasibility_raw = weighted_average(
        {
            "data_readiness": case.data_readiness,
            "process_clarity": case.process_clarity,
            "tool_fit": case.tool_fit,
            "stakeholder_readiness": case.stakeholder_readiness,
            "integration_complexity": 10 - case.integration_complexity,
        },
        {
            "data_readiness": 0.25,
            "process_clarity": 0.21,
            "tool_fit": 0.22,
            "stakeholder_readiness": 0.17,
            "integration_complexity": 0.15,
        },
    )
    feasibility = clamp(feasibility_raw)

    risk = weighted_average(
        {
            "sensitive_data": case.sensitive_data,
            "regulatory_exposure": case.regulatory_exposure,
            "hallucination_risk": case.hallucination_risk,
            "human_judgement": case.human_judgement,
            "audit_need": case.audit_need,
        },
        {
            "sensitive_data": 0.22,
            "regulatory_exposure": 0.24,
            "hallucination_risk": 0.21,
            "human_judgement": 0.17,
            "audit_need": 0.16,
        },
    )

    adoption = weighted_average(
        {
            "stakeholder_readiness": case.stakeholder_readiness,
            "feedback_channels": case.feedback_channels,
            "training_need": 10 - case.training_need,
            "change_complexity": 10 - case.change_complexity,
            "process_clarity": case.process_clarity,
        },
        {
            "stakeholder_readiness": 0.26,
            "feedback_channels": 0.22,
            "training_need": 0.17,
            "change_complexity": 0.17,
            "process_clarity": 0.18,
        },
    )

    readiness = clamp(0.38 * impact + 0.30 * feasibility + 0.20 * adoption - 0.12 * risk + 12)

    if risk >= 78 and impact < 75:
        decision = "Discovery first"
        decision_detail = "High control burden relative to expected value. Clarify data handling, human ownership, and regulatory exposure before building."
    elif impact >= 72 and feasibility >= 62 and risk <= 68:
        decision = "Fast-track controlled PoC"
        decision_detail = "Strong value and enough feasibility for a limited pilot with clear success metrics and human review."
    elif impact >= 65 and risk > 68:
        decision = "Controlled pilot with governance gate"
        decision_detail = "Value is promising, but risk controls, auditability, and escalation routes must be designed before user rollout."
    elif feasibility < 55:
        decision = "Pre-PoC discovery"
        decision_detail = "The opportunity may be useful, but the process, data, or tooling is not yet ready enough for a reliable pilot."
    else:
        decision = "Prioritise if capacity allows"
        decision_detail = "Suitable for backlog review or a small experiment after higher-impact or easier-to-scale opportunities."

    metrics = recommend_metrics(case)
    controls = recommend_controls(case, risk)
    plan = build_poc_plan(case, decision)

    return {
        "impact": round(impact),
        "feasibility": round(feasibility),
        "risk": round(risk),
        "adoption": round(adoption),
        "readiness": round(readiness),
        "decision": decision,
        "decision_detail": decision_detail,
        "metrics": metrics,
        "controls": controls,
        "plan": plan,
        "executive_summary": executive_summary(case, decision, readiness, impact, feasibility, risk, adoption),
        "prompt_pack": prompt_pack(case),
    }


def recommend_metrics(case: UseCase) -> List[str]:
    metrics = [
        "Time saved per case or workflow cycle",
        "User adoption rate and repeat usage",
        "Human-review correction rate",
        "User confidence / satisfaction score",
    ]
    if case.hallucination_risk >= 6:
        metrics.append("Unsupported claim rate or citation failure rate")
    if case.regulatory_exposure >= 6 or case.sensitive_data >= 6:
        metrics.append("Number of escalations, policy breaches, or blocked unsafe outputs")
    if case.quality_uplift >= 7:
        metrics.append("Quality score against human-reviewed baseline")
    return metrics


def recommend_controls(case: UseCase, risk: float) -> List[str]:
    controls = [
        "Human review before external or client-facing use",
        "Clear scope statement and list of out-of-scope requests",
        "Feedback channel for users to flag poor outputs",
        "Named business owner and technical owner for the PoC",
    ]
    if case.sensitive_data >= 6:
        controls.append("Use approved enterprise tools only; avoid pasting sensitive data into public AI systems")
    if case.regulatory_exposure >= 6:
        controls.append("Compliance review before pilot expansion")
    if case.audit_need >= 6:
        controls.append("Retain prompts, source references, reviewer decisions, and output version history")
    if case.hallucination_risk >= 6:
        controls.append("Require citations or source-grounding for factual claims")
    if risk >= 75:
        controls.append("Run a red-team style failure review before scaling")
    return controls


def build_poc_plan(case: UseCase, decision: str) -> List[Dict[str, str]]:
    return [
        {
            "phase": "Week 1 - Frame",
            "work": "Confirm user group, current workflow, data boundaries, success metric, and stop criteria.",
            "output": "One-page PoC charter and risk register.",
        },
        {
            "phase": "Week 2 - Prototype",
            "work": "Build a constrained workflow using approved tools and a small representative test set.",
            "output": "Clickable prototype or workflow demo with prompt / process documentation.",
        },
        {
            "phase": "Week 3 - Test",
            "work": "Run side-by-side comparison against the current process with human reviewers.",
            "output": "Evidence pack: time saved, quality deltas, errors, user feedback, and control gaps.",
        },
        {
            "phase": "Week 4 - Decide",
            "work": "Present recommendation to scale, iterate, pause, or stop.",
            "output": f"Decision memo: {decision}.",
        },
    ]


def executive_summary(
    case: UseCase,
    decision: str,
    readiness: float,
    impact: float,
    feasibility: float,
    risk: float,
    adoption: float,
) -> str:
    return (
        f"{case.title} is best treated as '{decision}'. "
        f"The opportunity has an overall readiness score of {round(readiness)}/100, "
        f"with impact {round(impact)}, feasibility {round(feasibility)}, risk {round(risk)}, "
        f"and adoption readiness {round(adoption)}. The main value is solving: {case.problem} "
        f"The recommended next step is a constrained four-week PoC with named owners, human review, "
        f"approved tooling, success metrics, and a clear scale / iterate / stop decision gate."
    )


def prompt_pack(case: UseCase) -> Dict[str, str]:
    context = f"""
Use case: {case.title}
Business area: {case.business_area}
Problem: {case.problem}
Current workflow: {case.current_workflow}
Proposed AI approach: {case.ai_approach}
Stakeholders: {case.stakeholders}
Data types: {case.data_types}
""".strip()

    return {
        "analysis_prompt": (
            "You are supporting an enterprise AI transformation team. Analyse the AI use case below. "
            "Return structured JSON with: business_value, users_affected, workflow_change, key_risks, "
            "required_controls, adoption_barriers, success_metrics, and first_poc_steps. "
            "Be practical, conservative about risk, and do not invent facts.\n\n" + context
        ),
        "challenge_prompt": (
            "Act as a skeptical risk, compliance, and operations reviewer. Identify the strongest reasons this AI use case "
            "could fail or cause harm. For each risk, propose a test or control that could be checked during a four-week PoC.\n\n"
            + context
        ),
        "comms_prompt": (
            "Rewrite this AI use case for three non-technical audiences: a frontline user, a team manager, and a senior leader. "
            "For each audience, explain the value, what changes in their workflow, what remains human-owned, and what success looks like.\n\n"
            + context
        ),
        "measurement_prompt": (
            "Design a measurement plan for this AI PoC. Include baseline metric, pilot metric, qualitative feedback question, "
            "safety metric, adoption metric, and stop/scale threshold.\n\n" + context
        ),
    }


if __name__ == "__main__":
    demo = UseCase(
        title="Copilot assistant for shareholder query summaries",
        business_area="Customer operations",
        problem="Service teams spend time reading long case notes and email threads before responding to shareholder queries.",
        current_workflow="Analysts manually read historical notes, extract key facts, draft response notes, and ask senior colleagues to check sensitive cases.",
        ai_approach="Use an approved GenAI assistant to summarise case history, identify missing information, and draft internal response notes for human review.",
        stakeholders="Customer service agents, team leaders, compliance, data protection, technology services",
        data_types="Customer service notes, email text, case metadata, internal knowledge articles",
        frequency=8,
        time_saved=7,
        quality_uplift=6,
        strategic_alignment=8,
        data_readiness=6,
        process_clarity=8,
        tool_fit=7,
        stakeholder_readiness=7,
        integration_complexity=4,
        sensitive_data=8,
        regulatory_exposure=7,
        hallucination_risk=6,
        human_judgement=7,
        audit_need=8,
        training_need=7,
        change_complexity=6,
        feedback_channels=6,
    )
    result = score_use_case(demo)
    print(result["decision"])
    print(result["executive_summary"])
