from __future__ import annotations

import html
import streamlit as st

from dashboard.data_loader import load_dashboard_metadata
from ui.components import data_lineage, pipeline_visual
from ui.styles import inject_global_styles
from ui.theme import current_theme


inject_global_styles(current_theme())

st.title("Data Pipeline")
data_lineage("pipeline")
pipeline_visual(class_name="pipeline-card")

metadata = load_dashboard_metadata()
source_rows = metadata.get("source_job_postings_rows")
sample_rows = metadata.get("sample_job_postings_rows")
skills_rows = metadata.get("sample_job_skills_rows")

pipeline_info = [
    (
        "Inputs",
        (
            f"Source tables include job_postings_fact, company_dim, skills_dim, and skills_job_dim. The verified source dataset contains {source_rows:,} job postings before hosted sampling."
            if source_rows
            else "Source tables include job_postings_fact, company_dim, skills_dim, and skills_job_dim before hosted sampling."
        ),
    ),
    (
        "Processing",
        "Python/Pandas prepares dashboard-ready files, PostgreSQL supports relational storage, and dbt organizes staging, intermediate, and mart models for analysis.",
    ),
    (
        "Outputs",
        (
            f"The portfolio dashboard uses a {sample_rows:,}-posting hosted sample with {skills_rows:,} job-skill rows and analytics-ready outputs for recruiter review."
            if sample_rows and skills_rows
            else "The hosted dashboard sample is generated from the real project data for faster startup on limited hosting resources."
        ),
    ),
]
pipeline_info_markup = "".join(
    (
        '<div class="section-card pipeline-card" tabindex="0">'
        f'<div class="section-title">{html.escape(title)}</div>'
        f'<div class="section-copy">{html.escape(body)}</div>'
        '</div>'
    )
    for title, body in pipeline_info
)
st.markdown(f'<section class="pipeline-info-grid">{pipeline_info_markup}</section>', unsafe_allow_html=True)
