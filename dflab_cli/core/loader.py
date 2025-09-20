import os, yaml

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

# Loads the creature index from the Configs/CreatureIndex.txt YAML file.
def load_creature_index():
    root = _root()
    path = os.path.join(root, "Configs", "CreatureIndex.txt")
    return _read_yaml(path)

# Loads a specific creature's data using its token.
# Raises ValueError if the token is not found in the index.
def load_creature(creature_token: str):
    idx = load_creature_index()
    m = idx.get("MAP", {})
    if creature_token not in m:
        raise ValueError(f"Unknown creature: {creature_token}")
    root = _root()
    path = os.path.join(root, "Creatures", m[creature_token])
    return _read_yaml(path)