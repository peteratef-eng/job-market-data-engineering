from __future__ import annotations

import base64
import html
from pathlib import Path
from textwrap import dedent

import streamlit as st

from dashboard.data_loader import load_dashboard_metadata
from portfolio.content.profile import PROFILE
from portfolio.content.projects import PROJECTS
from portfolio.content.skills import SKILL_GROUPS
from ui.styles import inject_global_styles
from ui.theme import current_theme


theme = current_theme()
inject_global_styles(theme)

ROOT = Path(__file__).resolve().parents[1]
HERO_PHOTO_PATH = ROOT / "assets" / "profile" / "peter-atef-hero.jpg"
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

resume_href = asset_data_uri(RESUME_PATH, "application/pdf")
resume_attr = ' download="Peter_Atef_Resume_2026.pdf"' if resume_href else ""
resume_link = resume_href or html.escape(PROFILE["resume_path"])
tech_stack = " - ".join(project["technologies"][:6])
hero_photo_src = asset_data_uri(HERO_PHOTO_PATH, "image/jpeg")
hero_photo_markup = (
    f'<img class="hero-profile-image" src="{hero_photo_src}" alt="Portrait of Peter Atef, Junior Data Engineer">'
    if hero_photo_src
    else '<div class="hero-photo-fallback" aria-label="Peter Atef portrait">PA</div>'
)

skill_pipeline_steps = [
    ("DATA SOURCES", "Files / APIs"),
    ("INGEST & PROCESS", "Python / Pandas"),
    ("STORE", "SQL / PostgreSQL"),
    ("TRANSFORM & MODEL", "dbt"),
    ("VALIDATE", "Data Quality"),
    ("DELIVER", "Analytics-Ready Data"),
]
skill_pipeline_markup = (
    '<span class="sr-only">Core Data Engineering workflow: Airflow orchestrates data ingestion from files and APIs, processing with Python and Pandas, storage in SQL and PostgreSQL, transformation with dbt, data-quality validation, and delivery of analytics-ready data.</span>'
    '<div class="core-workflow-orchestrator" aria-hidden="true">'
    '<span class="core-workflow-orchestrator-icon"></span>'
    '<span class="core-workflow-orchestrator-label"><strong>AIRFLOW</strong><small>Pipeline Orchestration</small></span>'
    '<span class="core-workflow-orchestrator-pulse"></span>'
    '</div>'
    '<span class="core-workflow-control-line core-workflow-control-line-1" aria-hidden="true"></span>'
    '<span class="core-workflow-control-line core-workflow-control-line-2" aria-hidden="true"></span>'
    '<span class="core-workflow-control-line core-workflow-control-line-3" aria-hidden="true"></span>'
    '<span class="hero-skill-rail" aria-hidden="true"></span>'
    '<span class="hero-skill-packet-track" aria-hidden="true">'
    '<span class="hero-skill-packet"></span>'
    '<span class="hero-skill-packet hero-skill-packet-secondary"></span>'
    '</span>'
)
for index, (stage, label) in enumerate(skill_pipeline_steps, start=1):
    input_port = '<span class="hero-skill-port hero-skill-port-in" aria-hidden="true"></span>' if index > 1 else ""
    output_port = '<span class="hero-skill-port hero-skill-port-out" aria-hidden="true"></span>' if index < len(skill_pipeline_steps) else ""
    skill_pipeline_markup += (
        f'<span class="hero-skill-node hero-skill-node-{index}">'
        f'{input_port}<span class="hero-skill-node-content">'
        f'<span class="core-workflow-stage">{html.escape(stage)}</span>'
        f'<strong class="core-workflow-tool">{html.escape(label)}</strong>'
        f'</span>{output_port}'
        '</span>'
    )

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
            <p class="hero-description">I build reliable data pipelines and transform raw, messy data into analytics-ready insights using Python, SQL, PostgreSQL, and dbt.</p>
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
        </div>
        <article class="hero-profile-card">
            <div class="hero-profile-media">
                <div class="hero-profile-image-wrap">
                    {hero_photo_markup}
                </div>
            </div>
            <div class="hero-profile-identity hero-profile-info">
                <div class="hero-profile-heading">
                    <h2 class="hero-profile-name">Peter Atef</h2>
                    <p class="hero-profile-role">Junior Data Engineer</p>
                </div>
                <div class="hero-profile-meta">
                    <span class="hero-profile-status">
                        <span class="hero-profile-status-dot" aria-hidden="true"></span>
                        Open to opportunities
                    </span>
                    <span class="hero-profile-location">
                        {html.escape(PROFILE["location"])}
                    </span>
                </div>
            </div>
        </article>
        <div class="hero-skill-section">
            <div class="hero-skill-label">CORE DATA ENGINEERING WORKFLOW</div>
            <div class="hero-skill-pipeline" aria-label="Core Data Engineering workflow: Airflow orchestrates data ingestion from files and APIs, processing with Python and Pandas, storage in SQL and PostgreSQL, transformation with dbt, data-quality validation, and delivery of analytics-ready data.">
                {skill_pipeline_markup}
            </div>
        </div>
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
        f'<div class="section-card home-skill-card home-skill-card-{index}" tabindex="0">'
        f'<div class="section-title">{html.escape(title)}</div>'
        '<div class="home-skill-badge-wrap">'
        + "".join(f'<span class="home-skill-badge">{html.escape(skill)}</span>' for skill in skills)
        + '</div>'
        '</div>'
    )
    for index, (title, skills) in enumerate(SKILL_GROUPS.items(), start=1)
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

repository_button = (
    f'<a class="portfolio-button" href="{html.escape(project["repository_url"])}" rel="noopener noreferrer">VIEW ON GITHUB</a>'
    if project.get("repository_url")
    else ""
)
preview_markup = dedent(
    """
    <div class="featured-lineage-preview" aria-label="Unified data lineage: staging company and job-posting models feed an enriched job-postings model and four analytics marts; staging job-skill and skill models feed an enriched skills model and the skill-demand mart.">
        <div class="featured-lineage-header">
            <span>Live Data Lineage</span>
            <small><span aria-hidden="true"></span>dbt models connected</small>
        </div>
        <div class="featured-lineage-canvas">
            <svg class="featured-lineage-svg" viewBox="0 0 1000 640" preserveAspectRatio="none" aria-hidden="true">
                <defs>
                    <linearGradient id="featuredLineageFlowGradient" x1="0%" y1="0%" x2="100%" y2="0%">
                        <stop offset="0%" stop-color="#2563eb"></stop>
                        <stop offset="100%" stop-color="#06b6d4"></stop>
                    </linearGradient>
                    <marker id="featured-lineage-arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
                        <path d="M0,0 L8,4 L0,8 Z"></path>
                    </marker>
                </defs>
                <path class="featured-lineage-connector" d="M280 105 C310 105 292 155 310 155"></path>
                <path class="featured-lineage-connector" d="M280 190 C306 190 294 155 310 155"></path>
                <path class="featured-lineage-connector" d="M280 355 C310 355 292 405 310 405"></path>
                <path class="featured-lineage-connector" d="M280 440 C306 440 294 405 310 405"></path>
                <path class="featured-lineage-connector" d="M610 155 C638 120 620 80 640 80"></path>
                <path class="featured-lineage-connector" d="M610 155 C632 155 624 165 640 165"></path>
                <path class="featured-lineage-connector" d="M610 155 C632 190 624 250 640 250"></path>
                <path class="featured-lineage-connector" d="M610 155 C632 225 624 335 640 335"></path>
                <path class="featured-lineage-connector" d="M610 405 C632 405 624 480 640 480"></path>
                <path id="featured-lineage-job-route" class="featured-lineage-route" d="M280 190 C306 190 294 155 310 155 C430 155 520 155 610 155 C632 190 624 250 640 250"></path>
                <path id="featured-lineage-skill-route" class="featured-lineage-route featured-lineage-route-skill" d="M280 440 C306 440 294 405 310 405 C430 405 520 405 610 405 C632 405 624 480 640 480"></path>
                <circle class="featured-lineage-packet featured-lineage-packet-job" r="5">
                    <animateMotion dur="10s" repeatCount="indefinite" calcMode="paced">
                        <mpath href="#featured-lineage-job-route"></mpath>
                    </animateMotion>
                </circle>
                <circle class="featured-lineage-packet featured-lineage-packet-skill" r="5">
                    <animateMotion dur="10s" begin="5s" repeatCount="indefinite" calcMode="paced">
                        <mpath href="#featured-lineage-skill-route"></mpath>
                    </animateMotion>
                </circle>
            </svg>
            <div class="featured-lineage-column featured-lineage-column-staging">
                <div class="featured-lineage-column-title">Staging</div>
                <div class="featured-lineage-node featured-lineage-node-staging featured-lineage-node-job-source" title="stg_companies" aria-label="stg_companies, staging model"><span class="featured-lineage-node-icon" aria-hidden="true"></span><span class="featured-lineage-model-name">stg_companies</span><small class="featured-lineage-model-type">STAGING MODEL</small></div>
                <div class="featured-lineage-node featured-lineage-node-staging featured-lineage-node-job-source" title="stg_job_postings" aria-label="stg_job_postings, staging model"><span class="featured-lineage-node-icon" aria-hidden="true"></span><span class="featured-lineage-model-name">stg_job_postings</span><small class="featured-lineage-model-type">STAGING MODEL</small></div>
                <div class="featured-lineage-node featured-lineage-node-staging featured-lineage-node-skill-source" title="stg_job_skills" aria-label="stg_job_skills, staging model"><span class="featured-lineage-node-icon" aria-hidden="true"></span><span class="featured-lineage-model-name">stg_job_skills</span><small class="featured-lineage-model-type">STAGING MODEL</small></div>
                <div class="featured-lineage-node featured-lineage-node-staging featured-lineage-node-skill-source" title="stg_skills" aria-label="stg_skills, staging model"><span class="featured-lineage-node-icon" aria-hidden="true"></span><span class="featured-lineage-model-name">stg_skills</span><small class="featured-lineage-model-type">STAGING MODEL</small></div>
            </div>
            <div class="featured-lineage-column featured-lineage-column-intermediate">
                <div class="featured-lineage-column-title">Intermediate</div>
                <div class="featured-lineage-node featured-lineage-node-intermediate featured-lineage-node-job-intermediate" title="int_job_postings_enriched" aria-label="int_job_postings_enriched, intermediate model"><span class="featured-lineage-node-icon" aria-hidden="true"></span><span class="featured-lineage-model-name">int_job_postings_<br>enriched</span><small class="featured-lineage-model-type">INTERMEDIATE MODEL</small></div>
                <div class="featured-lineage-node featured-lineage-node-intermediate featured-lineage-node-skill-intermediate" title="int_job_skills_enriched" aria-label="int_job_skills_enriched, intermediate model"><span class="featured-lineage-node-icon" aria-hidden="true"></span><span class="featured-lineage-model-name">int_job_skills_<br>enriched</span><small class="featured-lineage-model-type">INTERMEDIATE MODEL</small></div>
            </div>
            <div class="featured-lineage-column featured-lineage-column-mart">
                <div class="featured-lineage-column-title">Marts</div>
                <div class="featured-lineage-node featured-lineage-node-mart featured-lineage-node-job-mart" title="mart_company_leaderboard" aria-label="mart_company_leaderboard, mart model"><span class="featured-lineage-node-icon" aria-hidden="true"></span><span class="featured-lineage-model-name">mart_company_<br>leaderboard</span><small class="featured-lineage-model-type">MART MODEL</small></div>
                <div class="featured-lineage-node featured-lineage-node-mart featured-lineage-node-job-mart" title="mart_monthly_job_trends" aria-label="mart_monthly_job_trends, mart model"><span class="featured-lineage-node-icon" aria-hidden="true"></span><span class="featured-lineage-model-name">mart_monthly_<br>job_trends</span><small class="featured-lineage-model-type">MART MODEL</small></div>
                <div class="featured-lineage-node featured-lineage-node-mart featured-lineage-node-job-mart" title="mart_remote_work_trends" aria-label="mart_remote_work_trends, mart model"><span class="featured-lineage-node-icon" aria-hidden="true"></span><span class="featured-lineage-model-name">mart_remote_<br>work_trends</span><small class="featured-lineage-model-type">MART MODEL</small></div>
                <div class="featured-lineage-node featured-lineage-node-mart featured-lineage-node-job-mart" title="mart_salary_trends" aria-label="mart_salary_trends, mart model"><span class="featured-lineage-node-icon" aria-hidden="true"></span><span class="featured-lineage-model-name">mart_salary_<br>trends</span><small class="featured-lineage-model-type">MART MODEL</small></div>
                <div class="featured-lineage-node featured-lineage-node-mart featured-lineage-node-skill-mart" title="mart_skill_demand_by_role" aria-label="mart_skill_demand_by_role, mart model"><span class="featured-lineage-node-icon" aria-hidden="true"></span><span class="featured-lineage-model-name">mart_skill_demand_<br>by_role</span><small class="featured-lineage-model-type">MART MODEL</small></div>
            </div>
            <div class="featured-lineage-mobile-flows" aria-hidden="true">
                <div class="featured-lineage-mobile-flow featured-lineage-mobile-flow-job">
                    <div class="featured-lineage-mobile-title">Job Postings Lineage</div>
                    <div class="featured-lineage-mobile-group">
                        <div class="featured-lineage-mobile-group-label">Sources</div>
                        <div class="featured-lineage-node featured-lineage-node-staging featured-lineage-node-job-source" title="stg_companies"><span class="featured-lineage-node-icon" aria-hidden="true"></span><span class="featured-lineage-model-name">stg_companies</span><small class="featured-lineage-model-type">STAGING MODEL</small></div>
                        <div class="featured-lineage-node featured-lineage-node-staging featured-lineage-node-job-source" title="stg_job_postings"><span class="featured-lineage-node-icon" aria-hidden="true"></span><span class="featured-lineage-model-name">stg_job_postings</span><small class="featured-lineage-model-type">STAGING MODEL</small></div>
                    </div>
                    <div class="featured-lineage-mobile-connector"><span></span></div>
                    <div class="featured-lineage-node featured-lineage-node-intermediate featured-lineage-node-job-intermediate" title="int_job_postings_enriched"><span class="featured-lineage-node-icon" aria-hidden="true"></span><span class="featured-lineage-model-name">int_job_postings_<br>enriched</span><small class="featured-lineage-model-type">INTERMEDIATE MODEL</small></div>
                    <div class="featured-lineage-mobile-connector"><span></span></div>
                    <div class="featured-lineage-mobile-group">
                        <div class="featured-lineage-mobile-group-label">Marts</div>
                        <div class="featured-lineage-node featured-lineage-node-mart featured-lineage-node-job-mart" title="mart_company_leaderboard"><span class="featured-lineage-node-icon" aria-hidden="true"></span><span class="featured-lineage-model-name">mart_company_<br>leaderboard</span><small class="featured-lineage-model-type">MART MODEL</small></div>
                        <div class="featured-lineage-node featured-lineage-node-mart featured-lineage-node-job-mart" title="mart_monthly_job_trends"><span class="featured-lineage-node-icon" aria-hidden="true"></span><span class="featured-lineage-model-name">mart_monthly_<br>job_trends</span><small class="featured-lineage-model-type">MART MODEL</small></div>
                        <div class="featured-lineage-node featured-lineage-node-mart featured-lineage-node-job-mart" title="mart_remote_work_trends"><span class="featured-lineage-node-icon" aria-hidden="true"></span><span class="featured-lineage-model-name">mart_remote_<br>work_trends</span><small class="featured-lineage-model-type">MART MODEL</small></div>
                        <div class="featured-lineage-node featured-lineage-node-mart featured-lineage-node-job-mart" title="mart_salary_trends"><span class="featured-lineage-node-icon" aria-hidden="true"></span><span class="featured-lineage-model-name">mart_salary_<br>trends</span><small class="featured-lineage-model-type">MART MODEL</small></div>
                    </div>
                </div>
                <div class="featured-lineage-mobile-flow featured-lineage-mobile-flow-skill">
                    <div class="featured-lineage-mobile-title">Skills Lineage</div>
                    <div class="featured-lineage-mobile-group">
                        <div class="featured-lineage-mobile-group-label">Sources</div>
                        <div class="featured-lineage-node featured-lineage-node-staging featured-lineage-node-skill-source" title="stg_job_skills"><span class="featured-lineage-node-icon" aria-hidden="true"></span><span class="featured-lineage-model-name">stg_job_skills</span><small class="featured-lineage-model-type">STAGING MODEL</small></div>
                        <div class="featured-lineage-node featured-lineage-node-staging featured-lineage-node-skill-source" title="stg_skills"><span class="featured-lineage-node-icon" aria-hidden="true"></span><span class="featured-lineage-model-name">stg_skills</span><small class="featured-lineage-model-type">STAGING MODEL</small></div>
                    </div>
                    <div class="featured-lineage-mobile-connector"><span></span></div>
                    <div class="featured-lineage-node featured-lineage-node-intermediate featured-lineage-node-skill-intermediate" title="int_job_skills_enriched"><span class="featured-lineage-node-icon" aria-hidden="true"></span><span class="featured-lineage-model-name">int_job_skills_<br>enriched</span><small class="featured-lineage-model-type">INTERMEDIATE MODEL</small></div>
                    <div class="featured-lineage-mobile-connector"><span></span></div>
                    <div class="featured-lineage-node featured-lineage-node-mart featured-lineage-node-skill-mart" title="mart_skill_demand_by_role"><span class="featured-lineage-node-icon" aria-hidden="true"></span><span class="featured-lineage-model-name">mart_skill_demand_<br>by_role</span><small class="featured-lineage-model-type">MART MODEL</small></div>
                </div>
            </div>
        </div>
    </div>
    """
).strip()
featured_project_markup = dedent(
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
    """
).strip()
st.markdown(featured_project_markup, unsafe_allow_html=True)

st.markdown(
    f"""
    <section class="contact-cta home-contact-cta">
        <div>
            <p>Open to Junior Data Engineer opportunities.</p>
        </div>
        <div class="contact-cta-actions">
            <a class="portfolio-button portfolio-button-primary" href="/contact">CONTACT ME</a>
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)
