import os
from typing import Any

import yaml

from dflab.Core.constants import RACE_DIR, RACE_INDEX_FILE


def _read_yaml(rpath: str):
    with open(rpath, encoding="utf-8") as f:
        return yaml.safe_load(f)


def _load_race_index() -> dict[str, Any]:
    return _read_yaml(RACE_INDEX_FILE)


def _resolve_race_path(race: str) -> str:
    idx = _load_race_index()
    if race.upper() not in idx["MAP"]:
        raise ValueError(f"Race '{race}' not found in index!")
    else:
        race_select = idx["MAP"][race.upper()]
        race_spec_path = os.path.join(RACE_DIR, race_select)
        return race_spec_path


def load_species_specs(race: str) -> dict[str, Any]:
    path = _resolve_race_path(race)
    data = _read_yaml(path)
    if "CASTES" not in data:
        raise ValueError("CASTES key not found in race specifications!")
    else:
        return data
