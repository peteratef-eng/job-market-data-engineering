from __future__ import annotations

import html
import streamlit as st

from dashboard.data_loader import load_dashboard_metadata
from ui.components import pipeline_visual

st.title("Data Pipeline")
pipeline_visual()

metadata = load_dashboard_metadata()
source_rows = metadata.get("source_job_postings_rows")
sample_rows = metadata.get("sample_job_postings_rows")
skills_rows = metadata.get("sample_job_skills_rows")

pipeline_info = [
    (
        "INPUTS",
        "Source data",
        (
            f"{source_rows:,} verified source postings. Four relational source tables feed the pipeline."
            if source_rows
            else "Verified source postings from four relational source tables feed the pipeline."
        ),
    ),
    (
        "PROCESSING",
        "Engineering workflow",
        (
            f"{sample_rows:,}-posting hosted sample with {skills_rows:,} job-skill relationships. Python/Pandas, PostgreSQL, and dbt prepare the analytics layer."
            if sample_rows and skills_rows
            else "Python/Pandas, PostgreSQL, and dbt prepare the hosted analytics layer."
        ),
    ),
    (
        "OUTPUTS",
        "Analytics delivery",
        "Tested analytics marts power an interactive Streamlit dashboard with recruiter-ready market insights.",
    ),
]
pipeline_info_markup = "".join(
    (
        f'<div class="section-card pipeline-card pipeline-info-card-{index}" tabindex="0">'
        '<div class="pipeline-info-card-heading">'
        f'<span class="pipeline-info-icon" aria-hidden="true">{index}</span>'
        '<span>'
        f'<small>{html.escape(title)}</small>'
        f'<strong>{html.escape(label)}</strong>'
        '</span>'
        '</div>'
        f'<div class="section-copy">{html.escape(body)}</div>'
        '</div>'
    )
    for index, (title, label, body) in enumerate(pipeline_info, start=1)
)
st.markdown(f'<section class="pipeline-info-grid">{pipeline_info_markup}</section>', unsafe_allow_html=True)
