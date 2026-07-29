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
        .sidebar-links {{
            margin: 0 0 .65rem;
            color: var(--muted);
            font-size: .84rem;
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

        .portfolio-hero {{
            display: grid;
            grid-template-columns: minmax(0, 1.2fr) minmax(260px, .8fr);
            align-items: center;
            gap: clamp(1.4rem, 4vw, 3.6rem);
            padding: clamp(1.4rem, 4vw, 3rem) 0 1.15rem;
            overflow: visible;
        }}
        .hero-copy {{
            min-width: 0;
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
            margin-bottom: .55rem;
        }}
        .portfolio-hero h1 {{
            color: var(--text);
            font-size: clamp(2.45rem, 6vw, 4.85rem);
            line-height: .98;
            font-weight: 750;
            margin: 0;
        }}
        .portfolio-hero p,
        .contact-cta p {{
            color: var(--text-2);
            max-width: 680px;
            font-size: 1.05rem;
            line-height: 1.7;
            margin: 1rem 0 0;
        }}
        .hero-actions,
        .contact-cta-actions {{
            display: flex;
            flex-wrap: wrap;
            gap: .7rem;
            margin-top: 1.25rem;
        }}
        .portfolio-button {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            min-height: 2.65rem;
            padding: .7rem 1rem;
            border-radius: 10px;
            border: 1px solid var(--border);
            background: var(--surface);
            color: var(--text);
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
            background: var(--accent);
            border-color: var(--accent);
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
        .hero-stack {{
            display: flex;
            flex-wrap: wrap;
            gap: .35rem;
            margin-top: 1.15rem;
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
        .st-key-home_profile_card {{
            width: min(100%, 360px);
            margin: 1rem auto 0;
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
                transform 260ms cubic-bezier(0.22, 1, 0.36, 1),
                border-color 260ms ease,
                box-shadow 260ms ease;
        }}
        .st-key-home_profile_card [data-testid="stImage"] {{
            margin: 0 auto;
        }}
        .st-key-home_profile_card img {{
            display: block;
            width: 100%;
            aspect-ratio: 1;
            object-fit: cover;
            object-position: center top;
            border-radius: 14px;
            border: 1px solid rgba(37, 99, 235, .16);
            box-shadow: var(--shadow);
            transition: transform 260ms cubic-bezier(0.22, 1, 0.36, 1);
        }}
        .home-profile-copy {{
            text-align: center;
            padding-top: .85rem;
        }}
        .home-profile-name {{
            color: var(--text);
            font-size: 1.22rem;
            line-height: 1.2;
            font-weight: 800;
            transition: color 260ms ease;
        }}
        .home-profile-role {{
            color: var(--text-2);
            font-size: .94rem;
            line-height: 1.35;
            margin-top: .18rem;
        }}
        .home-profile-status {{
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
        .home-profile-status span {{
            width: .48rem;
            height: .48rem;
            border-radius: 999px;
            background: var(--positive);
            box-shadow: 0 0 0 3px color-mix(in srgb, var(--positive) 20%, transparent);
            transition: box-shadow 260ms ease;
        }}
        .project-evidence-strip {{
            display: grid;
            grid-template-columns: repeat(5, minmax(0, 1fr));
            gap: .8rem;
            margin: 1.35rem 0 2rem;
            overflow: visible;
        }}
        .project-evidence-card,
        .featured-project-card,
        .pipeline-step-card,
        .insight-card,
        .contact-cta {{
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 12px;
            box-shadow: var(--shadow);
        }}
        .project-evidence-card {{
            padding: .95rem;
            min-height: 132px;
        }}
        .evidence-value {{
            color: var(--text);
            font-size: clamp(1.18rem, 2.2vw, 1.55rem);
            font-weight: 800;
            line-height: 1.15;
            overflow-wrap: anywhere;
        }}
        .evidence-label {{
            color: var(--text);
            font-size: .86rem;
            font-weight: 700;
            line-height: 1.25;
            margin-top: .35rem;
        }}
        .evidence-note {{
            color: var(--muted);
            font-size: .78rem;
            line-height: 1.45;
            margin-top: .45rem;
        }}
        .featured-project-card {{
            display: grid;
            grid-template-columns: minmax(0, 1.05fr) minmax(280px, .95fr);
            gap: 1.25rem;
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
            border: 1px solid var(--border);
            border-radius: 10px;
            background: var(--surface-2);
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
        .home-section {{
            margin: 2rem 0;
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
            gap: .85rem;
            margin-top: 1rem;
            overflow: visible;
        }}
        .home-about-card,
        .home-skill-card {{
            min-height: 150px;
        }}
        .home-skill-badge-wrap {{
            display: flex;
            flex-wrap: wrap;
            gap: .5rem;
            margin-top: .7rem;
        }}
        .home-skill-badge {{
            display: inline-flex;
            align-items: center;
            max-width: 100%;
            border: 1px solid var(--border);
            background: var(--tag-bg);
            color: var(--tag-text);
            border-radius: 999px;
            padding: .42rem .68rem;
            font-size: .82rem;
            font-weight: 600;
            line-height: 1.25;
            overflow-wrap: anywhere;
        }}
        .home-pipeline-section {{
            overflow: hidden;
        }}
        .home-pipeline-track {{
            display: grid;
            grid-template-columns:
                minmax(112px, 1fr) 34px minmax(112px, 1fr) 34px minmax(112px, 1fr)
                34px minmax(112px, 1fr) 34px minmax(112px, 1fr) 34px minmax(112px, 1fr);
            align-items: center;
            gap: .45rem;
            margin-top: 1rem;
            overflow: visible;
        }}
        .home-pipeline-stage {{
            min-width: 0;
            opacity: .82;
            border: 1px solid var(--border);
            border-radius: 12px;
            background: var(--surface);
            box-shadow: var(--shadow);
            transform-origin: center center;
            translate: 0 0;
            scale: 1;
            animation: home-pipeline-stage-cycle 10s ease-in-out infinite;
            transition:
                border-color 220ms ease,
                box-shadow 220ms ease;
        }}
        .home-pipeline-stage-inner {{
            min-height: 150px;
            padding: .9rem .75rem;
            transform-origin: center center;
            transition: transform 220ms ease;
        }}
        .home-pipeline-icon {{
            width: 2.15rem;
            height: 2.15rem;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            border-radius: 10px;
            background: var(--tag-bg);
            color: var(--tag-text);
            font-size: .78rem;
            font-weight: 800;
            margin-bottom: .6rem;
        }}
        .home-pipeline-stage-name {{
            color: var(--text);
            font-size: .96rem;
            font-weight: 800;
            line-height: 1.2;
        }}
        .home-pipeline-stage-copy {{
            color: var(--text-2);
            font-size: .82rem;
            line-height: 1.45;
            margin-top: .38rem;
        }}
        .home-pipeline-connector {{
            position: relative;
            height: 3px;
            border-radius: 999px;
            background: linear-gradient(90deg, rgba(148, 163, 184, .35), rgba(37, 99, 235, .42), rgba(148, 163, 184, .35));
            background-size: 220% 100%;
            animation: home-pipeline-flow-line 10s linear infinite;
            overflow: visible;
        }}
        .home-pipeline-particle {{
            position: absolute;
            top: 50%;
            left: 0;
            width: .48rem;
            height: .48rem;
            border-radius: 999px;
            background: var(--accent);
            box-shadow: 0 0 12px rgba(37, 99, 235, .44);
            transform: translate(-50%, -50%);
            animation: home-pipeline-particle-flow 10s linear infinite;
        }}
        .pipeline-stage-1,
        .pipeline-connector-1 .home-pipeline-particle {{ animation-delay: 0s; }}
        .pipeline-stage-2,
        .pipeline-connector-2 .home-pipeline-particle {{ animation-delay: 1.65s; }}
        .pipeline-stage-3,
        .pipeline-connector-3 .home-pipeline-particle {{ animation-delay: 3.3s; }}
        .pipeline-stage-4,
        .pipeline-connector-4 .home-pipeline-particle {{ animation-delay: 4.95s; }}
        .pipeline-stage-5,
        .pipeline-connector-5 .home-pipeline-particle {{ animation-delay: 6.6s; }}
        .pipeline-stage-6 {{ animation-delay: 8.25s; }}
        @keyframes home-pipeline-stage-cycle {{
            0%, 16%, 100% {{
                opacity: .82;
                border-color: var(--border);
                box-shadow: var(--shadow);
                translate: 0 0;
                scale: 1;
            }}
            5%, 11% {{
                opacity: 1;
                border-color: rgba(37, 99, 235, 0.50);
                box-shadow: 0 12px 28px rgba(37, 99, 235, 0.16);
                translate: 0 -3px;
                scale: 1.015;
            }}
        }}
        @keyframes home-pipeline-flow-line {{
            0% {{ background-position: 100% 50%; }}
            100% {{ background-position: -120% 50%; }}
        }}
        @keyframes home-pipeline-particle-flow {{
            0%, 14% {{
                opacity: 0;
                left: 0;
            }}
            18%, 32% {{
                opacity: 1;
            }}
            42%, 100% {{
                opacity: 0;
                left: 100%;
            }}
        }}
        @media (hover: hover) and (pointer: fine) {{
            .st-key-home_profile_card:hover,
            .st-key-home_profile_card:focus-within {{
                transform: translateY(-6px) scale(1.025);
                border-color: rgba(37, 99, 235, 0.50);
                box-shadow: 0 20px 44px rgba(37, 99, 235, 0.18);
            }}
            .st-key-home_profile_card:hover img,
            .st-key-home_profile_card:focus-within img {{
                transform: scale(1.015);
            }}
            .st-key-home_profile_card:hover .home-profile-name,
            .st-key-home_profile_card:focus-within .home-profile-name {{
                color: var(--accent);
            }}
            .st-key-home_profile_card:hover .home-profile-status span,
            .st-key-home_profile_card:focus-within .home-profile-status span {{
                box-shadow: 0 0 0 4px color-mix(in srgb, var(--positive) 24%, transparent), 0 0 14px color-mix(in srgb, var(--positive) 45%, transparent);
            }}
            .home-pipeline-stage:hover,
            .home-pipeline-stage:focus-within {{
                border-color: rgba(37, 99, 235, 0.55);
                box-shadow: 0 14px 30px rgba(37, 99, 235, 0.16);
            }}
            .home-pipeline-stage:hover .home-pipeline-stage-inner,
            .home-pipeline-stage:focus-within .home-pipeline-stage-inner {{
                transform: translateY(-4px) scale(1.02);
            }}
        }}
        .pipeline-step-grid,
        .insight-card-grid {{
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: .85rem;
            margin-top: 1rem;
            overflow: visible;
        }}
        .pipeline-step-card,
        .insight-card {{
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
        .about-hover-card,
        .experience-hover-card {{
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
        .about-hover-card .section-title,
        .experience-hover-card .project-title {{
            transform-origin: left center;
            transition: color 220ms ease, font-size 220ms ease, transform 220ms ease;
        }}
        @media (hover: hover) and (pointer: fine) {{
            .about-hover-card:hover,
            .about-hover-card:focus-within,
            .experience-hover-card:hover,
            .experience-hover-card:focus-within {{
                transform: translateY(-3px) scale(1.018);
                border-color: rgba(37, 99, 235, 0.45);
                background-color: rgba(239, 246, 255, 0.65);
                box-shadow: 0 12px 28px rgba(37, 99, 235, 0.14);
                position: relative;
                z-index: 2;
            }}
            .about-hover-card:hover .section-title,
            .about-hover-card:focus-within .section-title,
            .experience-hover-card:hover .project-title,
            .experience-hover-card:focus-within .project-title {{
                color: var(--accent);
                font-size: 1.12rem;
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
            .experience-hover-card:hover .project-title,
            .experience-hover-card:focus-within .project-title {{
                font-size: 1.12rem;
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
        .contact-hover-card,
        .data-quality-hover-card,
        .home-about-card,
        .home-skill-card,
        .project-evidence-card,
        .featured-project-card,
        .pipeline-step-card,
        .insight-card {{
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
            padding: 1rem;
            margin: .7rem 0 1rem;
            min-height: 210px;
        }}
        .data-quality-hover-card {{
            padding: 1rem;
            margin: .7rem 0 1rem;
        }}
        .job-intelligence-hover-card .section-title,
        .job-intelligence-hover-card strong,
        .contact-hover-card .section-title,
        .data-quality-hover-card .section-title,
        .home-about-card .section-title,
        .home-skill-card .section-title,
        .project-evidence-card .evidence-label,
        .featured-project-card h2,
        .pipeline-step-card .pipeline-step-name,
        .insight-card .section-title {{
            transition: color 250ms ease;
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
                transform: translateY(-5px) scale(1.015);
                border-color: rgba(37, 99, 235, 0.45);
                background-color: rgba(239, 246, 255, 0.75);
                box-shadow: 0 14px 30px rgba(37, 99, 235, 0.14);
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
            .contact-hover-card:hover,
            .contact-hover-card:focus-within,
            .data-quality-hover-card:hover,
            .data-quality-hover-card:focus-within,
            .home-about-card:hover,
            .home-about-card:focus-within,
            .home-skill-card:hover,
            .home-skill-card:focus-within,
            .project-evidence-card:hover,
            .project-evidence-card:focus-within,
            .featured-project-card:hover,
            .featured-project-card:focus-within,
            .pipeline-step-card:hover,
            .pipeline-step-card:focus-within,
            .insight-card:hover,
            .insight-card:focus-within {{
                transform: translateY(-5px) scale(1.015);
                border-color: rgba(37, 99, 235, 0.45);
                background-color: rgba(239, 246, 255, 0.75);
                box-shadow: 0 14px 30px rgba(37, 99, 235, 0.14);
                position: relative;
                z-index: 2;
            }}
            .job-intelligence-hover-card:hover .section-title,
            .job-intelligence-hover-card:focus-within .section-title,
            .job-intelligence-hover-card:hover strong,
            .job-intelligence-hover-card:focus-within strong,
            .contact-hover-card:hover .section-title,
            .contact-hover-card:focus-within .section-title,
            .data-quality-hover-card:hover .section-title,
            .data-quality-hover-card:focus-within .section-title,
            .home-about-card:hover .section-title,
            .home-about-card:focus-within .section-title,
            .home-skill-card:hover .section-title,
            .home-skill-card:focus-within .section-title,
            .project-evidence-card:hover .evidence-label,
            .project-evidence-card:focus-within .evidence-label,
            .featured-project-card:hover h2,
            .featured-project-card:focus-within h2,
            .pipeline-step-card:hover .pipeline-step-name,
            .pipeline-step-card:focus-within .pipeline-step-name,
            .insight-card:hover .section-title,
            .insight-card:focus-within .section-title {{
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
            .project-evidence-card,
            .featured-project-card,
            .pipeline-step-card,
            .insight-card {{
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
            translate: 0 0;
            transform-origin: center center;
            border: 1px solid transparent;
            border-radius: 12px;
            overflow: visible;
            transition:
                transform 220ms ease,
                border-color 220ms ease,
                box-shadow 220ms ease;
        }}
        @supports (animation-timeline: view()) {{
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
                opacity: 0;
                translate: -45px 0;
                animation: chart-scroll-reveal 650ms cubic-bezier(0.22, 1, 0.36, 1) both;
                animation-timeline: view();
                animation-range: entry 12% entry 32%;
                will-change: opacity, translate;
            }}
        }}
        @keyframes chart-scroll-reveal {{
            from {{
                opacity: 0;
                translate: -45px 0;
            }}
            to {{
                opacity: 1;
                translate: 0 0;
            }}
        }}
        @media (hover: hover) and (pointer: fine) {{
            .st-key-market_dashboard_chart_job_title_demand:hover,
            .st-key-market_dashboard_chart_company_activity:hover,
            .st-key-market_dashboard_chart_salary_by_job_title:hover,
            .st-key-market_dashboard_chart_salary_by_country:hover,
            .st-key-market_dashboard_chart_remote_salary:hover,
            .st-key-market_dashboard_chart_monthly_posting_trend:hover,
            .st-key-market_dashboard_chart_monthly_growth:hover,
            .st-key-market_dashboard_chart_technical_skill_demand:hover,
            .st-key-market_dashboard_chart_high_salary_skills:hover,
            .st-key-market_dashboard_chart_data_engineer_skill_demand:hover {{
                transform: translateY(-3px) scale(1.008);
                border-color: rgba(37, 99, 235, 0.40);
                box-shadow: 0 16px 34px rgba(37, 99, 235, 0.14);
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
            .project-evidence-strip {{ grid-template-columns: repeat(3, minmax(0, 1fr)); }}
            .featured-project-card {{ grid-template-columns: 1fr; }}
            .featured-preview img {{ max-height: 320px; }}
        }}
        @media (max-width: 760px) {{
            .project-card-featured {{ max-width: 100%; }}
            .portfolio-hero {{
                grid-template-columns: 1fr;
                padding-top: 1rem;
            }}
            .hero-photo-shell {{
                order: -1;
                width: min(100%, 300px);
            }}
            .st-key-home_profile_card {{
                width: min(100%, 300px);
                transform: none;
            }}
            .home-pipeline-stage {{
                translate: 0 0;
                scale: 1;
            }}
            .project-evidence-strip,
            .home-about-grid,
            .home-skills-grid,
            .pipeline-step-grid,
            .insight-card-grid {{
                grid-template-columns: 1fr;
            }}
            .home-pipeline-track {{
                grid-template-columns: 1fr;
                gap: .45rem;
            }}
            .home-pipeline-stage-inner {{
                min-height: 0;
                padding: .9rem;
            }}
            .home-pipeline-connector {{
                width: 3px;
                height: 30px;
                margin: 0 auto;
                background: linear-gradient(180deg, rgba(148, 163, 184, .35), rgba(37, 99, 235, .42), rgba(148, 163, 184, .35));
                background-size: 100% 220%;
                animation-name: home-pipeline-flow-line-mobile;
            }}
            .home-pipeline-particle {{
                top: 0;
                left: 50%;
                animation-name: home-pipeline-particle-flow-mobile;
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
        @keyframes home-pipeline-flow-line-mobile {{
            0% {{ background-position: 50% 100%; }}
            100% {{ background-position: 50% -120%; }}
        }}
        @keyframes home-pipeline-particle-flow-mobile {{
            0%, 14% {{
                opacity: 0;
                top: 0;
            }}
            18%, 32% {{
                opacity: 1;
            }}
            42%, 100% {{
                opacity: 0;
                top: 100%;
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
            .st-key-home_profile_card,
            .st-key-home_profile_card:hover,
            .st-key-home_profile_card:focus-within,
            .st-key-home_profile_card img,
            .home-pipeline-stage,
            .home-pipeline-stage:hover,
            .home-pipeline-stage:focus-within,
            .home-pipeline-stage-inner,
            .home-pipeline-stage:hover .home-pipeline-stage-inner,
            .home-pipeline-stage:focus-within .home-pipeline-stage-inner,
            .home-pipeline-connector,
            .home-pipeline-particle,
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
            .project-evidence-card:hover,
            .project-evidence-card:focus-within,
            .featured-project-card:hover,
            .featured-project-card:focus-within,
            .pipeline-step-card:hover,
            .pipeline-step-card:focus-within,
            .insight-card:hover,
            .insight-card:focus-within,
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
                transform: none;
                animation: none !important;
                transition: none !important;
                opacity: 1 !important;
                translate: 0 0 !important;
                scale: 1 !important;
            }}
            .home-pipeline-stage,
            .st-key-home_profile_card {{
                opacity: 1 !important;
            }}
            .home-pipeline-particle {{
                display: none;
            }}
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )
