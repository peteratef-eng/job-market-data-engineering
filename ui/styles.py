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
            grid-template-columns: minmax(0, 1.2fr) minmax(260px, .8fr);
            align-items: center;
            gap: clamp(1.4rem, 4vw, 3.6rem);
            padding: clamp(1.4rem, 4vw, 3rem) 0 1.15rem;
            overflow: visible;
        }}
        .data-command-hero {{
            position: relative;
            isolation: isolate;
            padding: clamp(1.25rem, 4vw, 2.4rem);
            margin: .25rem 0 1rem;
            border: 1px solid rgba(37, 99, 235, .14);
            border-radius: 22px;
            background:
                radial-gradient(circle at 74% 34%, rgba(37, 99, 235, .12), transparent 34%),
                radial-gradient(circle at 16% 8%, rgba(6, 182, 212, .08), transparent 30%),
                linear-gradient(145deg, rgba(255, 255, 255, .96), rgba(248, 250, 252, .90));
            box-shadow: 0 22px 52px rgba(15, 23, 42, .08);
            overflow: hidden;
        }}
        .data-blueprint-grid {{
            position: absolute;
            inset: 0;
            z-index: -3;
            opacity: .46;
            background-image:
                linear-gradient(rgba(37, 99, 235, .055) 1px, transparent 1px),
                linear-gradient(90deg, rgba(37, 99, 235, .055) 1px, transparent 1px),
                linear-gradient(rgba(15, 23, 42, .035) 1px, transparent 1px);
            background-size: 34px 34px;
            mask-image: linear-gradient(135deg, rgba(0, 0, 0, .76), transparent 78%);
        }}
        .data-background-path {{
            display: none;
        }}
        .data-background-particle {{
            position: absolute;
            z-index: -1;
            width: .42rem;
            height: .42rem;
            border-radius: 999px;
            background: var(--data-cyan);
            box-shadow: 0 0 0 3px rgba(6, 182, 212, .10);
            opacity: 0;
            pointer-events: none;
            animation: data-background-particle-flow 9s linear infinite;
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
        }}
        .hero-kicker,
        .hero-copy h1,
        .hero-copy > p,
        .hero-value-rotator,
        .hero-actions,
        .hero-skill-pipeline,
        .hero-profile-card,
        .project-proof-console {{
            animation: home-entrance-rise 520ms ease-out both;
        }}
        .hero-kicker {{ animation-delay: 40ms; }}
        .hero-copy h1 {{ animation-delay: 120ms; }}
        .hero-copy > p {{ animation-delay: 200ms; }}
        .hero-value-rotator {{ animation-delay: 280ms; }}
        .hero-actions {{ animation-delay: 360ms; }}
        .hero-profile-card {{ animation-delay: 440ms; }}
        .hero-skill-pipeline {{ animation-delay: 520ms; }}
        .project-proof-console {{ animation-delay: 660ms; }}
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
            margin-top: 1.25rem;
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
        .hero-skill-pipeline {{
            position: relative;
            isolation: isolate;
            z-index: 5;
            display: grid;
            grid-template-columns: minmax(6.2rem, 1fr) minmax(7.2rem, 1fr) minmax(7.4rem, 1fr) minmax(3.4rem, .62fr) minmax(8rem, 1.15fr);
            align-items: center;
            gap: 1.05rem;
            width: min(100%, 760px);
            margin-top: 1.2rem;
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
            min-height: 2.75rem;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            padding: .44rem .58rem;
            border: 1px solid rgba(37, 99, 235, .18);
            border-radius: 10px;
            background: rgba(255, 255, 255, .90);
            box-shadow: 0 8px 18px rgba(15, 23, 42, .05);
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
            width: min(100%, 360px);
            padding: .85rem;
            border: 1px solid rgba(37, 99, 235, .20);
            border-radius: 24px;
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.98), rgba(239, 246, 255, 0.86));
            box-shadow: 0 12px 30px rgba(15, 23, 42, .10);
            overflow: hidden;
            transform: translateZ(0);
            transform-origin: center center;
            transition:
                transform 240ms ease,
                border-color 240ms ease,
                box-shadow 240ms ease;
        }}
        .hero-profile-card:focus-within {{
            border-color: rgba(37, 99, 235, 0.72);
            box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.12);
        }}
        .hero-profile-image-wrap {{
            position: relative;
            aspect-ratio: 1;
            border-radius: 18px;
            overflow: hidden;
            background: rgba(239, 246, 255, .76);
        }}
        .hero-profile-image {{
            display: block;
            width: 100%;
            height: 100%;
            object-fit: cover;
            object-position: center top;
            border-radius: 18px;
            border: 1px solid rgba(37, 99, 235, .16);
            box-shadow: var(--shadow);
            transform: none;
            animation: none;
        }}
        .hero-profile-content {{
            padding: .9rem .15rem .05rem;
            text-align: center;
        }}
        .hero-profile-name {{
            color: var(--text);
            font-size: 1.12rem;
            font-weight: 850;
            line-height: 1.15;
            transition: color 240ms ease;
        }}
        .hero-profile-role {{
            color: var(--accent);
            font-size: .92rem;
            font-weight: 800;
            margin-top: .16rem;
        }}
        .profile-availability {{
            display: flex;
            align-items: center;
            gap: .42rem;
            color: var(--tag-text);
            font-size: .74rem;
            font-weight: 750;
            margin-top: .55rem;
            line-height: 1.25;
        }}
        .profile-status-dot {{
            width: .5rem;
            height: .5rem;
            flex: 0 0 auto;
            border-radius: 999px;
            background: var(--positive);
            box-shadow: 0 0 0 3px color-mix(in srgb, var(--positive) 20%, transparent);
            animation: profile-status-dot-pulse 2.8s ease-in-out infinite;
        }}
        .hero-profile-location {{
            color: var(--muted);
            font-size: .72rem;
            font-weight: 700;
            margin-top: .35rem;
        }}
        @keyframes profile-status-dot-pulse {{
            0%, 100% {{ box-shadow: 0 0 0 3px color-mix(in srgb, var(--positive) 18%, transparent); }}
            50% {{ box-shadow: 0 0 0 5px color-mix(in srgb, var(--positive) 10%, transparent), 0 0 12px color-mix(in srgb, var(--positive) 32%, transparent); }}
        }}
        .project-proof-console {{
            position: relative;
            border: 1px solid rgba(37, 99, 235, .16);
            border-radius: 16px;
            background:
                linear-gradient(90deg, rgba(239, 246, 255, .85), rgba(255, 255, 255, .92));
            box-shadow: var(--shadow);
            margin: 1rem 0 .9rem;
            overflow: hidden;
        }}
        .project-proof-console::before {{
            content: "";
            display: block;
            height: 3px;
            background: linear-gradient(90deg, rgba(6, 182, 212, .34), rgba(37, 99, 235, .66), rgba(6, 182, 212, .34));
        }}
        .project-proof-console::after {{
            content: "";
            position: absolute;
            inset: 10px 1rem auto auto;
            width: 9rem;
            height: 4.8rem;
            opacity: .055;
            pointer-events: none;
            background:
                linear-gradient(var(--data-navy) 1px, transparent 1px),
                linear-gradient(90deg, var(--data-navy) 1px, transparent 1px);
            background-size: 100% 1.2rem, 3rem 100%;
        }}
        .proof-console-status {{
            color: var(--accent);
            font-size: .72rem;
            font-weight: 850;
            letter-spacing: .11em;
            padding: .72rem 1rem .15rem;
        }}
        .proof-console-grid {{
            display: grid;
            grid-template-columns: repeat(4, minmax(0, 1fr));
            padding: .35rem 1rem .95rem;
        }}
        .proof-console-item {{
            min-width: 0;
            padding: .25rem 1rem;
            border-left: 1px solid rgba(37, 99, 235, .14);
            animation: proof-console-enter 520ms ease-out both;
        }}
        .proof-console-item-1 {{
            border-left: 0;
            padding-left: 0;
        }}
        .proof-console-value {{
            color: var(--text);
            font-size: clamp(1.15rem, 2vw, 1.55rem);
            font-weight: 850;
            line-height: 1.1;
            overflow-wrap: anywhere;
        }}
        .proof-console-label {{
            color: var(--muted);
            font-size: .74rem;
            font-weight: 750;
            text-transform: uppercase;
            letter-spacing: .035em;
            margin-top: .22rem;
        }}
        @keyframes proof-console-enter {{
            from {{ opacity: 0; transform: translateY(.45rem); }}
            to {{ opacity: 1; transform: translateY(0); }}
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
            position: relative;
            display: grid;
            grid-template-columns: minmax(0, 1.05fr) minmax(280px, .95fr);
            gap: 1.25rem;
            align-items: center;
            padding: 1.25rem;
            margin: 1.4rem 0 2rem;
            overflow: visible;
        }}
        .featured-project-card::before {{
            content: "";
            position: absolute;
            inset: 1rem auto auto 1rem;
            width: 8.5rem;
            height: 4.5rem;
            opacity: .045;
            pointer-events: none;
            background:
                linear-gradient(var(--data-navy) 1px, transparent 1px),
                linear-gradient(90deg, var(--data-navy) 1px, transparent 1px);
            background-size: 100% 1.1rem, 2.7rem 100%;
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
            margin: 1.55rem 0;
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
                transform: translateY(-2px) scale(1.035);
                border-color: rgba(37, 99, 235, 0.50);
                box-shadow: 0 10px 22px rgba(37, 99, 235, 0.12);
            }}
            .hero-profile-card:hover {{
                transform: translateY(-6px) scale(1.025);
                border-color: rgba(37, 99, 235, 0.70);
                box-shadow:
                    0 20px 44px rgba(37, 99, 235, 0.18),
                    0 0 0 3px rgba(6, 182, 212, 0.06);
            }}
            .hero-profile-card:hover .hero-profile-name {{
                color: var(--accent);
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
            padding: .78rem 1rem;
            margin-top: 1rem;
            min-height: 0;
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
            padding: 1rem;
            margin: .7rem 0 1rem;
            min-height: 210px;
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
        .contact-hover-card .section-title,
        .data-quality-hover-card .section-title,
        .home-about-card .section-title,
        .home-skill-card .section-title,
        .project-evidence-card .evidence-label,
        .featured-project-card h2,
        .pipeline-step-card .pipeline-step-name {{
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
            .pipeline-step-card:focus-within {{
                transform: translateY(-4px) scale(1.012);
                border-color: rgba(37, 99, 235, 0.30);
                background-color: rgba(239, 246, 255, 0.58);
                box-shadow: 0 14px 28px rgba(15, 23, 42, 0.09);
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
            .pipeline-step-card:focus-within .pipeline-step-name {{
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
            padding: .95rem 1rem .45rem;
            margin: .85rem 0 .7rem;
            border: 1px solid var(--border);
            border-radius: 12px;
            background: var(--surface);
            box-shadow: var(--shadow);
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
            line-height: 2.4rem;
        }}
        @media (max-width: 1024px) {{
            .pipeline {{ grid-template-columns: repeat(3, minmax(0, 1fr)); }}
            .project-evidence-strip {{ grid-template-columns: repeat(3, minmax(0, 1fr)); }}
            .featured-project-card {{ grid-template-columns: 1fr; }}
            .featured-preview img {{ max-height: 320px; }}
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
            .hero-profile-card {{
                width: min(100%, 310px);
                margin: .35rem auto 0;
                padding: .75rem;
                transform: none;
            }}
            .project-proof-console {{
                margin-top: .85rem;
            }}
            .proof-console-grid {{
                grid-template-columns: repeat(2, minmax(0, 1fr));
                row-gap: .65rem;
            }}
            .proof-console-item-1,
            .proof-console-item-3 {{
                border-left: 0;
                padding-left: 0;
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
            .project-evidence-strip,
            .home-about-grid,
            .home-skills-grid,
            .pipeline-step-grid,
            .pipeline-info-grid {{
                grid-template-columns: 1fr;
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
                padding: .8rem .85rem .35rem;
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
            .project-evidence-card:hover,
            .project-evidence-card:focus-within,
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
            .profile-status-dot,
            .project-proof-console,
            .proof-console-item,
            .hero-skill-node,
            .hero-skill-packet-track,
            .hero-skill-packet {{
                animation: none !important;
                transition: none !important;
                transform: none !important;
                opacity: 1 !important;
            }}
            .hero-skill-packet-track {{
                display: none;
            }}
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )
