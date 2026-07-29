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

try:
    jobs, skills, metadata = load_dashboard_data()
except FileNotFoundError:
    st.error("Dataset unavailable. Generate the hosted sample data before sharing this portfolio.")
    st.stop()
except Exception:
    st.error("The dataset could not be loaded. Check the local setup and try again.")
    st.stop()

if jobs.empty:
    st.warning("No job postings are available in the hosted sample.")
    st.stop()

salary_min = float(jobs["salary_year_avg"].dropna().min()) if jobs["salary_year_avg"].notna().any() else 0.0
salary_max = float(jobs["salary_year_avg"].dropna().max()) if jobs["salary_year_avg"].notna().any() else 0.0
date_min = jobs["job_posted_date"].min().date()
date_max = jobs["job_posted_date"].max().date()

if "show_filter_panel" not in st.session_state:
    st.session_state.show_filter_panel = True

filter_head_cols = st.columns([1.25, 1, .85, .75])
with filter_head_cols[0]:
    st.markdown('<div class="filter-title">Filter Results</div>', unsafe_allow_html=True)
with filter_head_cols[1]:
    match_count_slot = st.empty()
with filter_head_cols[2]:
    if st.button("Reset Filters", type="secondary"):
        st.session_state.job_titles = []
        st.session_state.countries = []
        st.session_state.selected_skills = []
        st.session_state.companies = []
        st.session_state.remote_statuses = []
        st.session_state.salary_range = (salary_min, salary_max)
        st.session_state.selected_dates = (date_min, date_max)
        st.rerun()
with filter_head_cols[3]:
    st.toggle("Show filters", key="show_filter_panel")

if st.session_state.show_filter_panel:
    row_one = st.columns(4)
    with row_one[0]:
        job_titles = st.multiselect("Job title", sorted(jobs["job_title_short"].dropna().unique()), key="job_titles")
    with row_one[1]:
        countries = st.multiselect("Country", sorted(jobs["job_country"].dropna().unique()), key="countries")
    skill_options = sorted(skills["clean_skill_name"].dropna().unique())
    with row_one[2]:
        selected_skills = st.multiselect("Skill", skill_options, key="selected_skills")
    with row_one[3]:
        remote_statuses = st.multiselect(
            "Work mode",
            sorted(jobs["remote_status"].dropna().unique()),
            key="remote_statuses",
        )

    row_two = st.columns([1.45, 1, 1])
    company_options = (
        jobs["clean_company_name"].dropna().value_counts().head(250).index.sort_values().tolist()
    )
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
if isinstance(selected_dates, tuple) and len(selected_dates) == 2:
    date_range = (
        pd.Timestamp(selected_dates[0]),
        pd.Timestamp(selected_dates[1]) + pd.Timedelta(days=1),
    )

filtered_jobs = filter_jobs(
    jobs,
    skills,
    job_titles=job_titles,
    countries=countries,
    companies=companies,
    skills_filter=selected_skills,
    remote_statuses=remote_statuses,
    salary_range=salary_range,
    date_range=date_range,
)
filtered_skills = skills_for_jobs(skills, filtered_jobs)

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

source_rows = metadata.get("source_job_postings_rows")
sample_rows = metadata.get("sample_job_postings_rows", len(jobs))
if source_rows:
    st.markdown(
        f'<span class="meta-pill">{sample_rows:,} hosted sample postings</span>'
        f'<span class="meta-pill">{source_rows:,} source postings</span>',
        unsafe_allow_html=True,
    )

kpi_grid(kpi_values(filtered_jobs, filtered_skills))

chart_card("Most In-Demand Job Titles", "Role categories with the highest posting volume after filtering.")
st.plotly_chart(
    charts.bar(top_counts(filtered_jobs, "job_title_short"), "job_title_short", "postings", "Most In-Demand Job Titles", theme),
    use_container_width=True,
    key="market_dashboard_job_title_demand",
)
insight("Shows which role categories appear most often after the current filters.")

chart_card("Most In-Demand Technical Skills", "Unique postings connected to each skill in the selected market.")
st.plotly_chart(
    charts.bar(top_skills(filtered_skills), "clean_skill_name", "postings", "Most In-Demand Technical Skills", theme),
    use_container_width=True,
    key="market_dashboard_technical_skill_demand",
)
insight("Counts unique postings connected to each skill, helping recruiters see core technical demand.")

chart_card("Top Hiring Companies", "Companies or platforms with the most matching postings.")
st.plotly_chart(
    charts.bar(top_counts(filtered_jobs, "clean_company_name"), "clean_company_name", "postings", "Top Hiring Companies", theme),
    use_container_width=True,
    key="market_dashboard_company_activity",
)
insight("Company rankings may include job boards or aggregators, which is a known source limitation.")

chart_card("Average Salary by Job Title", "Salary averages by role where enough yearly salary data exists.")
st.plotly_chart(
    charts.salary_bar(salary_by_dimension(filtered_jobs, "job_title_short"), "job_title_short", "Average Salary by Job Title", theme),
    use_container_width=True,
    key="market_dashboard_salary_by_job_title",
)
insight("Uses only postings with yearly salary values and hides groups with fewer than three salary records.")

chart_card("Average Salary by Country", "Country-level salary comparison where enough salary data exists.")
st.plotly_chart(
    charts.salary_bar(salary_by_dimension(filtered_jobs, "job_country"), "job_country", "Average Salary by Country", theme),
    use_container_width=True,
    key="market_dashboard_salary_by_country",
)
insight("Compares salary levels by country where enough salary data exists.")

chart_card("Remote vs On-site Salary", "Salary averages by work-mode classification.")
st.plotly_chart(
    charts.remote_salary_chart(remote_salary(filtered_jobs), theme),
    use_container_width=True,
    key="market_dashboard_remote_salary",
)
insight("Compares salary averages for remote, on-site, and unknown-location postings.")

trend = monthly_trends(filtered_jobs)
chart_card("Job Posting Trends Over Time", "Monthly posting volume for the selected market segment.")
st.plotly_chart(
    charts.line(trend, "posted_month", "total_jobs", "Job Posting Trends Over Time", theme),
    use_container_width=True,
    key="market_dashboard_monthly_posting_trend",
)
insight("Tracks posting volume over time for the selected market segment.")

chart_card("Monthly Job-Market Growth", "Month-over-month percentage change in matching postings.")
st.plotly_chart(
    charts.line(trend.dropna(subset=["job_growth_percentage"]), "posted_month", "job_growth_percentage", "Monthly Job-Market Growth", theme),
    use_container_width=True,
    key="market_dashboard_monthly_growth",
)
insight("Shows month-over-month percentage change. Volatility can reflect seasonality or source coverage changes.")

chart_card("Skills Associated With Highest Salaries", "Skills ranked by average yearly salary where salary data exists.")
st.plotly_chart(
    charts.salary_bar(high_salary_skills(filtered_jobs, filtered_skills), "clean_skill_name", "Skills Associated With Highest Salaries", theme),
    use_container_width=True,
    key="market_dashboard_high_salary_skills",
)
insight("Ranks skills by average yearly salary among postings with salary data.")

chart_card("Data Engineer Skill Demand", "Skill demand within matching Data Engineer postings.")
data_engineer_jobs = filtered_jobs[filtered_jobs["job_title_short"].eq("Data Engineer")]
data_engineer_skills = skills_for_jobs(filtered_skills, data_engineer_jobs)
st.plotly_chart(
    charts.bar(top_skills(data_engineer_skills), "clean_skill_name", "postings", "Data Engineer Skill Demand", theme),
    use_container_width=True,
    key="market_dashboard_data_engineer_skill_demand",
)
insight("Focuses on Data Engineer postings in the current filter context.")

footer()
