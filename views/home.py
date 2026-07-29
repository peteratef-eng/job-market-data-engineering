from __future__ import annotations

from pathlib import Path

import streamlit as st

from portfolio.content.profile import PROFILE, SPECIALTIES
from portfolio.content.projects import PROJECTS
from ui.components import app_header, badge_row, footer, project_card, section_card
from ui.styles import inject_global_styles
from ui.theme import current_theme


theme = current_theme()
inject_global_styles(theme)

app_header(
    "Built by Peter | Junior Data Engineer",
    PROFILE["headline"],
    PROFILE["summary"],
    "home",
)

badge_row(SPECIALTIES)

cta_cols = st.columns([1.05, .85, .7, 2.4])
with cta_cols[0]:
    st.link_button("Explore My Projects", "/projects", type="primary")
with cta_cols[1]:
    st.link_button("Contact Me", "/contact")
with cta_cols[2]:
    st.link_button("GitHub", PROFILE["github_url"])

resume_path = Path(PROFILE["resume_path"])
if resume_path.exists():
    with resume_path.open("rb") as resume_file:
        st.download_button(
            "Download Resume",
            resume_file,
            file_name="Peter_Atef_Resume_2026.pdf",
            mime="application/pdf",
            type="secondary",
        )

st.subheader("What I Build")
cols = st.columns(3)
with cols[0]:
    section_card("Reliable Pipelines", "ETL workflows that move raw records into structured, trusted datasets.", class_name="home-hover-card")
with cols[1]:
    section_card("Analytics-Ready Models", "Clean staging layers, reusable joins, and marts designed around business questions.", class_name="home-hover-card")
with cols[2]:
    section_card("Quality Checks", "Validation for row counts, nulls, duplicates, joins, and calculation logic.", class_name="home-hover-card")

st.subheader("Featured Project")
project_card(PROJECTS[0])
actions = st.columns([1, .85, 3])
with actions[0]:
    st.link_button("View Case Study", "/project_overview", type="primary")
with actions[1]:
    st.link_button("Live Demo", "/market_dashboard")

footer()
