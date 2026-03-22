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


st.set_page_config(page_title="Convertisseur utile", page_icon="C", layout="wide")
inject_global_styles()

family_map = get_family_map()
recommended_specs = get_recommended_specs()

render_hero(
    "Accueil",
    "Un convertisseur vraiment utile au quotidien.",
    (
        "Cette application transforme des donnees concretes en decisions plus simples : "
        "cout reel, temps mobilise, impact d'un abonnement, charge de travail ou lecture d'un texte."
    ),
)

render_section_title(
    "Ce que l'app apporte",
    "Le but n'est pas de refaire des convertisseurs banals deja partout, mais d'aider a prendre une decision vite.",
)

value_cols = st.columns(3)
with value_cols[0]:
    render_light_card(
        "Utile tout de suite",
        "Chaque conversion est pensee pour repondre a une vraie question du quotidien ou du travail.",
    )
with value_cols[1]:
    render_light_card(
        "Facile a comprendre",
        "Le resultat principal est toujours accompagne d'indicateurs secondaires et d'une explication simple.",
    )
with value_cols[2]:
    render_light_card(
        "Structure proprement",
        "L'app est deja organisee pour evoluer vers plus de conversions et des regles metier plus fines.",
    )

render_section_title("Vue d'ensemble", "Quelques reperes rapides pour comprendre le perimetre actuel.")
metric_cols = st.columns(4)
with metric_cols[0]:
    st.metric("Conversions", str(len(CONVERSION_SPECS)))
with metric_cols[1]:
    st.metric("Familles", str(len(family_map)))
with metric_cols[2]:
    st.metric("Pages", "4")
with metric_cols[3]:
    st.metric("Niveau", "Prototype premium")

left_col, right_col = st.columns([1.15, 0.85], gap="large")

with left_col:
    render_section_title(
        "Demarrer en 3 etapes",
        "Le parcours a ete pense pour etre evident, meme si on decouvre l'app.",
    )
    step_cols = st.columns(3)
    with step_cols[0]:
        render_step(1, "Choisir un besoin", "Partez d'une question concrete : cout, temps, energie, productivite ou texte.")
    with step_cols[1]:
        render_step(2, "Entrer les donnees", "La page convertisseur affiche uniquement les champs utiles pour le calcul choisi.")
    with step_cols[2]:
        render_step(3, "Lire le resultat", "Vous obtenez une reponse claire, des verifications et une interpretation rapide.")

    render_section_title("Categories disponibles")
    category_cols = st.columns(len(family_map))
    for column, (family, specs) in zip(category_cols, family_map.items()):
        with column:
            render_light_card(family, items=[spec.title for spec in specs])

with right_col:
    render_dark_card(
        "Par quoi commencer",
        "Ces conversions sont les plus parlantes pour montrer la valeur de l'app des les premieres minutes.",
        items=[spec.title for spec in recommended_specs],
    )

    render_section_title("Navigation")
    if hasattr(st, "page_link"):
        st.page_link("pages/01_Convertisseur.py", label="Ouvrir le convertisseur", icon="C")
        st.page_link("pages/02_Guide_des_conversions.py", label="Voir le guide des conversions", icon="C")
        st.page_link("pages/03_Exemples_utiles.py", label="Explorer des cas d'usage", icon="C")
    else:
        st.info("Utilisez le menu lateral Streamlit pour naviguer entre les pages.")

    render_section_title("Questions que l'app sait deja clarifier")
    render_pills(
        [
            "Combien me coute cet appareil par mois ?",
            "Quel est le vrai cout d'une reunion ?",
            "Combien d'heures je perds en emails ?",
            "Combien de temps prendra ce telechargement ?",
            "Combien de temps faut-il pour lire ce texte ?",
        ]
    )
