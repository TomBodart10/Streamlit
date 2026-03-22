from __future__ import annotations

import math
import re

from .catalog import get_conversion_spec


WEEKS_PER_MONTH = 4.33
DAYS_PER_MONTH = 30.44


def _round(value: float, digits: int = 2) -> float:
    return round(float(value), digits)


def _format_currency(value: float, suffix: str = "EUR") -> str:
    return f"{value:,.2f} {suffix}".replace(",", " ")


def _format_hours_minutes(hours: float) -> str:
    total_minutes = round(hours * 60)
    if total_minutes < 60:
        return f"{total_minutes} min"
    whole_hours, remaining_minutes = divmod(total_minutes, 60)
    if remaining_minutes == 0:
        return f"{whole_hours} h"
    return f"{whole_hours} h {remaining_minutes} min"


def _format_duration(seconds: float) -> str:
    seconds = max(0, int(round(seconds)))
    hours, remainder = divmod(seconds, 3600)
    minutes, secs = divmod(remainder, 60)
    if hours:
        return f"{hours} h {minutes} min {secs} s"
    if minutes:
        return f"{minutes} min {secs} s"
    return f"{secs} s"


def _count_words(text: str) -> int:
    return len(re.findall(r"\b\w+\b", text, flags=re.UNICODE))


def _summarize_text(text: str, sentence_count: int) -> str:
    compact_text = " ".join(text.split())
    sentences = re.split(r"(?<=[.!?])\s+", compact_text)
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    if not sentences:
        words = compact_text.split()
        return " ".join(words[: min(40, len(words))])

    selected = []
    for sentence in sentences:
        if len(sentence.split()) >= 5:
            selected.append(sentence)
        if len(selected) == sentence_count:
            break

    if not selected:
        selected = sentences[:sentence_count]

    summary = " ".join(selected).strip()
    if len(summary) > 420:
        summary = summary[:417].rsplit(" ", 1)[0] + "..."
    return summary


def _result(
    headline: str,
    value: str,
    metrics: list[tuple[str, str]],
    insights: list[str],
) -> dict[str, object]:
    return {
        "headline": headline,
        "value": value,
        "metrics": metrics,
        "insights": insights,
    }


def convert(conversion_key: str, values: dict[str, object]) -> dict[str, object]:
    get_conversion_spec(conversion_key)

    if conversion_key == "work_hours_to_days_weeks":
        hours = float(values["hours"])
        hours_per_day = float(values["hours_per_day"])
        days_per_week = float(values["days_per_week"])
        days = hours / hours_per_day
        weeks = days / days_per_week
        return _result(
            "Charge de travail estimee",
            f"{_round(days, 2)} jours",
            [
                ("Semaines", f"{_round(weeks, 2)}"),
                ("Heures / jour", f"{_round(hours_per_day, 2)}"),
                ("Jours / semaine", f"{_round(days_per_week, 2)}"),
            ],
            [
                f"{_round(hours, 2)} heures correspondent a environ {_round(days, 2)} jours de travail.",
                f"Au rythme choisi, cela represente {_round(weeks, 2)} semaine(s).",
            ],
        )

    if conversion_key == "automation_minutes_to_month_hours":
        minutes_saved_per_day = float(values["minutes_saved_per_day"])
        workdays_per_month = float(values["workdays_per_month"])
        monthly_hours = minutes_saved_per_day * workdays_per_month / 60
        equivalent_days = monthly_hours / 7
        return _result(
            "Temps economise par mois",
            _format_hours_minutes(monthly_hours),
            [
                ("Heures / mois", f"{_round(monthly_hours, 2)} h"),
                ("Jours de 7 h", f"{_round(equivalent_days, 2)}"),
                ("Jours travailles", f"{_round(workdays_per_month, 0)}"),
            ],
            [
                f"Une economie quotidienne de {_round(minutes_saved_per_day, 2)} min libere {_round(monthly_hours, 2)} heures par mois.",
                f"Cela equivaut a environ {_round(equivalent_days, 2)} jour(s) de travail de 7 heures.",
            ],
        )

    if conversion_key == "business_days_to_calendar_days":
        business_days = float(values["business_days"])
        business_days_per_week = float(values["business_days_per_week"])
        calendar_days = business_days * 7 / business_days_per_week
        extra_days = calendar_days - business_days
        return _result(
            "Delai reel estime",
            f"{math.ceil(calendar_days)} jours calendaires",
            [
                ("Estimation precise", f"{_round(calendar_days, 2)} jours"),
                ("Week-end inclus", f"+{_round(extra_days, 2)} jours"),
                ("Base hebdo", f"{_round(business_days_per_week, 0)} jours ouvrables"),
            ],
            [
                f"{_round(business_days, 0)} jours ouvrables correspondent a environ {_round(calendar_days, 2)} jours calendaires.",
                "Le calcul est une estimation lineaire qui inclut les week-ends mais pas les jours feries.",
            ],
        )

    if conversion_key == "gross_to_net_salary":
        gross_salary = float(values["gross_salary"])
        salary_period = str(values["salary_period"])
        deduction_rate = float(values["deduction_rate"]) / 100
        net_salary = gross_salary * (1 - deduction_rate)
        annual_net = net_salary * 12 if salary_period == "Mensuel" else net_salary
        monthly_net = annual_net / 12
        return _result(
            "Salaire net estime",
            _format_currency(net_salary),
            [
                ("Periode", salary_period),
                ("Net mensuel estime", _format_currency(monthly_net)),
                ("Net annuel estime", _format_currency(annual_net)),
            ],
            [
                f"Avec une retenue estimee de {deduction_rate * 100:.0f} %, le net ressort a {_format_currency(net_salary)} sur la base {salary_period.lower()}.",
                "Cette conversion reste indicative et depend du pays, du statut et des avantages.",
            ],
        )

    if conversion_key == "monthly_to_annual_cost":
        monthly_cost = float(values["monthly_cost"])
        annual_cost = monthly_cost * 12
        return _result(
            "Budget annuel",
            _format_currency(annual_cost),
            [
                ("Mensuel", _format_currency(monthly_cost)),
                ("Trimestriel", _format_currency(monthly_cost * 3)),
                ("Hebdomadaire moyen", _format_currency(annual_cost / 52)),
            ],
            [
                f"Une depense de {_format_currency(monthly_cost)} par mois represente {_format_currency(annual_cost)} par an.",
            ],
        )

    if conversion_key == "annual_to_monthly_cost":
        annual_cost = float(values["annual_cost"])
        monthly_cost = annual_cost / 12
        return _result(
            "Equivalent mensuel",
            _format_currency(monthly_cost),
            [
                ("Annuel", _format_currency(annual_cost)),
                ("Trimestriel moyen", _format_currency(annual_cost / 4)),
                ("Journalier moyen", _format_currency(annual_cost / 365)),
            ],
            [
                f"Un engagement annuel de {_format_currency(annual_cost)} revient a environ {_format_currency(monthly_cost)} par mois.",
            ],
        )

    if conversion_key == "watts_to_monthly_cost":
        power_watts = float(values["power_watts"])
        hours_per_day = float(values["hours_per_day"])
        price_per_kwh = float(values["price_per_kwh"])
        monthly_kwh = (power_watts / 1000) * hours_per_day * DAYS_PER_MONTH
        monthly_cost = monthly_kwh * price_per_kwh
        return _result(
            "Cout mensuel estime",
            _format_currency(monthly_cost),
            [
                ("Consommation / mois", f"{_round(monthly_kwh, 2)} kWh"),
                ("Utilisation / jour", f"{_round(hours_per_day, 2)} h"),
                ("Prix du kWh", _format_currency(price_per_kwh)),
            ],
            [
                f"Un appareil de {_round(power_watts, 0)} W utilise {_round(monthly_kwh, 2)} kWh par mois.",
                f"Au tarif choisi, cela represente {_format_currency(monthly_cost)} par mois.",
            ],
        )

    if conversion_key == "fuel_to_trip_cost":
        distance_km = float(values["distance_km"])
        liters_per_100km = float(values["liters_per_100km"])
        fuel_price = float(values["fuel_price"])
        liters_used = distance_km * liters_per_100km / 100
        trip_cost = liters_used * fuel_price
        return _result(
            "Cout du trajet",
            _format_currency(trip_cost),
            [
                ("Litres consommes", f"{_round(liters_used, 2)} L"),
                ("Distance", f"{_round(distance_km, 0)} km"),
                ("Prix / litre", _format_currency(fuel_price)),
            ],
            [
                f"Pour {_round(distance_km, 0)} km, le vehicule consommera environ {_round(liters_used, 2)} L.",
                f"Le cout carburant estime est de {_format_currency(trip_cost)}.",
            ],
        )

    if conversion_key == "file_size_to_download_time":
        file_size = float(values["file_size"])
        file_size_unit = str(values["file_size_unit"])
        speed_value = float(values["speed_value"])
        speed_unit = str(values["speed_unit"])
        size_multipliers = {"MB": 8_000_000, "GB": 8_000_000_000, "TB": 8_000_000_000_000}
        speed_multipliers = {"Mbps": 1_000_000, "Gbps": 1_000_000_000, "MB/s": 8_000_000}
        total_bits = file_size * size_multipliers[file_size_unit]
        bits_per_second = speed_value * speed_multipliers[speed_unit]
        seconds = total_bits / bits_per_second if bits_per_second else 0
        return _result(
            "Temps de telechargement estime",
            _format_duration(seconds),
            [
                ("Taille", f"{_round(file_size, 2)} {file_size_unit}"),
                ("Debit", f"{_round(speed_value, 2)} {speed_unit}"),
                ("Secondes", f"{_round(seconds, 2)} s"),
            ],
            [
                "Le resultat est theorique et ne prend pas en compte la latence, les variations reseau ni les pertes.",
                f"A debit constant, le transfert prend environ {_format_duration(seconds)}.",
            ],
        )

    if conversion_key == "meeting_to_total_cost":
        meeting_minutes = float(values["meeting_minutes"])
        participants = float(values["participants"])
        hourly_cost = float(values["hourly_cost"])
        person_hours = (meeting_minutes / 60) * participants
        meeting_cost = person_hours * hourly_cost
        return _result(
            "Cout total de la reunion",
            _format_currency(meeting_cost),
            [
                ("Heures cumulees", f"{_round(person_hours, 2)} h"),
                ("Participants", f"{_round(participants, 0)}"),
                ("Cout horaire", _format_currency(hourly_cost)),
            ],
            [
                f"Une reunion de {_round(meeting_minutes, 0)} minutes mobilise {_round(person_hours, 2)} heures cumulees.",
                f"A ce cout horaire moyen, cela represente {_format_currency(meeting_cost)} de temps mobilise.",
            ],
        )

    if conversion_key == "emails_to_weekly_time_lost":
        emails_per_day = float(values["emails_per_day"])
        minutes_per_email = float(values["minutes_per_email"])
        workdays_per_week = float(values["workdays_per_week"])
        weekly_hours = emails_per_day * minutes_per_email * workdays_per_week / 60
        monthly_hours = weekly_hours * WEEKS_PER_MONTH
        return _result(
            "Temps email par semaine",
            _format_hours_minutes(weekly_hours),
            [
                ("Heures / semaine", f"{_round(weekly_hours, 2)} h"),
                ("Heures / mois", f"{_round(monthly_hours, 2)} h"),
                ("Emails / jour", f"{_round(emails_per_day, 0)}"),
            ],
            [
                f"A ce rythme, les emails consomment environ {_round(weekly_hours, 2)} heures par semaine.",
                f"Sur un mois moyen, cela represente {_round(monthly_hours, 2)} heures.",
            ],
        )

    if conversion_key == "task_time_to_monthly_workload":
        minutes_per_task = float(values["minutes_per_task"])
        tasks_per_week = float(values["tasks_per_week"])
        monthly_hours = minutes_per_task * tasks_per_week * WEEKS_PER_MONTH / 60
        yearly_hours = monthly_hours * 12
        return _result(
            "Charge mensuelle estimee",
            _format_hours_minutes(monthly_hours),
            [
                ("Heures / mois", f"{_round(monthly_hours, 2)} h"),
                ("Heures / an", f"{_round(yearly_hours, 2)} h"),
                ("Taches / semaine", f"{_round(tasks_per_week, 0)}"),
            ],
            [
                f"Une tache de {_round(minutes_per_task, 0)} minutes repetee {_round(tasks_per_week, 0)} fois par semaine finit par peser {_round(monthly_hours, 2)} heures par mois.",
            ],
        )

    if conversion_key == "text_to_word_count":
        text = str(values["text"]).strip()
        if not text:
            raise ValueError("Veuillez coller un texte a analyser.")
        word_count = _count_words(text)
        char_count = len(text)
        reading_minutes = word_count / 200
        speaking_minutes = word_count / 130
        return _result(
            "Volume du texte",
            f"{word_count} mots",
            [
                ("Caracteres", f"{char_count}"),
                ("Lecture moyenne", _format_hours_minutes(reading_minutes)),
                ("Lecture a voix haute", _format_hours_minutes(speaking_minutes)),
            ],
            [
                "Le comptage repose sur une separation simple des mots.",
                f"Un texte de {word_count} mots se lit en environ {_format_hours_minutes(reading_minutes)}.",
            ],
        )

    if conversion_key == "word_count_to_reading_time":
        word_count = float(values["word_count"])
        reading_speed = float(values["reading_speed"])
        reading_minutes = word_count / reading_speed
        return _result(
            "Temps de lecture estime",
            _format_hours_minutes(reading_minutes),
            [
                ("Mots", f"{_round(word_count, 0)}"),
                ("Vitesse", f"{_round(reading_speed, 0)} mots/min"),
                ("Minutes precises", f"{_round(reading_minutes, 2)}"),
            ],
            [
                f"A {_round(reading_speed, 0)} mots par minute, {_round(word_count, 0)} mots demandent environ {_round(reading_minutes, 2)} minutes de lecture.",
            ],
        )

    if conversion_key == "text_to_short_summary":
        text = str(values["text"]).strip()
        if not text:
            raise ValueError("Veuillez coller un texte a resumer.")
        summary_sentences = int(float(values["summary_sentences"]))
        summary = _summarize_text(text, summary_sentences)
        original_words = _count_words(text)
        summary_words = _count_words(summary)
        compression = 100 - ((summary_words / original_words) * 100) if original_words else 0
        return _result(
            "Resume court",
            summary,
            [
                ("Mots source", f"{original_words}"),
                ("Mots resume", f"{summary_words}"),
                ("Compression", f"{_round(compression, 1)} %"),
            ],
            [
                "Le resume est genere localement avec une heuristique simple, sans modele externe.",
                "Pour un vrai resume semantique, il faudrait une logique NLP plus evoluee ou un modele.",
            ],
        )

    raise KeyError(f"Unsupported conversion: {conversion_key}")
