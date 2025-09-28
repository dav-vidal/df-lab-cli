import os
from typing import Any

import yaml

from dflab.Core.constants import RACE_INDEX_FILE, SPECS_DIR


def _read_yaml(rpath: str):
    with open(rpath) as f:
        return yaml.safe_load(f)


def _load_race_index(rpath: str) -> dict[str, Any]:
    return _read_yaml(RACE_INDEX_FILE)


def _resolve_race_path(race: str) -> str:
    idx = _load_race_index(race)
    race_select = idx["MAP"][race.upper()]
    race_spec_path = os.path.join(SPECS_DIR, race_select)
    return race_spec_path


def load_species_specs(race: str) -> dict[str, Any]:
    path = _resolve_race_path(race)
    data = _read_yaml(path)
    return data
