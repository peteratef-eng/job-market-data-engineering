from __future__ import annotations

import streamlit as st


def portfolio_navigation() -> st.navigation:
    return st.navigation(
        {
            "Portfolio": [
                st.Page("views/home.py", title="Home"),
                st.Page("views/about.py", title="About Me"),
                st.Page("views/experience.py", title="Experience"),
                st.Page("views/skills.py", title="Skills"),
                st.Page("views/projects.py", title="Projects"),
                st.Page("views/contact.py", title="Contact"),
            ],
            "Featured Projects": [
                st.Page("views/project_overview.py", title="Job Market Intelligence"),
                st.Page("views/market_dashboard.py", title="Market Dashboard"),
                st.Page("views/data_pipeline.py", title="Data Pipeline"),
                st.Page("views/data_quality.py", title="Data Quality"),
            ],
        }
    )
