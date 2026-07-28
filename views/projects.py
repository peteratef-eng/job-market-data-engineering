from __future__ import annotations

import streamlit as st

from portfolio.content.projects import PROJECTS
from ui.components import footer, project_card
from ui.styles import inject_global_styles
from ui.theme import current_theme


inject_global_styles(current_theme())

st.title("Projects")
st.caption("Scalable project registry. Add future work in `portfolio/content/projects.py`.")

projects = sorted(PROJECTS, key=lambda item: item.get("sort_order", 999))
for row_start in range(0, len(projects), 3):
    columns = st.columns(3)
    for column, project in zip(columns, projects[row_start : row_start + 3]):
        with column:
            project_card(project)
            action_cols = st.columns(3)
            with action_cols[0]:
                st.link_button("View Case Study", "/project_overview", type="primary")
            if project.get("demo_url"):
                with action_cols[1]:
                    st.link_button("Live Demo", project["demo_url"])
            else:
                with action_cols[1]:
                    st.link_button("Live Demo", "/market_dashboard")
            if project.get("repository_url"):
                with action_cols[2]:
                    st.link_button("GitHub Repository", project["repository_url"])

footer()
