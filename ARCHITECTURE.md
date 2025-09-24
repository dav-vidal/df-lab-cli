# DF Lab CLI — Architecture

## Overview
Lightweight CLI that merges YAML specs into attribute profiles, rolls DF-style stats, and persists units.

## Components
- **constants.py**
  - Inputs: none
  - Outputs: defaults, catalogs, paths, spec keys
- **loader.py**
  - Inputs: specs/Defaults.yaml, specs/Creatures/*.yaml
  - Outputs: `profile` dict (per-species)
  - Contracts: 7-point ascending cutoffs; known attributes only
- **generator.py**
  - Inputs: profile, RNG
  - Outputs: `unit` dict {id, species, attributes, rolls, meta}
  - Rules: clamp ≥ ABS_MIN; 7-tier roll + offset
- **storage.py**
  - Inputs: unit or id
  - Outputs: Store/Units/<id>.yaml; Store/UnitIndex.yaml
  - Guarantees: mkdir -p, last_id maintained
- **commands/**
  - `generate`: profile→unit, optional save
  - `list`: read index, print summaries
  - `show`: load unit by id

## Orchestration (CLI flow)
`main.py` → argparse → subcommand
- generate: load profile → roll → save? → print
- list: load index → print
- show: load by id → print

## Data/Validation
- Medians: phys=1000, mental=1100 (overridable)
- Cutoffs: 7 ints [m-3s … m+3s], strictly ascending
- Attributes: in catalogs only
- ABS_MIN: global or per-attr override

## Paths
`STORE_DIR`, `UNITS_DIR`, `INDEX_PATH`

## Errors
Fail fast. Raise on bad spec keys, non-ascending cutoffs, unknown attrs, IO errors.

## Testing
- `python -m dflab generate --species Human --save`
- Unit tests for loader/generator/storage
