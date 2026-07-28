from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_DIR = ROOT / "data"
OUTPUT_DIR = RAW_DATA_DIR / "dashboard"

JOB_COLUMNS = [
    "job_id",
    "company_id",
    "job_title_short",
    "job_title",
    "job_location",
    "job_work_from_home",
    "job_posted_date",
    "job_country",
    "salary_year_avg",
]


def clean_text(series: pd.Series, default: str) -> pd.Series:
    cleaned = series.astype("string").str.strip()
    return cleaned.mask(cleaned.eq("") | cleaned.isna(), default)


def remote_status(row: pd.Series) -> str:
    location = row.get("job_location")
    work_from_home = row.get("job_work_from_home")
    is_remote_flag = str(work_from_home).strip().lower() in {"true", "1", "yes"}
    if pd.isna(location) or str(location).strip() == "":
        return "Unknown"
    if str(location).strip() == "Anywhere" or is_remote_flag:
        return "Remote"
    return "Onsite"


def build_dashboard_dataset(sample_size: int, random_state: int) -> dict:
    jobs_path = RAW_DATA_DIR / "job_postings_fact.csv"
    companies_path = RAW_DATA_DIR / "company_dim.csv"
    skills_path = RAW_DATA_DIR / "skills_dim.csv"
    bridge_path = RAW_DATA_DIR / "skills_job_dim.csv"

    for path in [jobs_path, companies_path, skills_path, bridge_path]:
        if not path.exists():
            raise FileNotFoundError(f"Required source file is missing: {path}")

    jobs = pd.read_csv(jobs_path, usecols=JOB_COLUMNS, low_memory=False)
    source_rows = len(jobs)
    sample_n = min(sample_size, source_rows)
    sampled_jobs = jobs.sample(n=sample_n, random_state=random_state).copy()

    companies = pd.read_csv(companies_path, usecols=["company_id", "name"], low_memory=False)
    companies["clean_company_name"] = clean_text(companies["name"], "Unknown Company")

    sampled_jobs["clean_job_title"] = clean_text(sampled_jobs["job_title"], "Unknown job title").str.lower()
    sampled_jobs["clean_job_location"] = clean_text(sampled_jobs["job_location"], "Unknown")
    sampled_jobs["job_country"] = clean_text(sampled_jobs["job_country"], "Unknown")
    sampled_jobs["job_posted_date"] = pd.to_datetime(sampled_jobs["job_posted_date"], errors="coerce")
    sampled_jobs["posted_month"] = sampled_jobs["job_posted_date"].dt.to_period("M").dt.to_timestamp()
    sampled_jobs["salary_year_avg"] = pd.to_numeric(sampled_jobs["salary_year_avg"], errors="coerce")
    sampled_jobs["remote_status"] = sampled_jobs.apply(remote_status, axis=1)
    sampled_jobs = sampled_jobs.merge(
        companies[["company_id", "clean_company_name"]], on="company_id", how="left"
    )
    sampled_jobs["clean_company_name"] = sampled_jobs["clean_company_name"].fillna("Unknown Company")

    job_ids = set(sampled_jobs["job_id"].dropna().astype("int64"))
    bridge_chunks = []
    for chunk in pd.read_csv(bridge_path, chunksize=750_000):
        bridge_chunks.append(chunk[chunk["job_id"].isin(job_ids)])
    sampled_bridge = pd.concat(bridge_chunks, ignore_index=True) if bridge_chunks else pd.DataFrame()

    skills = pd.read_csv(skills_path, low_memory=False)
    skills["clean_skill_name"] = clean_text(skills["skills"], "unknown skill name").str.lower()
    skills["clean_skill_type"] = clean_text(skills["type"], "unknown skill type").str.lower()
    sampled_skills = sampled_bridge.merge(
        skills[["skill_id", "clean_skill_name", "clean_skill_type"]], on="skill_id", how="left"
    )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    sampled_jobs[
        [
            "job_id",
            "company_id",
            "job_title_short",
            "clean_job_title",
            "clean_job_location",
            "job_country",
            "remote_status",
            "job_posted_date",
            "posted_month",
            "salary_year_avg",
            "clean_company_name",
        ]
    ].to_csv(OUTPUT_DIR / "jobs_sample.csv", index=False)
    sampled_skills[["job_id", "skill_id", "clean_skill_name", "clean_skill_type"]].to_csv(
        OUTPUT_DIR / "job_skills_sample.csv", index=False
    )

    metadata = {
        "source": "Generated from data/job_postings_fact.csv, company_dim.csv, skills_dim.csv, and skills_job_dim.csv",
        "source_job_postings_rows": int(source_rows),
        "sample_job_postings_rows": int(len(sampled_jobs)),
        "sample_job_skills_rows": int(len(sampled_skills)),
        "sample_size_requested": int(sample_size),
        "random_state": int(random_state),
        "method": "Random sample of source job postings, joined to matching companies and job-skill relationships.",
    }
    with (OUTPUT_DIR / "metadata.json").open("w", encoding="utf-8") as handle:
        json.dump(metadata, handle, indent=2)

    return metadata


def main() -> None:
    parser = argparse.ArgumentParser(description="Prepare optimized Streamlit dashboard data.")
    parser.add_argument("--sample-size", type=int, default=150_000)
    parser.add_argument("--random-state", type=int, default=42)
    args = parser.parse_args()

    metadata = build_dashboard_dataset(args.sample_size, args.random_state)
    print(json.dumps(metadata, indent=2))


if __name__ == "__main__":
    main()
