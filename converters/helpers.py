from __future__ import annotations

from collections import defaultdict

from .catalog import CONVERSION_SPECS, ConversionSpec


RECOMMENDED_KEYS = (
    "watts_to_monthly_cost",
    "file_size_to_download_time",
    "meeting_to_total_cost",
)


def get_family_map() -> dict[str, list[ConversionSpec]]:
    family_map: dict[str, list[ConversionSpec]] = defaultdict(list)
    for spec in CONVERSION_SPECS:
        family_map[spec.family].append(spec)
    return dict(family_map)


def get_spec_by_title(family: str, title: str) -> ConversionSpec:
    family_map = get_family_map()
    return next(spec for spec in family_map[family] if spec.title == title)


def get_recommended_specs() -> list[ConversionSpec]:
    return [spec for spec in CONVERSION_SPECS if spec.key in RECOMMENDED_KEYS]
