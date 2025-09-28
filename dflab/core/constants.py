"""
dflab/core/constants.py
-----------------------
Keep shared constants and attribute catalogs in one place.
Modular by design: add/remove attributes by editing the lists below.
"""

# --- Global numerical deafults (tunnable) ---
STEP = 250              # distance between cutoff tiers
ABS_MIN_DEFAULT = 0     # floor for any attribute unless overridden
DEFAULT_PHYS_ATTRS_CUTS = [200, 700, 900, 1000, 1100, 1300, 2000]
DEFAULT_MENT_ATTRS_CUTS = [300, 800, 1000, 1100, 1200, 1400, 2100]      # mental distribution has higher median

# --- Attribute catalogs (DF-inspired, no personalities here) ---

# Physical Attributes
PHYSICAL_ATTRS = [
    "STRENGTH",
    "AGILITY",
    "TOUGHNESS",
    "ENDURANCE",
    "RECUPERATION",
    "DISEASE_RESISTANCE",
]

# Mental Attributes
MENTAL_ATTRS = [
    "ANALYTICAL_ABILITY",
    "FOCUS",
    "WILLPOWER",
    "CREATIVITY",
    "INTUITION",
    "PATIENCE",
    "MEMORY",
    "LINGUISTIC_ABILITY",
    "SPATIAL_SENSE",
    "MUSICALITY",
    "KINESTHETIC_SENSE",
    "EMPATHY",
    "SOCIAL_AWARENESS",
]

# Unified ordered list used by loader/generator modules
ATTRIBUTES = PHYSICAL_ATTRS + MENTAL_ATTRS

# Simple grouping map for UIs,
ATTRIBUTES_GROUPS = {
    "PHYSICAL": PHYSICAL_ATTRS,
    "MENTAL": MENTAL_ATTRS,
}

# File system layout (kept here so storage/commands share one source of truth)
DFLAB_ROOT = "~/Projects/df-lab-cli"
STORE_DIR = f"{DFLAB_ROOT}/Store"
UNITS_DIR = f"{STORE_DIR}/Units"
INDEX_FILE = f"{STORE_DIR}/UnitIndex.yaml"
SPECS_DIR = f"{DFLAB_ROOT}/specs"
# Specs defaults (expected keys in YAML). Centralizing names avoids typos.


SPECS_KEYS = {
    "ATTRIBUTES": "ATTRIBUTES",
    "STEP": "STEP",
    "ABS_MIN_DEFAULT": "ABS_MIN_DEFAULT",
    "ABS_MIN": "ABS_MIN",
    "PHYS_ATT_RANGES": "PHYS_ATT_RANGES",
    "MENT_ATT_RANGES": "MENT_ATT_RANGES",
    "extends": "extends",
}
