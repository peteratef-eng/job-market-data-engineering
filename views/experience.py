from __future__ import annotations

import streamlit as st

from portfolio.content.experience import EXPERIENCE
from ui.components import footer, timeline_entry
from ui.styles import inject_global_styles
from ui.theme import current_theme


inject_global_styles(current_theme())

st.title("Experience")

for entry in EXPERIENCE:
    timeline_entry(entry, class_name="experience-hover-card")

footer()
