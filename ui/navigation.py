from __future__ import annotations

import streamlit as st


SIDEBAR_PROJECTS = [
    {
        "name": "Job Market Intelligence",
        "type": "Data Engineering Project",
        "pages": [
            {"label": "Overview", "path": "views/project_overview.py", "route": "/project_overview"},
            {"label": "Market Dashboard", "path": "views/market_dashboard.py", "route": "/market_dashboard"},
            {"label": "Data Pipeline", "path": "views/data_pipeline.py", "route": "/data_pipeline"},
            {"label": "Data Quality", "path": "views/data_quality.py", "route": "/data_quality"},
        ],
    },
]


def portfolio_navigation() -> st.navigation:
    project_pages = [
        st.Page(page["path"], title=page["label"], visibility="hidden")
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
