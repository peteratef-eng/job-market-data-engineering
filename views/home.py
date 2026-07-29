from __future__ import annotations

import base64
import html
from pathlib import Path

import streamlit as st

from dashboard.data_loader import load_dashboard_data, load_dashboard_metadata
from dashboard.transformations import remote_salary, salary_coverage, top_skills
from portfolio.content.profile import PROFILE
from portfolio.content.projects import PROJECTS
from portfolio.content.skills import SKILL_GROUPS
from ui.components import footer
from ui.styles import inject_global_styles
from ui.theme import current_theme


theme = current_theme()
inject_global_styles(theme)

ROOT = Path(__file__).resolve().parents[1]
HERO_PHOTO_PATH = ROOT / "assets" / "profile" / "peter-atef-hero.jpg"
PROJECT_PREVIEW_PATH = ROOT / "images" / "dbt_lineage.png"
RESUME_PATH = ROOT / PROFILE["resume_path"]


def asset_data_uri(path: Path, mime_type: str) -> str:
    if not path.exists():
        return ""
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime_type};base64,{encoded}"


def format_int(value: int | str | None) -> str:
    return f"{value:,}" if isinstance(value, int) else html.escape(str(value or "Verified"))


project = PROJECTS[0]
metadata = load_dashboard_metadata()
source_rows = metadata.get("source_job_postings_rows")
sample_rows = metadata.get("sample_job_postings_rows")
sample_skill_rows = metadata.get("sample_job_skills_rows")

try:
    jobs, skills, _ = load_dashboard_data()
    salary_label, salary_records, total_records = salary_coverage(jobs)
    remote_salary_data = remote_salary(jobs).set_index("remote_status")
    remote_avg = int(remote_salary_data.loc["Remote", "avg_salary"]) if "Remote" in remote_salary_data.index else None
    onsite_avg = int(remote_salary_data.loc["Onsite", "avg_salary"]) if "Onsite" in remote_salary_data.index else None
    top_skill_rows = top_skills(skills, 4)
    python_postings = int(top_skill_rows.loc[top_skill_rows["clean_skill_name"].eq("python"), "postings"].iloc[0])
    sql_postings = int(top_skill_rows.loc[top_skill_rows["clean_skill_name"].eq("sql"), "postings"].iloc[0])
    aws_postings = int(top_skill_rows.loc[top_skill_rows["clean_skill_name"].eq("aws"), "postings"].iloc[0])
    azure_postings = int(top_skill_rows.loc[top_skill_rows["clean_skill_name"].eq("azure"), "postings"].iloc[0])
    unique_skills = int(skills["clean_skill_name"].dropna().nunique())
except Exception:
    salary_label = "Verified"
    salary_records = None
    total_records = sample_rows
    remote_avg = None
    onsite_avg = None
    python_postings = None
    sql_postings = None
    aws_postings = None
    azure_postings = None
    unique_skills = None

preview_image = asset_data_uri(PROJECT_PREVIEW_PATH, "image/png")
resume_href = asset_data_uri(RESUME_PATH, "application/pdf")
resume_attr = ' download="Peter_Atef_Resume_2026.pdf"' if resume_href else ""
resume_link = resume_href or html.escape(PROFILE["resume_path"])
tech_stack = " - ".join(project["technologies"][:6])
hero_photo_src = asset_data_uri(HERO_PHOTO_PATH, "image/jpeg")
hero_photo_markup = (
    f'<img class="profile-terminal-photo" src="{hero_photo_src}" alt="Portrait of Peter Atef, Junior Data Engineer">'
    if hero_photo_src
    else '<div class="hero-photo-fallback" aria-label="Peter Atef portrait">PA</div>'
)

skill_pipeline_steps = [
    ("ETL Pipelines", "Flow"),
    ("Python / Pandas", "Clean"),
    ("SQL / PostgreSQL", "Store"),
    ("dbt", "Model"),
    ("Analytics-Ready Data", "Deliver"),
]
skill_pipeline_markup = ""
for index, (label, detail) in enumerate(skill_pipeline_steps, start=1):
    skill_pipeline_markup += (
        f'<div class="hero-skill-node hero-skill-node-{index}" tabindex="0">'
        f'<span>{html.escape(label)}</span>'
        f'<small>{html.escape(detail)}</small>'
        '</div>'
    )
    if index < len(skill_pipeline_steps):
        skill_pipeline_markup += f'<div class="hero-skill-connector hero-skill-connector-{index}" aria-hidden="true"></div>'

proof_items = [
    ("Source Job Postings", format_int(source_rows)),
    ("Hosted Sample", format_int(sample_rows)),
    ("Job-Skill Rows", format_int(sample_skill_rows)),
    ("Distinct Skills", format_int(unique_skills)),
]
proof_markup = "".join(
    (
        f'<div class="proof-console-item proof-console-item-{index}">'
        f'<div class="proof-console-value">{value}</div>'
        f'<div class="proof-console-label">{html.escape(label)}</div>'
        '</div>'
    )
    for index, (label, value) in enumerate(proof_items, start=1)
)

divider_steps = ["Raw Job Data", "Python/Pandas", "PostgreSQL", "dbt Models", "Data Quality", "Market Dashboard"]
divider_markup = ""
for index, label in enumerate(divider_steps, start=1):
    divider_markup += f'<span class="hero-pipeline-stage hero-pipeline-stage-{index}">{html.escape(label)}</span>'
    if index < len(divider_steps):
        divider_markup += f'<span class="hero-pipeline-connector hero-pipeline-connector-{index}" aria-hidden="true"></span>'

st.markdown(
    f"""
    <section class="portfolio-hero data-command-hero">
        <div class="data-blueprint-grid" aria-hidden="true"></div>
        <div class="data-background-path data-background-path-1" aria-hidden="true"></div>
        <div class="data-background-path data-background-path-2" aria-hidden="true"></div>
        <span class="data-background-particle data-background-particle-1" aria-hidden="true"></span>
        <span class="data-background-particle data-background-particle-2" aria-hidden="true"></span>
        <div class="hero-copy">
            <div class="hero-kicker">Hi, I'm Peter Atef</div>
            <h1>Junior Data Engineer</h1>
            <p>I build reliable data pipelines and transform raw, messy data into analytics-ready insights using Python, SQL, PostgreSQL, and dbt.</p>
            <div class="hero-value-rotator" aria-hidden="true">
                <span class="hero-value-line hero-value-line-1">Building Reliable Pipelines</span>
                <span class="hero-value-line hero-value-line-2">Transforming Messy Data</span>
                <span class="hero-value-line hero-value-line-3">Validating Trusted Models</span>
                <span class="hero-value-line hero-value-line-4">Delivering Analytics-Ready Insights</span>
            </div>
            <span class="hero-value-accessible-summary sr-only">Building reliable pipelines, transforming messy data, validating trusted models, and delivering analytics-ready insights.</span>
            <div class="hero-actions">
                <a class="portfolio-button portfolio-button-primary hero-primary-action" href="/project_overview">EXPLORE MY PROJECT<span aria-hidden="true">-&gt;</span></a>
                <a class="portfolio-button" href="{resume_link}"{resume_attr}>DOWNLOAD RESUME</a>
                <a class="portfolio-button portfolio-button-quiet" href="/contact">CONTACT ME</a>
            </div>
            <div class="hero-skill-pipeline" aria-label="Skills pipeline from ETL pipelines to analytics-ready data">
                <span class="hero-skill-packet hero-skill-packet-1" aria-hidden="true"></span>
                <span class="hero-skill-packet hero-skill-packet-2" aria-hidden="true"></span>
                {skill_pipeline_markup}
            </div>
        </div>
        <div class="profile-terminal">
            <div class="profile-terminal-label">PROFILE_01</div>
            <div class="profile-terminal-frame">
                <span class="profile-corner profile-corner-tl" aria-hidden="true"></span>
                <span class="profile-corner profile-corner-tr" aria-hidden="true"></span>
                <span class="profile-corner profile-corner-bl" aria-hidden="true"></span>
                <span class="profile-corner profile-corner-br" aria-hidden="true"></span>
                {hero_photo_markup}
            </div>
            <div class="profile-identity-card" tabindex="0">
                <div class="profile-identity-name">Peter Atef</div>
                <div class="profile-identity-role">Junior Data Engineer</div>
                <div class="profile-availability"><span class="profile-status-dot"></span>Open to Junior Data Engineer Opportunities</div>
                <div class="profile-identity-location">{html.escape(PROFILE["location"])}</div>
            </div>
        </div>
    </section>
    <section class="project-proof-console" aria-label="Project evidence">
        <div class="proof-console-status">PROJECT EVIDENCE</div>
        <div class="proof-console-grid">{proof_markup}</div>
    </section>
    <section class="hero-pipeline-divider" aria-label="Raw job data moves through Python and Pandas, PostgreSQL, dbt models, data quality, and the Market Dashboard">
        <span class="hero-pipeline-packet hero-pipeline-packet-1" aria-hidden="true"></span>
        <span class="hero-pipeline-packet hero-pipeline-packet-2" aria-hidden="true"></span>
        <div class="hero-pipeline-track">{divider_markup}</div>
    </section>
    """,
    unsafe_allow_html=True,
)

about_cards = [
    (
        "Professional Story",
        "After working across AI, NLP, data annotation leadership, quality assurance, and integration workflows, I moved deeper into Data Engineering. I enjoy building reliable pipelines, cleaning messy data, validating outputs, and turning raw records into analytics-ready models that teams can trust.",
    ),
    (
        "Current Focus",
        "I am targeting Junior Data Engineer opportunities where I can build dependable pipelines, improve data quality, and create models that make analysis easier for teams.",
    ),
]
about_markup = "".join(
    (
        '<div class="section-card home-about-card" tabindex="0">'
        f'<div class="section-title">{html.escape(title)}</div>'
        f'<div class="section-copy">{html.escape(body)}</div>'
        '</div>'
    )
    for title, body in about_cards
)
st.markdown(
    f"""
    <section class="home-section home-about-section">
        <div class="section-eyebrow">Professional Profile</div>
        <h2>About Me</h2>
        <div class="home-about-grid">{about_markup}</div>
    </section>
    """,
    unsafe_allow_html=True,
)

skills_markup = "".join(
    (
        '<div class="section-card home-skill-card" tabindex="0">'
        f'<div class="section-title">{html.escape(title)}</div>'
        '<div class="home-skill-badge-wrap">'
        + "".join(f'<span class="home-skill-badge">{html.escape(skill)}</span>' for skill in skills)
        + '</div>'
        '</div>'
    )
    for title, skills in SKILL_GROUPS.items()
)
st.markdown(
    f"""
    <section class="home-section home-skills-section">
        <div class="section-eyebrow">Workflow Skills</div>
        <h2>Skills</h2>
        <p class="home-section-copy">Grouped by the data engineering workflow areas demonstrated across my project and professional background.</p>
        <div class="home-skills-grid">{skills_markup}</div>
    </section>
    """,
    unsafe_allow_html=True,
)

live_pipeline_steps = [
    ("Raw Job Data", "Source job postings and skill relationships.", "DB"),
    ("Python Cleaning", "Normalize fields and prepare reliable records.", "PY"),
    ("PostgreSQL", "Store structured, query-ready data.", "SQL"),
    ("dbt Models", "Build staging and analytical marts.", "dbt"),
    ("Data Quality", "Validate relationships, calculations, and outputs.", "QA"),
    ("Market Dashboard", "Deliver trusted insights for interactive analysis.", "UI"),
]
live_pipeline_markup = ""
for index, (title, body, icon) in enumerate(live_pipeline_steps, start=1):
    live_pipeline_markup += (
        f'<div class="home-pipeline-stage pipeline-stage-{index}" tabindex="0">'
        '<div class="home-pipeline-stage-inner">'
        f'<div class="home-pipeline-icon">{html.escape(icon)}</div>'
        f'<div class="home-pipeline-stage-name">{html.escape(title)}</div>'
        f'<div class="home-pipeline-stage-copy">{html.escape(body)}</div>'
        '</div>'
        '</div>'
    )
    if index < len(live_pipeline_steps):
        live_pipeline_markup += (
            f'<div class="home-pipeline-connector pipeline-connector-{index}" aria-hidden="true">'
            '<span class="home-pipeline-particle"></span>'
            '<span class="home-pipeline-particle home-pipeline-particle-2"></span>'
            '<span class="home-pipeline-particle home-pipeline-particle-3"></span>'
            '</div>'
        )

st.markdown(
    f"""
    <section class="home-section home-pipeline-section">
        <div class="section-eyebrow">Data Pipeline</div>
        <h2>From Raw Data to Reliable Insights</h2>
        <p class="home-section-copy">A visual overview of how raw job-market records are cleaned, modeled, validated, and delivered for analysis.</p>
        <div class="home-pipeline-track" aria-label="Data pipeline flow">
            {live_pipeline_markup}
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)

repository_button = (
    f'<a class="portfolio-button" href="{html.escape(project["repository_url"])}" target="_blank" rel="noopener noreferrer">VIEW ON GITHUB</a>'
    if project.get("repository_url")
    else ""
)
preview_markup = (
    f'<img src="{preview_image}" alt="dbt lineage screenshot for the Job Market Intelligence project">'
    if preview_image
    else '<div class="featured-preview-fallback">dbt lineage preview</div>'
)
st.markdown(
    f"""
    <section class="featured-project-card" tabindex="0">
        <div class="featured-project-copy">
            <div class="section-eyebrow">Featured Project</div>
            <h2>{html.escape(project["title"])}</h2>
            <p>{html.escape(project["case_study_sections"]["Business problem"])}</p>
            <p>{html.escape(project["case_study_sections"]["Project summary"])}</p>
            <div class="featured-meta">
                <span>{html.escape(tech_stack)}</span>
                <span>{format_int(source_rows)} source postings</span>
                <span>{format_int(sample_rows)} hosted records</span>
            </div>
            <div class="hero-actions">
                <a class="portfolio-button portfolio-button-primary" href="/market_dashboard">VIEW LIVE PROJECT</a>
                {repository_button}
            </div>
        </div>
        <div class="featured-preview">
            {preview_markup}
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)

pipeline_steps = [
    ("Raw Job Data", "CSV source tables for postings, companies, skills, and job-skill relationships."),
    ("Python Cleaning", "Pandas prepares the hosted sample and normalized dashboard-ready files."),
    ("PostgreSQL", "Relational warehouse tables support structured modeling work."),
    ("dbt Models", "Staging, intermediate, and mart models organize analysis-ready data."),
    ("Data Quality", "SQL checks validate counts, keys, joins, duplicates, and calculations."),
    ("Market Dashboard", "Streamlit presents KPIs, filters, and project insights for review."),
]
pipeline_markup = "".join(
    (
        '<div class="pipeline-step-card" tabindex="0">'
        f'<div class="pipeline-step-name">{html.escape(title)}</div>'
        f'<div class="section-copy">{html.escape(body)}</div>'
        '</div>'
    )
    for title, body in pipeline_steps
)
st.markdown(
    f"""
    <section class="home-section">
        <div class="section-eyebrow">Project Journey</div>
        <h2>From Raw Records to Market Intelligence</h2>
        <div class="pipeline-step-grid">{pipeline_markup}</div>
    </section>
    """,
    unsafe_allow_html=True,
)

remote_text = (
    f"Remote roles average ${remote_avg:,} versus ${onsite_avg:,} onsite among salary-covered records."
    if remote_avg and onsite_avg
    else "Remote and onsite salary comparisons are available where salary data exists."
)
skills_text = (
    f"Python appears in {python_postings:,} postings and SQL appears in {sql_postings:,} postings in the hosted sample."
    if python_postings and sql_postings
    else "Python and SQL are core demand signals in the hosted skill sample."
)
cloud_text = (
    f"AWS appears in {aws_postings:,} postings and Azure appears in {azure_postings:,} postings in the hosted sample."
    if aws_postings and azure_postings
    else "Cloud platforms are tracked as part of the technical skill demand model."
)
insight_cards = [
    ("Remote Salary Signal", remote_text, f"Salary coverage: {salary_label} ({salary_records:,} of {total_records:,} records)." if salary_records and total_records else "Salary coverage is tracked in the dashboard."),
    ("Python and SQL Demand", skills_text, "These are the top two skills in the hosted skill-demand sample."),
    ("Cloud Skill Demand", cloud_text, "Cloud skills are modeled from unique posting-skill relationships."),
]
insight_markup = "".join(
    (
        '<div class="insight-card" tabindex="0">'
        f'<div class="section-title">{html.escape(title)}</div>'
        f'<div class="section-copy">{html.escape(body)}</div>'
        f'<div class="evidence-note">{html.escape(note)}</div>'
        '</div>'
    )
    for title, body, note in insight_cards
)
st.markdown(
    f"""
    <section class="home-section">
        <div class="section-eyebrow">Verified Insights</div>
        <h2>Signals Already Backed by the Data</h2>
        <div class="insight-card-grid">{insight_markup}</div>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <section class="contact-cta">
        <div>
            <div class="section-eyebrow">Contact</div>
            <h2>Let's Build Something Reliable</h2>
            <p>I'm open to Junior Data Engineer opportunities where I can build dependable pipelines, improve data quality, and make analytics easier for teams.</p>
        </div>
        <div class="contact-cta-actions">
            <a class="portfolio-button portfolio-button-primary" href="{html.escape(PROFILE["mailto_url"])}">Email</a>
            <a class="portfolio-button" href="{html.escape(PROFILE["linkedin_url"])}" target="_blank" rel="noopener noreferrer">LinkedIn</a>
            <a class="portfolio-button" href="{html.escape(PROFILE["github_url"])}" target="_blank" rel="noopener noreferrer">GitHub</a>
            <a class="portfolio-button" href="{resume_link}"{resume_attr}>Resume</a>
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)

footer()
