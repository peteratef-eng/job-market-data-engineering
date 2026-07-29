from __future__ import annotations

import html
import streamlit as st

from dashboard.data_loader import load_dashboard_metadata
from portfolio.content.projects import PROJECTS
from ui.components import (
    app_header,
    badge_row,
    metric_status_card,
    section_card,
)
from ui.styles import inject_global_styles
from ui.theme import current_theme


theme = current_theme()
inject_global_styles(theme)

project = PROJECTS[0]

app_header(
    "1.6M+ Job Postings",
    "Job Market Intelligence",
    "Explore hiring demand, salaries, technical skills, remote-work patterns, and market trends across 1.6M+ job postings.",
    "overview",
)

badge_row(project["technologies"][:6])

action_cols = st.columns([1.05, .95, .8, 2.4])
with action_cols[0]:
    st.markdown(
        '<a class="portfolio-button portfolio-button-primary" href="/market_dashboard">Explore Market Dashboard</a>',
        unsafe_allow_html=True,
    )
with action_cols[1]:
    st.markdown('<a class="portfolio-button" href="/data_pipeline">View Data Pipeline</a>', unsafe_allow_html=True)
with action_cols[2]:
    st.markdown(
        f'<a class="portfolio-button" href="{html.escape(project["repository_url"])}">GitHub</a>',
        unsafe_allow_html=True,
    )

metadata = {}
try:
    metadata = load_dashboard_metadata()
    source_rows = metadata.get("source_job_postings_rows", "1.6M+")
    sample_rows = metadata.get("sample_job_postings_rows", "Hosted sample")
    skill_rows = metadata.get("sample_job_skills_rows", "667,829")
    metric_status_card(sample_rows, source_rows, class_name="job-intelligence-hover-card")
except Exception:
    source_rows = "1.6M+"
    sample_rows = "Hosted sample"
    skill_rows = "667,829"
    st.warning("Dataset metadata unavailable. Generate the hosted sample data before sharing this portfolio.")

problem_solution = [
    (
        "The Problem",
        "Job-market data is noisy and difficult to analyze because of inconsistent locations, missing salary values, duplicate relationships, aggregator companies, and unstructured posting records.",
    ),
    (
        "The Solution",
        "A validated Data Engineering pipeline prepares, stores, models, tests, and delivers analytics-ready job-market data through an interactive dashboard.",
    ),
]
problem_cols = st.columns(2)
for col, (title, body) in zip(problem_cols, problem_solution):
    with col:
        section_card(title, body, class_name="job-intelligence-hover-card")

st.markdown(
    '<a class="portfolio-button project-overview-architecture-link" href="/data_pipeline">View the complete technical architecture -&gt;</a>',
    unsafe_allow_html=True,
)

source_value = f"{source_rows:,}" if isinstance(source_rows, int) else html.escape(str(source_rows))
sample_value = f"{sample_rows:,}" if isinstance(sample_rows, int) else html.escape(str(sample_rows))
skill_rows_value = f"{skill_rows:,}" if isinstance(skill_rows, int) else html.escape(str(skill_rows))

case_sections = [
    (
        "My Role",
        "Designed the project structure, SQL models, quality checks, documentation, and dashboard experience.",
    ),
    (
        "Key Features",
        "KPIs and filters for hiring demand, skill demand, salary analysis, company rankings, remote-work patterns, and monthly trends.",
    ),
    (
        "Key Results",
        f"{source_value} source postings processed, {sample_value} hosted sample postings, {skill_rows_value} job-skill rows, 241 distinct skills, and dashboard-ready analytical outputs.",
    ),
    (
        "Limitations",
        "Salary coverage is incomplete, company names may include aggregators, remote status is inferred from source fields, and the hosted dashboard uses a sample for deployment performance.",
    ),
]

for index in range(0, len(case_sections), 2):
    cols = st.columns(2)
    for col, (title, body) in zip(cols, case_sections[index : index + 2]):
        with col:
            section_card(title, body, class_name="job-intelligence-hover-card")

st.markdown(
    f"""
    <div class="case-study-links">
        <a class="portfolio-button portfolio-button-primary" href="/market_dashboard">Market Dashboard</a>
        <a class="portfolio-button" href="/data_pipeline">Data Pipeline</a>
        <a class="portfolio-button" href="/data_quality">Data Quality</a>
        <a class="portfolio-button" href="{html.escape(project["repository_url"])}" rel="noreferrer">GitHub</a>
    </div>
    """,
    unsafe_allow_html=True,
)
