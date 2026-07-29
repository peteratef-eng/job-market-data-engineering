from __future__ import annotations

import streamlit as st

from ui.analytics import initialize_analytics
from ui.components import sidebar_bottom
from ui.navigation import portfolio_navigation
from ui.styles import inject_global_styles
from ui.theme import current_theme


st.set_page_config(
    page_title="Job Market Intelligence | Data Engineering Portfolio",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get help": None,
        "Report a bug": None,
        "About": "Job Market Intelligence | Data Engineering Portfolio",
    },
)

theme = current_theme()
inject_global_styles(theme)
initialize_analytics()

sidebar_bottom()
navigation = portfolio_navigation()
navigation.run()
