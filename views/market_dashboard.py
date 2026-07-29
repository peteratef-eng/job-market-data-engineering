from __future__ import annotations

import html
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

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
from ui.components import app_header, chart_card, data_lineage
from ui.styles import inject_global_styles
from ui.theme import current_theme


MARKET_DASHBOARD_CHART_KEYS = (
    "market_dashboard_chart_job_title_demand",
    "market_dashboard_chart_company_activity",
    "market_dashboard_chart_salary_by_job_title",
    "market_dashboard_chart_salary_by_country",
    "market_dashboard_chart_remote_salary",
    "market_dashboard_chart_monthly_posting_trend",
    "market_dashboard_chart_monthly_growth",
    "market_dashboard_chart_technical_skill_demand",
    "market_dashboard_chart_high_salary_skills",
    "market_dashboard_chart_data_engineer_skill_demand",
)


def initialize_market_dashboard_chart_reveal() -> None:
    chart_keys = ",\n".join(f'"{key}"' for key in MARKET_DASHBOARD_CHART_KEYS)
    components.html(
        f"""
        <script>
        (function () {{
            try {{
                const parentWindow = window.parent;
                const parentDocument = parentWindow.document;

                if (!parentWindow || !parentDocument) {{
                    return;
                }}

                const chartKeys = [
                    {chart_keys}
                ];
                const keyClasses = chartKeys.map(function (key) {{
                    return "st-key-" + key;
                }});
                const chartSelector = keyClasses.map(function (className) {{
                    return "." + className;
                }}).join(",");
                const readyClass = "market-chart-reveal-ready";
                const visibleClass = "market-chart-reveal-visible";
                const completeClass = "market-chart-reveal-complete";
                const state = parentWindow.__marketDashboardChartReveal || {{
                    revealedKeys: new Set()
                }};
                parentWindow.__marketDashboardChartReveal = state;

                if (state.observer) {{
                    state.observer.disconnect();
                }}
                if (state.mutationObserver) {{
                    state.mutationObserver.disconnect();
                }}
                if (state.failSafeTimer) {{
                    parentWindow.clearTimeout(state.failSafeTimer);
                }}
                state.observerActive = false;

                const reducedMotion = parentWindow.matchMedia &&
                    parentWindow.matchMedia("(prefers-reduced-motion: reduce)").matches;
                const observedNodes = new WeakSet();

                function chartKeyFor(element) {{
                    for (let index = 0; index < chartKeys.length; index += 1) {{
                        if (element.classList.contains(keyClasses[index])) {{
                            return chartKeys[index];
                        }}
                    }}
                    return "";
                }}

                function finishReveal(element, key) {{
                    if (!element || !key) {{
                        return;
                    }}
                    element.classList.remove(readyClass, visibleClass);
                    element.classList.add(completeClass);
                    state.revealedKeys.add(key);
                    if (state.observer) {{
                        state.observer.unobserve(element);
                    }}
                }}

                function reveal(element, key) {{
                    if (!element || !key || element.classList.contains(completeClass)) {{
                        return;
                    }}
                    parentWindow.requestAnimationFrame(function () {{
                        parentWindow.requestAnimationFrame(function () {{
                            element.classList.remove(readyClass, completeClass);
                            element.classList.add(visibleClass);
                            parentWindow.setTimeout(function () {{
                                finishReveal(element, key);
                            }}, 700);
                        }});
                    }});
                }}

                function prepareChart(element) {{
                    const key = chartKeyFor(element);
                    if (!key) {{
                        return;
                    }}
                    if (reducedMotion || state.revealedKeys.has(key) || !("IntersectionObserver" in parentWindow)) {{
                        finishReveal(element, key);
                        return;
                    }}
                    if (observedNodes.has(element)) {{
                        return;
                    }}
                    try {{
                        state.observer.observe(element);
                        observedNodes.add(element);
                        element.classList.remove(visibleClass, completeClass);
                        element.classList.add(readyClass);
                    }} catch (error) {{
                        finishReveal(element, key);
                    }}
                }}

                function findCharts(root) {{
                    if (!root || (root.nodeType !== 1 && root.nodeType !== 9)) {{
                        return [];
                    }}
                    const matches = [];
                    if (root.matches && root.matches(chartSelector)) {{
                        matches.push(root);
                    }}
                    if (root.querySelectorAll) {{
                        root.querySelectorAll(chartSelector).forEach(function (element) {{
                            matches.push(element);
                        }});
                    }}
                    return matches;
                }}

                state.observer = new parentWindow.IntersectionObserver(function (entries) {{
                    entries.forEach(function (entry) {{
                        if (entry.isIntersecting || entry.intersectionRatio >= 0.12) {{
                            const element = entry.target;
                            reveal(element, chartKeyFor(element));
                        }}
                    }});
                }}, {{
                    threshold: 0.12,
                    rootMargin: "0px 0px -5% 0px"
                }});

                findCharts(parentDocument).forEach(prepareChart);

                const appView = parentDocument.querySelector('[data-testid="stMainBlockContainer"]') ||
                    parentDocument.querySelector('[data-testid="stAppViewContainer"]') ||
                    parentDocument.querySelector("main") ||
                    parentDocument.body;
                state.mutationObserver = new parentWindow.MutationObserver(function (mutations) {{
                    mutations.forEach(function (mutation) {{
                        mutation.addedNodes.forEach(function (node) {{
                            findCharts(node).forEach(prepareChart);
                        }});
                    }});
                }});
                state.mutationObserver.observe(appView, {{
                    childList: true,
                    subtree: true
                }});
                state.observerActive = true;
                state.failSafeTimer = parentWindow.setTimeout(function () {{
                    if (!state.observerActive) {{
                        parentDocument.querySelectorAll("." + readyClass).forEach(function (element) {{
                            finishReveal(element, chartKeyFor(element));
                        }});
                    }}
                }}, 3000);

                parentWindow.addEventListener("pagehide", function () {{
                    if (state.observer) {{
                        state.observer.disconnect();
                    }}
                    if (state.mutationObserver) {{
                        state.mutationObserver.disconnect();
                    }}
                }}, {{ once: true }});
            }} catch (error) {{
                try {{
                    const parentDocument = window.parent.document;
                    parentDocument.querySelectorAll(".market-chart-reveal-ready").forEach(function (element) {{
                        element.classList.remove("market-chart-reveal-ready", "market-chart-reveal-visible");
                        element.classList.add("market-chart-reveal-complete");
                    }});
                }} catch (fallbackError) {{}}
            }}
        }})();
        </script>
        """,
        height=0,
    )


theme = current_theme()
inject_global_styles(theme)


app_header(
    "Market Dashboard",
    "Hiring Demand and Salary Signals",
    "Explore hiring demand, salaries, technical skills, remote-work patterns, and market trends across the hosted job-posting sample.",
    "dashboard",
)
data_lineage("dashboard")
initialize_market_dashboard_chart_reveal()


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
    return {
        "filtered_jobs": filtered_jobs_data,
        "filtered_skills": filtered_skills_data,
        "kpis": kpi_values(filtered_jobs_data, filtered_skills_data),
        "coverage": (coverage_label_data, salary_records_data, total_records_data),
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


def active_filter_count(
    job_titles: list[str],
    countries: list[str],
    selected_skills: list[str],
    companies: list[str],
    remote_statuses: list[str],
    salary_range: tuple[float, float] | None,
    selected_dates: tuple[object, object] | list[object],
) -> int:
    count = sum(bool(value) for value in (job_titles, countries, selected_skills, companies, remote_statuses))
    if salary_range and salary_range != (salary_min, salary_max):
        count += 1
    if isinstance(selected_dates, (list, tuple)) and len(selected_dates) == 2:
        if selected_dates[0] != date_min or selected_dates[1] != date_max:
            count += 1
    return count


def dashboard_kpi_panel(values: dict[str, str]) -> None:
    primary = [
        ("Matching Jobs", values["Total postings"], "Filtered postings"),
        ("Average Salary", values["Avg salary"], "Salary records only"),
        ("Companies", values["Companies"], "Distinct organizations"),
        ("Remote Share", values["Remote share"], "Remote classification"),
    ]
    markup = "".join(
        (
            f'<div class="dashboard-primary-kpi dashboard-primary-kpi-{index}">'
            f'<div class="dashboard-kpi-label">{html.escape(label)}</div>'
            f'<div class="dashboard-kpi-value">{html.escape(value)}</div>'
            f'<div class="dashboard-kpi-note">{html.escape(note)}</div>'
            '</div>'
        )
        for index, (label, value, note) in enumerate(primary, start=1)
    )
    st.markdown(f'<section class="dashboard-primary-kpis">{markup}</section>', unsafe_allow_html=True)


def dashboard_metadata_strip(values: dict[str, str]) -> None:
    metadata_items = [
        ("Median Salary", values["Median salary"]),
        ("Salary Coverage", values["Salary coverage"]),
    ]
    markup = "".join(
        (
            f'<div class="dashboard-meta-item dashboard-meta-item-{index}">'
            f'<span>{html.escape(label)}</span>'
            f'<strong>{html.escape(value)}</strong>'
            '</div>'
        )
        for index, (label, value) in enumerate(metadata_items, start=1)
    )
    st.markdown(f'<section class="dashboard-metadata-strip">{markup}</section>', unsafe_allow_html=True)


def rank_limit_control(key: str) -> int:
    choice = st.radio(
        "Rows",
        ["Top 10", "Top 15"],
        horizontal=True,
        label_visibility="collapsed",
        key=key,
    )
    return 10 if choice == "Top 10" else 15


def render_chart(figure, key: str, *, remove_y_title: bool = True) -> None:
    if remove_y_title:
        figure.update_yaxes(title_text=None)
    if figure.layout.height and figure.layout.height > 520:
        figure.update_layout(height=520)
    st.plotly_chart(figure, width="stretch", key=key)


with st.container(key="dashboard_filter_panel"):
    st.markdown('<div class="filter-title">Filters</div>', unsafe_allow_html=True)
    primary_filter_cols = st.columns(4)
    with primary_filter_cols[0]:
        job_titles = st.multiselect("Job title", filter_options["job_titles"], key="job_titles")
    with primary_filter_cols[1]:
        countries = st.multiselect("Country", filter_options["countries"], key="countries")
    with primary_filter_cols[2]:
        selected_skills = st.multiselect("Skill", filter_options["skills"], key="selected_skills")
    with primary_filter_cols[3]:
        remote_statuses = st.multiselect("Work mode", filter_options["remote_statuses"], key="remote_statuses")

    with st.expander("Advanced Filters", expanded=False):
        advanced_filter_cols = st.columns([1.35, 1, 1])
        with advanced_filter_cols[0]:
            companies = st.multiselect("Company", filter_options["companies"], key="companies")
        with advanced_filter_cols[1]:
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
        with advanced_filter_cols[2]:
            selected_dates = st.date_input(
                "Posted date range",
                value=(date_min, date_max),
                min_value=date_min,
                max_value=date_max,
                key="selected_dates",
            )

date_range = None
date_range_values = None
if isinstance(selected_dates, (list, tuple)) and len(selected_dates) == 2:
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
active_filters = active_filter_count(
    job_titles,
    countries,
    selected_skills,
    companies,
    remote_statuses,
    salary_range,
    selected_dates,
)
status_text = (
    "No active filters &middot; Showing full hosted sample"
    if active_filters == 0
    else f"{len(filtered_jobs):,} results &middot; {active_filters} active filters"
)
status_cols = st.columns([1, 0.22])
with status_cols[0]:
    st.markdown(
        f'<div class="dashboard-results-status">{status_text}</div>',
        unsafe_allow_html=True,
    )
with status_cols[1]:
    if active_filters:
        st.button("Reset Filters", type="secondary", on_click=reset_dashboard_filters)

if filtered_jobs.empty:
    st.warning("No matching records. Remove one or more filters to continue.")
    st.stop()

source_rows = results["source_rows"]
sample_rows = results["sample_rows"]
coverage_label, salary_records, total_records = results["coverage"]
kpis = results["kpis"]
dashboard_kpi_panel(kpis)
dashboard_metadata_strip(kpis)

st.subheader("Demand")
demand_choice = st.radio(
    "Demand chart",
    ["Job Titles", "Companies"],
    horizontal=True,
    label_visibility="collapsed",
    key="market_dashboard_demand_chart_choice",
)
demand_limit = rank_limit_control("market_dashboard_demand_rank_limit")
if demand_choice == "Job Titles":
    with st.container(key="market_dashboard_chart_job_title_demand"):
        chart_card("Most In-Demand Job Titles", "Role categories with the highest posting volume.")
        render_chart(
            charts.bar(
                top_counts(filtered_jobs, "job_title_short", demand_limit),
                "job_title_short",
                "postings",
                "Most In-Demand Job Titles",
                theme,
            ),
            "market_dashboard_job_title_demand",
        )
else:
    with st.container(key="market_dashboard_chart_company_activity"):
        chart_card("Top Hiring Companies", "Companies or platforms with the most matching postings.")
        render_chart(
            charts.bar(
                top_counts(filtered_jobs, "clean_company_name", demand_limit),
                "clean_company_name",
                "postings",
                "Top Hiring Companies",
                theme,
            ),
            "market_dashboard_company_activity",
        )
        st.caption("Company rankings may include job boards or aggregators.")

st.subheader("Salary Insights")
st.caption(
    f"Salary analysis is based on {salary_records:,} records in the current result set."
)
salary_choice = st.radio(
    "Salary chart",
    ["By Job Title", "By Country", "Work Mode"],
    horizontal=True,
    label_visibility="collapsed",
    key="market_dashboard_salary_chart_choice",
)
if salary_choice in {"By Job Title", "By Country"}:
    salary_limit = rank_limit_control("market_dashboard_salary_rank_limit")
if salary_choice == "By Job Title":
    with st.container(key="market_dashboard_chart_salary_by_job_title"):
        chart_card("Average Salary by Job Title", "Salary averages by role where enough yearly salary data exists.")
        render_chart(
            charts.salary_bar(
                salary_by_dimension(filtered_jobs, "job_title_short", salary_limit),
                "job_title_short",
                "Average Salary by Job Title",
                theme,
            ),
            "market_dashboard_salary_by_job_title",
        )
elif salary_choice == "By Country":
    with st.container(key="market_dashboard_chart_salary_by_country"):
        chart_card("Average Salary by Country", "Country-level salary comparison where enough salary data exists.")
        render_chart(
            charts.salary_bar(
                salary_by_dimension(filtered_jobs, "job_country", salary_limit),
                "job_country",
                "Average Salary by Country",
                theme,
            ),
            "market_dashboard_salary_by_country",
        )
else:
    with st.container(key="market_dashboard_chart_remote_salary"):
        chart_card("Remote vs On-site Salary", "Salary averages by work-mode classification.")
        render_chart(
            charts.remote_salary_chart(remote_salary(filtered_jobs), theme),
            "market_dashboard_remote_salary",
            remove_y_title=False,
        )

st.subheader("Market Trends")
trend_choice = st.radio(
    "Trend chart",
    ["Posting Volume", "Monthly Growth"],
    horizontal=True,
    label_visibility="collapsed",
    key="market_dashboard_trend_chart_choice",
)
trend = monthly_trends(filtered_jobs)
if trend_choice == "Posting Volume":
    with st.container(key="market_dashboard_chart_monthly_posting_trend"):
        chart_card("Job Posting Trends Over Time", "Monthly posting volume for the selected market segment.")
        render_chart(
            charts.line(trend, "posted_month", "total_jobs", "Job Posting Trends Over Time", theme),
            "market_dashboard_monthly_posting_trend",
            remove_y_title=False,
        )
else:
    with st.container(key="market_dashboard_chart_monthly_growth"):
        chart_card("Monthly Job-Market Growth", "Month-over-month percentage change in matching postings.")
        render_chart(
            charts.line(
                trend.dropna(subset=["job_growth_percentage"]),
                "posted_month",
                "job_growth_percentage",
                "Monthly Job-Market Growth",
                theme,
            ),
            "market_dashboard_monthly_growth",
            remove_y_title=False,
        )

st.subheader("Technical Skills")
skill_choice = st.radio(
    "Technical skills chart",
    ["Overall Demand", "Highest Salaries", "Data Engineer"],
    horizontal=True,
    label_visibility="collapsed",
    key="market_dashboard_skill_chart_choice",
)
skill_limit = rank_limit_control("market_dashboard_skill_rank_limit")
if skill_choice == "Overall Demand":
    with st.container(key="market_dashboard_chart_technical_skill_demand"):
        chart_card("Most In-Demand Technical Skills", "Unique postings connected to each skill in the selected market.")
        render_chart(
            charts.bar(
                top_skills(filtered_skills, skill_limit),
                "clean_skill_name",
                "postings",
                "Most In-Demand Technical Skills",
                theme,
            ),
            "market_dashboard_technical_skill_demand",
        )
elif skill_choice == "Highest Salaries":
    with st.container(key="market_dashboard_chart_high_salary_skills"):
        chart_card("Skills Associated With Highest Salaries", "Skills ranked by average yearly salary where salary data exists.")
        render_chart(
            charts.salary_bar(
                high_salary_skills(filtered_jobs, filtered_skills, skill_limit),
                "clean_skill_name",
                "Skills Associated With Highest Salaries",
                theme,
            ),
            "market_dashboard_high_salary_skills",
        )
else:
    data_engineer_jobs = filtered_jobs[filtered_jobs["job_title_short"].eq("Data Engineer")]
    data_engineer_skills = skills_for_jobs(filtered_skills, data_engineer_jobs)
    with st.container(key="market_dashboard_chart_data_engineer_skill_demand"):
        chart_card("Data Engineer Skill Demand", "Skill demand within matching Data Engineer postings.")
        render_chart(
            charts.bar(
                top_skills(data_engineer_skills, skill_limit),
                "clean_skill_name",
                "postings",
                "Data Engineer Skill Demand",
                theme,
            ),
            "market_dashboard_data_engineer_skill_demand",
        )

with st.expander("Methodology & Data Notes", expanded=False):
    st.markdown(
        f"""
        <div class="dashboard-methodology">
            <p><strong>Hosted sample:</strong> {sample_rows:,} of {source_rows:,} source postings.</p>
            <p><strong>Countries:</strong> {html.escape(kpis["Countries"])} distinct job countries in the current result set.</p>
            <p><strong>Skills:</strong> {html.escape(kpis["Skills"])} distinct technical skills in the current result set.</p>
            <p><strong>Salary coverage:</strong> Salary analysis uses postings with yearly salary values; missing salaries are excluded from salary charts.</p>
            <p><strong>Minimum salary sample:</strong> Salary groups require at least 3 salary records.</p>
            <p><strong>Remote work:</strong> Unknown remote status is retained as its own classification when present.</p>
            <p><strong>Companies:</strong> Rankings may include job boards or aggregators.</p>
            <p><strong>Monthly trends:</strong> Monthly volatility may reflect seasonality or changes in source coverage.</p>
            <p><strong>Skills:</strong> Skill demand counts unique postings connected through job-skill relationships.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    '<div class="dashboard-compact-footer">Built by Peter Atef &middot; '
    '<a href="https://github.com/peteratef-eng/job-market-data-engineering" rel="noopener noreferrer">GitHub</a>'
    '</div>',
    unsafe_allow_html=True,
)
