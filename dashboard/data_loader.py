from __future__ import annotations

import json
import os
from pathlib import Path

import pandas as pd
import streamlit as st


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATA_DIR = PROJECT_ROOT / "data" / "dashboard"


@st.cache_data(show_spinner=False)
def load_dashboard_metadata(data_dir: str | None = None) -> dict:
    base_dir = Path(data_dir or os.getenv("DASHBOARD_DATA_DIR", DEFAULT_DATA_DIR))
    metadata_path = base_dir / "metadata.json"
    if not metadata_path.exists():
        return {}

    with metadata_path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


@st.cache_data(show_spinner=False)
def load_dashboard_data(data_dir: str | None = None) -> tuple[pd.DataFrame, pd.DataFrame, dict]:
    base_dir = Path(data_dir or os.getenv("DASHBOARD_DATA_DIR", DEFAULT_DATA_DIR))
    jobs_path = base_dir / "jobs_sample.csv"
    skills_path = base_dir / "job_skills_sample.csv"
    metadata_path = base_dir / "metadata.json"

    missing = [str(path) for path in (jobs_path, skills_path) if not path.exists()]
    if missing:
        raise FileNotFoundError(
            "Dashboard dataset is missing. Run `python scripts/prepare_dashboard_data.py` "
            f"from the project root. Missing files: {', '.join(missing)}"
        )

    jobs = pd.read_csv(
        jobs_path,
        parse_dates=["job_posted_date", "posted_month"],
        dtype={
            "job_id": "Int64",
            "company_id": "Int64",
            "job_title_short": "string",
            "clean_job_title": "string",
            "clean_job_location": "string",
            "job_country": "string",
            "remote_status": "string",
            "salary_year_avg": "float64",
            "clean_company_name": "string",
        },
    )
    skills = pd.read_csv(
        skills_path,
        dtype={
            "job_id": "Int64",
            "skill_id": "Int64",
            "clean_skill_name": "string",
            "clean_skill_type": "string",
        },
    )

    metadata = load_dashboard_metadata(str(base_dir))

    return jobs, skills, metadata


def filter_jobs(
    jobs: pd.DataFrame,
    skills: pd.DataFrame,
    *,
    job_titles: list[str],
    countries: list[str],
    companies: list[str],
    skills_filter: list[str],
    remote_statuses: list[str],
    salary_range: tuple[float, float] | None,
    date_range: tuple[pd.Timestamp, pd.Timestamp] | None,
) -> pd.DataFrame:
    filtered = jobs.copy()

    if job_titles:
        filtered = filtered[filtered["job_title_short"].isin(job_titles)]
    if countries:
        filtered = filtered[filtered["job_country"].isin(countries)]
    if companies:
        filtered = filtered[filtered["clean_company_name"].isin(companies)]
    if remote_statuses:
        filtered = filtered[filtered["remote_status"].isin(remote_statuses)]
    if salary_range is not None:
        low, high = salary_range
        salary = filtered["salary_year_avg"]
        filtered = filtered[salary.isna() | salary.between(low, high)]
    if date_range is not None:
        start, end = date_range
        filtered = filtered[
            filtered["job_posted_date"].between(pd.Timestamp(start), pd.Timestamp(end))
        ]
    if skills_filter:
        matching_job_ids = skills.loc[
            skills["clean_skill_name"].isin(skills_filter), "job_id"
        ].dropna()
        filtered = filtered[filtered["job_id"].isin(matching_job_ids)]

    return filtered


def skills_for_jobs(skills: pd.DataFrame, jobs: pd.DataFrame) -> pd.DataFrame:
    if jobs.empty:
        return skills.iloc[0:0].copy()
    return skills[skills["job_id"].isin(jobs["job_id"])]
