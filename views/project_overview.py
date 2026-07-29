from __future__ import annotations

import streamlit as st

from dashboard.data_loader import load_dashboard_metadata
from portfolio.content.projects import PROJECTS
from ui.components import (
    app_header,
    badge_row,
    challenge_points,
    footer,
    metric_status_card,
    pipeline_visual,
    purpose_cards,
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
    st.link_button("Explore Market Dashboard", "/market_dashboard", type="primary")
with action_cols[1]:
    st.link_button("View Data Pipeline", "/data_pipeline")
with action_cols[2]:
    st.link_button("GitHub", project["repository_url"])

try:
    metadata = load_dashboard_metadata()
    source_rows = metadata.get("source_job_postings_rows", "1.6M+")
    sample_rows = metadata.get("sample_job_postings_rows", "Hosted sample")
    metric_status_card(sample_rows, source_rows)
except Exception:
    st.warning("Dataset metadata unavailable. Generate the hosted sample data before sharing this portfolio.")

st.subheader("Project Purpose")
purpose_cards()

st.subheader("Business Challenge")
challenge_points()

st.subheader("Architecture")
pipeline_visual()

sections = project["case_study_sections"]
ordered_sections = [
    "Project summary",
    "Business problem",
    "My role",
    "Dataset or source",
    "Data pipeline",
    "Data-quality process",
    "Key features",
    "Key results",
    "Challenges and solutions",
    "Limitations",
]

for index in range(0, len(ordered_sections), 2):
    cols = st.columns(2)
    for col, title in zip(cols, ordered_sections[index : index + 2]):
        with col:
            section_card(title, sections[title])

footer()
