"""
dflab/core/constants.py
-----------------------
Keep shared constants and attribute catalogs in one place.
Modular by design: add/remove attributes by editing the lists below.
"""

# --- Global numerical deafults (tunnable) ---
STEP = 200              # distance between cutoff tiers
HUMAN_MEDIAN = 1000     # deafult central value for human-like species
ABS_MIN_DEFAULT = 0     # floor for any attribute unless overridden

# --- Attribute catalogs (DF-inspired, no personalities here) ---
# Keep this plain lists for easy editing. Order is intentional and stable.

# Physical Attributes
PHYSICAL_ATTRIBUTES = [
    "STRENGTH",
    "AGILITY",
    "TOUGHNESS",
    "ENDURANCE",
    "RECUPERATION",
    "DISEASE_RESISTANCE",
]

# Mental Attributes
MENTAL_ATTRIBUTES = [
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
ATTRIBUTES = PHYSICAL_ATTRIBUTES + MENTAL_ATTRIBUTES

# Simple grouping map for UIs,