from typing import Mapping, Sequence

REQ_BODY_KEY = "BASE_SIZE_CM3"
OPT_BMOD_KEYS = {"HEIGHT_%", "BROADNESS_%", "LENGTH_%"}

def _is_integer(x): return isinstance(x, int)

def _check_cutoffs(name: str, vals: Sequence[int]):
    if not isinstance(vals, (list, tuple)) or len(vals) != 7:
        raise ValueError(f"{name}: need 7 cutoff values")
    if not all(_is_integer(v) for v in vals):
        raise ValueError(f"{name}: cutoffs must be ints")
    if any(vals[i] >= vals[i+1] for i in range(6)):
        raise ValueError(f"{name}: cutoffs must be strictly ascending")
    
def _check_body_mods(bm: Mapping):
    if not isinstance(bm, Mapping):
        raise ValueError("BODY_MODS must be a mapping")
    if REQ_BODY_KEY not in bm:
        raise ValueError("BODY_MODS.BASE_SIZE_CM3 missing")
    v = bm[REQ_BODY_KEY]
    if not _is_integer(v) or v <= 0:
        raise ValueError("BODY_MODS.BASE_SIZE_CM3 must be positive int")
    for k in (OPT_BMOD_KEYS & set(bm.keys())):
        lohi = bm[k]
        if (not isinstance(lohi, (list, tuple)) or len(lohi) != 2 or
            not all(_is_integer(x) for x in lohi) or lohi[0] <= 0 or lohi[0] > lohi[1]):
            raise ValueError(f"BODY_MODS.{k} must be [lo, hi], ints, lo > 0, lo <= hi")

        
def _check_att_ranges(block: Mapping, key: str):
    rngs = block.get(key, {})
    if not isinstance(rngs, Mapping):
        raise ValueError(f"{key} must be a mapping of ATTR -> 7 cutoffs")
    for attr, vals in rngs.items():
        _check_cutoffs(f"{key}.{attr}", vals)
        
def _check_caste_block(c: Mapping):
    if "BODY_MODS" not in c:
        raise ValueError("caste missing BODY_MODS")
    _check_body_mods(c["BODY_MODS"])
    _check_att_ranges(c, "PHYS_ATT_RANGES")
    _check_att_ranges(c, "MENT_ATT_RANGES")
    
def validate_creature_dict(d: Mapping):
    if "CASTES" in d:
        castes = d["CASTES"]
        if not isinstance(castes, Mapping) or not castes:
            raise ValueError("CASTES must be a non-empty mapping")
        for name, block in castes.items():
            if not isinstance(block, Mapping):
                raise ValueError(f"CASTES.{name} must be a mapping")
            _check_caste_block(block)
    else:
        _check_caste_block(d)
    return True