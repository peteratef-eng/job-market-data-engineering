from __future__ import annotations

import streamlit as st

from portfolio.content.experience import EXPERIENCE
from ui.components import render_experience_card

st.title("Experience")

for entry in EXPERIENCE:
    render_experience_card(entry, class_name="experience-hover-card")
