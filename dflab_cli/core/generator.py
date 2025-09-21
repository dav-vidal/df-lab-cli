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


def generate_unit(creature_data, seed=None):
    # main generator: roll stats from cutoffs and body mods
    rng = random.Random(seed)
    
    # roll physical attributes
    phys = {}
    for attr, cutoffs in creature_data.get("PHYS_ATT_RANGE", {}).items():
        phys[attr] = roll_from_cutoffs(cutoffs, rng)

    # roll mental attributes
    ment = {}
    for attr, cutoffs in creature_data.get("MENT_ATT_RANGE", {}).items():
        ment[attr] = roll_from_cutoffs(cutoffs, rng)

    # copy body mods directly
    body = creature_data.get("BODY_MODS", {}).copy()
    
    # int empty skills
    skills = {}
    
    # return assembled unit dict
    return {
        "physical": phys,
        "mental": ment,
        "body_mods": body,
        "skills": skills,
    }
