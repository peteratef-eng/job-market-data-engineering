from __future__ import annotations

import streamlit as st

from portfolio.content.skills import SKILL_GROUPS
from ui.components import skill_group_card
from ui.styles import inject_global_styles
from ui.theme import current_theme


inject_global_styles(current_theme())

st.title("Skills")
st.caption("Grouped by data engineering workflow areas supported by the project and profile.")

items = list(SKILL_GROUPS.items())
for index in range(0, len(items), 2):
    cols = st.columns(2)
    for col, (title, skills) in zip(cols, items[index : index + 2]):
        with col:
            skill_group_card(title, skills, class_name="skills-hover-card")
