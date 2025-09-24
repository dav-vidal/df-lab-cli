from dflab.core.constants import (
    STEP,
    PHYS_MEDIAN_DEFAULT,
    MENT_MEDIAN_DEFAULT,
    ABS_MIN_DEFAULT,
    PHYSICAL_ATTRS,
    MENTAL_ATTRS,
    ATTRIBUTES,
)

def test_defaults_and_catalogs():
    assert STEP == 250
    assert PHYS_MEDIAN_DEFAULT == 1000
    assert MENT_MEDIAN_DEFAULT == 1100
    assert ABS_MIN_DEFAULT == 0
    assert isinstance(PHYSICAL_ATTRS, list) and "STRENGTH" in PHYSICAL_ATTRS
    assert isinstance(MENTAL_ATTRS, list) and "STRENGTH" in MENTAL_ATTRS
    assert set(ATTRIBUTES) == set(PHYSICAL_ATTRS) | set(MENTAL_ATTRS)
