from __future__ import annotations

import streamlit as st

from ui import inject_global_styles, render_hero, render_light_card, render_section_title


st.set_page_config(page_title="Exemples utiles", page_icon="💡", layout="wide")
inject_global_styles()

render_hero(
    "Exemples",
    "Des cas d'usage qui parlent tout de suite.",
    (
        "Cette page montre pourquoi ce convertisseur est utile dans la vraie vie, "
        "avec des scénarios concrets qui ne sont pas juste des conversions génériques."
    ),
)

examples = [
    (
        "Chauffage d'appoint",
        "Convertir des watts en coût mensuel estimé pour savoir si l'appareil vaut vraiment son confort.",
    ),
    (
        "Réunion d'équipe",
        "Transformer une durée de réunion en coût total de temps pour objectiver l'impact sur l'équipe.",
    ),
    (
        "Téléchargement d'un gros fichier",
        "Estimer si le transfert prendra quelques secondes, plusieurs minutes ou une vraie plage de travail.",
    ),
    (
        "Abonnement annuel",
        "Ramener un paiement annuel à son vrai équivalent mensuel pour mieux comparer plusieurs offres.",
    ),
    (
        "Flux d'e-mails",
        "Mesurer le temps hebdomadaire absorbé par les messages et visualiser la charge invisible.",
    ),
    (
        "Brief ou article",
        "Savoir si un texte est trop long, combien il prendra à lire, ou le condenser rapidement.",
    ),
]

render_section_title(
    "Pourquoi ces cas sont intéressants",
    "Ils produisent des réponses utiles pour décider, arbitrer, expliquer ou simplifier.",
)

top_row = st.columns(3)
bottom_row = st.columns(3)
for column, (title, text) in zip(top_row + bottom_row, examples):
    with column:
        render_light_card(title, text)

render_section_title("Suite logique", "Passez ensuite dans la page convertisseur pour tester ces cas avec vos propres données.")
if hasattr(st, "page_link"):
    st.page_link("pages/01_Convertisseur.py", label="Tester ces exemples dans le convertisseur", icon="🧮")
else:
    st.info("Utilisez le menu latéral pour ouvrir la page Convertisseur.")
