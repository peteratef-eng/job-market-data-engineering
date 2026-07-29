from __future__ import annotations

from pathlib import Path

import streamlit as st

from portfolio.content.profile import PROFILE
from ui.components import mailto_url
from ui.styles import inject_global_styles
from ui.theme import current_theme


inject_global_styles(current_theme())

st.title("Let's Connect")
st.markdown("I'm open to Junior Data Engineer opportunities and conversations about data projects.")

badge_cols = st.columns([0.28, 0.22, 0.5])
with badge_cols[0]:
    st.caption("Available for opportunities")
with badge_cols[1]:
    st.caption(f"Based in {PROFILE['location']}")

footer_email_url = mailto_url()
send_email_url = mailto_url("Junior Data Engineer opportunity")
linkedin_url = PROFILE.get("linkedin_url", "")
github_url = PROFILE.get("github_url", "")

cards = st.columns(3)
with cards[0]:
    with st.container(border=True):
        st.subheader("Email")
        st.caption("Send me a message")
        st.markdown(f"[{PROFILE['email']}]({footer_email_url})")
        st.link_button("Send Email", send_email_url, type="primary")

with cards[1]:
    with st.container(border=True):
        st.subheader("LinkedIn")
        st.caption("Connect professionally")
        st.markdown("peter-atef-eng")
        if linkedin_url.startswith("https://"):
            st.link_button("View LinkedIn", linkedin_url, type="primary")

with cards[2]:
    with st.container(border=True):
        st.subheader("GitHub")
        st.caption("Explore my repositories")
        st.markdown("peteratef-eng")
        if github_url.startswith("https://"):
            st.link_button("View GitHub", github_url, type="primary")

resume_path = Path(PROFILE["resume_path"])
if resume_path.exists():
    with st.container(border=True):
        st.subheader("Want the full overview?")
        st.markdown("Download my resume for experience, skills, and project details.")
        with resume_path.open("rb") as resume_file:
            st.download_button(
                "Download Resume",
                resume_file,
                file_name="Peter_Atef_Resume_2026.pdf",
                mime="application/pdf",
                type="primary",
            )

st.divider()
st.markdown("Peter - Junior Data Engineer")
st.caption(PROFILE["availability"])

footer_links = st.columns([0.12, 0.16, 0.14, 0.58])
with footer_links[0]:
    if footer_email_url:
        st.link_button("Email", footer_email_url)
with footer_links[1]:
    if linkedin_url.startswith("https://"):
        st.link_button("LinkedIn", linkedin_url)
with footer_links[2]:
    if github_url.startswith("https://"):
        st.link_button("GitHub", github_url)
