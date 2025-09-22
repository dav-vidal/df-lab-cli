import random

def roll_from_cutoffs(cutoffs, rng=None):
    # pick a random value of DF-style 7 cutoffs
    if rng is None:
        rng = random
        
    # choose a bucket with weighted probabilities
    bucket = rng.choices(range(8), weights=[5,15,30,30,15,4,0.9,0.1])[0]

    # pick value range for that bucket
    if bucket ==0:                  # bellow first cutoff
        low, high = 200, cutoffs[0]
    elif bucket == 7:               # above last cutoff
        low, high = cutoffs[6], min(cutoffs[6]*2, 5000)
    else:                           # between two cutoffs
        low, high = cutoffs[bucket-1], cutoffs[bucket]
    # draw value from that range
    return rng.randint(low, high)

def _roll_percent(lo_hi, rng):
    # roll a percentage in [lo, hi]
    lo, hi = lo_hi
    return rng.randint(lo, hi)

def generate_unit(creature_data: dict, seed: int | None = None) -> dict:
    # main generator: roll stats from cutoffs and body mods
    rng = random.Random(seed)
    
    # roll physical attributes
    phys = {}
    for attr, cutoffs in creature_data.get("PHYS_ATT_RANGES", {}).items():
        phys[attr] = roll_from_cutoffs(cutoffs, rng)

    # roll mental attributes
    ment = {}
    for attr, cutoffs in creature_data.get("MENT_ATT_RANGES", {}).items():
        ment[attr] = roll_from_cutoffs(cutoffs, rng)

    # copy body mods directly
    body_src = creature_data.get("BODY_MODS", {})
    body = dict(body_src)
    for key in ("HEIGHT_%", "BROADNESS_%", "LENGTH_%"):
        if key in body_src and isinstance(body_src[key], (list, tuple)) and len(body_src[key]) == 2:
            body[key] = _roll_percent(body_src[key], rng)
        elif key not in body_src:
            body[key] = 100 # deafult 100%
            
    # int empty skills
    skills = {}
    
    # return assembled unit dict
    return {
        "physical": phys,
        "mental": ment,
        "body_mods": body,
        "skills": skills,
    }
