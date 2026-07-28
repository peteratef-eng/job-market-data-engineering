from __future__ import annotations

import pandas as pd
import plotly.express as px

from ui.chart_theme import apply_chart_theme


LABELS = {
    "avg_salary": "Average salary",
    "clean_company_name": "Company",
    "clean_skill_name": "Technical skill",
    "job_country": "Country",
    "job_growth_percentage": "Monthly growth percentage",
    "job_title_short": "Job title",
    "posted_month": "Posted month",
    "postings": "Number of postings",
    "remote_status": "Work mode",
    "salary_jobs": "Salary records",
    "total_jobs": "Number of postings",
}


def chart_height(row_count: int = 0) -> int:
    return min(600, max(500, 170 + (row_count * 34)))


def empty_figure(title: str, theme: dict[str, str]):
    fig = px.scatter()
    fig.add_annotation(
        text="No data for the selected filters",
        showarrow=False,
        x=0.5,
        y=0.5,
        font=dict(color=theme["muted_text"], size=14),
    )
    fig.update_xaxes(visible=False)
    fig.update_yaxes(visible=False)
    return style(fig, theme)


def style(fig, theme: dict[str, str]):
    fig.update_layout(
        legend_title_text="",
        modebar_remove=[
            "zoom",
            "pan",
            "select",
            "lasso2d",
            "zoomIn",
            "zoomOut",
            "autoScale",
            "resetScale",
        ],
    )
    return apply_chart_theme(fig, theme)


def bar(df: pd.DataFrame, x: str, y: str, title: str, theme: dict[str, str], orientation: str = "h"):
    if df.empty:
        return empty_figure(title, theme)
    plot_df = df.sort_values(y, ascending=True) if orientation == "h" else df
    fig = px.bar(
        plot_df,
        x=y if orientation == "h" else x,
        y=x if orientation == "h" else y,
        orientation=orientation,
        labels=LABELS,
        color_discrete_sequence=theme["palette"],
        text=y,
        height=chart_height(len(plot_df)),
    )
    fig.update_traces(
        texttemplate="%{text:,.0f}",
        textposition="outside",
        cliponaxis=False,
        marker_line_width=0,
        hovertemplate="<b>%{y}</b><br>Postings: %{x:,.0f}<extra></extra>"
        if orientation == "h"
        else "<b>%{x}</b><br>Postings: %{y:,.0f}<extra></extra>",
    )
    fig = style(fig, theme)
    fig.update_layout(margin=dict(l=180 if orientation == "h" else 82, r=110, t=14, b=68))
    return fig


def salary_bar(df: pd.DataFrame, dimension: str, title: str, theme: dict[str, str]):
    if df.empty:
        return empty_figure(title, theme)
    plot_df = df.sort_values("avg_salary", ascending=True)
    hover_data = {"salary_jobs": ":,", "avg_salary": ":$,.0f"}
    if "median_salary" in plot_df.columns:
        hover_data["median_salary"] = ":$,.0f"
    fig = px.bar(
        plot_df,
        x="avg_salary",
        y=dimension,
        orientation="h",
        labels=LABELS,
        hover_data=hover_data,
        color_discrete_sequence=[theme["positive"]],
        height=chart_height(len(plot_df)),
    )
    fig.update_xaxes(tickprefix="$")
    fig.update_traces(marker_line_width=0, hovertemplate="<b>%{y}</b><br>Avg salary: $%{x:,.0f}<extra></extra>")
    fig = style(fig, theme)
    fig.update_layout(margin=dict(l=180, r=120, t=14, b=68))
    return fig


def line(df: pd.DataFrame, x: str, y: str, title: str, theme: dict[str, str]):
    if df.empty:
        return empty_figure(title, theme)
    fig = px.line(
        df,
        x=x,
        y=y,
        labels=LABELS,
        markers=True,
        color_discrete_sequence=[theme["accent"]],
        height=520,
    )
    fig.update_traces(line_width=3, marker_size=7, hovertemplate="%{x|%b %Y}<br>%{y:,.2f}<extra></extra>")
    fig = style(fig, theme)
    fig.update_layout(margin=dict(l=90, r=45, t=14, b=68))
    return fig


def remote_salary_chart(df: pd.DataFrame, theme: dict[str, str]):
    if df.empty:
        return empty_figure("Remote vs On-site Salary", theme)
    fig = px.bar(
        df,
        x="remote_status",
        y="avg_salary",
        labels=LABELS,
        hover_data={"salary_jobs": ":,", "avg_salary": ":$,.0f"},
        color="remote_status",
        color_discrete_sequence=theme["palette"],
        height=500,
    )
    fig.update_yaxes(tickprefix="$")
    fig.update_traces(marker_line_width=0, hovertemplate="<b>%{x}</b><br>Avg salary: $%{y:,.0f}<extra></extra>")
    fig = style(fig, theme)
    fig.update_layout(margin=dict(l=90, r=70, t=14, b=68))
    return fig
