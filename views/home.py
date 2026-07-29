from __future__ import annotations

import base64
import html
from pathlib import Path

import streamlit as st

from dashboard.data_loader import load_dashboard_data, load_dashboard_metadata
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
sample_rows = metadata.get("sample_job_postings_rows")
sample_skill_rows = metadata.get("sample_job_skills_rows")

try:
    jobs, skills, _ = load_dashboard_data()
    unique_skills = int(skills["clean_skill_name"].dropna().nunique())
except Exception:
    unique_skills = None

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

skill_pipeline_steps = ["ETL Pipelines", "Python / Pandas", "SQL / PostgreSQL", "dbt", "Analytics-Ready Data"]
skill_pipeline_markup = (
    '<span class="hero-skill-rail" aria-hidden="true"></span>'
    '<span class="hero-skill-packet-track" aria-hidden="true">'
    '<span class="hero-skill-packet"></span>'
    '</span>'
)
for index, label in enumerate(skill_pipeline_steps, start=1):
    input_port = '<span class="hero-skill-port hero-skill-port-in" aria-hidden="true"></span>' if index > 1 else ""
    output_port = '<span class="hero-skill-port hero-skill-port-out" aria-hidden="true"></span>' if index < len(skill_pipeline_steps) else ""
    skill_pipeline_markup += (
        f'<span class="hero-skill-node hero-skill-node-{index}">'
        f'{input_port}<span class="hero-skill-node-content">{html.escape(label)}</span>{output_port}'
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
            <div class="hero-skill-pipeline" aria-label="Data Engineering workflow: ingest through ETL pipelines, process with Python and Pandas, store and query with SQL and PostgreSQL, model with dbt, and deliver analytics-ready data.">
                {skill_pipeline_markup}
            </div>
        </div>
        <article class="hero-profile-card">
            <div class="hero-profile-media">
                <div class="hero-profile-image-accent" aria-hidden="true"></div>
                {hero_photo_markup}
            </div>
            <div class="hero-profile-identity">
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
                        <span class="hero-profile-location-icon" aria-hidden="true"></span>
                        {html.escape(PROFILE["location"])}
                    </span>
                </div>
            </div>
        </article>
    </section>
    <section class="project-proof-console" aria-label="Project evidence">
        <div class="proof-console-status">PROJECT EVIDENCE</div>
        <div class="proof-console-grid">{proof_markup}</div>
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
preview_markup = (
    """
    <div class="featured-lineage-preview" aria-label="Data lineage showing staging job and skill models flowing through enriched intermediate models into analytics marts.">
        <div class="featured-lineage-header">
            <span>Live Data Lineage</span>
            <small>dbt models connected</small>
        </div>
        <div class="featured-lineage-canvas">
            <svg class="featured-lineage-svg" viewBox="0 0 640 360" preserveAspectRatio="none" aria-hidden="true">
                <defs>
                    <marker id="featured-lineage-arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
                        <path d="M0,0 L8,4 L0,8 Z"></path>
                    </marker>
                </defs>
                <path class="featured-lineage-connector" d="M128 68 C184 68 202 120 272 120"></path>
                <path class="featured-lineage-connector" d="M128 126 C184 126 202 120 272 120"></path>
                <path class="featured-lineage-connector" d="M128 216 C184 216 202 238 272 238"></path>
                <path class="featured-lineage-connector" d="M128 274 C184 274 202 238 272 238"></path>
                <path class="featured-lineage-connector" d="M368 120 C430 90 452 66 512 66"></path>
                <path class="featured-lineage-connector" d="M368 120 C430 116 452 122 512 122"></path>
                <path class="featured-lineage-connector" d="M368 120 C430 142 452 178 512 178"></path>
                <path class="featured-lineage-connector" d="M368 120 C430 166 452 234 512 234"></path>
                <path class="featured-lineage-connector" d="M368 120 C430 190 452 290 512 290"></path>
                <path class="featured-lineage-connector" d="M368 238 C430 254 452 290 512 290"></path>
                <path id="featured-lineage-job-route" class="featured-lineage-route" d="M128 126 C184 126 202 120 272 120 C348 120 386 154 512 178"></path>
                <path id="featured-lineage-skill-route" class="featured-lineage-route featured-lineage-route-skill" d="M128 274 C184 274 202 238 272 238 C360 238 410 282 512 290"></path>
                <circle class="featured-lineage-packet featured-lineage-packet-job" r="5">
                    <animateMotion dur="6s" repeatCount="indefinite">
                        <mpath href="#featured-lineage-job-route"></mpath>
                    </animateMotion>
                </circle>
                <circle class="featured-lineage-packet featured-lineage-packet-skill" r="5">
                    <animateMotion dur="6s" begin="1.2s" repeatCount="indefinite">
                        <mpath href="#featured-lineage-skill-route"></mpath>
                    </animateMotion>
                </circle>
            </svg>
            <div class="featured-lineage-column featured-lineage-column-staging">
                <div class="featured-lineage-column-title">Staging</div>
                <div class="featured-lineage-node featured-lineage-node-staging featured-lineage-node-job-source"><span class="featured-lineage-node-icon" aria-hidden="true"></span><span>stg_companies</span><small>STAGING MODEL</small></div>
                <div class="featured-lineage-node featured-lineage-node-staging featured-lineage-node-job-source"><span class="featured-lineage-node-icon" aria-hidden="true"></span><span>stg_job_postings</span><small>STAGING MODEL</small></div>
                <div class="featured-lineage-node featured-lineage-node-staging featured-lineage-node-skill-source"><span class="featured-lineage-node-icon" aria-hidden="true"></span><span>stg_job_skills</span><small>STAGING MODEL</small></div>
                <div class="featured-lineage-node featured-lineage-node-staging featured-lineage-node-skill-source"><span class="featured-lineage-node-icon" aria-hidden="true"></span><span>stg_skills</span><small>STAGING MODEL</small></div>
            </div>
            <div class="featured-lineage-column featured-lineage-column-intermediate">
                <div class="featured-lineage-column-title">Intermediate</div>
                <div class="featured-lineage-node featured-lineage-node-intermediate featured-lineage-node-job-intermediate"><span class="featured-lineage-node-icon" aria-hidden="true"></span><span>int_job_postings_enriched</span><small>INTERMEDIATE MODEL</small></div>
                <div class="featured-lineage-node featured-lineage-node-intermediate featured-lineage-node-skill-intermediate"><span class="featured-lineage-node-icon" aria-hidden="true"></span><span>int_job_skills_enriched</span><small>INTERMEDIATE MODEL</small></div>
            </div>
            <div class="featured-lineage-column featured-lineage-column-mart">
                <div class="featured-lineage-column-title">Marts</div>
                <div class="featured-lineage-node featured-lineage-node-mart featured-lineage-node-job-mart"><span class="featured-lineage-node-icon" aria-hidden="true"></span><span>mart_company_leaderboard</span><small>MART MODEL</small></div>
                <div class="featured-lineage-node featured-lineage-node-mart featured-lineage-node-job-mart"><span class="featured-lineage-node-icon" aria-hidden="true"></span><span>mart_monthly_job_trends</span><small>MART MODEL</small></div>
                <div class="featured-lineage-node featured-lineage-node-mart featured-lineage-node-job-mart"><span class="featured-lineage-node-icon" aria-hidden="true"></span><span>mart_remote_work_trends</span><small>MART MODEL</small></div>
                <div class="featured-lineage-node featured-lineage-node-mart featured-lineage-node-job-mart"><span class="featured-lineage-node-icon" aria-hidden="true"></span><span>mart_salary_trends</span><small>MART MODEL</small></div>
                <div class="featured-lineage-node featured-lineage-node-mart featured-lineage-node-skill-mart"><span class="featured-lineage-node-icon" aria-hidden="true"></span><span>mart_skill_demand_by_role</span><small>MART MODEL</small></div>
            </div>
        </div>
    </div>
    """
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
