from __future__ import annotations

import base64
import html
from pathlib import Path

import streamlit as st

from portfolio.content.profile import PROFILE


KPI_ICONS = {
    "Total postings": "JP",
    "Companies": "CO",
    "Countries": "GL",
    "Skills": "SK",
    "Avg salary": "$",
    "Median salary": "MD",
    "Remote share": "RM",
    "Salary coverage": "%",
}

FOOTER_EMAIL_URL = PROFILE["mailto_url"]
PROFILE_PHOTO_PATH = Path(__file__).resolve().parents[1] / "assets" / "profile" / "peter.jpg"


def _profile_photo_markup() -> str:
    if not PROFILE_PHOTO_PATH.exists():
        return '<div class="brand-icon">P</div>'

    encoded_photo = base64.b64encode(PROFILE_PHOTO_PATH.read_bytes()).decode("ascii")
    return (
        '<img class="brand-photo" '
        'src="data:image/jpeg;base64,'
        f'{encoded_photo}" '
        'alt="Peter profile photo">'
    )


def sidebar_brand() -> None:
    profile_photo = _profile_photo_markup()
    st.sidebar.markdown(
        f"""
        <div class="sidebar-brand">
            {profile_photo}
            <div>
                <div class="brand-title">{html.escape(PROFILE["full_name"])}</div>
                <div class="brand-subtitle">Junior Data Engineer</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def app_header(kicker: str, title: str, subtitle: str, location: str) -> dict[str, str]:
    st.markdown(
        f"""
        <div class="page-header page-header-{html.escape(location)}">
            <div class="product-kicker">{html.escape(kicker)}</div>
            <h1 class="product-title">{html.escape(title)}</h1>
            <div class="product-subtitle">{html.escape(subtitle)}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    return {}


def sidebar_bottom() -> None:
    sidebar_brand()
    links = []
    if PROFILE.get("github_url"):
        links.append(f'<a href="{html.escape(PROFILE["github_url"])}" rel="noreferrer">GitHub</a>')
    if PROFILE.get("linkedin_url"):
        links.append(f'<a href="{html.escape(PROFILE["linkedin_url"])}" rel="noreferrer">LinkedIn</a>')
    links_markup = " | ".join(links)
    st.sidebar.markdown(
        f"""
        <div class="sidebar-links">{links_markup}</div>
        <div class="sidebar-divider"></div>
        """,
        unsafe_allow_html=True,
    )


def section_card(title: str, body: str, class_name: str = "") -> None:
    classes = " ".join(["section-card", class_name]).strip()
    tabindex = ' tabindex="0"' if class_name else ""
    st.markdown(
        f"""
        <div class="{html.escape(classes)}"{tabindex}>
            <div class="section-title">{html.escape(title)}</div>
            <div class="section-copy">{html.escape(body)}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def kpi_grid(values: dict[str, str]) -> None:
    notes = {
        "Total postings": "Filtered posting count",
        "Companies": "Distinct organizations",
        "Countries": "Distinct job countries",
        "Skills": "Distinct technical skills",
        "Avg salary": "Yearly salary records only",
        "Median salary": "Yearly salary records only",
        "Remote share": "Remote status classification",
        "Salary coverage": "Postings with salary data",
    }
    cols = st.columns(4)
    for index, (label, value) in enumerate(values.items()):
        icon = KPI_ICONS.get(label, "*")
        note = notes.get(label, "")
        if value == "N/A" and label in {"Avg salary", "Median salary"}:
            note = "No yearly salary records for this selection"
        with cols[index % 4]:
            st.markdown(
                f"""
                <div class="kpi-card">
                    <div class="kpi-icon">{html.escape(icon)}</div>
                    <div class="kpi-label">{html.escape(label)}</div>
                    <div class="kpi-value">{html.escape(value)}</div>
                    <div class="kpi-note">{html.escape(note)}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )


def pipeline_visual(class_name: str = "") -> None:
    steps = [
        ("01", "Raw CSVs", "Input tables"),
        ("02", "Python / Pandas", "Prepared sample"),
        ("03", "PostgreSQL", "Warehouse tables"),
        ("04", "dbt Models", "Staging and joins"),
        ("05", "Quality Checks", "Validation SQL"),
        ("06", "Analytics Marts", "Business-ready marts"),
        ("07", "Streamlit Dashboard", "Interactive portfolio"),
    ]
    step_classes = " ".join(["pipeline-step", class_name]).strip()
    tabindex = ' tabindex="0"' if class_name else ""
    markup = "".join(
        (
            f'<div class="{html.escape(step_classes)}"{tabindex}>'
            f'<span>{number}</span>'
            f'<strong>{html.escape(label)}</strong>'
            f'<small>{html.escape(output)}</small>'
            '</div>'
        )
        for number, label, output in steps
    )
    st.markdown(f'<div class="pipeline">{markup}</div>', unsafe_allow_html=True)


def insight(text: str) -> None:
    st.markdown(f'<div class="insight">{html.escape(text)}</div>', unsafe_allow_html=True)


def active_filter_chips(filters: dict[str, list[str] | tuple[float, float] | tuple[object, object] | None]) -> None:
    chips = []
    for label, value in filters.items():
        if value is None:
            continue
        if isinstance(value, list) and value:
            display = ", ".join(str(item) for item in value[:3])
            if len(value) > 3:
                display += f" +{len(value) - 3}"
            chips.append(f"{label}: {display}")
        elif isinstance(value, tuple):
            chips.append(f"{label}: active")
    if not chips:
        st.markdown('<div class="active-filter-wrap"><span class="active-chip">No active filters</span></div>', unsafe_allow_html=True)
        return
    markup = "".join(f'<span class="active-chip">{html.escape(chip)}</span>' for chip in chips)
    st.markdown(f'<div class="active-filter-wrap">{markup}</div>', unsafe_allow_html=True)


def footer() -> None:
    links = []
    if PROFILE.get("email"):
        links.append(f'<a href="{html.escape(FOOTER_EMAIL_URL)}">Email</a>')
    if PROFILE.get("linkedin_url"):
        links.append(f'<a href="{html.escape(PROFILE["linkedin_url"])}" rel="noreferrer">LinkedIn</a>')
    if PROFILE.get("github_url"):
        links.append(f'<a href="{html.escape(PROFILE["github_url"])}" rel="noreferrer">GitHub</a>')
    links_markup = " | ".join(links)
    st.markdown(
        f'<div class="footer">Peter &mdash; Junior Data Engineer<br>{html.escape(PROFILE["availability"])}<br>{links_markup}</div>',
        unsafe_allow_html=True,
    )


def metric_status_card(sample_rows: int, source_rows: int | str, class_name: str = "") -> None:
    source_value = f"{source_rows:,}" if isinstance(source_rows, int) else html.escape(str(source_rows))
    sample_value = f"{sample_rows:,}" if isinstance(sample_rows, int) else html.escape(str(sample_rows))
    classes = " ".join(["dataset-card", class_name]).strip()
    tabindex = ' tabindex="0"' if class_name else ""
    st.markdown(
        f"""
        <div class="{html.escape(classes)}"{tabindex}>
            <div class="dataset-icon">DB</div>
            <div class="dataset-metrics">
                <div>
                    <div class="dataset-value">{sample_value}</div>
                    <div class="dataset-label">hosted sample postings</div>
                </div>
                <div>
                    <div class="dataset-value">{source_value}</div>
                    <div class="dataset-label">source postings</div>
                </div>
                <div>
                    <div class="dataset-value">Verified</div>
                    <div class="dataset-label">real project data</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def purpose_cards(class_name: str = "") -> None:
    cards = [
        ("Understand Demand", "See which roles, companies, and markets show the strongest hiring activity."),
        ("Compare Salaries", "Review salary patterns across roles, countries, and remote-work status where salary data exists."),
        ("Track Skills", "Explore the technical skills most associated with job postings and Data Engineer demand."),
    ]
    columns = st.columns(3)
    for column, (title, body) in zip(columns, cards):
        with column:
            section_card(title, body, class_name=class_name)


def challenge_points(class_name: str = "") -> None:
    points = [
        "Inconsistent locations",
        "Missing salary values",
        "Duplicate relationships",
        "Aggregator companies",
        "Noisy job-posting records",
    ]
    markup = "".join(f'<span class="challenge-chip">{html.escape(point)}</span>' for point in points)
    classes = " ".join(["challenge-panel", class_name]).strip()
    tabindex = ' tabindex="0"' if class_name else ""
    st.markdown(f'<div class="{html.escape(classes)}"{tabindex}>{markup}</div>', unsafe_allow_html=True)


def chart_card(title: str, description: str):
    st.markdown(
        f"""
        <div class="chart-card-heading">
            <div class="section-title">{html.escape(title)}</div>
            <div class="section-copy">{html.escape(description)}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def badge_row(items: list[str]) -> None:
    markup = "".join(f'<span class="meta-pill">{html.escape(item)}</span>' for item in items)
    st.markdown(f"<div>{markup}</div>", unsafe_allow_html=True)


def _project_pipeline_visual() -> str:
    stages = [
        ("raw", "Raw Data", "Source", "M4 5h16v14H4z M7 9h10 M7 13h7"),
        ("etl", "Python ETL", "Pandas", "M12 3v18 M5 8h14 M5 16h14"),
        ("warehouse project-warehouse-stage", "PostgreSQL", "Warehouse", "M6 6c0-1.7 12-1.7 12 0v12c0 1.7-12 1.7-12 0V6z M6 6c0 1.7 12 1.7 12 0 M6 12c0 1.7 12 1.7 12 0"),
        ("marts", "dbt Marts", "Analytics", "M5 18V8l7-4 7 4v10 M9 18v-6h6v6"),
        ("dashboard", "Dashboard", "Streamlit", "M4 5h16v12H4z M8 21h8 M12 17v4"),
    ]
    stage_markup = []
    for index, (class_name, label, detail, icon_path) in enumerate(stages, start=1):
        stage_markup.append(
            f"""
            <div class="project-pipeline-stage project-pipeline-stage-{index} {class_name}">
                <svg class="project-pipeline-icon" viewBox="0 0 24 24" aria-hidden="true">
                    <path d="{icon_path}"></path>
                </svg>
                <span class="project-pipeline-label">{html.escape(label)}</span>
                <span class="project-pipeline-detail">{html.escape(detail)}</span>
            </div>
            """
        )
        if index < len(stages):
            stage_markup.append(f'<div class="project-pipeline-connector project-pipeline-connector-{index}" aria-hidden="true"></div>')

    particles = "".join(
        f'<span class="project-pipeline-particle project-pipeline-particle-{index}" aria-hidden="true"></span>'
        for index in range(1, 4)
    )
    return (
        '<div class="project-visual project-pipeline-banner" '
        'aria-label="Data pipeline from raw data through Python ETL, PostgreSQL, dbt marts, and dashboard">'
        '<div class="project-pipeline-track">'
        f'{particles}'
        f'{"".join(stage_markup)}'
        '</div>'
        '</div>'
    )


def project_card(project: dict, *, actions: bool = False, featured: bool = False) -> None:
    tech_markup = "".join(
        f'<span class="meta-pill">{html.escape(tech)}</span>' for tech in project.get("technologies", [])[:6]
    )
    action_markup = ""
    if actions:
        demo_url = project.get("demo_url") or "/market_dashboard"
        repository_url = project.get("repository_url", "")
        repository_link = (
            f'<a class="project-action" href="{html.escape(repository_url)}" rel="noopener noreferrer">GitHub Repository</a>'
            if repository_url
            else ""
        )
        case_study_link = (
            ""
            if featured and project.get("slug") == "job-market-intelligence"
            else '<a class="project-action project-action-primary" href="/project_overview">View Case Study</a>'
        )
        demo_class = "project-action project-action-primary" if not case_study_link else "project-action"
        action_markup = (
            '<div class="project-actions">'
            f'{case_study_link}'
            f'<a class="{demo_class}" href="{html.escape(demo_url)}">Live Demo</a>'
            f'{repository_link}'
            '</div>'
        )
    card_class = "project-card project-card-featured" if featured else "project-card"
    visual_markup = (
        _project_pipeline_visual()
        if featured and project.get("slug") == "job-market-intelligence"
        else '<div class="project-visual">DATA</div>'
    )
    st.markdown(
        f"""
        <div class="{card_class}">
            {visual_markup}
            <div class="project-meta">{html.escape(project.get("category", ""))} | {html.escape(project.get("status", ""))}</div>
            <div class="project-title">{html.escape(project["title"])}</div>
            <div class="section-copy">{html.escape(project["short_description"])}</div>
            <div class="project-metric">{html.escape(project.get("key_metric", ""))}</div>
            <div>{tech_markup}</div>
            {action_markup}
        </div>
        """,
        unsafe_allow_html=True,
    )


def timeline_entry(entry: dict, class_name: str = "") -> None:
    responsibilities = "".join(
        f"<li>{html.escape(item)}</li>" for item in entry.get("responsibilities", [])
    )
    technologies = "".join(
        f'<span class="meta-pill">{html.escape(item)}</span>' for item in entry.get("technologies", [])
    )
    classes = " ".join(["timeline-card", class_name]).strip()
    tabindex = ' tabindex="0"' if class_name else ""
    st.markdown(
        f"""
        <div class="{html.escape(classes)}"{tabindex}>
            <div class="timeline-date">{html.escape(entry["start_date"])} - {html.escape(entry["end_date"])}</div>
            <div class="project-title">{html.escape(entry["role"])}</div>
            <div class="project-meta">{html.escape(entry["company"])} | {html.escape(entry.get("location", ""))}</div>
            {f'<div class="section-copy">{html.escape(entry["summary"])}</div>' if entry.get("summary") else ""}
            <ul>{responsibilities}</ul>
            <div>{technologies}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def skill_group_card(title: str, skills: list[str], class_name: str = "") -> None:
    skills_markup = "".join(
        f'<span class="challenge-chip skill-chip">{html.escape(skill)}</span>' for skill in skills
    )
    classes = " ".join(["section-card", "skill-card", class_name]).strip()
    tabindex = ' tabindex="0"' if class_name else ""
    st.markdown(
        f"""
        <div class="{html.escape(classes)}"{tabindex}>
            <div class="section-title">{html.escape(title)}</div>
            <div class="skill-chip-wrap">{skills_markup}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
