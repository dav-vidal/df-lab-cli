"""
dflab/core/constants.py
-----------------------
Keep shared constants and attribute catalogs in one place.
Modular by design: add/remove attributes by editing the lists below.
"""

# --- Global numerical deafults (tunnable) ---
STEP = 200              # distance between cutoff tiers
PHYS_MEDIAN_DEFAULT = 1000     # fallback median for physical attributes
MENT_MEDIAN_DEFAULT = 1100     # fallback median for mental atrributes
ABS_MIN_DEFAULT = 0     # floor for any attribute unless overridden

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
STORE_DIR = "Store"
UNITS_DIR = f"{STORE_DIR}/Units"
INDEX_PATH = f"{STORE_DIR}/UnitIndex.yaml"

# Specs defaults (expected keys in YAML). Centralizing names avoids typos.
SPEC_KEYS = {
    "ATTRIBUTES": "ATTRIBUTES",
    "STEPS": "STEPS",
    "ABS_MIN_DEFAULT": "ABS_MIN_DEFAULT",
    "ABS_MIN": "ABS_MIN",
    "PHYS_ATT_RANGES": "PHYS_ATT_RANGES",
    "MENT_ATT_RANGES": "MENT_ATT_RANGES",
    "extends": "extends",
}
