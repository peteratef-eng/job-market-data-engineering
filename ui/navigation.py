from __future__ import annotations

import streamlit as st


SIDEBAR_PROJECTS = [
    {
        "name": "Job Market Intelligence",
        "type": "Data Engineering Project",
        "pages": [
            {"label": "Overview", "path": "views/project_overview.py"},
            {"label": "Market Dashboard", "path": "views/market_dashboard.py"},
            {"label": "Data Pipeline", "path": "views/data_pipeline.py"},
            {"label": "Data Quality", "path": "views/data_quality.py"},
        ],
    },
]


def portfolio_navigation() -> st.navigation:
    project_pages = [
        st.Page(page["path"], title=page["label"])
        for project in SIDEBAR_PROJECTS
        for page in project["pages"]
    ]
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
            "PROJECTS": project_pages,
        }
    )
