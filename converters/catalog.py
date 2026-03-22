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
        description="Utile pour estimer rapidement une charge de travail sur un planning reel.",
        formula="Jours = heures / heures par jour. Semaines = jours / jours par semaine.",
        example="Exemple : 42 heures avec 7 heures par jour = 6 jours = 1.2 semaine.",
        inputs=(
            FieldSpec("hours", "Nombre d'heures", "number", min_value=0.0, step=0.5, value=35.0),
            FieldSpec("hours_per_day", "Heures par jour", "number", min_value=1.0, step=0.5, value=7.0),
            FieldSpec("days_per_week", "Jours par semaine", "number", min_value=1.0, step=0.5, value=5.0),
        ),
    ),
    ConversionSpec(
        key="automation_minutes_to_month_hours",
        family="Temps utile",
        title="Minutes gagnees par automatisation vers heures par mois",
        summary="Mesure le temps economise chaque mois grace a une automatisation.",
        description="Pratique pour justifier un script, un outil ou une optimisation repetitive.",
        formula="Heures par mois = minutes gagnees par jour x jours de travail par mois / 60.",
        example="Exemple : 12 minutes gagnees par jour sur 22 jours = 4.4 heures par mois.",
        inputs=(
            FieldSpec("minutes_saved_per_day", "Minutes gagnees par jour", "number", min_value=0.0, step=1.0, value=12.0),
            FieldSpec("workdays_per_month", "Jours de travail par mois", "number", min_value=1.0, step=1.0, value=22.0),
        ),
    ),
    ConversionSpec(
        key="business_days_to_calendar_days",
        family="Temps utile",
        title="Jours ouvrables vers jours calendaires",
        summary="Donne une estimation simple d'un delai reel en jours calendaires.",
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
        summary="Calcule une estimation nette a partir d'un brut et d'un taux de retenue.",
        description="Pratique pour une estimation rapide, sans pretendre remplacer une fiche de paie.",
        formula="Net estime = brut x (1 - taux de retenue).",
        example="Exemple : 3 000 brut avec 23 % de retenue = 2 310 net estime.",
        inputs=(
            FieldSpec("gross_salary", "Salaire brut", "number", min_value=0.0, step=50.0, value=3000.0),
            FieldSpec("salary_period", "Periode", "select", options=("Mensuel", "Annuel"), value="Mensuel"),
            FieldSpec("deduction_rate", "Retenue estimee (%)", "number", min_value=0.0, max_value=100.0, step=1.0, value=23.0),
        ),
    ),
    ConversionSpec(
        key="monthly_to_annual_cost",
        family="Budget concret",
        title="Prix mensuel vers cout annuel",
        summary="Convertit une depense mensuelle en budget annuel total.",
        description="Ideal pour mesurer l'impact reel d'un abonnement ou d'un poste recurrrent.",
        formula="Cout annuel = prix mensuel x 12.",
        example="Exemple : 29.90 par mois = 358.80 par an.",
        inputs=(
            FieldSpec("monthly_cost", "Prix mensuel", "number", min_value=0.0, step=1.0, value=29.9),
        ),
    ),
    ConversionSpec(
        key="annual_to_monthly_cost",
        family="Budget concret",
        title="Abonnement annuel vers cout mensuel reel",
        summary="Ramene un paiement annuel a son equivalent mensuel.",
        description="Pratique pour comparer un abonnement annuel avec une offre mensuelle.",
        formula="Cout mensuel = prix annuel / 12.",
        example="Exemple : 240 par an = 20 par mois.",
        inputs=(
            FieldSpec("annual_cost", "Prix annuel", "number", min_value=0.0, step=1.0, value=240.0),
        ),
    ),
    ConversionSpec(
        key="watts_to_monthly_cost",
        family="Maison et energie",
        title="Watts vers cout mensuel estime",
        summary="Estime ce que coute un appareil electrique sur un mois.",
        description="Tres utile pour comprendre le cout reel d'un chauffage, PC, serveur ou climatiseur.",
        formula="kWh par mois = watts / 1000 x heures par jour x 30.44. Cout = kWh x prix du kWh.",
        example="Exemple : 1200 watts pendant 3 heures par jour a 0.25 EUR/kWh = environ 27.40 EUR par mois.",
        inputs=(
            FieldSpec("power_watts", "Puissance (watts)", "number", min_value=0.0, step=10.0, value=1200.0),
            FieldSpec("hours_per_day", "Heures d'utilisation par jour", "number", min_value=0.0, max_value=24.0, step=0.5, value=3.0),
            FieldSpec("price_per_kwh", "Prix de l'electricite (par kWh)", "number", min_value=0.0, step=0.01, value=0.25),
        ),
    ),
    ConversionSpec(
        key="fuel_to_trip_cost",
        family="Maison et energie",
        title="Litres / 100 km vers cout trajet",
        summary="Estime le cout carburant d'un trajet selon la consommation du vehicule.",
        description="Permet d'estimer un deplacement ou de comparer deux vehicules.",
        formula="Litres consommes = distance x litres/100 km / 100. Cout = litres x prix du litre.",
        example="Exemple : 450 km a 6.2 L/100 avec carburant a 1.85 = environ 51.62.",
        inputs=(
            FieldSpec("distance_km", "Distance du trajet (km)", "number", min_value=0.0, step=1.0, value=450.0),
            FieldSpec("liters_per_100km", "Consommation (L / 100 km)", "number", min_value=0.0, step=0.1, value=6.2),
            FieldSpec("fuel_price", "Prix du carburant (par litre)", "number", min_value=0.0, step=0.01, value=1.85),
        ),
    ),
    ConversionSpec(
        key="file_size_to_download_time",
        family="Maison et energie",
        title="Taille fichier vers temps de telechargement",
        summary="Traduit une taille de fichier en temps de telechargement estime.",
        description="Utile pour un transfert, une sauvegarde cloud ou un partage de fichiers lourds.",
        formula="Temps = taille en bits / debit en bits par seconde.",
        example="Exemple : 2.5 Go sur 100 Mbps = environ 3 min 25 s hors perte reseau.",
        inputs=(
            FieldSpec("file_size", "Taille du fichier", "number", min_value=0.0, step=0.1, value=2.5),
            FieldSpec("file_size_unit", "Unite de taille", "select", options=("MB", "GB", "TB"), value="GB"),
            FieldSpec("speed_value", "Debit", "number", min_value=0.0, step=1.0, value=100.0),
            FieldSpec("speed_unit", "Unite de debit", "select", options=("Mbps", "Gbps", "MB/s"), value="Mbps"),
        ),
    ),
    ConversionSpec(
        key="meeting_to_total_cost",
        family="Productivite",
        title="Reunion vers cout total de temps",
        summary="Calcule le cout cumule d'une reunion selon sa duree et le nombre de participants.",
        description="Tres utile pour objectiver le poids reel des reunions dans une equipe.",
        formula="Heures cumulees = duree x participants. Cout = heures cumulees x cout horaire moyen.",
        example="Exemple : 45 minutes, 8 personnes, 35 EUR/h = 210 EUR de temps mobilise.",
        inputs=(
            FieldSpec("meeting_minutes", "Duree de la reunion (minutes)", "number", min_value=0.0, step=5.0, value=45.0),
            FieldSpec("participants", "Nombre de participants", "number", min_value=1.0, step=1.0, value=8.0),
            FieldSpec("hourly_cost", "Cout horaire moyen par personne", "number", min_value=0.0, step=1.0, value=35.0),
        ),
    ),
    ConversionSpec(
        key="emails_to_weekly_time_lost",
        family="Productivite",
        title="Emails par jour vers temps perdu par semaine",
        summary="Estime le temps hebdomadaire consomme par la gestion des emails.",
        description="Pratique pour mesurer la charge invisible d'un flux de messages.",
        formula="Temps hebdo = emails par jour x minutes par email x jours de travail par semaine.",
        example="Exemple : 35 emails par jour, 3 minutes chacun, 5 jours = 8.75 heures par semaine.",
        inputs=(
            FieldSpec("emails_per_day", "Emails par jour", "number", min_value=0.0, step=1.0, value=35.0),
            FieldSpec("minutes_per_email", "Minutes par email", "number", min_value=0.0, step=0.5, value=3.0),
            FieldSpec("workdays_per_week", "Jours de travail par semaine", "number", min_value=1.0, max_value=7.0, step=1.0, value=5.0),
        ),
    ),
    ConversionSpec(
        key="task_time_to_monthly_workload",
        family="Productivite",
        title="Temps par tache vers charge mensuelle",
        summary="Convertit une tache repetitive en charge de travail mensuelle.",
        description="Permet de voir l'impact reel d'une action apparemment courte mais frequente.",
        formula="Heures mensuelles = temps par tache x taches par semaine x 4.33 / 60.",
        example="Exemple : 18 minutes par tache, 14 taches par semaine = environ 18.19 heures par mois.",
        inputs=(
            FieldSpec("minutes_per_task", "Minutes par tache", "number", min_value=0.0, step=1.0, value=18.0),
            FieldSpec("tasks_per_week", "Nombre de taches par semaine", "number", min_value=0.0, step=1.0, value=14.0),
        ),
    ),
    ConversionSpec(
        key="text_to_word_count",
        family="Texte",
        title="Texte brut vers nombre de mots",
        summary="Compte rapidement les mots, caracteres et temps de lecture d'un texte.",
        description="Utile pour du contenu, une page web, une note ou un brief.",
        formula="Comptage simple des mots et estimation du temps de lecture sur base d'une vitesse moyenne.",
        example="Exemple : un texte de 480 mots se lit en environ 2.4 minutes a 200 mots/minute.",
        inputs=(
            FieldSpec("text", "Texte", "text", placeholder="Collez ici votre texte"),
        ),
    ),
    ConversionSpec(
        key="word_count_to_reading_time",
        family="Texte",
        title="Nombre de mots vers temps de lecture",
        summary="Estime un temps de lecture a partir d'un volume de mots.",
        description="Pratique pour calibrer un article, une presentation ou un script.",
        formula="Temps de lecture = nombre de mots / vitesse de lecture.",
        example="Exemple : 1 200 mots a 220 mots/minute = environ 5.45 minutes.",
        inputs=(
            FieldSpec("word_count", "Nombre de mots", "number", min_value=0.0, step=10.0, value=1200.0),
            FieldSpec("reading_speed", "Vitesse de lecture (mots/minute)", "number", min_value=50.0, step=10.0, value=220.0),
        ),
    ),
    ConversionSpec(
        key="text_to_short_summary",
        family="Texte",
        title="Texte long vers resume court",
        summary="Produit un resume local et simple a partir des phrases les plus representatives.",
        description="Version locale et heuristique, utile pour raccourcir un texte sans dependance externe.",
        formula="Selection des premieres phrases significatives puis compression du texte cible.",
        example="Exemple : resume en 2 ou 3 phrases d'un texte plus long.",
        inputs=(
            FieldSpec("text", "Texte", "text", placeholder="Collez ici un texte assez long"),
            FieldSpec("summary_sentences", "Nombre de phrases du resume", "number", min_value=1.0, max_value=5.0, step=1.0, value=3.0),
        ),
    ),
)


def get_conversion_spec(conversion_key: str) -> ConversionSpec:
    for spec in CONVERSION_SPECS:
        if spec.key == conversion_key:
            return spec
    raise KeyError(f"Unknown conversion: {conversion_key}")
