from __future__ import annotations

import streamlit as st


def portfolio_navigation() -> st.navigation:
    return st.navigation(
        {
            "PORTFOLIO": [
                st.Page("views/home.py", title="Home"),
                st.Page("views/about.py", title="About Me", visibility="hidden"),
                st.Page("views/experience.py", title="Experience"),
                st.Page("views/skills.py", title="Skills", visibility="hidden"),
                # Restore this sidebar item when a second portfolio project is added.
                st.Page("views/projects.py", title="Projects", visibility="hidden"),
                st.Page("views/contact.py", title="Contact"),
            ],
            "FEATURED PROJECT": [
                st.Page("views/project_overview.py", title="Overview"),
                st.Page("views/market_dashboard.py", title="Market Dashboard"),
                st.Page("views/data_pipeline.py", title="Data Pipeline"),
                st.Page("views/data_quality.py", title="Data Quality"),
            ],
        }
    )
