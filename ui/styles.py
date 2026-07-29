from __future__ import annotations

import streamlit as st


def inject_global_styles(theme: dict[str, str]) -> None:
    st.markdown(
        f"""
        <style>
        :root {{
            color-scheme: {theme["mode"]};
            --bg: {theme["background"]};
            --sidebar: {theme["sidebar"]};
            --surface: {theme["surface"]};
            --surface-2: {theme["surface_secondary"]};
            --surface-elevated: {theme["surface_elevated"]};
            --text: {theme["primary_text"]};
            --text-2: {theme["secondary_text"]};
            --muted: {theme["muted_text"]};
            --border: {theme["border"]};
            --accent: {theme["accent"]};
            --accent-hover: {theme["accent_hover"]};
            --accent-bright: {theme["bright_accent"]};
            --input-bg: {theme["input_bg"]};
            --input-text: {theme["input_text"]};
            --on-accent: {theme["on_accent"]};
            --tag-bg: {theme["tag_bg"]};
            --tag-text: {theme["tag_text"]};
            --positive: {theme["positive"]};
            --warning: {theme["warning"]};
            --negative: {theme["negative"]};
            --shadow: {theme["shadow"]};
            --shadow-accent: {theme["shadow_accent"]};
            --hover: {theme["hover"]};
            --disabled: {theme["disabled"]};
            --font: "Inter", "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        }}

        html, body, .stApp {{
            background: var(--bg);
            color: var(--text);
        }}
        .stApp, .block-container, [data-testid="stSidebar"], [data-testid="stSidebar"] * {{
            box-sizing: border-box;
        }}
        .material-icons,
        .material-icons-round,
        .material-icons-rounded,
        .material-symbols-outlined,
        .material-symbols-rounded,
        .material-symbols-sharp,
        [class*="material-icons"],
        [class*="material-symbols"] {{
            font-family: "Material Symbols Rounded", "Material Symbols Outlined", "Material Icons" !important;
            font-weight: normal !important;
            font-style: normal !important;
            font-size: 1.25rem;
            line-height: 1;
            letter-spacing: normal !important;
            text-transform: none !important;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            white-space: nowrap;
            word-wrap: normal;
            direction: ltr;
            font-feature-settings: "liga";
            -webkit-font-feature-settings: "liga";
            -webkit-font-smoothing: antialiased;
            text-rendering: optimizeLegibility;
        }}

        header[data-testid="stHeader"] {{
            background: var(--bg);
            color: var(--text);
            border-bottom: 1px solid transparent;
        }}

        .block-container {{
            max-width: 1220px;
            padding: .35rem 1.35rem 2.5rem;
        }}

        h1, h2, h3, h4 {{
            color: var(--text);
            font-family: var(--font);
            letter-spacing: 0;
            line-height: 1.15;
        }}
        h1 {{ font-size: clamp(2rem, 3.8vw, 3.35rem); font-weight: 700; }}
        h2 {{ font-size: clamp(1.65rem, 2.6vw, 2rem); font-weight: 650; margin-top: 1.4rem; }}
        h3 {{ font-size: 1.2rem; font-weight: 650; }}
        p, li {{
            color: var(--text-2);
            font-size: 1rem;
            line-height: 1.65;
            font-family: var(--font);
        }}
        a {{
            color: var(--accent);
            font-weight: 500;
            text-decoration: none;
        }}
        a:hover {{
            color: var(--accent-hover);
            text-decoration: underline;
        }}
        a:focus-visible {{
            outline: 3px solid color-mix(in srgb, var(--accent) 34%, transparent);
            outline-offset: 3px;
            border-radius: 6px;
        }}
        [data-testid="stHeadingWithActionElements"] a,
        h1 a, h2 a, h3 a {{
            opacity: 0;
            transition: opacity 140ms ease;
        }}
        [data-testid="stHeadingWithActionElements"]:hover a,
        [data-testid="stHeadingWithActionElements"]:focus-within a,
        h1:hover a, h2:hover a, h3:hover a {{
            opacity: 1;
        }}

        [data-testid="stSidebar"] {{
            background: var(--sidebar);
            border-right: 1px solid var(--border);
            overflow-x: clip;
        }}
        [data-testid="stSidebar"] > div:first-child {{
            padding: 1rem .85rem;
            max-width: 100%;
            min-width: 0;
        }}
        [data-testid="stSidebar"] label,
        [data-testid="stSidebar"] p {{
            color: var(--text-2);
            font-family: var(--font);
        }}
        [data-testid="stSidebarNav"] a {{
            width: 100%;
            max-width: 100%;
            min-width: 0;
            border-radius: 10px;
            color: var(--text-2);
            font-weight: 500;
            padding: .48rem .65rem;
            margin: .08rem 0;
            transition: background-color 180ms ease, border-color 180ms ease, color 180ms ease;
        }}
        [data-testid="stSidebarNav"] a:hover {{
            background: var(--hover);
            color: var(--text);
        }}
        [data-testid="stSidebarNav"] a[aria-current="page"] {{
            background: var(--tag-bg);
            color: var(--tag-text);
            border: 1px solid var(--border);
        }}

        .sidebar-brand {{
            display: flex;
            align-items: center;
            gap: .75rem;
            border: 1px solid var(--border);
            background: var(--surface);
            border-radius: 10px;
            padding: .68rem .72rem;
            margin: .2rem 0 1rem;
            box-shadow: var(--shadow);
            width: 100%;
            max-width: 100%;
            min-width: 0;
        }}
        .sidebar-brand > div:last-child {{
            min-width: 0;
        }}
        .brand-icon, .dataset-icon, .kpi-icon {{
            width: 36px;
            height: 36px;
            border-radius: 10px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            background: var(--tag-bg);
            color: var(--tag-text);
            font-weight: 700;
            flex: 0 0 auto;
        }}
        .brand-photo {{
            width: 44px;
            height: 44px;
            border-radius: 10px;
            flex: 0 0 44px;
            object-fit: cover;
            object-position: center top;
            display: block;
        }}
        .brand-title {{ color: var(--text); font-weight: 700; line-height: 1.15; }}
        .brand-subtitle {{ color: var(--muted); font-size: .82rem; margin-top: .12rem; }}
        .sidebar-bottom {{
            border-top: 1px solid var(--border);
            margin-top: clamp(1rem, 4vh, 2rem);
            padding-top: .85rem;
            width: 100%;
            max-width: 100%;
            min-width: 0;
        }}
        .sidebar-links {{
            margin-top: .7rem;
            color: var(--muted);
            font-size: .84rem;
        }}
        .sidebar-links a {{
            color: var(--accent-bright);
            text-decoration: none;
            font-weight: 500;
            transition: color 180ms ease, opacity 180ms ease;
        }}
        .sidebar-signature {{
            color: var(--muted);
            font-size: .78rem;
            margin-top: .55rem;
        }}

        .page-header {{
            margin: .15rem 0 1rem;
            max-width: 900px;
        }}
        .page-header-home,
        .page-header-overview {{
            margin-top: 1rem;
        }}
        .page-header-home .product-kicker {{
            color: #17367D;
            border-color: #B8CEF4;
            font-size: .96rem;
            font-weight: 700;
            padding: .5rem .875rem;
            white-space: normal;
        }}
        .page-header-overview {{
            margin-top: 1.55rem;
        }}
        .page-header-overview .product-kicker {{
            margin-bottom: .8rem;
        }}
        .product-kicker {{
            display: inline-flex;
            align-items: center;
            min-height: 1.9rem;
            line-height: 1.2;
            color: var(--tag-text);
            background: var(--tag-bg);
            border: 1px solid var(--border);
            border-radius: 999px;
            padding: .34rem .58rem;
            font-weight: 600;
            font-size: .82rem;
            margin-bottom: .6rem;
        }}
        .product-title {{
            color: var(--text);
            font-size: clamp(1.95rem, 4vw, 3.25rem);
            line-height: 1.1;
            font-weight: 700;
            margin: 0;
        }}
        .product-subtitle {{
            color: var(--text-2);
            max-width: 780px;
            line-height: 1.65;
            margin-top: .7rem;
            font-size: 1rem;
            font-weight: 400;
        }}

        .section-card, .dataset-card, .challenge-panel, .kpi-card {{
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 12px;
            box-shadow: var(--shadow);
        }}
        .project-card, .timeline-card {{
            display: block;
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 12px;
            box-shadow: var(--shadow);
            padding: 1rem;
            margin: .7rem 0 1rem;
            text-decoration: none;
            color: var(--text);
            transition: background-color 180ms ease, border-color 180ms ease, box-shadow 180ms ease, transform 180ms ease;
        }}
        .project-card {{
            min-height: 360px;
        }}
        .project-card:hover {{
            border-color: var(--accent);
            background: var(--surface-elevated);
            transform: translateY(-1px);
        }}
        .project-visual {{
            height: 118px;
            border-radius: 10px;
            border: 1px solid var(--border);
            background:
                linear-gradient(135deg, var(--tag-bg), transparent),
                repeating-linear-gradient(90deg, transparent 0 22px, color-mix(in srgb, var(--border) 70%, transparent) 22px 23px);
            color: var(--tag-text);
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;
            margin-bottom: .8rem;
        }}
        .project-title {{
            color: var(--text);
            font-weight: 700;
            font-size: 1.12rem;
            line-height: 1.25;
            margin: .22rem 0 .42rem;
        }}
        .project-meta, .timeline-date {{
            color: var(--muted);
            font-weight: 600;
            font-size: .82rem;
            text-transform: uppercase;
            letter-spacing: .02em;
        }}
        .project-metric {{
            color: var(--accent-bright);
            font-weight: 700;
            margin: .65rem 0 .4rem;
        }}
        .timeline-card ul {{
            color: var(--text-2);
            margin-top: .55rem;
            padding-left: 1.2rem;
        }}
        [data-testid="stVerticalBlockBorderWrapper"] {{
            border-color: var(--border);
            border-radius: 16px;
            background: var(--surface);
            box-shadow: var(--shadow);
        }}
        [data-testid="stVerticalBlockBorderWrapper"] [data-testid="stMarkdownContainer"] {{
            overflow-wrap: anywhere;
        }}
        .section-card {{
            padding: 1rem 1.05rem;
            margin: .7rem 0 1rem;
            min-height: 100px;
        }}
        .section-title {{
            font-size: 1.08rem;
            color: var(--text);
            font-weight: 600;
            margin-bottom: .32rem;
            line-height: 1.25;
        }}
        .section-copy, .muted {{
            color: var(--text-2);
            line-height: 1.62;
            font-size: .96rem;
        }}
        .dataset-card {{
            display: flex;
            align-items: center;
            gap: 1rem;
            padding: .95rem 1rem;
            margin: 1rem 0;
        }}
        .dataset-metrics {{
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: .85rem;
            width: 100%;
        }}
        .dataset-value {{ color: var(--text); font-size: 1.08rem; font-weight: 700; }}
        .dataset-label {{ color: var(--muted); font-size: .8rem; margin-top: .15rem; }}

        .challenge-panel {{
            display: flex;
            flex-wrap: wrap;
            gap: .55rem;
            padding: 1rem;
            margin: .75rem 0 1.1rem;
        }}
        .challenge-chip, .meta-pill, .active-chip {{
            border: 1px solid var(--border);
            background: var(--tag-bg);
            color: var(--tag-text);
            border-radius: 999px;
            font-size: .82rem;
            font-weight: 500;
            transition: background-color 160ms ease, border-color 160ms ease, color 160ms ease;
        }}
        .challenge-chip {{ padding: .42rem .7rem; }}
        .skill-card {{
            overflow: visible;
            height: auto;
        }}
        .skill-chip-wrap {{
            display: flex;
            flex-wrap: wrap;
            gap: .55rem .5rem;
            align-items: flex-start;
            max-width: 100%;
            min-width: 0;
            overflow: visible;
        }}
        .skill-chip {{
            display: inline-flex;
            align-items: center;
            max-width: 100%;
            min-width: 0;
            white-space: normal;
            overflow-wrap: anywhere;
            line-height: 1.3;
            padding: .46rem .72rem;
        }}
        .meta-pill {{
            display: inline-flex;
            align-items: center;
            gap: .35rem;
            padding: .34rem .58rem;
            margin: .15rem .25rem .15rem 0;
        }}
        .active-filter-wrap {{ margin: .45rem 0 .9rem; }}
        .active-chip {{
            display: inline-block;
            max-width: 100%;
            padding: .28rem .55rem;
            margin: .12rem .18rem .12rem 0;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
        }}

        .kpi-card {{
            min-height: 132px;
            padding: .95rem 1rem;
            transition: border-color .14s ease, background .14s ease, transform .14s ease;
        }}
        .kpi-card:hover {{
            transform: translateY(-1px);
            border-color: var(--accent);
            background: var(--surface-elevated);
        }}
        .kpi-icon {{
            width: 31px;
            height: 31px;
            margin-bottom: .55rem;
        }}
        .kpi-label {{
            font-size: .82rem;
            color: var(--muted);
            margin-bottom: .22rem;
            font-weight: 500;
        }}
        .kpi-value {{
            font-size: clamp(1.24rem, 2.8vw, 1.7rem);
            font-weight: 700;
            color: var(--text);
            overflow-wrap: anywhere;
            line-height: 1.2;
        }}
        .kpi-note {{
            color: var(--muted);
            font-size: .76rem;
            margin-top: .35rem;
            line-height: 1.35;
        }}

        .pipeline {{
            display: grid;
            grid-template-columns: repeat(6, minmax(0, 1fr));
            gap: .65rem;
            margin: 1rem 0 1.25rem;
        }}
        .pipeline-step {{
            border: 1px solid var(--border);
            background: var(--surface);
            border-radius: 10px;
            padding: .85rem .62rem;
            text-align: center;
            font-weight: 600;
            color: var(--text);
            box-shadow: var(--shadow);
        }}
        .pipeline-step span {{
            display: block;
            color: var(--accent-bright);
            font-size: .92rem;
            margin-bottom: .22rem;
        }}

        .chart-card-heading {{
            background: var(--surface);
            border: 1px solid var(--border);
            border-bottom: 0;
            border-radius: 12px 12px 0 0;
            box-shadow: var(--shadow);
            padding: .9rem 1rem .35rem;
            margin-top: .8rem;
        }}
        div[data-testid="stPlotlyChart"] {{
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 0 0 12px 12px;
            box-shadow: var(--shadow);
            padding: .55rem;
            margin-bottom: .25rem;
        }}
        .insight {{
            color: var(--muted);
            border-left: 3px solid var(--accent);
            padding: .34rem .65rem;
            margin: -.08rem 0 1.05rem;
            font-size: .86rem;
            line-height: 1.45;
        }}
        .footer {{
            color: var(--muted);
            border-top: 1px solid var(--border);
            margin-top: 2rem;
            padding-top: 1rem;
            font-size: .86rem;
            line-height: 1.7;
        }}
        .footer a {{
            color: var(--accent-bright);
            text-decoration: none;
            font-weight: 500;
        }}
        .footer a:hover {{
            text-decoration: underline;
        }}

        .stButton button, .stLinkButton a, .stDownloadButton button {{
            min-height: 2.45rem;
            border-radius: 10px;
            border: 1px solid var(--border);
            background: var(--surface);
            color: var(--text);
            font-weight: 500;
            font-family: var(--font);
            box-shadow: none;
            transition: background-color 180ms ease, border-color 180ms ease, color 180ms ease, box-shadow 180ms ease;
        }}
        .stButton button * , .stLinkButton a *, .stDownloadButton button * {{
            color: inherit;
        }}
        .stLinkButton a[kind="primary"],
        [data-testid="stLinkButton"] a[kind="primary"],
        .stButton button[kind="primary"],
        .stDownloadButton button[kind="primary"] {{
            background: var(--accent);
            border-color: var(--accent);
            color: var(--on-accent) !important;
            box-shadow: var(--shadow-accent);
        }}
        .stButton button:hover, .stLinkButton a:hover, .stDownloadButton button:hover {{
            border-color: var(--accent);
            background: var(--hover);
            color: var(--text);
        }}
        .stLinkButton a[kind="primary"]:hover,
        [data-testid="stLinkButton"] a[kind="primary"]:hover,
        .stButton button[kind="primary"]:hover,
        .stDownloadButton button[kind="primary"]:hover {{
            background: var(--accent-hover);
            border-color: var(--accent-hover);
            color: var(--on-accent) !important;
        }}
        .stButton button:focus, .stLinkButton a:focus,
        [data-baseweb="select"] > div:focus-within,
        input:focus, textarea:focus {{
            outline: 3px solid color-mix(in srgb, var(--accent) 34%, transparent);
            outline-offset: 2px;
        }}

        div[data-testid="stAlert"] {{
            border-radius: 10px;
            border: 1px solid var(--border);
            background: var(--surface-2);
            color: var(--text);
        }}
        div[data-testid="stAlert"] * {{
            color: var(--text);
        }}

        [data-testid="stExpander"] {{
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 10px;
        }}
        [data-testid="stExpander"] summary,
        [data-testid="stExpander"] summary * {{
            color: var(--text);
            font-weight: 600;
        }}

        label, [data-testid="stWidgetLabel"], [data-testid="stWidgetLabel"] * {{
            color: var(--text-2);
            font-family: var(--font);
            font-weight: 500;
        }}
        [data-baseweb="select"] > div,
        [data-baseweb="input"] > div,
        [data-testid="stDateInput"] input,
        [data-testid="stTextInput"] input {{
            background: var(--input-bg);
            color: var(--input-text);
            border-color: var(--border);
            border-radius: 10px;
            min-height: 2.45rem;
        }}
        [data-baseweb="select"] span,
        [data-baseweb="select"] input,
        [data-baseweb="input"] input,
        [data-testid="stDateInput"] input {{
            color: var(--input-text);
        }}
        [data-baseweb="tag"] {{
            background: var(--tag-bg);
            border: 1px solid var(--border);
            color: var(--tag-text);
            border-radius: 999px;
            max-width: 100%;
        }}
        [data-baseweb="tag"] span {{
            color: var(--tag-text);
            font-size: .78rem;
        }}
        [data-baseweb="select"] [role="combobox"] {{
            max-height: 92px;
            overflow-y: auto;
            align-items: flex-start;
            padding-top: .25rem;
            padding-bottom: .25rem;
        }}
        [data-baseweb="popover"], [data-baseweb="menu"], [role="listbox"] {{
            background: var(--surface-elevated);
            color: var(--text);
            border: 1px solid var(--border);
            border-radius: 10px;
            box-shadow: var(--shadow);
            z-index: 999999;
            max-height: 280px;
            overflow-y: auto;
        }}
        [role="option"], [data-baseweb="menu"] li {{
            color: var(--text);
            background: var(--surface-elevated);
            font-family: var(--font);
        }}
        [role="option"]:hover,
        [role="option"][aria-selected="true"],
        [data-baseweb="menu"] li:hover {{
            background: var(--hover);
            color: var(--text);
        }}
        [data-baseweb="popover"] div {{
            color: var(--text-2);
        }}
        input::placeholder {{
            color: var(--muted);
            opacity: 1;
        }}
        [data-testid="stSlider"] * {{
            color: var(--text-2);
        }}

        [data-testid="stDataFrame"] {{
            border: 1px solid var(--border);
            border-radius: 10px;
            overflow: hidden;
        }}
        .filter-title {{
            color: var(--text);
            font-size: 1.15rem;
            font-weight: 700;
            line-height: 2.4rem;
        }}
        @media (max-width: 1024px) {{
            .pipeline {{ grid-template-columns: repeat(3, minmax(0, 1fr)); }}
        }}
        @media (max-width: 860px) {{
            .dataset-metrics {{ grid-template-columns: 1fr; }}
        }}
        @media (max-width: 560px) {{
            .block-container {{ padding: .35rem 1rem 2.5rem; }}
            .pipeline {{ grid-template-columns: 1fr; }}
            .section-card {{ padding: 1rem; }}
            .kpi-card {{ min-height: 118px; }}
        }}
        @media (prefers-reduced-motion: reduce) {{
            *, *::before, *::after {{
                transition-duration: 0.01ms !important;
                animation-duration: 0.01ms !important;
                animation-iteration-count: 1 !important;
                scroll-behavior: auto !important;
            }}
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )
