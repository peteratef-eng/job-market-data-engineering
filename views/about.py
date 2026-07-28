from __future__ import annotations

import streamlit as st

from portfolio.content.profile import PROFILE
from ui.components import footer, section_card
from ui.styles import inject_global_styles
from ui.theme import current_theme


inject_global_styles(current_theme())

st.title("About Me")
section_card("Professional Story", PROFILE["bio"])
section_card(
    "Current Focus",
    "I am targeting Junior Data Engineer opportunities where I can build dependable pipelines, improve data quality, and create models that make analysis easier for teams.",
)
section_card(
    "Background",
    "My experience includes data annotation leadership, quality assurance, structured dataset preparation, API integrations, automation, and cross-functional data workflows.",
)

footer()
