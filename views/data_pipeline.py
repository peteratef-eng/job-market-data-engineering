from __future__ import annotations

import streamlit as st

from dashboard.data_loader import load_dashboard_metadata
from ui.components import pipeline_visual, section_card
from ui.styles import inject_global_styles
from ui.theme import current_theme


inject_global_styles(current_theme())

st.title("Data Pipeline")
pipeline_visual(class_name="pipeline-card")

metadata = load_dashboard_metadata()
source_rows = metadata.get("source_job_postings_rows")
sample_rows = metadata.get("sample_job_postings_rows")
skills_rows = metadata.get("sample_job_skills_rows")

section_card(
    "Inputs",
    (
        f"Source tables include job_postings_fact, company_dim, skills_dim, and skills_job_dim. The verified source dataset contains {source_rows:,} job postings before hosted sampling."
        if source_rows
        else "Source tables include job_postings_fact, company_dim, skills_dim, and skills_job_dim before hosted sampling."
    ),
    class_name="pipeline-card",
)
section_card(
    "Processing",
    "Python/Pandas prepares dashboard-ready files, PostgreSQL supports relational storage, and dbt organizes staging, intermediate, and mart models for analysis.",
    class_name="pipeline-card",
)
section_card(
    "Outputs",
    (
        f"The portfolio dashboard uses a {sample_rows:,}-posting hosted sample with {skills_rows:,} job-skill rows and analytics-ready outputs for recruiter review."
        if sample_rows and skills_rows
        else "The hosted dashboard sample is generated from the real project data for faster startup on limited hosting resources."
    ),
    class_name="pipeline-card",
)
