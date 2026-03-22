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
                radial-gradient(circle at top left, rgba(197, 225, 255, 0.88), transparent 30%),
                radial-gradient(circle at top right, rgba(255, 224, 183, 0.76), transparent 28%),
                linear-gradient(180deg, #f7f4ee 0%, #efebe4 100%);
            color: #18212b;
        }

        .block-container {
            padding-top: 2rem;
            padding-bottom: 2.25rem;
            max-width: 1180px;
        }

        .hero-shell {
            background: rgba(255, 255, 255, 0.76);
            border: 1px solid rgba(24, 33, 43, 0.08);
            border-radius: 30px;
            padding: 2rem;
            box-shadow: 0 20px 60px rgba(31, 41, 55, 0.08);
            backdrop-filter: blur(10px);
        }

        .eyebrow {
            display: inline-block;
            padding: 0.45rem 0.8rem;
            border-radius: 999px;
            background: #13202c;
            color: #f6efe5;
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
            color: #13202c;
        }

        .hero-copy {
            margin-top: 1rem;
            margin-bottom: 0;
            font-size: 1.05rem;
            line-height: 1.7;
            color: #425163;
            max-width: 780px;
        }

        .section-title {
            margin-top: 1.45rem;
            margin-bottom: 0.4rem;
            font-size: 1.08rem;
            font-weight: 800;
            color: #13202c;
            letter-spacing: -0.02em;
        }

        .section-note {
            color: #5b6877;
            font-size: 0.96rem;
            margin-bottom: 1rem;
        }

        .light-card {
            background: rgba(255, 255, 255, 0.82);
            border: 1px solid rgba(19, 32, 44, 0.08);
            border-radius: 22px;
            padding: 1.15rem 1.2rem;
            box-shadow: 0 14px 30px rgba(19, 32, 44, 0.06);
            min-height: 100%;
        }

        .light-card h3 {
            margin: 0 0 0.7rem 0;
            font-size: 1rem;
            color: #13202c;
        }

        .light-card p {
            margin: 0;
            color: #506072;
            line-height: 1.65;
        }

        .light-card ul {
            margin: 0;
            padding-left: 1rem;
            color: #506072;
            line-height: 1.7;
        }

        .dark-card {
            background: linear-gradient(135deg, #13202c 0%, #203446 100%);
            color: #f7f4ee;
            border-radius: 24px;
            padding: 1.35rem 1.4rem;
            box-shadow: 0 18px 40px rgba(19, 32, 44, 0.16);
        }

        .dark-card h3 {
            margin-top: 0;
            margin-bottom: 0.65rem;
            font-size: 1rem;
        }

        .dark-card p,
        .dark-card li {
            color: rgba(247, 244, 238, 0.92);
            line-height: 1.65;
        }

        .dark-card ul {
            padding-left: 1rem;
            margin-bottom: 0;
        }

        .glass-panel {
            background: rgba(255, 255, 255, 0.78);
            border: 1px solid rgba(19, 32, 44, 0.08);
            border-radius: 24px;
            padding: 1.2rem 1.25rem;
            box-shadow: 0 14px 30px rgba(19, 32, 44, 0.06);
        }

        .result-shell {
            background: rgba(255, 255, 255, 0.84);
            border: 1px solid rgba(19, 32, 44, 0.08);
            border-radius: 26px;
            padding: 1.3rem 1.35rem;
            box-shadow: 0 18px 34px rgba(19, 32, 44, 0.08);
        }

        .result-label {
            color: #697889;
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
            color: #13202c;
            margin-top: 0.45rem;
            margin-bottom: 0.6rem;
            word-break: break-word;
        }

        .placeholder-note {
            background: rgba(255, 255, 255, 0.74);
            border: 1px dashed rgba(19, 32, 44, 0.22);
            border-radius: 24px;
            padding: 1.25rem 1.35rem;
            color: #516171;
        }

        .pill {
            display: inline-block;
            padding: 0.35rem 0.65rem;
            border-radius: 999px;
            background: rgba(19, 32, 44, 0.08);
            color: #203446;
            font-size: 0.84rem;
            font-weight: 700;
            margin: 0.15rem 0.35rem 0.15rem 0;
        }

        .step-card {
            background: rgba(255, 255, 255, 0.82);
            border: 1px solid rgba(19, 32, 44, 0.08);
            border-radius: 22px;
            padding: 1.15rem 1.2rem;
            box-shadow: 0 14px 30px rgba(19, 32, 44, 0.06);
        }

        .step-number {
            width: 2rem;
            height: 2rem;
            border-radius: 999px;
            background: #13202c;
            color: #f7f4ee;
            font-weight: 800;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 0.75rem;
        }

        .step-card h3 {
            margin: 0 0 0.55rem 0;
            font-size: 1rem;
            color: #13202c;
        }

        .step-card p {
            margin: 0;
            color: #506072;
            line-height: 1.65;
        }

        div[data-testid="stSelectbox"],
        div[data-testid="stTextArea"],
        div[data-testid="stNumberInput"] {
            background: rgba(255, 255, 255, 0.72);
            border-radius: 18px;
            padding: 0.2rem 0.35rem 0.35rem 0.35rem;
            border: 1px solid rgba(19, 32, 44, 0.08);
            box-shadow: 0 10px 24px rgba(19, 32, 44, 0.04);
        }

        div[data-testid="stButton"] > button,
        div[data-testid="stFormSubmitButton"] > button,
        a[data-testid="stPageLink-NavLink"] {
            border-radius: 16px;
            min-height: 3rem;
            border: 0;
            box-shadow: 0 18px 36px rgba(19, 32, 44, 0.14);
        }

        div[data-testid="metric-container"] {
            background: rgba(255, 255, 255, 0.74);
            border: 1px solid rgba(19, 32, 44, 0.08);
            padding: 0.9rem 1rem;
            border-radius: 18px;
            box-shadow: 0 10px 22px rgba(19, 32, 44, 0.05);
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
        st.markdown(f'<div class="section-note">{html.escape(note)}</div>', unsafe_allow_html=True)


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
