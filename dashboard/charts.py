from __future__ import annotations

import pandas as pd
import plotly.express as px

from ui.chart_theme import apply_chart_theme


def empty_figure(title: str, theme: dict[str, str]):
    fig = px.scatter(title=title)
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
        title=title,
        color_discrete_sequence=theme["palette"],
        text=y,
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
    return style(fig, theme)


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
        title=title,
        hover_data=hover_data,
        color_discrete_sequence=[theme["positive"]],
    )
    fig.update_xaxes(tickprefix="$")
    fig.update_traces(marker_line_width=0, hovertemplate="<b>%{y}</b><br>Avg salary: $%{x:,.0f}<extra></extra>")
    return style(fig, theme)


def line(df: pd.DataFrame, x: str, y: str, title: str, theme: dict[str, str]):
    if df.empty:
        return empty_figure(title, theme)
    fig = px.line(
        df,
        x=x,
        y=y,
        title=title,
        markers=True,
        color_discrete_sequence=[theme["accent"]],
    )
    fig.update_traces(line_width=3, marker_size=7, hovertemplate="%{x|%b %Y}<br>%{y:,.2f}<extra></extra>")
    return style(fig, theme)


def remote_salary_chart(df: pd.DataFrame, theme: dict[str, str]):
    if df.empty:
        return empty_figure("Remote vs On-site Salary", theme)
    fig = px.bar(
        df,
        x="remote_status",
        y="avg_salary",
        title="Remote vs On-site Salary",
        hover_data={"salary_jobs": ":,", "avg_salary": ":$,.0f"},
        color="remote_status",
        color_discrete_sequence=theme["palette"],
    )
    fig.update_yaxes(tickprefix="$")
    fig.update_traces(marker_line_width=0, hovertemplate="<b>%{x}</b><br>Avg salary: $%{y:,.0f}<extra></extra>")
    return style(fig, theme)
