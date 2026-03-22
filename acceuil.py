from __future__ import annotations

import streamlit as st

from converters import CONVERSION_SPECS, get_family_map, get_recommended_specs
from ui import (
    inject_global_styles,
    render_dark_card,
    render_hero,
    render_light_card,
    render_pills,
    render_section_title,
    render_step,
)


st.set_page_config(page_title="Convertisseur_Alpha1.0", page_icon="🧮", layout="wide")
inject_global_styles()

family_map = get_family_map()
recommended_specs = get_recommended_specs()

render_hero(
    "Accueil",
    "Un convertisseur utile au quotidien pour Kiara.",
    (
        "Cette application transforme des données concrètes en décisions plus simples : "
        "coût réel, temps mobilisé, impact d'un abonnement, charge de travail ou lecture d'un texte."
    ),
)

render_section_title(
    "Ce que l'app apporte",
    "Le but n'est pas de refaire des convertisseurs banals déjà partout, mais d'aider à prendre une décision rapide.",
)

value_cols = st.columns(3)
with value_cols[0]:
    render_light_card(
        "Utile tout de suite",
        "Chaque conversion est pensée pour répondre à une vraie question du quotidien ou du travail.",
    )
with value_cols[1]:
    render_light_card(
        "Facile à comprendre",
        "Le résultat principal est toujours accompagné d'indicateurs secondaires et d'une explication simple.",
    )
with value_cols[2]:
    render_light_card(
        "Structure proprement",
        "L'app est déjà organisée pour évoluer vers plus de conversions et des règles métier plus fines.",
    )

render_section_title("Vue d'ensemble", "Quelques repères rapides pour comprendre le périmètre actuel (version Alpha1.0).")
metric_cols = st.columns(4)
with metric_cols[0]:
    st.metric("Conversions", str(len(CONVERSION_SPECS)))
with metric_cols[1]:
    st.metric("Familles", str(len(family_map)))
with metric_cols[2]:
    st.metric("Pages", "4")
with metric_cols[3]:
    st.metric("Niveau", "Alpha 1.0T")

left_col, right_col = st.columns([1.15, 0.85], gap="large")

with left_col:
    render_section_title(
        "Démarrer en 3 étapes",
        "Le parcours a été pensé pour être évident, même si on découvre l'app.",
    )
    step_cols = st.columns(3)
    with step_cols[0]:
        render_step(1, "Choisir un besoin", "Partez d'une question concrète : coût, temps, énergie, productivité ou texte.")
    with step_cols[1]:
        render_step(2, "Entrer les données", "La page convertisseur affiche uniquement les champs utiles pour le calcul choisi.")
    with step_cols[2]:
        render_step(3, "Lire le résultat", "Vous obtenez une réponse claire, des vérifications et une interprétation rapide.")

    render_section_title("Catégories disponibles")
    family_items = list(family_map.items())
    for row_start in range(0, len(family_items), 3):
        row_columns = st.columns(3)
        for column, (family, specs) in zip(row_columns, family_items[row_start : row_start + 3]):
            with column:
                render_light_card(family, items=[spec.title for spec in specs])

with right_col:
    render_dark_card(
        "Par quoi commencer",
        "Ces conversions sont les plus parlantes pour montrer la valeur de l'app dès les premières minutes.",
        items=[spec.title for spec in recommended_specs],
    )

    render_section_title("Navigation")
    if hasattr(st, "page_link"):
        st.page_link("pages/01_Convertisseur.py", label="Ouvrir le convertisseur", icon="🧮")
        st.page_link("pages/02_Guide_des_conversions.py", label="Voir le guide des conversions", icon="📘")
        st.page_link("pages/03_Exemples_utiles.py", label="Explorer des cas d'usage", icon="💡")
    else:
        st.info("Utilisez le menu latéral Streamlit pour naviguer entre les pages.")

    render_section_title("Questions que l'app sait déjà clarifier")
    render_pills(
        [
            "Combien me coûte cet appareil par mois ?",
            "Quel est le vrai coût d'une réunion ?",
            "Combien d'heures je perds en e-mails ?",
            "Combien de temps prendra ce téléchargement ?",
            "Combien de temps faut-il pour lire ce texte ?",
        ]
    )
