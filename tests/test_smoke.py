import os, types
from dflab_cli.core import loader, generator

def test_load_dwarf_male():
    data, caste = loader.load_creature_caste("DWARF", "MALE")
    assert caste == "MALE"
    assert "BODY_MODS" in data
    assert "PHYS_ATT_RANGE" in data
    assert "MENT_ATT_RANGE" in data
    # spot-check a few expected attributes
    for k in ("STRENGTH", "AGILITY", "TOUGHNESS",):
        assert k in data["PHYS_ATT_RANGE"]
        assert len(data["PHYS_ATT_RANGE"][k]) == 7
        
def test_generate_unit_reproducible():
    data, _ = loader.load_creature_caste("DWARF", "MALE")
    u1 = generator.generate_unit(data, seed=42)
    u2 = generator.generate_unit(data, seed=42)
    assert u1["physical"] == u2["physical"]
    assert u1["mental"] == u2["mental"]
    assert u1["body_mods"] == u2["body_mods"]
    # structure sanity
    assert isinstance(u1["physical"], dict) and u1["physical"]
    assert isinstance(u1["mental"], dict) and u1["mental"]
    assert isinstance(u1["body_mods"], dict)