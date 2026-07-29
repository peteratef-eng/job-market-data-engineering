from __future__ import annotations

import pandas as pd
import streamlit as st

from dashboard import charts
from dashboard.data_loader import filter_jobs, load_dashboard_data, skills_for_jobs
from dashboard.transformations import (
    high_salary_skills,
    kpi_values,
    monthly_trends,
    remote_salary,
    salary_coverage,
    salary_by_dimension,
    top_counts,
    top_skills,
)
from ui.components import active_filter_chips, app_header, chart_card, footer, insight, kpi_grid
from ui.styles import inject_global_styles
from ui.theme import current_theme


theme = current_theme()
inject_global_styles(theme)


app_header(
    "Market Dashboard",
    "Hiring Demand and Salary Signals",
    "Filter the hosted sample to explore demand, salaries, technical skills, remote-work patterns, and monthly market movement.",
    "dashboard",
)


@st.cache_data(show_spinner=False)
def dashboard_filter_options() -> dict[str, object]:
    jobs_data, skills_data, _ = load_dashboard_data()
    salary = jobs_data["salary_year_avg"].dropna()
    return {
        "job_titles": sorted(jobs_data["job_title_short"].dropna().unique()),
        "countries": sorted(jobs_data["job_country"].dropna().unique()),
        "skills": sorted(skills_data["clean_skill_name"].dropna().unique()),
        "remote_statuses": sorted(jobs_data["remote_status"].dropna().unique()),
        "companies": jobs_data["clean_company_name"].dropna().value_counts().head(250).index.sort_values().tolist(),
        "salary_min": float(salary.min()) if not salary.empty else 0.0,
        "salary_max": float(salary.max()) if not salary.empty else 0.0,
        "date_min": jobs_data["job_posted_date"].min().date(),
        "date_max": jobs_data["job_posted_date"].max().date(),
    }


@st.cache_data(show_spinner=False)
def dashboard_results(
    job_titles: tuple[str, ...],
    countries: tuple[str, ...],
    selected_skills: tuple[str, ...],
    companies: tuple[str, ...],
    remote_statuses: tuple[str, ...],
    salary_range: tuple[float, float] | None,
    date_range_values: tuple[str, str] | None,
) -> dict[str, object]:
    jobs_data, skills_data, metadata_data = load_dashboard_data()
    date_range_filter = (
        (pd.Timestamp(date_range_values[0]), pd.Timestamp(date_range_values[1]) + pd.Timedelta(days=1))
        if date_range_values is not None
        else None
    )
    filtered_jobs_data = filter_jobs(
        jobs_data,
        skills_data,
        job_titles=list(job_titles),
        countries=list(countries),
        companies=list(companies),
        skills_filter=list(selected_skills),
        remote_statuses=list(remote_statuses),
        salary_range=salary_range,
        date_range=date_range_filter,
    )
    filtered_skills_data = skills_for_jobs(skills_data, filtered_jobs_data)
    coverage_label_data, salary_records_data, total_records_data = salary_coverage(filtered_jobs_data)
    trend_data = monthly_trends(filtered_jobs_data)
    data_engineer_jobs_data = filtered_jobs_data[filtered_jobs_data["job_title_short"].eq("Data Engineer")]
    data_engineer_skills_data = skills_for_jobs(filtered_skills_data, data_engineer_jobs_data)
    return {
        "filtered_jobs": filtered_jobs_data,
        "filtered_skills": filtered_skills_data,
        "kpis": kpi_values(filtered_jobs_data, filtered_skills_data),
        "coverage": (coverage_label_data, salary_records_data, total_records_data),
        "top_job_titles": top_counts(filtered_jobs_data, "job_title_short"),
        "top_companies": top_counts(filtered_jobs_data, "clean_company_name"),
        "salary_by_title": salary_by_dimension(filtered_jobs_data, "job_title_short"),
        "salary_by_country": salary_by_dimension(filtered_jobs_data, "job_country"),
        "remote_salary": remote_salary(filtered_jobs_data),
        "trend": trend_data,
        "monthly_growth": trend_data.dropna(subset=["job_growth_percentage"]),
        "top_skills": top_skills(filtered_skills_data),
        "high_salary_skills": high_salary_skills(filtered_jobs_data, filtered_skills_data),
        "data_engineer_skills": top_skills(data_engineer_skills_data),
        "source_rows": metadata_data.get("source_job_postings_rows"),
        "sample_rows": metadata_data.get("sample_job_postings_rows", len(jobs_data)),
    }

try:
    jobs, _, _ = load_dashboard_data()
except FileNotFoundError:
    st.error("Dataset unavailable. Generate the hosted sample data before sharing this portfolio.")
    st.stop()
except Exception:
    st.error("The dataset could not be loaded. Check the local setup and try again.")
    st.stop()

if jobs.empty:
    st.warning("No job postings are available in the hosted sample.")
    st.stop()

filter_options = dashboard_filter_options()
salary_min = filter_options["salary_min"]
salary_max = filter_options["salary_max"]
date_min = filter_options["date_min"]
date_max = filter_options["date_max"]

if "show_filter_panel" not in st.session_state:
    st.session_state.show_filter_panel = True


def reset_dashboard_filters() -> None:
    for key in (
        "job_titles",
        "countries",
        "selected_skills",
        "companies",
        "remote_statuses",
        "salary_range",
        "selected_dates",
    ):
        if key in st.session_state:
            del st.session_state[key]


filter_head_cols = st.columns([1.25, 1, .85, .75])
with filter_head_cols[0]:
    st.markdown('<div class="filter-title">Filter Results</div>', unsafe_allow_html=True)
with filter_head_cols[1]:
    match_count_slot = st.empty()
with filter_head_cols[2]:
    st.button("Reset Filters", type="secondary", on_click=reset_dashboard_filters)
with filter_head_cols[3]:
    st.toggle("Show filters", key="show_filter_panel")

if st.session_state.show_filter_panel:
    row_one = st.columns(4)
    with row_one[0]:
        job_titles = st.multiselect("Job title", filter_options["job_titles"], key="job_titles")
    with row_one[1]:
        countries = st.multiselect("Country", filter_options["countries"], key="countries")
    skill_options = filter_options["skills"]
    with row_one[2]:
        selected_skills = st.multiselect("Skill", skill_options, key="selected_skills")
    with row_one[3]:
        remote_statuses = st.multiselect(
            "Work mode",
            filter_options["remote_statuses"],
            key="remote_statuses",
        )

    row_two = st.columns([1.45, 1, 1])
    company_options = filter_options["companies"]
    with row_two[0]:
        companies = st.multiselect("Company", company_options, key="companies")
    with row_two[1]:
        salary_range = None
        if salary_max > salary_min:
            salary_range = st.slider(
                "Yearly salary range",
                min_value=salary_min,
                max_value=salary_max,
                value=(salary_min, salary_max),
                step=1_000.0,
                format="$%.0f",
                key="salary_range",
            )
    with row_two[2]:
        selected_dates = st.date_input(
            "Posted date range",
            value=(date_min, date_max),
            min_value=date_min,
            max_value=date_max,
            key="selected_dates",
        )
else:
    job_titles = st.session_state.get("job_titles", [])
    countries = st.session_state.get("countries", [])
    selected_skills = st.session_state.get("selected_skills", [])
    companies = st.session_state.get("companies", [])
    remote_statuses = st.session_state.get("remote_statuses", [])
    salary_range = st.session_state.get("salary_range", (salary_min, salary_max) if salary_max > salary_min else None)
    selected_dates = st.session_state.get("selected_dates", (date_min, date_max))

date_range = None
date_range_values = None
if isinstance(selected_dates, tuple) and len(selected_dates) == 2:
    date_range = (
        pd.Timestamp(selected_dates[0]),
        pd.Timestamp(selected_dates[1]) + pd.Timedelta(days=1),
    )
    date_range_values = (
        pd.Timestamp(selected_dates[0]).date().isoformat(),
        pd.Timestamp(selected_dates[1]).date().isoformat(),
    )

results = dashboard_results(
    tuple(job_titles),
    tuple(countries),
    tuple(selected_skills),
    tuple(companies),
    tuple(remote_statuses),
    salary_range,
    date_range_values,
)
filtered_jobs = results["filtered_jobs"]
filtered_skills = results["filtered_skills"]

salary_active = salary_range if salary_range and salary_range != (salary_min, salary_max) else None
date_active = date_range if date_range and (selected_dates[0] != date_min or selected_dates[1] != date_max) else None
active_filter_chips(
    {
        "Title": job_titles,
        "Country": countries,
        "Skill": selected_skills,
        "Company": companies,
        "Work mode": remote_statuses,
        "Salary": salary_active,
        "Date": date_active,
    }
)

st.markdown(f'<span class="meta-pill">{len(filtered_jobs):,} matching records</span>', unsafe_allow_html=True)
match_count_slot.markdown(
    f'<span class="meta-pill">{len(filtered_jobs):,} matching records</span>',
    unsafe_allow_html=True,
)

if filtered_jobs.empty:
    st.warning("No matching records. Remove one or more filters to continue.")
    st.stop()

source_rows = results["source_rows"]
sample_rows = results["sample_rows"]
if source_rows:
    st.markdown(
        f'<span class="meta-pill">{sample_rows:,} hosted sample postings</span>'
        f'<span class="meta-pill">{source_rows:,} source postings</span>',
        unsafe_allow_html=True,
    )

kpi_grid(results["kpis"])

coverage_label, salary_records, total_records = results["coverage"]
st.caption(
    f"Salary coverage: {coverage_label} ({salary_records:,} of {total_records:,} matching postings). "
    "Salary insights are based only on postings containing salary information."
)

st.subheader("Demand")
with st.container(key="market_dashboard_chart_job_title_demand"):
    chart_card("Most In-Demand Job Titles", "Role categories with the highest posting volume after filtering.")
    st.plotly_chart(
        charts.bar(results["top_job_titles"], "job_title_short", "postings", "Most In-Demand Job Titles", theme),
        use_container_width=True,
        key="market_dashboard_job_title_demand",
    )
    insight("Shows which role categories appear most often after the current filters.")

with st.container(key="market_dashboard_chart_company_activity"):
    chart_card("Top Hiring Companies", "Companies or platforms with the most matching postings.")
    st.plotly_chart(
        charts.bar(results["top_companies"], "clean_company_name", "postings", "Top Hiring Companies", theme),
        use_container_width=True,
        key="market_dashboard_company_activity",
    )
    insight("Company rankings may include job boards or aggregators, which is a known source limitation.")

st.subheader("Salary Insights")
st.caption(
    f"Salary coverage: {coverage_label} ({salary_records:,} of {total_records:,} matching postings). "
    "Salary charts exclude postings without salary information."
)

with st.container(key="market_dashboard_chart_salary_by_job_title"):
    chart_card("Average Salary by Job Title", "Salary averages by role where enough yearly salary data exists.")
    st.plotly_chart(
        charts.salary_bar(results["salary_by_title"], "job_title_short", "Average Salary by Job Title", theme),
        use_container_width=True,
        key="market_dashboard_salary_by_job_title",
    )
    insight("Uses only postings with yearly salary values and hides groups with fewer than three salary records.")

with st.container(key="market_dashboard_chart_salary_by_country"):
    chart_card("Average Salary by Country", "Country-level salary comparison where enough salary data exists.")
    st.plotly_chart(
        charts.salary_bar(results["salary_by_country"], "job_country", "Average Salary by Country", theme),
        use_container_width=True,
        key="market_dashboard_salary_by_country",
    )
    insight("Compares salary levels by country where enough salary data exists.")

with st.container(key="market_dashboard_chart_remote_salary"):
    chart_card("Remote vs On-site Salary", "Salary averages by work-mode classification.")
    st.plotly_chart(
        charts.remote_salary_chart(results["remote_salary"], theme),
        use_container_width=True,
        key="market_dashboard_remote_salary",
    )
    insight("Compares salary averages for remote, on-site, and unknown-location postings.")

st.subheader("Market Trends")
trend = results["trend"]
with st.container(key="market_dashboard_chart_monthly_posting_trend"):
    chart_card("Job Posting Trends Over Time", "Monthly posting volume for the selected market segment.")
    st.plotly_chart(
        charts.line(trend, "posted_month", "total_jobs", "Job Posting Trends Over Time", theme),
        use_container_width=True,
        key="market_dashboard_monthly_posting_trend",
    )
    insight("Tracks posting volume over time for the selected market segment.")

with st.container(key="market_dashboard_chart_monthly_growth"):
    chart_card("Monthly Job-Market Growth", "Month-over-month percentage change in matching postings.")
    st.plotly_chart(
        charts.line(results["monthly_growth"], "posted_month", "job_growth_percentage", "Monthly Job-Market Growth", theme),
        use_container_width=True,
        key="market_dashboard_monthly_growth",
    )
    insight("Shows month-over-month percentage change. Volatility can reflect seasonality or source coverage changes.")

st.subheader("Technical Skills")
with st.container(key="market_dashboard_chart_technical_skill_demand"):
    chart_card("Most In-Demand Technical Skills", "Unique postings connected to each skill in the selected market.")
    st.plotly_chart(
        charts.bar(results["top_skills"], "clean_skill_name", "postings", "Most In-Demand Technical Skills", theme),
        use_container_width=True,
        key="market_dashboard_technical_skill_demand",
    )
    insight("Counts unique postings connected to each skill, helping recruiters see core technical demand.")

st.caption(
    f"Salary coverage: {coverage_label} ({salary_records:,} of {total_records:,} matching postings). "
    "Salary-linked skill rankings only use postings containing salary information."
)
with st.container(key="market_dashboard_chart_high_salary_skills"):
    chart_card("Skills Associated With Highest Salaries", "Skills ranked by average yearly salary where salary data exists.")
    st.plotly_chart(
        charts.salary_bar(results["high_salary_skills"], "clean_skill_name", "Skills Associated With Highest Salaries", theme),
        use_container_width=True,
        key="market_dashboard_high_salary_skills",
    )
    insight("Ranks skills by average yearly salary among postings with salary data.")

with st.container(key="market_dashboard_chart_data_engineer_skill_demand"):
    chart_card("Data Engineer Skill Demand", "Skill demand within matching Data Engineer postings.")
    st.plotly_chart(
        charts.bar(results["data_engineer_skills"], "clean_skill_name", "postings", "Data Engineer Skill Demand", theme),
        use_container_width=True,
        key="market_dashboard_data_engineer_skill_demand",
    )
    insight("Focuses on Data Engineer postings in the current filter context.")

footer()
