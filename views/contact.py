from __future__ import annotations

import base64
import html
from pathlib import Path

import streamlit as st

from portfolio.content.profile import PROFILE
from ui.styles import inject_global_styles
from ui.theme import current_theme


inject_global_styles(current_theme())

st.title("Let's Build Something Reliable")
st.markdown("I'm open to Junior Data Engineer opportunities where I can build dependable pipelines, improve data quality, and make analytics easier for teams.")

badge_cols = st.columns([0.28, 0.22, 0.5])
with badge_cols[0]:
    st.caption("Available for opportunities")
with badge_cols[1]:
    st.caption(f"Based in {PROFILE['location']}")

footer_email_url = PROFILE["mailto_url"]
send_email_url = PROFILE["mailto_url"]
linkedin_url = PROFILE.get("linkedin_url", "")
github_url = PROFILE.get("github_url", "")

cards = st.columns(3)
with cards[0]:
    st.markdown(
        f"""
        <div class="contact-hover-card" tabindex="0">
            <div class="section-title">Email</div>
            <div class="section-copy">Send me a message</div>
            <p>{html.escape(PROFILE["email"])}</p>
            <a class="contact-card-action" href="{html.escape(send_email_url)}">Send Email</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

with cards[1]:
    linkedin_action = (
        f'<a class="contact-card-action" href="{html.escape(linkedin_url)}" rel="noreferrer">View LinkedIn</a>'
        if linkedin_url.startswith("https://")
        else ""
    )
    st.markdown(
        f"""
        <div class="contact-hover-card" tabindex="0">
            <div class="section-title">LinkedIn</div>
            <div class="section-copy">Connect professionally</div>
            <p>peter-atef-eng</p>
            {linkedin_action}
        </div>
        """,
        unsafe_allow_html=True,
    )

with cards[2]:
    github_action = (
        f'<a class="contact-card-action" href="{html.escape(github_url)}" rel="noreferrer">View GitHub</a>'
        if github_url.startswith("https://")
        else ""
    )
    st.markdown(
        f"""
        <div class="contact-hover-card" tabindex="0">
            <div class="section-title">GitHub</div>
            <div class="section-copy">Explore my repositories</div>
            <p>peteratef-eng</p>
            {github_action}
        </div>
        """,
        unsafe_allow_html=True,
    )

resume_path = Path(PROFILE["resume_path"])
if resume_path.exists():
    encoded_resume = base64.b64encode(resume_path.read_bytes()).decode("ascii")
    st.markdown(
        f"""
        <div class="contact-hover-card" tabindex="0">
            <div class="section-title">Want the full overview?</div>
            <div class="section-copy">Download my resume for experience, skills, and project details.</div>
            <a class="contact-card-action" href="data:application/pdf;base64,{encoded_resume}" download="Peter_Atef_Resume_2026.pdf">Download Resume</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.divider()
st.markdown("Peter - Junior Data Engineer")
st.caption(PROFILE["availability"])

footer_links = st.columns([0.12, 0.16, 0.14, 0.58])
with footer_links[0]:
    if footer_email_url:
        st.markdown(f'<a class="portfolio-button" href="{html.escape(footer_email_url)}">Email</a>', unsafe_allow_html=True)
with footer_links[1]:
    if linkedin_url.startswith("https://"):
        st.markdown(f'<a class="portfolio-button" href="{html.escape(linkedin_url)}">LinkedIn</a>', unsafe_allow_html=True)
with footer_links[2]:
    if github_url.startswith("https://"):
        st.markdown(f'<a class="portfolio-button" href="{html.escape(github_url)}">GitHub</a>', unsafe_allow_html=True)
