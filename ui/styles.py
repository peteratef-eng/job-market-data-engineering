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
            --data-navy: #0F172A;
            --data-blue: #2563EB;
            --data-blue-dark: #1D4ED8;
            --data-cyan: #06B6D4;
            --data-cyan-soft: rgba(6, 182, 212, 0.12);
            --data-indigo: #4F46E5;
            --data-green: #10B981;
            --data-green-soft: rgba(16, 185, 129, 0.10);
            --data-amber: #F59E0B;
            --data-amber-soft: rgba(245, 158, 11, 0.10);
            --data-red: #DC2626;
            --data-surface: #FFFFFF;
            --data-background: #F8FAFC;
            --data-background-blue: #EFF6FF;
            --data-border: #CBD5E1;
            --data-border-soft: rgba(148, 163, 184, 0.28);
            --data-text: #0F172A;
            --data-text-secondary: #64748B;
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
            padding: .85rem .9rem 1.1rem;
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
            border-radius: 8px;
            color: var(--text-2);
            font-weight: 500;
            padding: .42rem .55rem;
            margin: .02rem 0;
            transition: background-color 180ms ease, border-color 180ms ease, color 180ms ease;
        }}
        [data-testid="stSidebarNav"] {{
            margin-top: .2rem;
        }}
        [data-testid="stSidebarNav"] ul {{
            gap: .08rem;
        }}
        [data-testid="stSidebarNav"] [role="heading"],
        [data-testid="stSidebarNav"] summary,
        [data-testid="stSidebarNav"] p {{
            color: var(--text);
            font-size: .78rem;
            font-weight: 700;
            letter-spacing: .04em;
            text-transform: uppercase;
            margin: .75rem 0 .25rem;
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
            border-radius: 8px;
            padding: .65rem .7rem;
            margin: .15rem 0 .65rem;
            box-shadow: var(--shadow);
            width: 100%;
            max-width: 100%;
            min-width: 0;
            transform-origin: center;
            transition:
                transform 240ms ease,
                border-color 240ms ease,
                background-color 240ms ease,
                box-shadow 240ms ease;
        }}
        @media (hover: hover) and (pointer: fine) {{
            .sidebar-brand:hover,
            .sidebar-brand:focus-within {{
                transform: translateY(-5px) scale(1.015);
                border-color: rgba(37, 99, 235, 0.45);
                background-color: rgba(239, 246, 255, 0.75);
                box-shadow: 0 14px 30px rgba(37, 99, 235, 0.14);
                position: relative;
                z-index: 2;
            }}
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
            width: 42px;
            height: 42px;
            border-radius: 8px;
            flex: 0 0 42px;
            object-fit: cover;
            object-position: center top;
            display: block;
        }}
        .brand-title {{ color: var(--text); font-weight: 700; line-height: 1.15; }}
        .brand-subtitle {{ color: var(--muted); font-size: .82rem; margin-top: .12rem; }}
        .sidebar-profile-divider {{
            height: 1px;
            margin: 1rem 0 .85rem;
            background: rgba(148, 163, 184, .28);
        }}
        .sidebar-profile-card {{
            margin-top: 0;
            margin-bottom: .65rem;
        }}
        .sidebar-links {{
            margin: 0 0 .65rem;
            color: var(--muted);
            font-size: .84rem;
        }}
        .sidebar-social-links {{
            display: block;
        }}
        .sidebar-links a {{
            color: var(--accent-bright);
            text-decoration: none;
            font-weight: 500;
            transition: color 180ms ease, opacity 180ms ease;
        }}
        .sidebar-divider {{
            height: 1px;
            background: var(--border);
            margin: .75rem 0 .35rem;
        }}
        .sidebar-projects-expander {{
            width: 100%;
            max-width: 100%;
            margin: .95rem 0 .5rem;
        }}
        .sidebar-projects-summary {{
            min-height: 42px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: .75rem;
            padding: .65rem .7rem;
            border: 1px solid transparent;
            border-radius: 10px;
            color: var(--text);
            font-size: .72rem;
            font-weight: 800;
            letter-spacing: .1em;
            text-transform: uppercase;
            cursor: pointer;
            list-style: none;
            user-select: none;
            transition:
                background-color 180ms ease,
                border-color 180ms ease,
                color 180ms ease;
        }}
        .sidebar-projects-summary::-webkit-details-marker,
        .sidebar-project-summary::-webkit-details-marker {{
            display: none;
        }}
        .sidebar-projects-summary::marker,
        .sidebar-project-summary::marker {{
            content: "";
        }}
        .sidebar-projects-summary:hover,
        .sidebar-projects-summary:focus-visible {{
            background: rgba(239, 246, 255, .72);
            border-color: rgba(37, 99, 235, .20);
            outline: none;
        }}
        .sidebar-projects-summary:focus-visible,
        .sidebar-project-summary:focus-visible {{
            box-shadow: 0 0 0 3px rgba(37, 99, 235, .16);
        }}
        .sidebar-expander-chevron,
        .sidebar-project-chevron {{
            width: 16px;
            height: 16px;
            flex: 0 0 16px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            color: var(--data-blue);
            transition: transform 220ms cubic-bezier(0.22, 1, 0.36, 1);
            transform-origin: center;
        }}
        .sidebar-expander-chevron svg,
        .sidebar-project-chevron svg {{
            width: 14px;
            height: 14px;
            fill: none;
            stroke: currentColor;
            stroke-width: 2;
            stroke-linecap: round;
            stroke-linejoin: round;
        }}
        .sidebar-projects-expander[open] > .sidebar-projects-summary .sidebar-expander-chevron,
        .sidebar-project-expander[open] > .sidebar-project-summary .sidebar-project-chevron {{
            transform: rotate(180deg);
        }}
        .sidebar-projects-content {{
            width: 100%;
            max-width: 100%;
            margin-top: .25rem;
        }}
        .sidebar-projects-expander[open] > .sidebar-projects-content {{
            animation: sidebar-project-content-in 220ms cubic-bezier(0.22, 1, 0.36, 1) both;
        }}
        @keyframes sidebar-project-content-in {{
            from {{
                opacity: 0;
                transform: translateY(-4px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}
        .sidebar-project-expander {{
            width: 100%;
            max-width: 100%;
            min-width: 0;
        }}
        .sidebar-project-summary {{
            cursor: pointer;
            list-style: none;
            user-select: none;
        }}
        .sidebar-project-card {{
            position: relative;
            width: 100%;
            min-height: 92px;
            padding: .75rem 2rem .75rem .75rem;
            border: 1px solid rgba(37, 99, 235, .18);
            border-radius: 11px;
            background:
                radial-gradient(circle at 85% 15%, rgba(6, 182, 212, .09), transparent 38%),
                linear-gradient(145deg, rgba(255, 255, 255, .96), rgba(239, 246, 255, .86));
            box-shadow: 0 8px 20px rgba(15, 23, 42, .06);
            overflow: hidden;
            transition:
                transform 220ms cubic-bezier(0.22, 1, 0.36, 1),
                border-color 220ms ease,
                box-shadow 220ms ease;
        }}
        .sidebar-project-chevron {{
            position: absolute;
            top: .78rem;
            right: .68rem;
        }}
        .sidebar-project-card-active {{
            border-color: rgba(37, 99, 235, .34);
            background:
                radial-gradient(circle at 85% 15%, rgba(6, 182, 212, .12), transparent 38%),
                rgba(239, 246, 255, .92);
        }}
        .sidebar-project-expander.is-active > .sidebar-project-summary {{
            border-color: rgba(37, 99, 235, .42);
            background:
                radial-gradient(circle at 85% 15%, rgba(6, 182, 212, .11), transparent 38%),
                rgba(239, 246, 255, .94);
        }}
        .sidebar-project-card-header {{
            display: flex;
            align-items: center;
            gap: .62rem;
            min-width: 0;
        }}
        .sidebar-project-icon {{
            width: 30px;
            height: 30px;
            flex: 0 0 30px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            border-radius: 9px;
            color: var(--data-blue);
            background: rgba(37, 99, 235, .10);
            border: 1px solid rgba(37, 99, 235, .16);
        }}
        .sidebar-project-icon svg {{
            width: 17px;
            height: 17px;
            fill: none;
            stroke: currentColor;
            stroke-width: 1.8;
            stroke-linecap: round;
            stroke-linejoin: round;
        }}
        .sidebar-project-copy {{
            min-width: 0;
            padding-right: .7rem;
        }}
        .sidebar-project-name {{
            color: var(--text);
            font-size: .86rem;
            font-weight: 800;
            line-height: 1.16;
            overflow-wrap: anywhere;
        }}
        .sidebar-project-type {{
            color: var(--muted);
            font-size: .7rem;
            font-weight: 650;
            line-height: 1.2;
            margin-top: .18rem;
        }}
        .sidebar-project-links {{
            position: relative;
            display: flex;
            flex-direction: column;
            gap: .08rem;
            margin: .25rem 0 .15rem .8rem;
            padding: .35rem 0 .25rem .85rem;
            border-left: 1px solid rgba(37, 99, 235, .20);
        }}
        .sidebar-project-expander[open] > .sidebar-project-links {{
            animation: sidebar-project-content-in 220ms cubic-bezier(0.22, 1, 0.36, 1) both;
        }}
        .sidebar-project-link {{
            position: relative;
            display: flex;
            align-items: center;
            min-height: 2.05rem;
            padding: .38rem .5rem;
            border-radius: 8px;
            color: var(--text-2);
            font-size: .82rem;
            font-weight: 600;
            line-height: 1.2;
            text-decoration: none;
            transition:
                background-color 180ms ease,
                color 180ms ease,
                border-color 180ms ease;
        }}
        .sidebar-project-link::before {{
            content: "";
            position: absolute;
            left: -.98rem;
            top: 50%;
            width: 6px;
            height: 6px;
            border-radius: 999px;
            background: rgba(37, 99, 235, .26);
            transform: translateY(-50%);
        }}
        .sidebar-project-link:hover,
        .sidebar-project-link:focus-visible {{
            color: var(--data-blue);
            background: rgba(239, 246, 255, .82);
            text-decoration: none;
        }}
        .sidebar-project-link:hover::before,
        .sidebar-project-link:focus-visible::before {{
            background: var(--data-blue);
        }}
        .sidebar-project-link-active {{
            color: var(--data-blue);
            background: rgba(37, 99, 235, .09);
            font-weight: 700;
        }}
        .sidebar-project-link-active::before {{
            background: #2563eb;
            box-shadow: 0 0 0 3px rgba(37, 99, 235, .12);
        }}
        .sidebar-project-mini-lineage {{
            position: relative;
            display: grid;
            grid-template-columns: 10px minmax(0, 1fr) 10px minmax(0, 1fr) 10px;
            align-items: center;
            gap: .25rem;
            height: 22px;
            margin-top: .62rem;
            opacity: .82;
            pointer-events: none;
        }}
        .sidebar-mini-stage {{
            position: relative;
            z-index: 3;
            width: 10px;
            height: 10px;
            border-radius: 4px;
            background: rgba(255, 255, 255, .95);
            border: 1px solid rgba(37, 99, 235, .26);
        }}
        .sidebar-mini-mart {{
            border-color: rgba(6, 182, 212, .35);
            background: rgba(236, 254, 255, .95);
        }}
        .sidebar-mini-track {{
            position: relative;
            z-index: 1;
            height: 2px;
            border-radius: 999px;
            background: linear-gradient(90deg, rgba(37, 99, 235, .24), rgba(6, 182, 212, .26));
        }}
        .sidebar-mini-packet {{
            position: absolute;
            z-index: 2;
            left: 3px;
            top: 50%;
            width: 5px;
            height: 5px;
            border-radius: 50%;
            background: #2563eb;
            box-shadow:
                0 0 0 3px rgba(37, 99, 235, .10),
                0 0 7px rgba(37, 99, 235, .26);
            transform: translate3d(0, -50%, 0);
            animation: sidebar-mini-packet-flow 4s linear infinite;
            pointer-events: none;
        }}
        @keyframes sidebar-mini-packet-flow {{
            0% {{ left: 3px; opacity: 0; background: #2563eb; }}
            8% {{ opacity: 1; }}
            72% {{ opacity: 1; background: #2563eb; }}
            88% {{ opacity: 1; background: #06b6d4; }}
            96%, 100% {{ left: calc(100% - 8px); opacity: 0; background: #06b6d4; }}
        }}
        .sidebar-projects-expander:not([open]) .sidebar-mini-packet {{
            animation-play-state: paused;
        }}
        @media (hover: hover) and (pointer: fine) {{
            .sidebar-project-card:hover,
            .sidebar-project-card:focus-within {{
                transform: translateY(-2px);
                border-color: rgba(37, 99, 235, .38);
                box-shadow: 0 10px 24px rgba(37, 99, 235, .10);
            }}
        }}

        .page-header {{
            position: relative;
            margin: .15rem 0 1rem;
            max-width: 900px;
        }}
        .page-header-overview::after,
        .page-header-dashboard::after {{
            content: "";
            position: absolute;
            right: .2rem;
            top: .35rem;
            width: 6.5rem;
            height: 3.6rem;
            opacity: .045;
            pointer-events: none;
            background:
                radial-gradient(circle, var(--data-blue) 0 2px, transparent 3px),
                linear-gradient(90deg, transparent 48%, var(--data-cyan) 49% 51%, transparent 52%);
            background-size: 1.7rem 1.7rem, 100% 100%;
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

        .portfolio-hero {{
            display: grid;
            grid-template-columns: minmax(0, 1.55fr) minmax(290px, .75fr);
            align-items: center;
            column-gap: clamp(2rem, 4vw, 4.5rem);
            row-gap: 0;
            padding: clamp(1.35rem, 3vw, 2.2rem) 0 1rem;
            overflow: visible;
        }}
        .data-command-hero {{
            position: relative;
            isolation: isolate;
            padding: clamp(1.25rem, 3.6vw, 2.25rem);
            margin: .25rem 0 1rem;
            border: 1px solid rgba(37, 99, 235, .14);
            border-radius: 22px;
            background:
                radial-gradient(circle at 78% 52%, rgba(37, 99, 235, .11), transparent 31%),
                radial-gradient(circle at 26% 30%, rgba(6, 182, 212, .075), transparent 28%),
                linear-gradient(145deg, rgba(255, 255, 255, .96), rgba(248, 250, 252, .90));
            box-shadow: 0 22px 52px rgba(15, 23, 42, .08);
            overflow: hidden;
        }}
        .data-blueprint-grid {{
            position: absolute;
            inset: 0;
            z-index: -3;
            opacity: .34;
            background-image:
                linear-gradient(rgba(37, 99, 235, .045) 1px, transparent 1px),
                linear-gradient(90deg, rgba(37, 99, 235, .045) 1px, transparent 1px),
                linear-gradient(rgba(15, 23, 42, .035) 1px, transparent 1px);
            background-size: 34px 34px;
            mask-image: linear-gradient(135deg, rgba(0, 0, 0, .76), transparent 78%);
        }}
        .data-background-path {{
            display: none;
        }}
        .data-background-particle {{
            display: none;
        }}
        .data-background-particle-1 {{
            left: 10%;
            bottom: 18%;
        }}
        .data-background-particle-2 {{
            right: 18%;
            top: 24%;
            animation-delay: 4.4s;
        }}
        @keyframes data-background-particle-flow {{
            0%, 12% {{ opacity: 0; transform: translate3d(0, 0, 0); }}
            18%, 60% {{ opacity: .75; }}
            84%, 100% {{ opacity: 0; transform: translate3d(78px, -34px, 0); }}
        }}
        .hero-copy {{
            min-width: 0;
            display: flex;
            flex-direction: column;
            grid-column: 1;
            grid-row: 1;
        }}
        .hero-kicker,
        .hero-copy h1,
        .hero-copy > p,
        .hero-value-rotator,
        .hero-actions,
        .hero-skill-section,
        .hero-profile-card {{
            animation: home-entrance-rise 520ms ease-out both;
        }}
        .hero-kicker {{ animation-delay: 40ms; }}
        .hero-copy h1 {{ animation-delay: 120ms; }}
        .hero-copy > p {{ animation-delay: 200ms; }}
        .hero-value-rotator {{ animation-delay: 280ms; }}
        .hero-actions {{ animation-delay: 360ms; }}
        .hero-profile-card {{ animation-delay: 440ms; }}
        .hero-skill-section {{ animation-delay: 520ms; }}
        @keyframes home-entrance-rise {{
            from {{ opacity: 0; transform: translateY(.65rem); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        @keyframes home-skill-node-enter {{
            from {{ opacity: 0; transform: translateX(-.45rem); }}
            to {{ opacity: 1; transform: translateX(0); }}
        }}
        .sr-only {{
            position: absolute;
            width: 1px;
            height: 1px;
            padding: 0;
            margin: -1px;
            overflow: hidden;
            clip: rect(0, 0, 0, 0);
            white-space: nowrap;
            border: 0;
        }}
        .portfolio-hero-spacer {{
            height: 1.15rem;
        }}
        .hero-kicker,
        .section-eyebrow {{
            color: var(--accent);
            font-size: .82rem;
            font-weight: 700;
            letter-spacing: .08em;
            text-transform: uppercase;
            margin-bottom: 0;
        }}
        .portfolio-hero h1 {{
            color: var(--text);
            font-size: clamp(3.3rem, 5.5vw, 5.15rem);
            line-height: .98;
            font-weight: 750;
            letter-spacing: -0.045em;
            max-width: 700px;
            margin: 1.8rem 0 0;
        }}
        .portfolio-hero p,
        .contact-cta p {{
            color: var(--text-2);
            max-width: 680px;
            font-size: 1.05rem;
            line-height: 1.7;
            margin: 1rem 0 0;
        }}
        .hero-description {{
            max-width: 720px;
            margin-top: 2.25rem;
            line-height: 1.65;
        }}
        .hero-value-rotator {{
            position: relative;
            width: min(100%, 31rem);
            min-height: 2.25rem;
            margin-top: 1rem;
            border-left: 3px solid rgba(37, 99, 235, .42);
            padding: .4rem .75rem;
            color: var(--accent);
            font-size: .9rem;
            font-weight: 800;
            letter-spacing: .01em;
            overflow: hidden;
        }}
        .hero-value-line {{
            position: absolute;
            inset: .4rem auto auto .75rem;
            opacity: 0;
            transform: translateY(.55rem);
            animation: hero-value-rotate 16s ease-in-out infinite;
        }}
        .hero-value-line-1 {{ animation-delay: 0s; }}
        .hero-value-line-2 {{ animation-delay: 4s; }}
        .hero-value-line-3 {{ animation-delay: 8s; }}
        .hero-value-line-4 {{ animation-delay: 12s; }}
        @keyframes hero-value-rotate {{
            0%, 5% {{ opacity: 0; transform: translateY(.55rem); }}
            10%, 21% {{ opacity: 1; transform: translateY(0); }}
            26%, 100% {{ opacity: 0; transform: translateY(-.45rem); }}
        }}
        .hero-actions,
        .contact-cta-actions {{
            display: flex;
            flex-wrap: wrap;
            gap: .7rem;
            margin-top: 1.4rem;
        }}
        .portfolio-button {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            min-height: 2.65rem;
            padding: .7rem 1rem;
            border-radius: 10px;
            border: 1px solid rgba(37, 99, 235, .22);
            background: var(--surface);
            color: var(--data-blue);
            font-weight: 700;
            font-size: .82rem;
            line-height: 1.15;
            text-decoration: none;
            transition: background-color 180ms ease, border-color 180ms ease, color 180ms ease, box-shadow 180ms ease, transform 180ms ease;
        }}
        .portfolio-button:hover {{
            border-color: var(--accent);
            background: var(--hover);
            color: var(--accent);
            text-decoration: none;
        }}
        .portfolio-button-primary {{
            background: var(--data-blue);
            border-color: var(--data-blue);
            color: var(--on-accent) !important;
            box-shadow: var(--shadow-accent);
        }}
        .portfolio-button-primary:hover {{
            background: var(--accent-hover);
            border-color: var(--accent-hover);
            color: var(--on-accent) !important;
        }}
        .portfolio-button-quiet {{
            background: transparent;
        }}
        .hero-primary-action {{
            gap: .42rem;
        }}
        .hero-primary-action span {{
            display: inline-block;
            transform: translateX(0);
            transition: transform 180ms ease;
        }}
        .hero-stack {{
            display: flex;
            flex-wrap: wrap;
            gap: .35rem;
            margin-top: 1.15rem;
        }}
        .hero-skill-section {{
            grid-column: 1;
            grid-row: 2;
            margin-top: 1.5rem;
            width: min(100%, 760px);
        }}
        .hero-skill-label {{
            margin-bottom: .65rem;
            color: var(--text-2);
            font-size: .68rem;
            font-weight: 750;
            letter-spacing: .11em;
            text-transform: uppercase;
        }}
        .hero-skill-pipeline {{
            position: relative;
            isolation: isolate;
            z-index: 5;
            display: grid;
            grid-template-columns: minmax(6.2rem, 1fr) minmax(7.2rem, 1fr) minmax(7.4rem, 1fr) minmax(3.4rem, .62fr) minmax(8rem, 1.15fr);
            align-items: center;
            gap: .95rem;
            width: 100%;
            margin-top: 0;
            overflow: visible;
        }}
        .hero-skill-rail {{
            position: absolute;
            z-index: 1;
            top: 50%;
            left: 7%;
            right: 7%;
            height: 2px;
            transform: translateY(-50%);
            border-radius: 999px;
            background: linear-gradient(90deg, rgba(148, 163, 184, .38), rgba(37, 99, 235, .48), rgba(6, 182, 212, .38));
            pointer-events: none;
        }}
        .hero-skill-packet-track {{
            position: absolute;
            z-index: 2;
            top: 50%;
            left: 7%;
            right: 7%;
            height: 0;
            pointer-events: none;
            animation: hero-skill-packet-run 4s linear infinite;
            will-change: transform;
        }}
        .hero-skill-node {{
            position: relative;
            z-index: 3;
            min-width: 0;
            min-height: 2.8rem;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            padding: .44rem .58rem;
            border: 1px solid rgba(37, 99, 235, .18);
            border-radius: 10px;
            background: rgba(255, 255, 255, .90);
            box-shadow: 0 6px 14px rgba(15, 23, 42, .045);
            color: var(--text);
            font-size: .76rem;
            font-weight: 850;
            line-height: 1.12;
            text-align: center;
            transform-origin: center;
            animation: home-skill-node-enter 420ms ease-out both;
        }}
        .hero-skill-packet {{
            position: absolute;
            z-index: 1;
            top: 0;
            left: 0;
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background:
                radial-gradient(circle at center, #FFFFFF 0 28%, var(--data-cyan) 31% 100%);
            border: 2px solid #FFFFFF;
            box-shadow:
                0 0 0 2px rgba(6, 182, 212, 0.14),
                0 2px 7px rgba(37, 99, 235, 0.24);
            transform: translate3d(-50%, -50%, 0);
            pointer-events: none;
        }}
        .hero-skill-node-content {{
            position: relative;
            z-index: 5;
        }}
        .hero-skill-port {{
            position: absolute;
            z-index: 4;
            top: 50%;
            width: 6px;
            height: 6px;
            border-radius: 999px;
            background: #93C5FD;
            border: 1px solid #FFFFFF;
            transform: translateY(-50%);
            pointer-events: none;
        }}
        .hero-skill-port-in {{ left: -3px; }}
        .hero-skill-port-out {{ right: -3px; }}
        .hero-skill-node-1 {{ animation-delay: 560ms; }}
        .hero-skill-node-2 {{ animation-delay: 620ms; }}
        .hero-skill-node-3 {{ animation-delay: 680ms; }}
        .hero-skill-node-4 {{ animation-delay: 740ms; }}
        .hero-skill-node-5 {{ animation-delay: 800ms; }}
        @keyframes hero-skill-packet-run {{
            0% {{ opacity: 1; transform: translate3d(0, 0, 0); }}
            94% {{ opacity: 1; transform: translate3d(100%, 0, 0); }}
            95%, 100% {{ opacity: 0; transform: translate3d(100%, 0, 0); }}
        }}
        .hero-photo-shell {{
            justify-self: center;
            width: min(100%, 360px);
            aspect-ratio: 1;
            border-radius: 34px;
            padding: 1rem;
            background:
                radial-gradient(circle at 72% 18%, rgba(37, 99, 235, .2), transparent 36%),
                linear-gradient(145deg, rgba(239, 246, 255, .95), rgba(255, 255, 255, .5));
            border: 1px solid rgba(37, 99, 235, .18);
            box-shadow: 0 22px 44px rgba(37, 99, 235, .14);
            overflow: hidden;
        }}
        .hero-photo {{
            width: 100%;
            height: 100%;
            display: block;
            object-fit: cover;
            object-position: center top;
            border-radius: 26px;
            box-shadow: var(--shadow);
        }}
        .hero-photo-fallback {{
            display: flex;
            align-items: center;
            justify-content: center;
            background: var(--tag-bg);
            color: var(--tag-text);
            font-size: 3rem;
            font-weight: 800;
        }}
        .st-key-home_profile_photo_shell,
        .st-key-home_profile_info_card {{
            width: min(100%, 360px);
            margin-left: auto;
            margin-right: auto;
            overflow: visible;
        }}
        .st-key-home_profile_photo_shell {{
            margin-top: 1rem;
            transform: none;
            animation: none;
        }}
        .st-key-home_profile_info_card {{
            margin-top: .75rem;
        }}
        .st-key-home_profile_photo_shell [data-testid="stImage"] {{
            margin: 0 auto;
            transform: none;
            animation: none;
        }}
        .st-key-home_profile_photo_shell img {{
            display: block;
            width: 100%;
            aspect-ratio: 1;
            object-fit: cover;
            object-position: center top;
            border-radius: 18px;
            border: 1px solid rgba(37, 99, 235, .18);
            box-shadow: 0 18px 38px rgba(37, 99, 235, .12);
            transform: none;
            animation: none;
        }}
        .st-key-home_profile_photo_shell:hover,
        .st-key-home_profile_photo_shell:focus-within,
        .st-key-home_profile_photo_shell:hover img,
        .st-key-home_profile_photo_shell [data-testid="stImage"]:hover img {{
            transform: none;
        }}
        .home-profile-info-card {{
            padding: 1rem 1rem 1.05rem;
            border: 1px solid rgba(37, 99, 235, .22);
            border-radius: 18px;
            background:
                radial-gradient(circle at 72% 12%, rgba(37, 99, 235, .14), transparent 34%),
                linear-gradient(145deg, rgba(255, 255, 255, .96), rgba(248, 250, 252, .92));
            box-shadow: 0 18px 38px rgba(37, 99, 235, .12);
            overflow: hidden;
            transform-origin: center center;
            transition:
                transform 250ms cubic-bezier(0.22, 1, 0.36, 1),
                border-color 250ms ease,
                box-shadow 250ms ease;
        }}
        .home-profile-info-card {{
            text-align: center;
        }}
        .home-profile-info-name {{
            color: var(--text);
            font-size: 1.22rem;
            line-height: 1.2;
            font-weight: 800;
            transition: color 250ms ease;
        }}
        .home-profile-info-role {{
            color: var(--accent);
            font-size: .94rem;
            font-weight: 700;
            line-height: 1.35;
            margin-top: .18rem;
        }}
        .home-profile-info-status {{
            display: inline-flex;
            align-items: center;
            gap: .38rem;
            color: var(--tag-text);
            background: var(--tag-bg);
            border: 1px solid var(--border);
            border-radius: 999px;
            padding: .34rem .58rem;
            font-size: .78rem;
            font-weight: 700;
            margin-top: .7rem;
        }}
        .home-profile-info-status span {{
            width: .48rem;
            height: .48rem;
            border-radius: 999px;
            background: var(--positive);
            box-shadow: 0 0 0 3px color-mix(in srgb, var(--positive) 20%, transparent);
            transition: box-shadow 250ms ease;
        }}
        .hero-profile-card {{
            position: relative;
            justify-self: center;
            align-self: center;
            grid-column: 2;
            grid-row: 1 / span 2;
            width: min(100%, 340px);
            padding: .7rem;
            border: 1px solid rgba(37, 99, 235, .22);
            border-radius: 22px;
            background:
                radial-gradient(circle at 75% 88%, rgba(37, 99, 235, 0.10), transparent 34%),
                linear-gradient(145deg, rgba(255, 255, 255, 0.98), rgba(239, 246, 255, 0.88));
            box-shadow: 0 16px 38px rgba(15, 23, 42, 0.10);
            overflow: hidden;
            transform: translateZ(0);
            transform-origin: center center;
            transition:
                transform 240ms cubic-bezier(0.22, 1, 0.36, 1),
                border-color 240ms ease,
                box-shadow 240ms ease;
        }}
        .hero-profile-card:focus-within {{
            border-color: rgba(37, 99, 235, 0.72);
            box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.12);
        }}
        .hero-profile-media {{
            position: relative;
            background: transparent;
        }}
        .hero-profile-image-wrap {{
            aspect-ratio: 1 / 1.02;
            overflow: hidden;
            border-radius: 17px;
            background: #eef2f7;
            border: 1px solid rgba(148, 163, 184, 0.18);
        }}
        .hero-profile-image {{
            display: block;
            width: 100%;
            height: 100%;
            object-fit: cover;
            object-position: center top;
            border-radius: 0;
            border: 0;
            background: #E2E8F0;
            box-shadow: none;
            transform: none;
            animation: none;
        }}
        .hero-profile-identity {{
            display: flex;
            flex-direction: column;
            gap: 0;
            padding: 1rem .3rem .2rem;
            text-align: left;
            border-top: 0;
        }}
        .hero-profile-heading {{
            display: flex;
            flex-direction: column;
            gap: 3px;
        }}
        .hero-profile-name {{
            margin: 0;
            color: #0F172A;
            font-size: 1.55rem;
            font-weight: 800;
            line-height: 1.15;
        }}
        .hero-profile-role {{
            margin: .3rem 0 0;
            color: var(--text-2);
            font-size: .98rem;
            font-weight: 650;
            line-height: 1.3;
        }}
        .hero-profile-meta {{
            display: flex;
            align-items: center;
            justify-content: flex-start;
            flex-wrap: wrap;
            gap: .55rem;
            margin-top: .8rem;
        }}
        .hero-profile-status {{
            display: inline-flex;
            align-items: center;
            gap: 7px;
            min-height: 30px;
            padding: 5px 10px;
            border: 1px solid rgba(16, 185, 129, 0.22);
            border-radius: 999px;
            background: rgba(16, 185, 129, 0.08);
            color: #047857;
            font-size: .76rem;
            font-weight: 650;
            line-height: 1.2;
            white-space: nowrap;
        }}
        .hero-profile-status-dot {{
            width: 7px;
            height: 7px;
            flex: 0 0 7px;
            border-radius: 50%;
            background: #10B981;
            box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.12);
        }}
        .hero-profile-location {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            min-height: 30px;
            padding: 5px 10px;
            border: 1px solid rgba(148, 163, 184, 0.25);
            border-radius: 999px;
            background: rgba(248, 250, 252, 0.92);
            color: #475569;
            font-size: .76rem;
            font-weight: 600;
            line-height: 1.2;
            white-space: nowrap;
        }}
        .hero-profile-location-icon {{
            position: relative;
            width: 9px;
            height: 9px;
            flex: 0 0 9px;
            border: 1.6px solid currentColor;
            border-radius: 50% 50% 50% 0;
            transform: rotate(-45deg);
        }}
        .hero-profile-location-icon::after {{
            content: "";
            position: absolute;
            inset: 2px;
            border-radius: 999px;
            background: currentColor;
        }}
        .featured-project-card,
        .pipeline-step-card,
        .contact-cta {{
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 12px;
            box-shadow: var(--shadow);
        }}
        .featured-project-card {{
            position: relative;
            display: grid;
            grid-template-columns: minmax(0, 1fr) minmax(540px, 1.02fr);
            gap: clamp(2rem, 3vw, 3.25rem);
            align-items: center;
            padding: 1.25rem;
            margin: 1.4rem 0 2rem;
            overflow: visible;
        }}
        .featured-project-copy h2,
        .home-section h2,
        .contact-cta h2 {{
            color: var(--text);
            font-size: clamp(1.55rem, 3vw, 2.15rem);
            line-height: 1.12;
            margin: 0;
        }}
        .featured-project-copy p {{
            color: var(--text-2);
            line-height: 1.65;
            margin: .75rem 0 0;
        }}
        .featured-meta {{
            display: flex;
            flex-wrap: wrap;
            gap: .5rem;
            margin-top: 1rem;
        }}
        .featured-meta span {{
            display: inline-flex;
            border: 1px solid var(--border);
            background: var(--tag-bg);
            color: var(--tag-text);
            border-radius: 999px;
            padding: .34rem .58rem;
            font-size: .82rem;
            font-weight: 600;
            line-height: 1.25;
        }}
        .featured-preview {{
            width: min(100%, 670px);
            justify-self: end;
            border: 1px solid var(--border);
            border-radius: 10px;
            background:
                radial-gradient(circle at 55% 45%, rgba(37, 99, 235, 0.10), transparent 48%),
                linear-gradient(145deg, rgba(255,255,255,0.98), rgba(239,246,255,0.88));
            overflow: hidden;
            min-height: 230px;
        }}
        .featured-preview img {{
            width: 100%;
            height: 100%;
            min-height: 230px;
            object-fit: cover;
            object-position: center;
            display: block;
        }}
        .featured-preview-fallback {{
            min-height: 230px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--muted);
            font-weight: 700;
        }}
        .featured-lineage-preview {{
            position: relative;
            width: min(100%, 670px);
            min-height: 0;
            height: auto;
            padding: .9rem .95rem 1rem;
            border-radius: 16px;
            overflow: hidden;
        }}
        .featured-lineage-header {{
            position: relative;
            z-index: 4;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1rem;
            min-height: 24px;
            margin-bottom: .75rem;
        }}
        .featured-lineage-header span {{
            color: var(--data-blue);
            font-size: .69rem;
            font-weight: 850;
            letter-spacing: .09em;
            text-transform: uppercase;
        }}
        .featured-lineage-header small {{
            display: inline-flex;
            align-items: center;
            gap: .38rem;
            color: var(--muted);
            font-size: .64rem;
            font-weight: 700;
            white-space: nowrap;
        }}
        .featured-lineage-header small span {{
            width: .375rem;
            height: .375rem;
            border-radius: 999px;
            background: var(--data-green);
            box-shadow: 0 0 0 3px rgba(16, 185, 129, .10);
        }}
        .featured-lineage-canvas {{
            position: relative;
            display: block;
            width: 100%;
            height: 350px;
            isolation: isolate;
        }}
        .featured-lineage-lanes {{
            display: grid;
            grid-template-rows: minmax(0, 1.35fr) minmax(0, .85fr);
            gap: .8rem;
            height: 100%;
        }}
        .featured-lineage-lane {{
            position: relative;
            display: grid;
            grid-template-columns:
                minmax(0, .9fr)
                minmax(28px, .16fr)
                minmax(0, 1fr)
                minmax(28px, .16fr)
                minmax(0, 1.18fr);
            align-items: center;
            gap: .35rem;
            min-width: 0;
            padding: 1.45rem .75rem .75rem;
            border: 1px solid rgba(148, 163, 184, .18);
            border-radius: 13px;
            background: rgba(255, 255, 255, .44);
            overflow: hidden;
        }}
        .featured-lineage-lane-label {{
            position: absolute;
            top: .48rem;
            left: .7rem;
            color: var(--text-2);
            font-size: .56rem;
            font-weight: 800;
            letter-spacing: .09em;
            line-height: 1;
            text-transform: uppercase;
        }}
        .featured-lineage-source-group {{
            position: relative;
            display: grid;
            gap: .35rem;
            min-width: 0;
            padding: .45rem;
            border: 1px solid rgba(100, 116, 139, .18);
            border-radius: 10px;
            background: rgba(248, 250, 252, .90);
        }}
        .featured-lineage-source-group::after {{
            content: "";
            position: absolute;
            right: -.75rem;
            top: 50%;
            width: .75rem;
            height: 1px;
            background: rgba(100, 116, 139, .24);
            transform: translateY(-50%);
        }}
        .featured-lineage-source-row,
        .featured-lineage-mart-row {{
            min-width: 0;
            display: flex;
            align-items: center;
            gap: .4rem;
            border-radius: 7px;
            line-height: 1.12;
        }}
        .featured-lineage-source-row {{
            min-height: 28px;
            padding: .3rem .38rem;
            background: rgba(255, 255, 255, .82);
        }}
        .featured-lineage-intermediate-card,
        .featured-lineage-single-mart {{
            position: relative;
            z-index: 3;
            min-width: 0;
            min-height: 58px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            padding: .55rem .65rem;
            border-radius: 11px;
            box-shadow: 0 7px 16px rgba(15, 23, 42, .045);
            transition:
                border-color 180ms ease,
                background-color 180ms ease,
                box-shadow 180ms ease,
                opacity 180ms ease;
        }}
        .featured-lineage-intermediate-card {{
            border: 1px solid rgba(37, 99, 235, .30);
            background: rgba(239, 246, 255, .96);
            color: var(--data-blue);
        }}
        .featured-lineage-mart-group,
        .featured-lineage-single-mart {{
            border: 1px solid rgba(6, 182, 212, .30);
            background: rgba(236, 254, 255, .78);
            color: var(--data-cyan);
        }}
        .featured-lineage-mart-group {{
            position: relative;
            z-index: 3;
            min-width: 0;
            padding: .5rem;
            border-radius: 11px;
        }}
        .featured-lineage-mart-group::before {{
            content: "";
            position: absolute;
            left: .82rem;
            top: 2rem;
            bottom: .7rem;
            width: 1px;
            background: rgba(6, 182, 212, .24);
        }}
        .featured-lineage-mart-group-title {{
            margin-bottom: .35rem;
            color: var(--data-cyan);
            font-size: .54rem;
            font-weight: 800;
            letter-spacing: .07em;
            line-height: 1;
            text-transform: uppercase;
        }}
        .featured-lineage-mart-row {{
            position: relative;
            z-index: 1;
            min-height: 25px;
            gap: .35rem;
            padding: .25rem .3rem;
            color: var(--text);
            font-size: .66rem;
            font-weight: 700;
            background: rgba(255, 255, 255, .55);
        }}
        .featured-lineage-connector {{
            position: relative;
            z-index: 1;
            height: 2px;
            min-width: 28px;
            border-radius: 999px;
            background: linear-gradient(90deg, rgba(37, 99, 235, .30), rgba(6, 182, 212, .34));
        }}
        .featured-lineage-connector::after {{
            content: "";
            position: absolute;
            right: -1px;
            top: 50%;
            width: 6px;
            height: 6px;
            border-top: 1.5px solid rgba(6, 182, 212, .72);
            border-right: 1.5px solid rgba(6, 182, 212, .72);
            transform: translateY(-50%) rotate(45deg);
        }}
        .featured-lineage-packet {{
            position: absolute;
            z-index: 2;
            left: 0;
            top: 50%;
            width: 6px;
            height: 6px;
            border-radius: 50%;
            background: #2563eb;
            box-shadow:
                0 0 0 3px rgba(37, 99, 235, .10),
                0 0 8px rgba(37, 99, 235, .26);
            opacity: 0;
            transform: translate3d(-50%, -50%, 0);
            pointer-events: none;
        }}
        .featured-lineage-connector-out .featured-lineage-packet,
        .featured-lineage-lane-skills .featured-lineage-packet {{
            background: #06b6d4;
        }}
        .featured-lineage-lane-jobs .featured-lineage-connector-in .featured-lineage-packet {{
            animation: featured-lineage-packet-in 5.8s linear infinite;
        }}
        .featured-lineage-lane-jobs .featured-lineage-connector-out .featured-lineage-packet {{
            animation: featured-lineage-packet-out 5.8s linear infinite;
        }}
        .featured-lineage-lane-skills .featured-lineage-connector-in .featured-lineage-packet {{
            animation: featured-lineage-packet-skill-in 5.8s linear infinite;
        }}
        .featured-lineage-lane-skills .featured-lineage-connector-out .featured-lineage-packet {{
            animation: featured-lineage-packet-skill-out 5.8s linear infinite;
        }}
        .featured-lineage-intermediate-job {{
            animation: featured-lineage-job-intermediate-state 5.8s cubic-bezier(0.22, 1, 0.36, 1) infinite;
        }}
        .featured-lineage-output-job {{
            animation: featured-lineage-job-output-state 5.8s cubic-bezier(0.22, 1, 0.36, 1) infinite;
        }}
        .featured-lineage-intermediate-skill {{
            animation: featured-lineage-skill-intermediate-state 5.8s cubic-bezier(0.22, 1, 0.36, 1) infinite;
        }}
        .featured-lineage-output-skill {{
            animation: featured-lineage-skill-output-state 5.8s cubic-bezier(0.22, 1, 0.36, 1) infinite;
        }}
        .featured-lineage-svg {{
            position: absolute;
            inset: 0;
            z-index: 1;
            width: 100%;
            height: 100%;
            pointer-events: none;
        }}
        .featured-lineage-svg marker path {{
            fill: rgba(37, 99, 235, .44);
        }}
        .featured-lineage-connector {{
            fill: none;
            stroke: rgba(100, 116, 139, .25);
            stroke-width: 1.5;
            marker-end: url(#featured-lineage-arrow);
        }}
        .featured-lineage-route {{
            fill: none;
            stroke: url(#featuredLineageFlowGradient);
            stroke-width: 2.4;
            stroke-linecap: round;
            stroke-dasharray: 82 460;
            stroke-dashoffset: 460;
            opacity: 0;
            animation: featured-lineage-route-flow 5.5s linear infinite;
        }}
        .featured-lineage-route-skill {{
            animation-delay: 2.75s;
        }}
        .featured-lineage-packet {{
            fill: var(--data-blue);
            stroke: #FFFFFF;
            stroke-width: 2.2;
            filter: drop-shadow(0 0 4px rgba(37, 99, 235, .34)) drop-shadow(0 0 9px rgba(37, 99, 235, .20));
        }}
        .featured-lineage-packet-skill {{
            fill: var(--data-cyan);
        }}
        .featured-lineage-column {{
            position: absolute;
            z-index: 3;
            display: flex;
            flex-direction: column;
            min-width: 0;
        }}
        .featured-lineage-column-staging {{
            left: 0;
            top: 6%;
            width: 29%;
            gap: .625rem;
        }}
        .featured-lineage-column-intermediate {{
            left: 34%;
            top: 50%;
            width: 31%;
            gap: .9rem;
            transform: translateY(-50%);
        }}
        .featured-lineage-column-mart {{
            right: 0;
            top: 4.5%;
            width: 34%;
            gap: .55rem;
        }}
        .featured-lineage-column-title {{
            color: var(--muted);
            font-size: .61rem;
            font-weight: 850;
            letter-spacing: .09em;
            text-transform: uppercase;
            margin-bottom: .08rem;
        }}
        .featured-lineage-node {{
            position: relative;
            z-index: 4;
            display: grid;
            grid-template-columns: auto minmax(0, 1fr);
            column-gap: .48rem;
            row-gap: .22rem;
            align-items: center;
            min-height: 46px;
            padding: .44rem .55rem;
            border: 1px solid rgba(148, 163, 184, .28);
            border-radius: 10px;
            background: rgba(255, 255, 255, .95);
            color: var(--text);
            box-shadow: 0 7px 16px rgba(15, 23, 42, .045);
            transition:
                transform 180ms ease,
                border-color 180ms ease,
                background-color 180ms ease,
                box-shadow 180ms ease;
        }}
        .featured-lineage-node-intermediate {{
            min-height: 54px;
        }}
        .featured-lineage-node-mart {{
            min-height: 49px;
        }}
        .featured-lineage-model-name {{
            min-width: 0;
            color: var(--text);
            font-size: clamp(.69rem, .78vw, .79rem);
            font-weight: 750;
            line-height: 1.1;
            overflow-wrap: normal;
            word-break: normal;
            hyphens: none;
        }}
        .featured-lineage-model-type {{
            grid-column: 2;
            color: var(--muted);
            margin-top: .18rem;
            font-size: clamp(.52rem, .55vw, .58rem);
            font-weight: 800;
            letter-spacing: .065em;
            line-height: 1;
        }}
        .featured-lineage-node-icon {{
            grid-row: 1 / span 2;
            width: .62rem;
            height: .62rem;
            border-radius: 3px;
            background: currentColor;
            box-shadow: 0 0 0 3px rgba(37, 99, 235, .08);
        }}
        .featured-lineage-node-staging {{
            color: #64748B;
            background: rgba(248, 250, 252, .96);
        }}
        .featured-lineage-node-intermediate {{
            color: var(--data-blue);
            border-color: rgba(37, 99, 235, .28);
            background: rgba(239, 246, 255, .96);
        }}
        .featured-lineage-node-mart {{
            color: var(--data-cyan);
            border-color: rgba(6, 182, 212, .22);
            background: rgba(240, 253, 250, .92);
        }}
        .featured-lineage-node-job-source,
        .featured-lineage-node-job-intermediate,
        .featured-lineage-node-job-mart {{
            animation: featured-lineage-node-job 5.5s cubic-bezier(0.22, 1, 0.36, 1) infinite;
        }}
        .featured-lineage-node-skill-source,
        .featured-lineage-node-skill-intermediate,
        .featured-lineage-node-skill-mart {{
            animation: featured-lineage-node-skill 5.5s cubic-bezier(0.22, 1, 0.36, 1) infinite;
            animation-delay: 2.75s;
        }}
        @media (hover: hover) and (pointer: fine) {{
            .featured-lineage-node:hover {{
                transform: translateY(-2px);
                border-color: rgba(37, 99, 235, 0.45);
                background-color: rgba(239, 246, 255, .98);
                box-shadow: 0 8px 20px rgba(37, 99, 235, 0.12);
            }}
        }}
        @keyframes featured-lineage-route-flow {{
            0%, 8% {{ opacity: 0; stroke-dashoffset: 460; }}
            12%, 72% {{ opacity: 1; }}
            82% {{ opacity: 0; stroke-dashoffset: 0; }}
            100% {{ opacity: 0; stroke-dashoffset: 0; }}
        }}
        @keyframes featured-lineage-packet-in {{
            0%, 3% {{ opacity: 0; left: 0; }}
            5%, 20% {{ opacity: 1; }}
            24% {{ opacity: 0; left: 100%; }}
            25%, 100% {{ opacity: 0; left: 100%; }}
        }}
        @keyframes featured-lineage-packet-out {{
            0%, 25% {{ opacity: 0; left: 0; }}
            27%, 42% {{ opacity: 1; }}
            46% {{ opacity: 0; left: 100%; }}
            47%, 100% {{ opacity: 0; left: 100%; }}
        }}
        @keyframes featured-lineage-packet-skill-in {{
            0%, 52% {{ opacity: 0; left: 0; }}
            54%, 68% {{ opacity: 1; }}
            72% {{ opacity: 0; left: 100%; }}
            73%, 100% {{ opacity: 0; left: 100%; }}
        }}
        @keyframes featured-lineage-packet-skill-out {{
            0%, 73% {{ opacity: 0; left: 0; }}
            75%, 88% {{ opacity: 1; }}
            92% {{ opacity: 0; left: 100%; }}
            93%, 100% {{ opacity: 0; left: 100%; }}
        }}
        @keyframes featured-lineage-job-intermediate-state {{
            0%, 20%, 38%, 100% {{ border-color: rgba(37, 99, 235, .30); background-color: rgba(239, 246, 255, .96); box-shadow: 0 7px 16px rgba(15, 23, 42, .045); opacity: 1; }}
            24%, 34% {{ border-color: rgba(37, 99, 235, .58); background-color: rgba(239, 246, 255, .99); box-shadow: 0 8px 20px rgba(37, 99, 235, .13); opacity: 1; }}
        }}
        @keyframes featured-lineage-job-output-state {{
            0%, 42%, 60%, 100% {{ border-color: rgba(6, 182, 212, .30); background-color: rgba(236, 254, 255, .78); box-shadow: none; opacity: 1; }}
            46%, 56% {{ border-color: rgba(6, 182, 212, .52); background-color: rgba(236, 254, 255, .92); box-shadow: 0 8px 18px rgba(6, 182, 212, .10); opacity: 1; }}
        }}
        @keyframes featured-lineage-skill-intermediate-state {{
            0%, 68%, 82%, 100% {{ border-color: rgba(37, 99, 235, .30); background-color: rgba(239, 246, 255, .96); box-shadow: 0 7px 16px rgba(15, 23, 42, .045); opacity: 1; }}
            72%, 80% {{ border-color: rgba(37, 99, 235, .58); background-color: rgba(239, 246, 255, .99); box-shadow: 0 8px 20px rgba(37, 99, 235, .13); opacity: 1; }}
        }}
        @keyframes featured-lineage-skill-output-state {{
            0%, 88%, 100% {{ border-color: rgba(6, 182, 212, .30); background-color: rgba(236, 254, 255, .78); box-shadow: none; opacity: 1; }}
            92%, 98% {{ border-color: rgba(6, 182, 212, .52); background-color: rgba(236, 254, 255, .92); box-shadow: 0 8px 18px rgba(6, 182, 212, .10); opacity: 1; }}
        }}
        @keyframes featured-lineage-node-job {{
            0%, 10%, 88%, 100% {{ border-color: rgba(148, 163, 184, .28); background-color: rgba(255, 255, 255, .95); box-shadow: 0 7px 16px rgba(15, 23, 42, .045); }}
            16%, 34% {{ border-color: rgba(37, 99, 235, .55); background-color: rgba(239, 246, 255, .98); box-shadow: 0 8px 20px rgba(37, 99, 235, .14); }}
            58%, 76% {{ border-color: rgba(6, 182, 212, .55); background-color: rgba(236, 254, 255, .96); box-shadow: 0 8px 20px rgba(6, 182, 212, .12); }}
        }}
        @keyframes featured-lineage-node-skill {{
            0%, 10%, 88%, 100% {{ border-color: rgba(148, 163, 184, .28); background-color: rgba(255, 255, 255, .95); box-shadow: 0 7px 16px rgba(15, 23, 42, .045); }}
            16%, 34% {{ border-color: rgba(37, 99, 235, .55); background-color: rgba(239, 246, 255, .98); box-shadow: 0 8px 20px rgba(37, 99, 235, .14); }}
            58%, 76% {{ border-color: rgba(6, 182, 212, .55); background-color: rgba(236, 254, 255, .96); box-shadow: 0 8px 20px rgba(6, 182, 212, .12); }}
        }}
        .home-section {{
            margin: 1.55rem 0;
        }}
        .home-about-section {{
            margin-top: 2.25rem;
        }}
        .home-section-copy {{
            color: var(--text-2);
            max-width: 720px;
            line-height: 1.65;
            margin: .6rem 0 0;
        }}
        .home-about-grid {{
            display: grid;
            grid-template-columns: minmax(0, 1.25fr) minmax(0, .75fr);
            gap: .85rem;
            margin-top: 1rem;
            overflow: visible;
        }}
        .home-skills-grid {{
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: .7rem;
            margin-top: .8rem;
            overflow: visible;
        }}
        .home-about-card,
        .home-skill-card {{
            min-height: 126px;
        }}
        .home-skill-card {{
            border-top-width: 3px;
        }}
        .home-skill-card .section-title::before {{
            content: "";
            display: inline-block;
            width: .48rem;
            height: .48rem;
            border-radius: 999px;
            margin-right: .42rem;
            vertical-align: .06rem;
            background: var(--data-blue);
        }}
        .home-skill-card-1 {{
            border-top-color: rgba(37, 99, 235, .42);
        }}
        .home-skill-card-1 .section-title::before {{
            background: var(--data-blue);
        }}
        .home-skill-card-2 {{
            border-top-color: rgba(6, 182, 212, .42);
        }}
        .home-skill-card-2 .section-title::before {{
            background: var(--data-cyan);
        }}
        .home-skill-card-3 {{
            border-top-color: rgba(79, 70, 229, .42);
        }}
        .home-skill-card-3 .section-title::before {{
            background: var(--data-indigo);
        }}
        .home-skill-card-4 {{
            border-top-color: rgba(51, 65, 85, .34);
        }}
        .home-skill-card-4 .section-title::before {{
            background: #475569;
        }}
        .home-skill-badge-wrap {{
            display: flex;
            flex-wrap: wrap;
            gap: .38rem;
            margin-top: .58rem;
        }}
        .home-skill-badge {{
            display: inline-flex;
            align-items: center;
            max-width: 100%;
            border: 1px solid var(--border);
            background: var(--tag-bg);
            color: var(--tag-text);
            border-radius: 999px;
            padding: .36rem .58rem;
            font-size: .78rem;
            font-weight: 600;
            line-height: 1.25;
            overflow-wrap: anywhere;
        }}
        @media (hover: hover) and (pointer: fine) {{
            .data-command-hero .portfolio-button:hover,
            .data-command-hero .portfolio-button:focus-visible {{
                transform: translateY(-2px);
                box-shadow: 0 10px 24px rgba(37, 99, 235, .13);
            }}
            .data-command-hero .portfolio-button-primary:hover span,
            .data-command-hero .portfolio-button-primary:focus-visible span {{
                transform: translateX(.18rem);
            }}
            .hero-skill-node:hover {{
                transform: translateY(-2px);
                border-color: rgba(37, 99, 235, 0.50);
                box-shadow: 0 10px 22px rgba(37, 99, 235, 0.12);
            }}
            .hero-profile-card:hover {{
                transform: translateY(-4px) scale(1.012);
                border-color: rgba(37, 99, 235, 0.42);
                box-shadow: 0 20px 44px rgba(37, 99, 235, 0.15);
            }}
            .home-profile-info-card:hover,
            .home-profile-info-card:focus-within {{
                transform: translateY(-5px) scale(1.025);
                border-color: rgba(37, 99, 235, 0.50);
                box-shadow: 0 18px 38px rgba(37, 99, 235, 0.17);
            }}
            .home-profile-info-card:hover .home-profile-info-name,
            .home-profile-info-card:focus-within .home-profile-info-name {{
                color: var(--accent);
            }}
            .home-profile-info-card:hover .home-profile-info-status span,
            .home-profile-info-card:focus-within .home-profile-info-status span {{
                box-shadow: 0 0 0 4px color-mix(in srgb, var(--positive) 24%, transparent), 0 0 14px color-mix(in srgb, var(--positive) 45%, transparent);
            }}
        }}
        .pipeline-step-grid {{
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: .85rem;
            margin-top: 1rem;
            overflow: visible;
        }}
        .pipeline-step-card {{
            padding: 1rem;
            min-height: 150px;
        }}
        .pipeline-step-name {{
            color: var(--text);
            font-size: 1rem;
            font-weight: 800;
            line-height: 1.25;
            margin-bottom: .45rem;
        }}
        .contact-cta {{
            display: grid;
            grid-template-columns: minmax(0, 1fr) auto;
            align-items: center;
            gap: 1.2rem;
            padding: 1.25rem;
            margin: 2rem 0 1rem;
        }}
        .home-contact-cta {{
            padding: .85rem 1rem;
            margin: 1.15rem 0 .5rem;
        }}
        .home-contact-cta p {{
            margin: 0;
            font-size: .98rem;
            line-height: 1.45;
        }}
        .home-contact-cta .contact-cta-actions {{
            margin-top: 0;
        }}
        .project-overview-header {{
            margin: .25rem 0 1.85rem;
            max-width: 920px;
        }}
        .project-overview-badges {{
            display: flex;
            flex-wrap: wrap;
            align-items: center;
            gap: .5rem;
            margin-bottom: 1rem;
        }}
        .project-verified-badge,
        .project-scale-badge {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            min-height: 30px;
            padding: 5px 10px;
            border-radius: 999px;
            font-size: .76rem;
            font-weight: 750;
            line-height: 1.1;
        }}
        .project-verified-badge {{
            border: 1px solid rgba(16, 185, 129, 0.24);
            background: rgba(16, 185, 129, 0.08);
            color: #047857;
        }}
        .project-verified-badge span {{
            width: 7px;
            height: 7px;
            border-radius: 999px;
            background: #10B981;
        }}
        .project-scale-badge {{
            border: 1px solid rgba(37, 99, 235, 0.20);
            background: rgba(239, 246, 255, 0.82);
            color: var(--data-blue);
        }}
        .project-overview-header h1 {{
            color: var(--text);
            font-size: clamp(2rem, 5vw, 3.7rem);
            line-height: 1.02;
            font-weight: 760;
            margin: 0;
        }}
        .project-overview-header p {{
            color: var(--text-2);
            max-width: 760px;
            font-size: 1.02rem;
            line-height: 1.65;
            margin: 1.05rem 0 0;
        }}
        .project-tech-stack {{
            display: flex;
            flex-wrap: wrap;
            gap: 7px;
            margin-top: 1rem;
        }}
        .project-tech-pill {{
            display: inline-flex;
            align-items: center;
            padding: 5px 9px;
            border: 1px solid rgba(37, 99, 235, 0.16);
            border-radius: 999px;
            background: rgba(239, 246, 255, 0.68);
            color: var(--data-blue);
            font-size: .78rem;
            font-weight: 650;
            line-height: 1.15;
        }}
        .project-header-actions {{
            display: flex;
            flex-wrap: wrap;
            align-items: center;
            gap: 12px;
            margin-top: 1rem;
        }}
        .project-header-secondary-action {{
            background: transparent;
        }}
        .project-evidence-compact {{
            display: inline-grid;
            grid-template-columns: repeat(2, auto);
            align-items: center;
            gap: 28px;
            margin-top: 1.5rem;
            padding: 12px 16px;
            border: 1px solid rgba(148, 163, 184, 0.24);
            border-radius: 12px;
            background: rgba(255, 255, 255, 0.82);
        }}
        .project-evidence-item {{
            display: flex;
            align-items: baseline;
            gap: 7px;
            min-width: 0;
        }}
        .project-evidence-item strong {{
            color: var(--text);
            font-size: 1.05rem;
            font-weight: 800;
            line-height: 1.1;
        }}
        .project-evidence-item span {{
            color: var(--muted);
            font-size: .78rem;
            font-weight: 700;
            white-space: nowrap;
        }}
        .project-overview-architecture-link {{
            display: inline-flex;
            align-items: center;
            color: var(--data-blue);
            font-size: .9rem;
            font-weight: 750;
            text-decoration: none;
            width: fit-content;
            margin: .25rem 0 .95rem;
        }}
        .project-overview-architecture-link:hover {{
            color: var(--accent-hover);
            text-decoration: underline;
        }}
        .pipeline-info-grid {{
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: .85rem;
            align-items: stretch;
            margin-top: 1rem;
        }}
        .pipeline-info-grid .pipeline-card {{
            position: relative;
            height: 100%;
            margin: 0;
            border-top: 3px solid rgba(6, 182, 212, .38);
        }}
        .pipeline-info-grid .pipeline-card::after {{
            content: "";
            position: absolute;
            right: .85rem;
            bottom: .75rem;
            width: 4.8rem;
            height: 2.8rem;
            opacity: .045;
            pointer-events: none;
            background:
                linear-gradient(var(--data-navy) 1px, transparent 1px),
                linear-gradient(90deg, var(--data-navy) 1px, transparent 1px);
            background-size: 100% .9rem, 1.6rem 100%;
        }}
        .contact-resume-strip {{
            display: grid;
            grid-template-columns: minmax(0, 1fr) auto;
            align-items: center;
            gap: 1rem;
            height: auto;
            padding: .8rem 1rem;
            margin-top: 1rem;
            min-height: 0;
        }}
        .contact-hover-card.contact-resume-strip {{
            min-height: 0;
            height: auto;
        }}
        .contact-resume-strip .section-copy {{
            font-size: .88rem;
            line-height: 1.4;
        }}
        .contact-resume-strip .contact-card-action {{
            margin-top: 0;
            white-space: nowrap;
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
        .project-card-featured {{
            max-width: 860px;
            min-height: 0;
            margin-left: auto;
            margin-right: auto;
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
        .project-pipeline-banner {{
            position: relative;
            align-items: stretch;
            justify-content: stretch;
            padding: .72rem .8rem;
            overflow: hidden;
            background:
                radial-gradient(circle at 50% 45%, rgba(37, 99, 235, 0.13), transparent 28%),
                linear-gradient(135deg, rgba(239, 246, 255, 0.98), rgba(255, 255, 255, 0.88)),
                repeating-linear-gradient(90deg, transparent 0 22px, rgba(147, 197, 253, 0.18) 22px 23px);
        }}
        .project-pipeline-track {{
            position: relative;
            z-index: 1;
            display: grid;
            grid-template-columns: minmax(4.5rem, 1fr) minmax(1rem, .5fr) minmax(4.9rem, 1fr) minmax(1rem, .5fr) minmax(5.4rem, 1.12fr) minmax(1rem, .5fr) minmax(4.9rem, 1fr) minmax(1rem, .5fr) minmax(4.8rem, 1fr);
            align-items: center;
            width: 100%;
            height: 100%;
            gap: .28rem;
        }}
        .project-pipeline-stage {{
            position: relative;
            z-index: 2;
            display: grid;
            justify-items: center;
            align-content: center;
            gap: .12rem;
            min-width: 0;
            min-height: 4.45rem;
            padding: .42rem .34rem;
            border: 1px solid rgba(37, 99, 235, 0.18);
            border-radius: 9px;
            background: rgba(255, 255, 255, 0.78);
            color: var(--text);
            opacity: .78;
            transform: scale(1);
            animation: project-pipeline-stage-pulse 8s ease-in-out infinite;
            box-shadow: 0 5px 14px rgba(15, 23, 42, 0.06);
        }}
        .project-pipeline-stage-1 {{ animation-delay: 0s; }}
        .project-pipeline-stage-2 {{ animation-delay: 1.45s; }}
        .project-pipeline-stage-3 {{ animation-delay: 2.9s; }}
        .project-pipeline-stage-4 {{ animation-delay: 4.35s; }}
        .project-pipeline-stage-5 {{ animation-delay: 5.8s; }}
        .project-pipeline-icon {{
            width: 1.22rem;
            height: 1.22rem;
            fill: none;
            stroke: var(--accent);
            stroke-width: 1.8;
            stroke-linecap: round;
            stroke-linejoin: round;
        }}
        .project-pipeline-label {{
            max-width: 100%;
            color: var(--text);
            font-size: .68rem;
            font-weight: 800;
            line-height: 1.05;
            text-align: center;
            white-space: normal;
        }}
        .project-pipeline-detail {{
            max-width: 100%;
            color: var(--muted);
            font-size: .55rem;
            font-weight: 700;
            line-height: 1;
            text-align: center;
            white-space: normal;
        }}
        .project-warehouse-stage {{
            min-height: 5rem;
            border-color: rgba(37, 99, 235, 0.32);
            background:
                radial-gradient(circle at 50% 36%, rgba(37, 99, 235, 0.18), transparent 55%),
                rgba(255, 255, 255, 0.86);
            animation-name: project-pipeline-warehouse-pulse;
        }}
        .project-warehouse-stage .project-pipeline-icon {{
            width: 1.42rem;
            height: 1.42rem;
        }}
        .project-pipeline-connector {{
            position: relative;
            height: 2px;
            min-width: 0;
            border-radius: 999px;
            background: linear-gradient(90deg, rgba(37, 99, 235, 0.18), rgba(37, 99, 235, 0.5));
            overflow: hidden;
        }}
        .project-pipeline-connector::after {{
            content: "";
            position: absolute;
            inset: 0;
            background: linear-gradient(90deg, transparent, rgba(37, 99, 235, 0.78), transparent);
            animation: project-pipeline-connector-flow 2.8s linear infinite;
        }}
        .project-pipeline-particle {{
            position: absolute;
            z-index: 1;
            top: 50%;
            left: 3.2%;
            width: .46rem;
            height: .46rem;
            border-radius: 999px;
            background: rgba(37, 99, 235, 0.92);
            box-shadow: 0 0 11px rgba(37, 99, 235, 0.42);
            transform: translate3d(0, -50%, 0);
            animation: project-pipeline-particle-flow 8s cubic-bezier(0.45, 0, 0.2, 1) infinite;
        }}
        .project-pipeline-particle-2 {{
            animation-delay: 2.65s;
            width: .38rem;
            height: .38rem;
            opacity: .82;
        }}
        .project-pipeline-particle-3 {{
            animation-delay: 5.25s;
            width: .34rem;
            height: .34rem;
            opacity: .72;
        }}
        @keyframes project-pipeline-particle-flow {{
            0% {{ left: 3.2%; opacity: 0; transform: translate3d(0, -50%, 0); }}
            7%, 82% {{ opacity: 1; }}
            95%, 100% {{ left: 96.8%; opacity: 0; transform: translate3d(-100%, -50%, 0); }}
        }}
        @keyframes project-pipeline-stage-pulse {{
            0%, 16%, 100% {{
                opacity: .78;
                transform: scale(1);
                border-color: rgba(37, 99, 235, 0.18);
                box-shadow: 0 5px 14px rgba(15, 23, 42, 0.06);
            }}
            7%, 11% {{
                opacity: 1;
                transform: translateY(-2px) scale(1.025);
                border-color: rgba(37, 99, 235, 0.50);
                box-shadow: 0 8px 22px rgba(37, 99, 235, 0.16);
            }}
        }}
        @keyframes project-pipeline-warehouse-pulse {{
            0%, 16%, 100% {{
                opacity: .82;
                transform: scale(1);
                border-color: rgba(37, 99, 235, 0.32);
                box-shadow: 0 5px 14px rgba(15, 23, 42, 0.06);
            }}
            7%, 11% {{
                opacity: 1;
                transform: translateY(-2px) scale(1.03);
                border-color: rgba(37, 99, 235, 0.56);
                box-shadow: 0 8px 24px rgba(37, 99, 235, 0.20);
            }}
        }}
        @keyframes project-pipeline-connector-flow {{
            from {{ transform: translateX(-100%); }}
            to {{ transform: translateX(100%); }}
        }}
        @media (max-width: 680px) {{
            .project-pipeline-banner {{
                padding: .58rem .55rem;
            }}
            .project-pipeline-track {{
                grid-template-columns: repeat(5, minmax(0, 1fr));
                gap: .18rem;
            }}
            .project-pipeline-stage {{
                min-height: 4rem;
                padding: .32rem .18rem;
                border-radius: 8px;
            }}
            .project-warehouse-stage {{
                min-height: 4.25rem;
            }}
            .project-pipeline-icon {{
                width: 1rem;
                height: 1rem;
            }}
            .project-warehouse-stage .project-pipeline-icon {{
                width: 1.14rem;
                height: 1.14rem;
            }}
            .project-pipeline-label {{
                font-size: .58rem;
            }}
            .project-pipeline-detail {{
                display: none;
            }}
            .project-pipeline-connector-1 {{
                position: absolute;
                z-index: 1;
                left: 8%;
                right: 8%;
                top: 50%;
                width: auto;
            }}
            .project-pipeline-connector-2,
            .project-pipeline-connector-3,
            .project-pipeline-connector-4 {{
                display: none;
            }}
            .project-pipeline-particle {{
                width: .34rem;
                height: .34rem;
                box-shadow: 0 0 7px rgba(37, 99, 235, 0.32);
            }}
            .project-card-featured .project-actions {{
                flex-direction: column;
            }}
            .project-card-featured .project-action {{
                width: 100%;
            }}
        }}
        @media (prefers-reduced-motion: reduce) {{
            .project-pipeline-stage,
            .project-warehouse-stage {{
                opacity: 1;
                transform: none;
                animation: none !important;
            }}
            .project-pipeline-connector::after,
            .project-pipeline-particle {{
                animation: none !important;
            }}
            .project-pipeline-particle {{
                display: none;
            }}
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
        .project-actions {{
            display: flex;
            flex-wrap: wrap;
            gap: .55rem;
            margin-top: 1rem;
        }}
        .project-action {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            min-height: 2.45rem;
            padding: .58rem .85rem;
            border-radius: 10px;
            border: 1px solid var(--border);
            background: var(--surface);
            color: var(--text);
            font-weight: 600;
            line-height: 1.15;
            white-space: nowrap;
            text-decoration: none;
            flex: 1 1 12rem;
        }}
        .project-action-primary {{
            background: var(--accent);
            border-color: var(--accent);
            color: var(--on-accent) !important;
            box-shadow: var(--shadow-accent);
        }}
        .timeline-card ul {{
            color: var(--text-2);
            margin-top: .55rem;
            padding-left: 1.2rem;
        }}
        .about-hover-card {{
            transform-origin: center;
            outline: none;
            overflow: visible;
            margin-top: .85rem;
            margin-bottom: 1.15rem;
            transition:
                transform 220ms ease,
                border-color 220ms ease,
                background-color 220ms ease,
                box-shadow 220ms ease;
        }}
        .experience-hover-card {{
            transform-origin: center;
            outline: none;
            overflow: visible;
            margin-top: .85rem;
            margin-bottom: 1.15rem;
            transition:
                transform 230ms cubic-bezier(0.22, 1, 0.36, 1),
                border-color 230ms ease,
                background-color 230ms ease,
                box-shadow 230ms ease;
        }}
        .about-hover-card .section-title {{
            transform-origin: left center;
            transition: color 220ms ease, font-size 220ms ease, transform 220ms ease;
        }}
        .experience-hover-card .project-title {{
            transform-origin: left center;
            transition: color 230ms ease;
        }}
        @media (hover: hover) and (pointer: fine) {{
            .about-hover-card:hover,
            .about-hover-card:focus-within {{
                transform: translateY(-3px) scale(1.018);
                border-color: rgba(37, 99, 235, 0.45);
                background-color: rgba(239, 246, 255, 0.65);
                box-shadow: 0 12px 28px rgba(37, 99, 235, 0.14);
                position: relative;
                z-index: 2;
            }}
            .experience-hover-card:hover,
            .experience-hover-card:focus-within {{
                transform: translateY(-4px) scale(1.015);
                border-color: rgba(37, 99, 235, 0.38);
                background-color: rgba(239, 246, 255, 0.62);
                box-shadow: 0 14px 30px rgba(37, 99, 235, 0.13);
                position: relative;
                z-index: 2;
            }}
            .about-hover-card:hover .section-title,
            .about-hover-card:focus-within .section-title {{
                color: var(--accent);
                font-size: 1.12rem;
            }}
            .experience-hover-card:hover .project-title,
            .experience-hover-card:focus-within .project-title {{
                color: var(--accent);
            }}
        }}
        @media (hover: none), (pointer: coarse), (max-width: 760px) {{
            .about-hover-card,
            .experience-hover-card {{
                transform: none;
                transition: none;
            }}
            .about-hover-card:hover,
            .about-hover-card:focus-within,
            .experience-hover-card:hover,
            .experience-hover-card:focus-within {{
                transform: none;
                border-color: var(--border);
                background-color: var(--surface);
                box-shadow: var(--shadow);
            }}
            .about-hover-card:hover .section-title,
            .about-hover-card:focus-within .section-title,
            .experience-hover-card:hover .project-title,
            .experience-hover-card:focus-within .project-title {{
                color: var(--text);
                transform: none;
            }}
            .about-hover-card:hover .section-title,
            .about-hover-card:focus-within .section-title {{
                font-size: 1.08rem;
            }}
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
        .home-card,
        .skill-card,
        .pipeline-card {{
            transform-origin: center;
            will-change: transform;
            transition:
                transform 240ms ease,
                border-color 240ms ease,
                background-color 240ms ease,
                box-shadow 240ms ease;
        }}
        .home-card .section-title,
        .skill-card .section-title,
        .pipeline-card .section-title,
        .pipeline-card strong {{
            transition: color 240ms ease;
        }}
        .job-intelligence-hover-card,
        .data-quality-hover-card,
        .home-about-card,
        .home-skill-card,
        .featured-project-card,
        .pipeline-step-card {{
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 12px;
            box-shadow: var(--shadow);
            transform-origin: center;
            overflow: visible;
            will-change: transform;
            transition:
                transform 250ms ease,
                border-color 250ms ease,
                background-color 250ms ease,
                box-shadow 250ms ease;
        }}
        .contact-hover-card {{
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 12px;
            box-shadow: var(--shadow);
            transform-origin: center;
            overflow: visible;
            padding: 1rem;
            margin: .7rem 0 1rem;
            min-height: 210px;
            transition:
                transform 230ms cubic-bezier(0.22, 1, 0.36, 1),
                border-color 230ms ease,
                background-color 230ms ease,
                box-shadow 230ms ease;
        }}
        .data-quality-hover-card {{
            padding: 1rem;
            margin: .7rem 0 1rem;
        }}
        .quality-summary-panel,
        .quality-limitation-callout {{
            position: relative;
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 12px;
            box-shadow: var(--shadow);
            padding: 1rem;
            margin: .85rem 0 1rem;
        }}
        .quality-summary-grid {{
            position: relative;
            z-index: 1;
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: .65rem;
            margin-top: .4rem;
        }}
        .quality-summary-panel::after {{
            content: "";
            position: absolute;
            right: 1rem;
            top: .85rem;
            width: 7rem;
            height: 4rem;
            opacity: .05;
            pointer-events: none;
            background:
                radial-gradient(circle, var(--data-green) 0 2px, transparent 3px),
                linear-gradient(90deg, transparent 47%, var(--data-green) 48% 52%, transparent 53%);
            background-size: 2rem 2rem, 100% 100%;
        }}
        .quality-summary-item {{
            min-width: 0;
            border: 1px solid rgba(37, 99, 235, .16);
            border-radius: 10px;
            background: rgba(239, 246, 255, .52);
            padding: .65rem .75rem;
        }}
        .quality-summary-item-1,
        .quality-summary-item-2,
        .quality-summary-item-3,
        .quality-summary-item-4,
        .quality-summary-item-6 {{
            border-color: rgba(16, 185, 129, .24);
            background: rgba(16, 185, 129, .06);
        }}
        .quality-summary-item-5 {{
            border-color: rgba(245, 158, 11, .28);
            background: var(--data-amber-soft);
        }}
        .quality-summary-item span {{
            display: block;
            color: var(--muted);
            font-size: .74rem;
            font-weight: 750;
            text-transform: uppercase;
            letter-spacing: .035em;
            line-height: 1.2;
        }}
        .quality-summary-item strong {{
            display: block;
            color: var(--text);
            font-size: .92rem;
            line-height: 1.25;
            margin-top: .22rem;
        }}
        .quality-limitation-callout {{
            border-color: rgba(245, 158, 11, .38);
            border-left: 4px solid var(--data-amber);
            background:
                linear-gradient(135deg, rgba(245, 158, 11, .10), rgba(255, 255, 255, .94));
        }}
        .quality-limitation-callout .section-title::before {{
            content: "";
            display: inline-block;
            width: .52rem;
            height: .52rem;
            border-radius: 999px;
            margin-right: .42rem;
            background: var(--data-amber);
            box-shadow: 0 0 0 3px var(--data-amber-soft);
            vertical-align: .04rem;
        }}
        .quality-limitation-callout p {{
            color: var(--text-2);
            margin: .35rem 0 0;
            line-height: 1.45;
        }}
        .data-quality-detail {{
            padding: .15rem 0 .3rem;
            animation: data-quality-detail-in 220ms ease-out both;
        }}
        @keyframes data-quality-detail-in {{
            from {{ opacity: 0; transform: translateY(.25rem); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        .job-intelligence-hover-card .section-title,
        .job-intelligence-hover-card strong,
        .data-quality-hover-card .section-title,
        .home-about-card .section-title,
        .home-skill-card .section-title,
        .featured-project-card h2,
        .pipeline-step-card .pipeline-step-name {{
            transition: color 250ms ease;
        }}
        .contact-hover-card .section-title {{
            transition: color 230ms ease;
        }}
        .contact-card-action {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            min-height: 2.45rem;
            padding: .58rem .85rem;
            border-radius: 10px;
            border: 1px solid var(--accent);
            background: var(--accent);
            color: var(--on-accent) !important;
            font-weight: 600;
            line-height: 1.15;
            text-decoration: none;
            box-shadow: var(--shadow-accent);
            margin-top: .55rem;
        }}
        .quality-metric-grid {{
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: .7rem;
            margin: .8rem 0 .65rem;
        }}
        .quality-metric {{
            border: 1px solid var(--border);
            border-radius: 10px;
            background: var(--surface-2);
            padding: .65rem .7rem;
        }}
        .quality-metric-label {{
            color: var(--muted);
            font-size: .78rem;
            line-height: 1.25;
        }}
        .quality-metric-value {{
            color: var(--text);
            font-size: 1.22rem;
            font-weight: 700;
            line-height: 1.2;
            margin-top: .22rem;
        }}
        @media (hover: hover) and (pointer: fine) {{
            .home-card:hover,
            .home-card:focus-within,
            .skill-card:hover,
            .skill-card:focus-within,
            .pipeline-card:hover,
            .pipeline-card:focus-within {{
                transform: translateY(-3px);
                border-color: rgba(37, 99, 235, 0.30);
                background-color: rgba(239, 246, 255, 0.58);
                box-shadow: 0 14px 28px rgba(15, 23, 42, 0.09);
                position: relative;
                z-index: 2;
            }}
            .home-card:hover .section-title,
            .home-card:focus-within .section-title,
            .skill-card:hover .section-title,
            .skill-card:focus-within .section-title,
            .pipeline-card:hover .section-title,
            .pipeline-card:focus-within .section-title,
            .pipeline-card:hover strong,
            .pipeline-card:focus-within strong {{
                color: var(--accent);
            }}
            .job-intelligence-hover-card:hover,
            .job-intelligence-hover-card:focus-within,
            .data-quality-hover-card:hover,
            .data-quality-hover-card:focus-within,
            .home-about-card:hover,
            .home-about-card:focus-within,
            .home-skill-card:hover,
            .home-skill-card:focus-within,
            .featured-project-card:hover,
            .featured-project-card:focus-within,
            .pipeline-step-card:hover,
            .pipeline-step-card:focus-within {{
                transform: translateY(-4px) scale(1.012);
                border-color: rgba(37, 99, 235, 0.30);
                background-color: rgba(239, 246, 255, 0.58);
                box-shadow: 0 14px 28px rgba(15, 23, 42, 0.09);
                position: relative;
                z-index: 2;
            }}
            .contact-hover-card:hover,
            .contact-hover-card:focus-within {{
                transform: translateY(-4px) scale(1.015);
                border-color: rgba(37, 99, 235, 0.38);
                background-color: rgba(239, 246, 255, 0.62);
                box-shadow: 0 14px 30px rgba(37, 99, 235, 0.13);
                position: relative;
                z-index: 2;
            }}
            .contact-hover-card.contact-resume-strip:hover,
            .contact-hover-card.contact-resume-strip:focus-within {{
                transform: translateY(-2px);
                border-color: rgba(37, 99, 235, 0.38);
                background-color: rgba(239, 246, 255, 0.62);
                box-shadow: 0 12px 24px rgba(37, 99, 235, 0.11);
            }}
            .job-intelligence-hover-card:hover .section-title,
            .job-intelligence-hover-card:focus-within .section-title,
            .job-intelligence-hover-card:hover strong,
            .job-intelligence-hover-card:focus-within strong,
            .data-quality-hover-card:hover .section-title,
            .data-quality-hover-card:focus-within .section-title,
            .home-about-card:hover .section-title,
            .home-about-card:focus-within .section-title,
            .home-skill-card:hover .section-title,
            .home-skill-card:focus-within .section-title,
            .featured-project-card:hover h2,
            .featured-project-card:focus-within h2,
            .pipeline-step-card:hover .pipeline-step-name,
            .pipeline-step-card:focus-within .pipeline-step-name {{
                color: var(--accent);
            }}
            .contact-hover-card:hover .section-title,
            .contact-hover-card:focus-within .section-title {{
                color: var(--accent);
            }}
        }}
        @media (hover: none), (pointer: coarse), (max-width: 760px) {{
            .home-card,
            .skill-card,
            .pipeline-card,
            .job-intelligence-hover-card,
            .contact-hover-card,
            .data-quality-hover-card,
            .home-about-card,
            .home-skill-card,
            .featured-project-card,
            .pipeline-step-card {{
                transform: none;
                will-change: auto;
            }}
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
        .st-key-dashboard_filter_panel {{
            display: block;
            padding: 1.25rem 1.3rem 1.1rem;
            margin: .85rem 0 .7rem;
            border: 1px solid var(--border);
            border-radius: 12px;
            background: var(--surface);
            box-shadow: var(--shadow);
        }}
        .market-filters-heading {{
            margin: 0 0 .9rem;
            line-height: 1.15;
        }}
        .st-key-market_basic_filters_grid [data-testid="stHorizontalBlock"] {{
            gap: clamp(1.2rem, 1.6vw, 1.5rem);
        }}
        .st-key-market_basic_filters_grid [data-testid="stWidgetLabel"],
        .st-key-market_advanced_filters [data-testid="stWidgetLabel"] {{
            margin-bottom: .45rem;
        }}
        .st-key-market_advanced_filters {{
            margin-top: .7rem;
        }}
        .dashboard-results-status {{
            display: inline-flex;
            align-items: center;
            min-height: 2.35rem;
            color: var(--tag-text);
            background: var(--tag-bg);
            border: 1px solid var(--border);
            border-radius: 999px;
            padding: .42rem .75rem;
            font-size: .84rem;
            font-weight: 750;
            margin: .4rem 0 .75rem;
        }}
        .dashboard-primary-kpis {{
            display: grid;
            grid-template-columns: repeat(4, minmax(0, 1fr));
            gap: .75rem;
            margin: .75rem 0 .75rem;
        }}
        .dashboard-primary-kpi {{
            min-width: 0;
            min-height: 112px;
            padding: .9rem 1rem;
            border: 1px solid var(--border);
            border-top: 3px solid var(--data-blue);
            border-radius: 12px;
            background: var(--surface);
            box-shadow: var(--shadow);
        }}
        .dashboard-primary-kpi-2 {{
            border-top-color: var(--data-cyan);
        }}
        .dashboard-primary-kpi-3 {{
            border-top-color: #64748B;
        }}
        .dashboard-primary-kpi-4 {{
            border-top-color: var(--data-green);
        }}
        .dashboard-kpi-label {{
            color: var(--muted);
            font-size: .78rem;
            font-weight: 750;
            text-transform: uppercase;
            letter-spacing: .035em;
        }}
        .dashboard-kpi-value {{
            color: var(--text);
            font-size: clamp(1.35rem, 2.8vw, 1.85rem);
            font-weight: 850;
            line-height: 1.1;
            margin-top: .34rem;
            overflow-wrap: anywhere;
        }}
        .dashboard-kpi-note {{
            color: var(--muted);
            font-size: .76rem;
            line-height: 1.3;
            margin-top: .38rem;
        }}
        .dashboard-metadata-strip {{
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            margin: 0 0 1.2rem;
            padding: .65rem .85rem;
            border: 1px solid rgba(37, 99, 235, .16);
            border-radius: 12px;
            background: rgba(239, 246, 255, .55);
        }}
        .dashboard-meta-item {{
            min-width: 0;
            padding: .15rem .85rem;
            border-left: 1px solid rgba(37, 99, 235, .16);
            border-top: 3px solid transparent;
        }}
        .dashboard-meta-item-1 {{
            border-top-color: var(--data-indigo);
        }}
        .dashboard-meta-item-2 {{
            border-top-color: var(--data-amber);
        }}
        .dashboard-meta-item:first-child {{
            border-left: 0;
            padding-left: 0;
        }}
        .dashboard-meta-item span {{
            display: block;
            color: var(--muted);
            font-size: .72rem;
            font-weight: 750;
            text-transform: uppercase;
            letter-spacing: .035em;
        }}
        .dashboard-meta-item strong {{
            display: block;
            color: var(--text);
            font-size: .94rem;
            line-height: 1.2;
            margin-top: .18rem;
            overflow-wrap: anywhere;
        }}
        .dashboard-methodology {{
            color: var(--text-2);
            font-size: .9rem;
            line-height: 1.55;
        }}
        .dashboard-methodology p {{
            margin: .35rem 0;
        }}
        .dashboard-compact-footer {{
            color: var(--muted);
            border-top: 1px solid var(--border);
            margin-top: 1.6rem;
            padding-top: .75rem;
            font-size: .82rem;
        }}
        .dashboard-compact-footer a {{
            color: var(--accent);
            font-weight: 750;
            text-decoration: none;
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
            grid-template-columns: repeat(7, minmax(0, 1fr));
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
        .pipeline-step strong {{
            display: block;
            line-height: 1.25;
        }}
        .pipeline-step small {{
            display: block;
            color: var(--muted);
            font-weight: 500;
            font-size: .76rem;
            line-height: 1.3;
            margin-top: .28rem;
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
        .st-key-market_dashboard_chart_job_title_demand,
        .st-key-market_dashboard_chart_company_activity,
        .st-key-market_dashboard_chart_salary_by_job_title,
        .st-key-market_dashboard_chart_salary_by_country,
        .st-key-market_dashboard_chart_remote_salary,
        .st-key-market_dashboard_chart_monthly_posting_trend,
        .st-key-market_dashboard_chart_monthly_growth,
        .st-key-market_dashboard_chart_technical_skill_demand,
        .st-key-market_dashboard_chart_high_salary_skills,
        .st-key-market_dashboard_chart_data_engineer_skill_demand {{
            opacity: 1;
            transform: none;
            transform-origin: center center;
            border: 1px solid transparent;
            border-radius: 12px;
            overflow: visible;
            transition:
                transform 220ms ease,
                border-color 220ms ease,
                box-shadow 220ms ease;
        }}
        .market-chart-reveal-ready {{
            opacity: 0 !important;
            transform: translate3d(-60px, 0, 0) !important;
            transition: none !important;
            will-change: opacity, transform;
        }}
        .market-chart-reveal-visible {{
            opacity: 1 !important;
            transform: translate3d(0, 0, 0) !important;
            transition:
                opacity 650ms ease-out,
                transform 650ms cubic-bezier(0.22, 1, 0.36, 1) !important;
            will-change: opacity, transform;
        }}
        .market-chart-reveal-complete {{
            opacity: 1 !important;
            transform: none;
            transition:
                transform 220ms ease,
                border-color 220ms ease,
                box-shadow 220ms ease;
            will-change: auto;
        }}
        @media (hover: hover) and (pointer: fine) {{
            .market-chart-reveal-complete:hover {{
                transform: translate3d(0, -2px, 0) scale(1.006);
                border-color: rgba(37, 99, 235, 0.40);
                box-shadow: 0 10px 24px rgba(37, 99, 235, 0.12);
                position: relative;
                z-index: 2;
            }}
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
        .st-key-dashboard_filter_panel [data-baseweb="select"] > div:focus-within {{
            outline: 0 !important;
            border-color: rgba(37, 99, 235, 0.70) !important;
            box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.12) !important;
        }}
        .st-key-dashboard_filter_panel [data-baseweb="select"] input,
        .st-key-dashboard_filter_panel [data-baseweb="select"] input:focus,
        .st-key-dashboard_filter_panel [data-baseweb="select"] input:focus-visible {{
            border: 0 !important;
            outline: 0 !important;
            box-shadow: none !important;
            background: transparent !important;
            border-radius: 0 !important;
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
            line-height: 1.15;
            margin: 0 0 .7rem;
        }}
        @media (max-width: 1100px) {{
            .portfolio-hero {{
                grid-template-columns: minmax(0, 1.45fr) minmax(280px, .72fr);
                column-gap: clamp(1.5rem, 3vw, 2.4rem);
            }}
            .portfolio-hero h1 {{
                font-size: clamp(3rem, 5vw, 4.35rem);
            }}
            .hero-profile-card {{
                width: min(100%, 310px);
            }}
            .hero-profile-name {{
                font-size: 1.42rem;
            }}
            .hero-skill-section {{
                width: min(100%, 700px);
            }}
            .featured-project-card {{
                grid-template-columns: 1fr;
            }}
            .featured-preview,
            .featured-lineage-preview {{
                width: 100%;
                justify-self: stretch;
            }}
            .featured-lineage-canvas {{
                height: clamp(335px, 34vw, 360px);
            }}
        }}
        @media (max-width: 1024px) {{
            .pipeline {{ grid-template-columns: repeat(3, minmax(0, 1fr)); }}
            .featured-preview img {{ max-height: 320px; }}
            .featured-lineage-preview {{ min-height: 0; }}
            .st-key-market_basic_filters_grid [data-testid="stHorizontalBlock"] {{
                display: grid;
                grid-template-columns: repeat(2, minmax(0, 1fr));
                column-gap: 1rem;
                row-gap: 1rem;
            }}
            .st-key-market_basic_filters_grid [data-testid="column"] {{
                width: 100% !important;
            }}
            .hero-skill-pipeline {{
                grid-template-columns: minmax(0, 12.5rem);
                justify-content: start;
                gap: .7rem;
            }}
            .hero-skill-rail {{
                top: .5rem;
                bottom: .5rem;
                left: 50%;
                right: auto;
                width: 2px;
                height: auto;
                transform: translateX(-50%);
                background: linear-gradient(180deg, rgba(148, 163, 184, .38), rgba(37, 99, 235, .48), rgba(6, 182, 212, .38));
            }}
            .hero-skill-packet-track {{
                left: 50%;
                top: .5rem;
                right: auto;
                bottom: .5rem;
                width: 0;
                height: auto;
                animation: hero-skill-packet-run-mobile 4.8s linear infinite;
            }}
            .hero-skill-packet {{
                left: 50%;
                top: 0;
                transform: translate3d(-50%, -50%, 0);
            }}
            .hero-skill-port {{
                left: 50%;
                transform: translateX(-50%);
            }}
            .hero-skill-port-in {{
                top: -3px;
            }}
            .hero-skill-port-out {{
                top: auto;
                right: auto;
                bottom: -3px;
            }}
            .dashboard-primary-kpis,
            .dashboard-metadata-strip {{
                grid-template-columns: repeat(2, minmax(0, 1fr));
            }}
            .quality-summary-grid {{
                grid-template-columns: repeat(2, minmax(0, 1fr));
            }}
            .pipeline-info-grid {{
                grid-template-columns: repeat(2, minmax(0, 1fr));
            }}
            .pipeline-info-grid .pipeline-card:last-child {{
                grid-column: 1 / -1;
            }}
            .dashboard-meta-item-1,
            .dashboard-meta-item-3 {{
                border-left: 0;
                padding-left: 0;
            }}
        }}
        @media (max-width: 760px) {{
            .project-card-featured {{ max-width: 100%; }}
            .portfolio-hero {{
                grid-template-columns: 1fr;
                padding-top: 1rem;
                row-gap: 1.15rem;
            }}
            .data-command-hero {{
                padding: 1rem;
                border-radius: 18px;
                background:
                    radial-gradient(circle at 50% 12%, rgba(37, 99, 235, .10), transparent 32%),
                    linear-gradient(145deg, rgba(255, 255, 255, .98), rgba(248, 250, 252, .94));
            }}
            .data-blueprint-grid {{
                opacity: .28;
                background-size: 28px 28px;
            }}
            .hero-value-rotator {{
                width: 100%;
            }}
            .hero-copy,
            .hero-profile-card,
            .hero-skill-section {{
                grid-column: 1;
                grid-row: auto;
            }}
            .portfolio-hero h1 {{
                font-size: clamp(2.65rem, 15vw, 3.65rem);
                margin-top: 1.35rem;
                max-width: 100%;
            }}
            .hero-description {{
                margin-top: 1.35rem;
            }}
            .hero-actions {{
                margin-top: 1.25rem;
            }}
            .hero-profile-card {{
                width: min(100%, 300px);
                margin: 0 auto;
                transform: none;
            }}
            .hero-profile-identity {{
                text-align: center;
                padding: .9rem .2rem .15rem;
            }}
            .hero-profile-meta {{
                justify-content: center;
            }}
            .hero-skill-section {{
                width: 100%;
                margin-top: 0;
            }}
            .hero-skill-pipeline {{
                grid-template-columns: minmax(0, 100%);
                justify-content: stretch;
            }}
            .hero-photo-shell {{
                order: -1;
                width: min(100%, 300px);
            }}
            .st-key-home_profile_photo_shell,
            .st-key-home_profile_info_card {{
                width: min(100%, 300px);
                transform: none;
            }}
            .home-profile-info-card {{
                transform: none;
            }}
            .home-about-grid,
            .home-skills-grid,
            .pipeline-step-grid,
            .pipeline-info-grid {{
                grid-template-columns: 1fr;
            }}
            .featured-lineage-preview {{
                min-height: auto;
                padding: .85rem;
            }}
            .featured-lineage-header {{
                align-items: flex-start;
                flex-direction: column;
                gap: .15rem;
            }}
            .featured-lineage-canvas {{
                display: grid;
                grid-template-columns: 1fr;
                gap: .65rem;
                min-height: 0;
                height: auto;
            }}
            .featured-lineage-lanes {{
                grid-template-rows: auto auto;
                gap: .7rem;
                height: auto;
            }}
            .featured-lineage-lane {{
                grid-template-columns: 1fr;
                gap: .45rem;
                padding: 1.45rem .7rem .7rem;
            }}
            .featured-lineage-connector {{
                justify-self: center;
                width: 2px;
                min-width: 0;
                height: 22px;
                background: linear-gradient(180deg, rgba(37, 99, 235, .30), rgba(6, 182, 212, .34));
            }}
            .featured-lineage-connector::after {{
                right: auto;
                top: auto;
                left: 50%;
                bottom: -1px;
                transform: translateX(-50%) rotate(135deg);
            }}
            .featured-lineage-packet {{
                left: 50%;
                top: 0;
                transform: translate3d(-50%, -50%, 0);
            }}
            .featured-lineage-lane-jobs .featured-lineage-connector-in .featured-lineage-packet {{
                animation-name: featured-lineage-packet-down-in;
            }}
            .featured-lineage-lane-jobs .featured-lineage-connector-out .featured-lineage-packet {{
                animation-name: featured-lineage-packet-down-out;
            }}
            .featured-lineage-lane-skills .featured-lineage-connector-in .featured-lineage-packet {{
                animation-name: featured-lineage-packet-down-skill-in;
            }}
            .featured-lineage-lane-skills .featured-lineage-connector-out .featured-lineage-packet {{
                animation-name: featured-lineage-packet-down-skill-out;
            }}
            .featured-lineage-mart-group::before,
            .featured-lineage-source-group::after {{
                display: none;
            }}
            .featured-lineage-svg {{
                display: none;
            }}
            .featured-lineage-column {{
                position: relative;
                left: auto;
                right: auto;
                top: auto;
                width: 100%;
                transform: none;
                gap: .42rem;
                padding-left: .75rem;
                border-left: 2px solid rgba(6, 182, 212, .26);
            }}
            .featured-lineage-column-title {{
                margin-bottom: .05rem;
            }}
            .featured-lineage-column:not(:last-child)::after {{
                content: "";
                width: 7px;
                height: 7px;
                border-right: 2px solid rgba(6, 182, 212, .65);
                border-bottom: 2px solid rgba(6, 182, 212, .65);
                transform: rotate(45deg);
                margin: .1rem 0 .05rem .2rem;
            }}
            .featured-lineage-node {{
                min-height: 0;
                padding: .48rem .55rem;
            }}
            .featured-lineage-node small {{
                display: none;
            }}
            .project-overview-header {{
                margin-bottom: 1.45rem;
            }}
            .project-header-actions {{
                gap: .65rem;
            }}
            .project-header-actions .portfolio-button {{
                flex: 1 1 13rem;
            }}
            .project-evidence-compact {{
                display: grid;
                grid-template-columns: 1fr;
                gap: .6rem;
                width: 100%;
            }}
            .project-evidence-item {{
                justify-content: space-between;
                align-items: center;
                gap: 1rem;
            }}
            .contact-cta {{
                grid-template-columns: 1fr;
            }}
            .contact-cta-actions {{
                width: 100%;
            }}
            .contact-cta-actions .portfolio-button,
            .hero-actions .portfolio-button {{
                flex: 1 1 13rem;
            }}
            .contact-resume-strip {{
                grid-template-columns: 1fr;
            }}
            .contact-resume-strip .contact-card-action {{
                width: 100%;
            }}
            .st-key-dashboard_filter_panel {{
                padding: 1.05rem 1rem .95rem;
            }}
            .market-filters-heading {{
                margin-bottom: .9rem;
            }}
            .st-key-market_basic_filters_grid [data-testid="stHorizontalBlock"] {{
                grid-template-columns: 1fr;
                row-gap: .9rem;
            }}
            .dashboard-primary-kpis,
            .dashboard-metadata-strip {{
                grid-template-columns: 1fr;
            }}
            .quality-summary-grid {{
                grid-template-columns: 1fr;
            }}
            .dashboard-meta-item {{
                border-left: 0;
                border-top: 1px solid rgba(37, 99, 235, .14);
                padding: .55rem 0;
            }}
            .dashboard-meta-item:first-child {{
                border-top: 0;
                padding-top: .15rem;
            }}
            .dashboard-results-status {{
                width: 100%;
                justify-content: center;
                border-radius: 12px;
            }}
            .st-key-market_dashboard_chart_job_title_demand,
            .st-key-market_dashboard_chart_company_activity,
            .st-key-market_dashboard_chart_salary_by_job_title,
            .st-key-market_dashboard_chart_salary_by_country,
            .st-key-market_dashboard_chart_remote_salary,
            .st-key-market_dashboard_chart_monthly_posting_trend,
            .st-key-market_dashboard_chart_monthly_growth,
            .st-key-market_dashboard_chart_technical_skill_demand,
            .st-key-market_dashboard_chart_high_salary_skills,
            .st-key-market_dashboard_chart_data_engineer_skill_demand {{
                animation: none !important;
                opacity: 1 !important;
                translate: 0 0 !important;
                transform: none !important;
            }}
        }}
        @media (max-width: 860px) {{
            .dataset-metrics {{ grid-template-columns: 1fr; }}
            .quality-metric-grid {{ grid-template-columns: 1fr; }}
        }}
        @media (max-width: 560px) {{
            .block-container {{ padding: .35rem 1rem 2.5rem; }}
            .pipeline {{ grid-template-columns: 1fr; }}
            .section-card {{ padding: 1rem; }}
            .kpi-card {{ min-height: 118px; }}
        }}
        @keyframes hero-skill-packet-run-mobile {{
            0% {{ opacity: 1; transform: translate3d(0, 0, 0); }}
            94% {{ opacity: 1; transform: translate3d(0, 100%, 0); }}
            95%, 100% {{ opacity: 0; transform: translate3d(0, 100%, 0); }}
        }}
        @keyframes featured-lineage-packet-down-in {{
            0%, 3% {{ opacity: 0; top: 0; }}
            5%, 20% {{ opacity: 1; }}
            24% {{ opacity: 0; top: 100%; }}
            25%, 100% {{ opacity: 0; top: 100%; }}
        }}
        @keyframes featured-lineage-packet-down-out {{
            0%, 25% {{ opacity: 0; top: 0; }}
            27%, 42% {{ opacity: 1; }}
            46% {{ opacity: 0; top: 100%; }}
            47%, 100% {{ opacity: 0; top: 100%; }}
        }}
        @keyframes featured-lineage-packet-down-skill-in {{
            0%, 52% {{ opacity: 0; top: 0; }}
            54%, 68% {{ opacity: 1; }}
            72% {{ opacity: 0; top: 100%; }}
            73%, 100% {{ opacity: 0; top: 100%; }}
        }}
        @keyframes featured-lineage-packet-down-skill-out {{
            0%, 73% {{ opacity: 0; top: 0; }}
            75%, 88% {{ opacity: 1; }}
            92% {{ opacity: 0; top: 100%; }}
            93%, 100% {{ opacity: 0; top: 100%; }}
        }}
        @media (hover: none), (pointer: coarse) {{
            .hero-skill-node:hover {{
                transform: none;
                border-color: rgba(37, 99, 235, .18);
                box-shadow: 0 8px 18px rgba(15, 23, 42, .05);
            }}
            .hero-profile-card,
            .hero-profile-card:hover {{
                transform: none;
                border-color: rgba(37, 99, 235, .28);
                box-shadow: 0 12px 30px rgba(15, 23, 42, .10);
            }}
        }}
        @media (prefers-reduced-motion: reduce) {{
            *, *::before, *::after {{
                transition-duration: 0.01ms !important;
                animation-duration: 0.01ms !important;
                animation-iteration-count: 1 !important;
                scroll-behavior: auto !important;
            }}
            .about-hover-card:hover,
            .about-hover-card:focus-within,
            .experience-hover-card:hover,
            .experience-hover-card:focus-within,
            .sidebar-project-card,
            .sidebar-project-card:hover,
            .sidebar-project-card:focus-within,
            .sidebar-projects-content,
            .sidebar-project-links,
            .sidebar-expander-chevron,
            .sidebar-project-chevron,
            .sidebar-mini-packet,
            .st-key-home_profile_photo_shell,
            .st-key-home_profile_photo_shell img,
            .st-key-home_profile_info_card,
            .home-profile-info-card,
            .home-profile-info-card:hover,
            .home-profile-info-card:focus-within,
            .hero-profile-card,
            .hero-profile-card:hover,
            .hero-skill-node,
            .hero-skill-node:hover,
            .hero-skill-packet-track,
            .hero-skill-packet,
            .data-quality-detail,
            .sidebar-brand:hover,
            .sidebar-brand:focus-within,
            .home-card:hover,
            .home-card:focus-within,
            .skill-card:hover,
            .skill-card:focus-within,
            .pipeline-card:hover,
            .pipeline-card:focus-within,
            .job-intelligence-hover-card:hover,
            .job-intelligence-hover-card:focus-within,
            .contact-hover-card:hover,
            .contact-hover-card:focus-within,
            .data-quality-hover-card:hover,
            .data-quality-hover-card:focus-within,
            .home-about-card:hover,
            .home-about-card:focus-within,
            .home-skill-card:hover,
            .home-skill-card:focus-within,
            .featured-project-card:hover,
            .featured-project-card:focus-within,
            .pipeline-step-card:hover,
            .pipeline-step-card:focus-within,
            .st-key-market_dashboard_chart_job_title_demand,
            .st-key-market_dashboard_chart_company_activity,
            .st-key-market_dashboard_chart_salary_by_job_title,
            .st-key-market_dashboard_chart_salary_by_country,
            .st-key-market_dashboard_chart_remote_salary,
            .st-key-market_dashboard_chart_monthly_posting_trend,
            .st-key-market_dashboard_chart_monthly_growth,
            .st-key-market_dashboard_chart_technical_skill_demand,
            .st-key-market_dashboard_chart_high_salary_skills,
            .st-key-market_dashboard_chart_data_engineer_skill_demand,
            .market-chart-reveal-ready,
            .market-chart-reveal-visible,
            .market-chart-reveal-complete {{
                transform: none;
                animation: none !important;
                transition: none !important;
                opacity: 1 !important;
                translate: 0 0 !important;
                scale: 1 !important;
            }}
            .home-profile-info-card,
            .st-key-home_profile_photo_shell,
            .st-key-home_profile_info_card {{
                opacity: 1 !important;
            }}
            .data-background-particle {{
                display: none;
            }}
            .hero-value-rotator {{
                overflow: visible;
            }}
            .hero-value-line {{
                display: none;
                position: static;
                opacity: 1;
                transform: none;
            }}
            .hero-value-line-1 {{
                display: inline;
            }}
            .hero-profile-card,
            .hero-profile-card:hover,
            .hero-profile-status-dot,
            .hero-skill-node,
            .hero-skill-packet-track,
            .hero-skill-packet,
            .featured-lineage-route,
            .featured-lineage-node-job-source,
            .featured-lineage-node-job-intermediate,
            .featured-lineage-node-job-mart,
            .featured-lineage-node-skill-source,
            .featured-lineage-node-skill-intermediate,
            .featured-lineage-node-skill-mart,
            .featured-lineage-intermediate-card,
            .featured-lineage-mart-group,
            .featured-lineage-single-mart {{
                animation: none !important;
                transition: none !important;
                transform: none !important;
                opacity: 1 !important;
            }}
            .featured-lineage-route {{
                stroke-dashoffset: 0 !important;
                opacity: 0 !important;
            }}
            .featured-lineage-packet {{
                display: none;
            }}
            .sidebar-mini-packet {{
                display: none;
            }}
            .hero-skill-packet-track {{
                display: none;
            }}
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )
