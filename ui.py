from __future__ import annotations

import html

import streamlit as st


def inject_global_styles() -> None:
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap');

        html, body, [class*="css"] {
            font-family: 'Manrope', sans-serif;
        }

        .stApp {
            background:
                radial-gradient(circle at top left, rgba(112, 96, 79, 0.18), transparent 30%),
                radial-gradient(circle at top right, rgba(88, 96, 110, 0.12), transparent 26%),
                linear-gradient(180deg, #0d0f12 0%, #121418 48%, #181a1e 100%);
            color: #f3eee7;
        }

        .block-container {
            padding-top: 2rem;
            padding-bottom: 2.25rem;
            max-width: 1180px;
        }

        .hero-shell {
            background: linear-gradient(180deg, rgba(24, 26, 30, 0.92) 0%, rgba(17, 19, 23, 0.94) 100%);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 30px;
            padding: 2rem;
            box-shadow: 0 24px 60px rgba(0, 0, 0, 0.28);
            backdrop-filter: blur(10px);
        }

        .eyebrow {
            display: inline-block;
            padding: 0.45rem 0.8rem;
            border-radius: 999px;
            background: rgba(243, 238, 231, 0.08);
            border: 1px solid rgba(243, 238, 231, 0.12);
            color: #f3eee7;
            font-size: 0.78rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            margin-bottom: 1rem;
        }

        .hero-title {
            margin: 0;
            font-size: 3.25rem;
            line-height: 0.96;
            letter-spacing: -0.06em;
            color: #f7f3ed;
        }

        .hero-copy {
            margin-top: 1rem;
            margin-bottom: 0;
            font-size: 1.05rem;
            line-height: 1.7;
            color: #b5babf;
            max-width: 780px;
        }

        .section-title {
            margin-top: 1.45rem;
            margin-bottom: 0.4rem;
            font-size: 1.08rem;
            font-weight: 800;
            color: #f6f1ea !important;
            letter-spacing: -0.02em;
        }

        .section-note {
            color: #9aa1a9 !important;
            font-size: 0.96rem;
            margin-bottom: 1rem;
        }

        .light-card {
            background: linear-gradient(180deg, rgba(31, 33, 38, 0.94) 0%, rgba(22, 24, 28, 0.94) 100%);
            border: 1px solid rgba(255, 255, 255, 0.07);
            border-radius: 22px;
            padding: 1.15rem 1.2rem;
            box-shadow: 0 18px 32px rgba(0, 0, 0, 0.18);
            min-height: 100%;
        }

        .light-card h3 {
            margin: 0 0 0.7rem 0;
            font-size: 1rem;
            color: #f4efe8;
        }

        .light-card p {
            margin: 0;
            color: #a8afb7;
            line-height: 1.65;
        }

        .light-card ul {
            margin: 0;
            padding-left: 1rem;
            color: #a8afb7;
            line-height: 1.7;
        }

        .dark-card {
            background: linear-gradient(145deg, #0a0b0d 0%, #13151a 100%);
            border: 1px solid rgba(255, 255, 255, 0.08);
            color: #f7f4ee;
            border-radius: 24px;
            padding: 1.35rem 1.4rem;
            box-shadow: 0 22px 40px rgba(0, 0, 0, 0.28);
        }

        .dark-card h3 {
            margin-top: 0;
            margin-bottom: 0.65rem;
            font-size: 1rem;
        }

        .dark-card p,
        .dark-card li {
            color: rgba(247, 244, 238, 0.88);
            line-height: 1.65;
        }

        .dark-card ul {
            padding-left: 1rem;
            margin-bottom: 0;
        }

        .glass-panel {
            background: linear-gradient(180deg, rgba(29, 32, 36, 0.92) 0%, rgba(22, 24, 28, 0.92) 100%);
            border: 1px solid rgba(255, 255, 255, 0.07);
            border-radius: 24px;
            padding: 1.2rem 1.25rem;
            box-shadow: 0 18px 32px rgba(0, 0, 0, 0.18);
        }

        .result-shell {
            background: linear-gradient(180deg, rgba(29, 32, 36, 0.94) 0%, rgba(17, 19, 23, 0.94) 100%);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 26px;
            padding: 1.3rem 1.35rem;
            box-shadow: 0 20px 36px rgba(0, 0, 0, 0.22);
        }

        .result-label {
            color: #9ea5ae;
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            font-weight: 800;
        }

        .result-value {
            font-size: 2rem;
            line-height: 1.15;
            letter-spacing: -0.04em;
            font-weight: 800;
            color: #f6f1ea;
            margin-top: 0.45rem;
            margin-bottom: 0.6rem;
            word-break: break-word;
        }

        .placeholder-note {
            background: rgba(24, 27, 31, 0.9);
            border: 1px dashed rgba(255, 255, 255, 0.18);
            border-radius: 24px;
            padding: 1.25rem 1.35rem;
            color: #a7afb7;
        }

        .pill {
            display: inline-block;
            padding: 0.35rem 0.65rem;
            border-radius: 999px;
            background: rgba(255, 255, 255, 0.08);
            color: #ece6de;
            font-size: 0.84rem;
            font-weight: 700;
            margin: 0.15rem 0.35rem 0.15rem 0;
        }

        .step-card {
            background: linear-gradient(180deg, rgba(30, 32, 37, 0.94) 0%, rgba(21, 23, 27, 0.94) 100%);
            border: 1px solid rgba(255, 255, 255, 0.07);
            border-radius: 22px;
            padding: 1.15rem 1.2rem;
            box-shadow: 0 18px 32px rgba(0, 0, 0, 0.18);
        }

        .step-number {
            width: 2rem;
            height: 2rem;
            border-radius: 999px;
            background: #f0e7dc;
            color: #101215;
            font-weight: 800;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 0.75rem;
        }

        .step-card h3 {
            margin: 0 0 0.55rem 0;
            font-size: 1rem;
            color: #f4efe8;
        }

        .step-card p {
            margin: 0;
            color: #a8afb7;
            line-height: 1.65;
        }

        div[data-testid="stSelectbox"],
        div[data-testid="stTextArea"],
        div[data-testid="stNumberInput"] {
            background: rgba(25, 27, 31, 0.92);
            border-radius: 18px;
            padding: 0.2rem 0.35rem 0.35rem 0.35rem;
            border: 1px solid rgba(255, 255, 255, 0.08);
            box-shadow: 0 12px 24px rgba(0, 0, 0, 0.16);
        }

        div[data-testid="stButton"] > button,
        div[data-testid="stFormSubmitButton"] > button,
        a[data-testid="stPageLink-NavLink"] {
            border-radius: 16px;
            min-height: 3rem;
            border: 1px solid rgba(255, 255, 255, 0.08);
            background: linear-gradient(180deg, #efe5d8 0%, #d7cbbb 100%);
            color: #101215 !important;
            box-shadow: 0 18px 36px rgba(0, 0, 0, 0.22);
        }

        div[data-testid="stButton"] > button *,
        div[data-testid="stFormSubmitButton"] > button *,
        div[data-testid="stButton"] > button p,
        div[data-testid="stFormSubmitButton"] > button p,
        div[data-testid="stButton"] > button span,
        div[data-testid="stFormSubmitButton"] > button span {
            color: #101215 !important;
        }

        a[data-testid="stPageLink-NavLink"] *,
        a[data-testid="stPageLink-NavLink"] p,
        a[data-testid="stPageLink-NavLink"] span {
            color: #101215 !important;
        }

        div[data-testid="metric-container"] {
            background: rgba(24, 27, 31, 0.92);
            border: 1px solid rgba(255, 255, 255, 0.08);
            padding: 0.9rem 1rem;
            border-radius: 18px;
            box-shadow: 0 12px 22px rgba(0, 0, 0, 0.18);
        }

        label, .stMarkdown, .stText, p, li, div[data-testid="stMetricLabel"] {
            color: #ece7df !important;
        }

        div[data-baseweb="select"] > div,
        input,
        textarea {
            color: #f5efe8 !important;
        }

        div[data-baseweb="select"] svg {
            fill: #f5efe8;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_hero(eyebrow: str, title: str, body: str) -> None:
    st.markdown(
        f"""
        <div class="hero-shell">
            <div class="eyebrow">{html.escape(eyebrow)}</div>
            <h1 class="hero-title">{html.escape(title)}</h1>
            <p class="hero-copy">{html.escape(body)}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_section_title(title: str, note: str | None = None) -> None:
    st.markdown(f'<div class="section-title">{html.escape(title)}</div>', unsafe_allow_html=True)
    if note:
        note_html = html.escape(note).replace("\n", "<br>")
        st.markdown(f'<div class="section-note">{note_html}</div>', unsafe_allow_html=True)


def render_light_card(title: str, text: str | None = None, items: list[str] | None = None) -> None:
    if items:
        items_html = "".join(f"<li>{html.escape(item)}</li>" for item in items)
        body = f"<ul>{items_html}</ul>"
    else:
        body = f"<p>{html.escape(text or '')}</p>"
    st.markdown(
        f"""
        <div class="light-card">
            <h3>{html.escape(title)}</h3>
            {body}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_dark_card(title: str, text: str, items: list[str] | None = None) -> None:
    items_html = ""
    if items:
        items_html = "<ul>" + "".join(f"<li>{html.escape(item)}</li>" for item in items) + "</ul>"
    st.markdown(
        f"""
        <div class="dark-card">
            <h3>{html.escape(title)}</h3>
            <p>{html.escape(text)}</p>
            {items_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_glass_panel(title: str, paragraphs: list[str]) -> None:
    body = "".join(f"<p>{html.escape(paragraph)}</p>" for paragraph in paragraphs)
    st.markdown(
        f"""
        <div class="glass-panel">
            <strong>{html.escape(title)}</strong>
            <div style="height: 0.65rem;"></div>
            {body}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_result_shell(headline: str, value: str) -> None:
    st.markdown(
        f"""
        <div class="result-shell">
            <div class="result-label">{html.escape(headline)}</div>
            <div class="result-value">{html.escape(value)}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_placeholder(title: str, text: str) -> None:
    st.markdown(
        f"""
        <div class="placeholder-note">
            <strong>{html.escape(title)}</strong><br><br>
            {html.escape(text)}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_pills(items: list[str]) -> None:
    pills = "".join(f'<span class="pill">{html.escape(item)}</span>' for item in items)
    st.markdown(pills, unsafe_allow_html=True)


def render_step(step_number: int, title: str, text: str) -> None:
    st.markdown(
        f"""
        <div class="step-card">
            <div class="step-number">{step_number}</div>
            <h3>{html.escape(title)}</h3>
            <p>{html.escape(text)}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
