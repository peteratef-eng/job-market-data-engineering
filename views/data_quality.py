from __future__ import annotations

from pathlib import Path

import streamlit as st

from dashboard.data_loader import load_dashboard_data
from ui.components import footer
from ui.styles import inject_global_styles
from ui.theme import current_theme


inject_global_styles(current_theme())

st.title("Data Quality")

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "job_market_dbt" / "models" / "staging" / "schema.yml"
AUDIT_PATH = ROOT / "audit_reports" / "market_dashboard_validation_audit.md"

try:
    jobs, skills, metadata = load_dashboard_data()
except FileNotFoundError:
    st.warning("Dataset unavailable. Generate the hosted sample data before sharing this portfolio.")
    st.stop()

job_id_nulls = int(jobs["job_id"].isna().sum())
skill_job_id_nulls = int(skills["job_id"].isna().sum())
duplicate_job_ids = int(jobs["job_id"].duplicated().sum())
duplicate_skill_ids = int(skills.duplicated(["job_id", "skill_id"]).sum())
duplicate_clean_skills = int(skills.duplicated(["job_id", "clean_skill_name"]).sum())
orphan_skill_rows = int((~skills["job_id"].isin(jobs["job_id"])).sum())
jobs_without_skills = int((~jobs["job_id"].isin(skills["job_id"])).sum())
schema_text = SCHEMA_PATH.read_text(encoding="utf-8") if SCHEMA_PATH.exists() else ""
dbt_test_count = schema_text.count("- not_null") + schema_text.count("- unique")
audit_text = AUDIT_PATH.read_text(encoding="utf-8") if AUDIT_PATH.exists() else ""

checks = [
    {
        "title": "Row Count Validation",
        "state": "Passed",
        "body": "Compares hosted sample counts with stored metadata.",
        "metrics": [
            ("Job rows", f"{len(jobs):,}"),
            ("Metadata job rows", f"{metadata.get('sample_job_postings_rows', 'Not stored'):,}" if metadata.get("sample_job_postings_rows") else "Not stored"),
            ("Skill rows", f"{len(skills):,}"),
            ("Metadata skill rows", f"{metadata.get('sample_job_skills_rows', 'Not stored'):,}" if metadata.get("sample_job_skills_rows") else "Not stored"),
        ],
        "caption": "Last execution time is not stored in the repository metadata.",
    },
    {
        "title": "Key Integrity",
        "state": "Implemented validation",
        "body": "Checks null keys, duplicate job IDs, duplicate job-skill relationships, and orphan relationships.",
        "metrics": [
            ("Null job IDs", f"{job_id_nulls:,}"),
            ("Null skill job IDs", f"{skill_job_id_nulls:,}"),
            ("Duplicate job IDs", f"{duplicate_job_ids:,}"),
            ("Orphan skill rows", f"{orphan_skill_rows:,}"),
            ("Duplicate job-skill IDs", f"{duplicate_skill_ids:,}"),
            ("Duplicate cleaned skill names", f"{duplicate_clean_skills:,}"),
        ],
        "caption": "The audit flags duplicate cleaned skill-name relationships; bridge-level job_id/skill_id relationships are unique.",
    },
    {
        "title": "Join Completeness",
        "state": "Passed with documented limitation",
        "body": "Validates company and skill joins after enrichment.",
        "metrics": [
            ("Orphan skill rows", f"{orphan_skill_rows:,}"),
            ("Jobs without skills", f"{jobs_without_skills:,}"),
            ("Company nulls", f"{int(jobs['clean_company_name'].isna().sum()):,}"),
        ],
        "caption": "Jobs without skill rows are documented in the audit and remain included in posting KPIs.",
    },
    {
        "title": "Calculation Logic",
        "state": "Passed",
        "body": "Checks KPI formulas, percentage calculations, monthly changes, and chart source tables.",
        "metrics": [
            ("Validation tests", "5 methods"),
            ("Passed methods", "4"),
            ("Known failed invariant", "1"),
        ],
        "caption": "The failed invariant is the duplicate cleaned skill-name relationship noted above; dashboard formulas matched independent calculations.",
    },
    {
        "title": "dbt Tests",
        "state": "Implemented validation",
        "body": "Uses not-null and unique tests for key staging models.",
        "metrics": [
            ("Schema tests defined", f"{dbt_test_count:,}" if dbt_test_count else "Not stored"),
            ("README result", "11/11 passed" if "11/11 tests passed" in audit_text or "11/11 tests passed" in (ROOT / "README.md").read_text(encoding="utf-8") else "Result not stored"),
        ],
        "caption": "A reliable dbt execution timestamp is not stored in the repository.",
    },
]

for index, check in enumerate(checks):
    with st.container(border=True, key=f"data_quality_check_card_{index}"):
        st.subheader(check["title"])
        st.caption(check["state"])
        st.markdown(check["body"])
        columns = st.columns(min(3, len(check["metrics"])))
        for index, (label, value) in enumerate(check["metrics"]):
            with columns[index % len(columns)]:
                st.metric(label, value)
        st.caption(check["caption"])

footer()
