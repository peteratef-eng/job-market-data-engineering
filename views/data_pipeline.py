from __future__ import annotations

import streamlit as st

from dashboard.data_loader import load_dashboard_metadata
from ui.components import footer, pipeline_visual, section_card
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
    "Architecture",
    "Raw CSVs -> Python/Pandas -> PostgreSQL -> dbt Models -> Quality Checks -> Analytics Marts -> Streamlit Dashboard.",
    class_name="pipeline-card",
)
section_card(
    "Inputs",
    (
        f"Raw CSV sources include job_postings_fact, company_dim, skills_dim, and skills_job_dim. Verified source postings: {source_rows:,}."
        if source_rows
        else "Raw CSV sources include job_postings_fact, company_dim, skills_dim, and skills_job_dim."
    ),
    class_name="pipeline-card",
)
section_card(
    "Processing",
    "Python/Pandas prepares the hosted sample, PostgreSQL stores relational tables, and dbt builds staging models, intermediate joins, quality checks, and analytics marts.",
    class_name="pipeline-card",
)
section_card(
    "Outputs",
    (
        f"The hosted dashboard uses {sample_rows:,} postings and {skills_rows:,} job-skill rows generated from the real project data."
        if sample_rows and skills_rows
        else "The hosted dashboard sample is generated from the real project data for faster startup on limited hosting resources."
    ),
    class_name="pipeline-card",
)

footer()
