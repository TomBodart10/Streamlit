from __future__ import annotations

import streamlit as st

from converters import get_family_map
from ui import inject_global_styles, render_hero, render_section_title


st.set_page_config(page_title="Guide des conversions", page_icon="C", layout="wide")
inject_global_styles()

family_map = get_family_map()

render_hero(
    "Guide",
    "Comprendre avant meme de calculer.",
    (
        "Cette page explique simplement ce que fait chaque conversion, quand l'utiliser, "
        "ce qu'il faut renseigner et a quoi sert le resultat."
    ),
)

render_section_title(
    "Mode d'emploi",
    "Parcourez les familles ci-dessous. Chaque conversion est decrite en langage simple pour faciliter la prise en main.",
)

for family, specs in family_map.items():
    render_section_title(family, f"{len(specs)} conversion(s) disponibles")
    for spec in specs:
        with st.expander(spec.title, expanded=False):
            st.write(f"**A quoi ca sert :** {spec.summary}")
            st.write(f"**Quand l'utiliser :** {spec.description}")
            st.write(f"**Formule :** {spec.formula}")
            st.write(f"**Exemple :** {spec.example}")
            st.write("**Champs demandes :**")
            for field in spec.inputs:
                st.write(f"- {field.label}")
