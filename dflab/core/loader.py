from dflab.core.constants import INDEX_PATH, ATTRIBUTES
import yaml

def _read_yaml(path: str):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def
