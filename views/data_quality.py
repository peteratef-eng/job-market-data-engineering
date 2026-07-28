from __future__ import annotations

import streamlit as st

from ui.components import footer, section_card
from ui.styles import inject_global_styles
from ui.theme import current_theme


inject_global_styles(current_theme())

st.title("Data Quality")

checks = [
    ("Row Count Validation", "Compares row counts across staging, intermediate, and mart layers."),
    ("Key Integrity", "Checks null keys, duplicate job IDs, duplicate job-skill relationships, and orphan relationships."),
    ("Join Completeness", "Validates company and skill joins after enrichment."),
    ("Calculation Logic", "Checks percentage calculations, month-over-month changes, and mart grain."),
    ("dbt Tests", "Uses not-null and unique tests for key staging models."),
]

for title, body in checks:
    section_card(title, body)

footer()
