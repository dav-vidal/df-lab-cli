import os, yaml, random

def _root():
    # find root path for specs (env var or fallback)
    env = os.getenv("DFLAB_SPEC_ROOT")
    if env:
        return env
    here = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    vendored = os.path.join(here, "specs")   
    return vendored   

def _read_yaml(path):
    # read YAML file into Python dict
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def load_creature_index():
    # load index file mapping tokens -> yaml paths
    root = _root()
    path = os.path.join(root, "Configs", "CreatureIndex.yaml")
    return _read_yaml(path)

def load_creature_raw(creature_token: str):
    # load a raw creature spec given its token
    idx = load_creature_index()
    mp = idx.get("MAP", {})
    if creature_token not in mp:
        raise ValueError(f"Unknown creature: {creature_token}")
    root = _root()
    path = os.path.join(root, mp[creature_token])
    return _read_yaml(path)

def resolve_caste(data: dict, caste: str | None):
    # pick a caste block, or default if no castes
    if "CASTES" not in data:
        return data, "(single)"
    castes = data["CASTES"]
    if not isinstance(castes, dict) or not castes:
        raise ValueError("CASTES must be a non-empty mapping")
    if caste:
        c = caste.upper()
        if c not in castes:
            raise ValueError(f"Caste '{c}' not found. Available: {', '.join(castes)}")
        return castes[c], c
    #auto-pick first key (DF-like deterministic)
    first = next(iter(castes.keys()))
    return castes[first], first

# Return (caste_block, chosen_caste_name).
def load_creature_caste(creature: str, caste: str | None):
    # wrapper: load raw then resolve caste
    raw = load_creature_raw(creature)
    return resolve_caste(raw, caste)
