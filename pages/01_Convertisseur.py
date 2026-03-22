from __future__ import annotations

import streamlit as st

from converters import convert, get_family_map, get_recommended_specs, get_spec_by_title
from ui import (
    inject_global_styles,
    render_dark_card,
    render_glass_panel,
    render_hero,
    render_light_card,
    render_placeholder,
    render_result_shell,
    render_section_title,
)


def render_field(field, conversion_key: str):
    widget_key = f"{conversion_key}_{field.key}"
    if field.kind == "number":
        return st.number_input(
            field.label,
            min_value=field.min_value,
            max_value=field.max_value,
            step=field.step or 1.0,
            value=float(field.value) if field.value is not None else 0.0,
            help=field.help_text or None,
            key=widget_key,
        )
    if field.kind == "select":
        return st.selectbox(
            field.label,
            field.options,
            index=field.options.index(field.value) if field.value in field.options else 0,
            help=field.help_text or None,
            key=widget_key,
        )
    if field.kind == "text":
        return st.text_area(
            field.label,
            placeholder=field.placeholder,
            help=field.help_text or None,
            key=widget_key,
            height=180,
        )
    raise ValueError(f"Unsupported field kind: {field.kind}")


st.set_page_config(page_title="Convertisseur", page_icon="🧮", layout="wide")
inject_global_styles()

family_map = get_family_map()
recommended_specs = get_recommended_specs()

render_hero(
    "Convertisseur",
    "Choisir, saisir, comprendre.",
    (
        "Cette page vous guide vers une conversion utile, affiche seulement les champs nécessaires, "
        "puis présente le résultat de façon claire et exploitable."
    ),
)

render_section_title(
    "Comment utiliser cette page",
    "1. Choisissez la famille.\n"
    "2. Sélectionnez la conversion.\n"
    "3. Entrez vos données puis lancez le calcul.",
)

left_col, right_col = st.columns([1.2, 0.8], gap="large")

with left_col:
    family_names = list(family_map.keys())
    selected_family = st.selectbox("Famille de conversion", family_names)
    selected_title = st.selectbox(
        "Type de conversion",
        [spec.title for spec in family_map[selected_family]],
    )
    selected_spec = get_spec_by_title(selected_family, selected_title)

    render_glass_panel(
        selected_spec.title,
        [
            selected_spec.summary,
            f"Formule : {selected_spec.formula}",
            f"Exemple : {selected_spec.example}",
        ],
    )

    form_values: dict[str, object] = {}
    with st.form(f"form_{selected_spec.key}", border=False):
        render_section_title("Paramètres à renseigner", "Les champs changent automatiquement selon la conversion choisie.")
        for field in selected_spec.inputs:
            form_values[field.key] = render_field(field, selected_spec.key)
        submitted = st.form_submit_button("Lancer le calcul")

result = None
error_message = None
if "selected_spec" in locals() and submitted:
    try:
        result = convert(selected_spec.key, form_values)
    except ValueError as exc:
        error_message = str(exc)

with right_col:
    render_dark_card(
        "Conversions recommandées",
        "Si vous voulez tester rapidement l'app avec des résultats très parlants, commencez ici.",
        items=[spec.title for spec in recommended_specs],
    )

    st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)

    if error_message:
        st.error(error_message)
    elif result:
        render_result_shell(str(result["headline"]), str(result["value"]))
        metric_cols = st.columns(len(result["metrics"]))
        for column, (label, value) in zip(metric_cols, result["metrics"]):
            with column:
                st.metric(label, value)

        render_section_title("Comment lire ce résultat")
        for insight in result["insights"]:
            st.write(f"- {insight}")
    else:
        render_placeholder(
            "Résultat en attente",
            "Renseignez les champs à gauche puis lancez le calcul pour obtenir un résultat principal, des métriques secondaires et une explication rapide.",
        )

        render_section_title("À quoi vous attendre")
        preview_cols = st.columns(3)
        with preview_cols[0]:
            render_light_card("Résultat principal", "Une réponse courte et immédiatement compréhensible.")
        with preview_cols[1]:
            render_light_card("Indicateurs", "Des chiffres supplémentaires pour vérifier et contextualiser.")
        with preview_cols[2]:
            render_light_card("Interprétation", "Une lecture en langage simple pour comprendre ce que le calcul veut dire.")
