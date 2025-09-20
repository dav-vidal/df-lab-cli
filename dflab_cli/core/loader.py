import os, yaml, random

# Finds the root directory for specs, either from an environment variable or by falling back to a default path.
def _root():
    env = os.getenv("DFLAB_SPEC_ROOT")
    if env:
        return env
    # fallback to vendored path inside cli repo (optional future)
    here = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    vendored = os.path.join(here, "specs")   
    return vendored   

# Reads a YAML file from the given path and returns its contents as a Python object.
def _read_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

# Loads the creature index from the Configs/CreatureIndex.yaml 
def load_creature_index():
    root = _root()
    path = os.path.join(root, "Configs", "CreatureIndex.yaml")
    return _read_yaml(path)

# Loads a specific creature's data using its token.
# Raises ValueError if the token is not found in the index.
def load_creature_raw(creature_token: str):
    idx = load_creature_index()
    mp = idx.get("MAP", {})
    if creature_token not in mp:
        raise ValueError(f"Unknown creature: {creature_token}")
    root = _root()
    path = os.path.join(root, mp[creature_token])
    return _read_yaml(path)

def resolve_caste(data: dict, caste: str | None):
    # If caste not present, treate whole file as a single "default caste"
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
    raw = load_creature_raw(creature)
    return resolve_caste(raw, caste)