from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class FieldSpec:
    key: str
    label: str
    kind: str
    help_text: str = ""
    min_value: float | int | None = None
    max_value: float | int | None = None
    step: float | int | None = None
    value: float | int | str | None = None
    options: tuple[str, ...] = ()
    placeholder: str = ""


@dataclass(frozen=True)
class ConversionSpec:
    key: str
    family: str
    title: str
    summary: str
    description: str
    formula: str
    example: str
    inputs: tuple[FieldSpec, ...]


CONVERSION_SPECS: tuple[ConversionSpec, ...] = (
    ConversionSpec(
        key="work_hours_to_days_weeks",
        family="Temps utile",
        title="Heures de travail vers jours ou semaines",
        summary="Transforme un volume d'heures en jours et semaines de travail.",
        description="Utile pour estimer rapidement une charge de travail sur un planning réel.",
        formula="Jours = heures / heures par jour. Semaines = jours / jours par semaine.",
        example="Exemple : 42 heures avec 7 heures par jour = 6 jours = 1,2 semaine.",
        inputs=(
            FieldSpec("hours", "Nombre d'heures", "number", min_value=0.0, step=0.5, value=35.0),
            FieldSpec("hours_per_day", "Heures par jour", "number", min_value=1.0, step=0.5, value=7.0),
            FieldSpec("days_per_week", "Jours par semaine", "number", min_value=1.0, step=0.5, value=5.0),
        ),
    ),
    ConversionSpec(
        key="automation_minutes_to_month_hours",
        family="Temps utile",
        title="Minutes gagnées par automatisation vers heures par mois",
        summary="Mesure le temps économisé chaque mois grâce à une automatisation.",
        description="Pratique pour justifier un script, un outil ou une optimisation répétitive.",
        formula="Heures par mois = minutes gagnées par jour x jours de travail par mois / 60.",
        example="Exemple : 12 minutes gagnées par jour sur 22 jours = 4,4 heures par mois.",
        inputs=(
            FieldSpec("minutes_saved_per_day", "Minutes gagnées par jour", "number", min_value=0.0, step=1.0, value=12.0),
            FieldSpec("workdays_per_month", "Jours de travail par mois", "number", min_value=1.0, step=1.0, value=22.0),
        ),
    ),
    ConversionSpec(
        key="business_days_to_calendar_days",
        family="Temps utile",
        title="Jours ouvrables vers jours calendaires",
        summary="Donne une estimation simple d'un délai réel en jours calendaires.",
        description="Utile pour convertir un planning interne en date de livraison plus lisible.",
        formula="Jours calendaires = jours ouvrables x 7 / jours ouvrables par semaine.",
        example="Exemple : 10 jours ouvrables avec une semaine de 5 jours = 14 jours calendaires.",
        inputs=(
            FieldSpec("business_days", "Jours ouvrables", "number", min_value=0.0, step=1.0, value=10.0),
            FieldSpec("business_days_per_week", "Jours ouvrables par semaine", "number", min_value=1.0, max_value=7.0, step=1.0, value=5.0),
        ),
    ),
    ConversionSpec(
        key="gross_to_net_salary",
        family="Budget concret",
        title="Salaire brut vers estimation nette",
        summary="Calcule une estimation nette à partir d'un brut et d'un taux de retenue.",
        description="Pratique pour une estimation rapide, sans prétendre remplacer une fiche de paie.",
        formula="Net estimé = brut x (1 - taux de retenue).",
        example="Exemple : 3 000 brut avec 23 % de retenue = 2 310 net estimé.",
        inputs=(
            FieldSpec("gross_salary", "Salaire brut", "number", min_value=0.0, step=50.0, value=3000.0),
            FieldSpec("salary_period", "Période", "select", options=("Mensuel", "Annuel"), value="Mensuel"),
            FieldSpec("deduction_rate", "Retenue estimée (%)", "number", min_value=0.0, max_value=100.0, step=1.0, value=23.0),
        ),
    ),
    ConversionSpec(
        key="monthly_to_annual_cost",
        family="Budget concret",
        title="Prix mensuel vers coût annuel",
        summary="Convertit une dépense mensuelle en budget annuel total.",
        description="Idéal pour mesurer l'impact réel d'un abonnement ou d'un poste récurrent.",
        formula="Coût annuel = prix mensuel x 12.",
        example="Exemple : 29,90 par mois = 358,80 par an.",
        inputs=(
            FieldSpec("monthly_cost", "Prix mensuel", "number", min_value=0.0, step=1.0, value=29.9),
        ),
    ),
    ConversionSpec(
        key="annual_to_monthly_cost",
        family="Budget concret",
        title="Abonnement annuel vers coût mensuel réel",
        summary="Ramène un paiement annuel à son équivalent mensuel.",
        description="Pratique pour comparer un abonnement annuel avec une offre mensuelle.",
        formula="Coût mensuel = prix annuel / 12.",
        example="Exemple : 240 par an = 20 par mois.",
        inputs=(
            FieldSpec("annual_cost", "Prix annuel", "number", min_value=0.0, step=1.0, value=240.0),
        ),
    ),
    ConversionSpec(
        key="watts_to_monthly_cost",
        family="Maison et énergie",
        title="Watts vers coût mensuel estimé",
        summary="Estime ce que coûte un appareil électrique sur un mois.",
        description="Très utile pour comprendre le coût réel d'un chauffage, PC, serveur ou climatiseur.",
        formula="kWh par mois = watts / 1000 x heures par jour x 30.44. Coût = kWh x prix du kWh.",
        example="Exemple : 1200 watts pendant 3 heures par jour à 0.25 EUR/kWh = environ 27.40 EUR par mois.",
        inputs=(
            FieldSpec("power_watts", "Puissance (watts)", "number", min_value=0.0, step=10.0, value=1200.0),
            FieldSpec("hours_per_day", "Heures d'utilisation par jour", "number", min_value=0.0, max_value=24.0, step=0.5, value=3.0),
            FieldSpec("price_per_kwh", "Prix de l'électricité (par kWh)", "number", min_value=0.0, step=0.01, value=0.25),
        ),
    ),
    ConversionSpec(
        key="fuel_to_trip_cost",
        family="Maison et énergie",
        title="Litres / 100 km vers coût trajet",
        summary="Estime le coût carburant d'un trajet selon la consommation du véhicule.",
        description="Permet d'estimer un déplacement ou de comparer deux véhicules.",
        formula="Litres consommés = distance x litres/100 km / 100. Coût = litres x prix du litre.",
        example="Exemple : 450 km à 6.2 L/100 avec carburant à 1.85 = environ 51.62.",
        inputs=(
            FieldSpec("distance_km", "Distance du trajet (km)", "number", min_value=0.0, step=1.0, value=450.0),
            FieldSpec("liters_per_100km", "Consommation (L / 100 km)", "number", min_value=0.0, step=0.1, value=6.2),
            FieldSpec("fuel_price", "Prix du carburant (par litre)", "number", min_value=0.0, step=0.01, value=1.85),
        ),
    ),
    ConversionSpec(
        key="file_size_to_download_time",
        family="Maison et énergie",
        title="Taille fichier vers temps de téléchargement",
        summary="Traduit une taille de fichier en temps de téléchargement estimé.",
        description="Utile pour un transfert, une sauvegarde cloud ou un partage de fichiers lourds.",
        formula="Temps = taille en bits / débit en bits par seconde.",
        example="Exemple : 2.5 Go sur 100 Mbps = environ 3 min 25 s hors perte réseau.",
        inputs=(
            FieldSpec("file_size", "Taille du fichier", "number", min_value=0.0, step=0.1, value=2.5),
            FieldSpec("file_size_unit", "Unité de taille", "select", options=("MB", "GB", "TB"), value="GB"),
            FieldSpec("speed_value", "Débit", "number", min_value=0.0, step=1.0, value=100.0),
            FieldSpec("speed_unit", "Unité de débit", "select", options=("Mbps", "Gbps", "MB/s"), value="Mbps"),
        ),
    ),
    ConversionSpec(
        key="meeting_to_total_cost",
        family="Productivité",
        title="Réunion vers coût total de temps",
        summary="Calcule le coût cumulé d'une réunion selon sa durée et le nombre de participants.",
        description="Très utile pour objectiver le poids réel des réunions dans une équipe.",
        formula="Heures cumulées = durée x participants. Coût = heures cumulées x coût horaire moyen.",
        example="Exemple : 45 minutes, 8 personnes, 35 EUR/h = 210 EUR de temps mobilisé.",
        inputs=(
            FieldSpec("meeting_minutes", "Durée de la réunion (minutes)", "number", min_value=0.0, step=5.0, value=45.0),
            FieldSpec("participants", "Nombre de participants", "number", min_value=1.0, step=1.0, value=8.0),
            FieldSpec("hourly_cost", "Coût horaire moyen par personne", "number", min_value=0.0, step=1.0, value=35.0),
        ),
    ),
    ConversionSpec(
        key="emails_to_weekly_time_lost",
        family="Productivité",
        title="E-mails par jour vers temps perdu par semaine",
        summary="Estime le temps hebdomadaire consommé par la gestion des e-mails.",
        description="Pratique pour mesurer la charge invisible d'un flux de messages.",
        formula="Temps hebdo = e-mails par jour x minutes par e-mail x jours de travail par semaine.",
        example="Exemple : 35 e-mails par jour, 3 minutes chacun, 5 jours = 8.75 heures par semaine.",
        inputs=(
            FieldSpec("emails_per_day", "E-mails par jour", "number", min_value=0.0, step=1.0, value=35.0),
            FieldSpec("minutes_per_email", "Minutes par e-mail", "number", min_value=0.0, step=0.5, value=3.0),
            FieldSpec("workdays_per_week", "Jours de travail par semaine", "number", min_value=1.0, max_value=7.0, step=1.0, value=5.0),
        ),
    ),
    ConversionSpec(
        key="task_time_to_monthly_workload",
        family="Productivité",
        title="Temps par tâche vers charge mensuelle",
        summary="Convertit une tâche répétitive en charge de travail mensuelle.",
        description="Permet de voir l'impact réel d'une action apparemment courte mais fréquente.",
        formula="Heures mensuelles = temps par tâche x tâches par semaine x 4.33 / 60.",
        example="Exemple : 18 minutes par tâche, 14 tâches par semaine = environ 18.19 heures par mois.",
        inputs=(
            FieldSpec("minutes_per_task", "Minutes par tâche", "number", min_value=0.0, step=1.0, value=18.0),
            FieldSpec("tasks_per_week", "Nombre de tâches par semaine", "number", min_value=0.0, step=1.0, value=14.0),
        ),
    ),
    ConversionSpec(
        key="text_to_word_count",
        family="Texte",
        title="Texte brut vers nombre de mots",
        summary="Compte rapidement les mots, caractères et temps de lecture d'un texte.",
        description="Utile pour du contenu, une page web, une note ou un brief.",
        formula="Comptage simple des mots et estimation du temps de lecture sur base d'une vitesse moyenne.",
        example="Exemple : un texte de 480 mots se lit en environ 2.4 minutes à 200 mots/minute.",
        inputs=(
            FieldSpec("text", "Texte", "text", placeholder="Collez ici votre texte"),
        ),
    ),
    ConversionSpec(
        key="word_count_to_reading_time",
        family="Texte",
        title="Nombre de mots vers temps de lecture",
        summary="Estime un temps de lecture à partir d'un volume de mots.",
        description="Pratique pour calibrer un article, une présentation ou un script.",
        formula="Temps de lecture = nombre de mots / vitesse de lecture.",
        example="Exemple : 1 200 mots à 220 mots/minute = environ 5.45 minutes.",
        inputs=(
            FieldSpec("word_count", "Nombre de mots", "number", min_value=0.0, step=10.0, value=1200.0),
            FieldSpec("reading_speed", "Vitesse de lecture (mots/minute)", "number", min_value=50.0, step=10.0, value=220.0),
        ),
    ),
    ConversionSpec(
        key="text_to_short_summary",
        family="Texte",
        title="Texte long vers résumé court",
        summary="Produit un résumé local et simple à partir des phrases les plus représentatives.",
        description="Version locale et heuristique, utile pour raccourcir un texte sans dépendance externe.",
        formula="Sélection des premières phrases significatives puis compression du texte cible.",
        example="Exemple : résumé en 2 ou 3 phrases d'un texte plus long.",
        inputs=(
            FieldSpec("text", "Texte", "text", placeholder="Collez ici un texte assez long"),
            FieldSpec("summary_sentences", "Nombre de phrases du résumé", "number", min_value=1.0, max_value=5.0, step=1.0, value=3.0),
        ),
    ),
)


def get_conversion_spec(conversion_key: str) -> ConversionSpec:
    for spec in CONVERSION_SPECS:
        if spec.key == conversion_key:
            return spec
    raise KeyError(f"Unknown conversion: {conversion_key}")
