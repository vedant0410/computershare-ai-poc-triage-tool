from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


OUTPUT = "AI_PoC_Triage_and_Adoption_Planner_Overview.pdf"


def para(text, style):
    return Paragraph(text, style)


def build_pdf():
    doc = SimpleDocTemplate(
        OUTPUT,
        pagesize=A4,
        rightMargin=0.62 * inch,
        leftMargin=0.62 * inch,
        topMargin=0.58 * inch,
        bottomMargin=0.58 * inch,
    )
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="TitleClean",
            parent=styles["Title"],
            fontName="Helvetica-Bold",
            fontSize=22,
            leading=26,
            textColor=colors.HexColor("#111827"),
            spaceAfter=8,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Section",
            parent=styles["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=12,
            leading=15,
            textColor=colors.HexColor("#174457"),
            spaceBefore=8,
            spaceAfter=5,
        )
    )
    styles.add(
        ParagraphStyle(
            name="BodyClean",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=9.4,
            leading=12.2,
            textColor=colors.HexColor("#111827"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="Small",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=8.3,
            leading=10.5,
            textColor=colors.HexColor("#475467"),
        )
    )

    story = [
        para("AI PoC Triage and Adoption Planner", styles["TitleClean"]),
        para(
            "A compact prototype for AI transformation teams: evaluate internal AI ideas, decide whether they are ready for a controlled proof-of-concept, and define the adoption plan, success metrics, and guardrails needed before scaling.",
            styles["BodyClean"],
        ),
        Spacer(1, 8),
    ]

    data = [
        [
            para("<b>What it assesses</b>", styles["Small"]),
            para("Business impact, delivery feasibility, responsible AI / operational risk, and adoption readiness.", styles["Small"]),
        ],
        [
            para("<b>What it generates</b>", styles["Small"]),
            para("Stage-gate recommendation, four-week PoC plan, controls, success metrics, adoption materials, executive summary, and LLM prompt pack.", styles["Small"]),
        ],
        [
            para("<b>Why it matters</b>", styles["Small"]),
            para("AI ideas often fail between prototype and adoption. This tool makes the decision process explicit, measurable, and safer for regulated business settings.", styles["Small"]),
        ],
    ]
    table = Table(data, colWidths=[1.55 * inch, 5.3 * inch])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#f8fafc")),
                ("BOX", (0, 0), (-1, -1), 0.6, colors.HexColor("#d0d5dd")),
                ("INNERGRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#e4e7ec")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 7),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
            ]
        )
    )
    story += [table, Spacer(1, 10)]

    story += [
        para("Product Flow", styles["Section"]),
        para(
            "1. Define the use case, target users, workflow and data types. 2. Score impact, feasibility, risk and adoption. 3. Receive a stage-gate recommendation: fast-track controlled PoC, controlled pilot with governance gate, pre-PoC discovery, or backlog. 4. Generate the PoC plan, controls, measurement plan and communication prompts.",
            styles["BodyClean"],
        ),
        para("Why this fits Computershare", styles["Section"]),
        para(
            "Computershare's AI insights emphasise reusable frameworks, short low-risk experimentation, leadership alignment, responsible AI, clear success measures, training, and a 'test, measure, analyse and repeat' approach. This prototype follows that mindset: it turns promising AI ideas into governed PoCs with explicit value, feasibility, controls, adoption needs and measurement before scale.",
            styles["BodyClean"],
        ),
        para("Example Use Cases", styles["Section"]),
        para(
            "The prototype includes sample scenarios relevant to financial administration: Copilot-assisted shareholder query summaries, corporate-actions obligation extraction, employee share-plan FAQ support, and internal AI adoption reporting.",
            styles["BodyClean"],
        ),
        para("AI Usage Demonstrated", styles["Section"]),
        para(
            "The app demonstrates AI-assisted product development, prompt design, structured scoring, risk-aware workflow design, and non-technical communication. It treats AI as a tool inside a controlled business process rather than an unchecked answer generator.",
            styles["BodyClean"],
        ),
        para("Technical Components", styles["Section"]),
        para(
            "Standalone HTML/JavaScript app for easy review, Python scoring engine for reusable logic, optional Streamlit app for deployment, JSON sample cases, and an application note explaining the design choices.",
            styles["BodyClean"],
        ),
        para("How I would extend it", styles["Section"]),
        para(
            "With enterprise access, I would connect it to approved Copilot/LLM tooling, add authentication, maintain an AI use-case register, log reviewer decisions, and connect adoption metrics to internal reporting dashboards.",
            styles["BodyClean"],
        ),
    ]

    doc.build(story)


if __name__ == "__main__":
    build_pdf()
