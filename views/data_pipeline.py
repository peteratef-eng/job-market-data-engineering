from __future__ import annotations

import streamlit as st

from ui.components import footer, pipeline_visual, section_card
from ui.styles import inject_global_styles
from ui.theme import current_theme


inject_global_styles(current_theme())

st.title("Data Pipeline")
pipeline_visual()

section_card(
    "Architecture",
    "Source Data -> Python/Pandas -> PostgreSQL -> dbt Models -> Quality Checks -> Market Insights.",
)
section_card(
    "Source Tables",
    "job_postings_fact, company_dim, skills_dim, and skills_job_dim from the MotherDuck/DuckDB source workflow.",
)
section_card(
    "Model Layers",
    "Staging models standardize raw fields, intermediate models join reusable entities, and marts produce business-ready analytics for demand, salaries, remote work, companies, and monthly trends.",
)
section_card(
    "Deployment Dataset",
    "The hosted sample is generated from the real project data for faster startup on limited hosting resources.",
)

footer()
