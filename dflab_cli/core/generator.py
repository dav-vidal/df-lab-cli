import random

def roll_from_cutoffs(cutoffs, rng=None): # cutoffs is a list of 7 ascending ints [c1..c7]
    if rng is None:
        rng = random
        
    # Pick a bucket with weighted probabilities
    bucket = rng.choices(range(8), weights=[5,15,30,30,15,4,0.9,0.1])[0]

    #Decide value range for that bucket
    if bucket ==0:
        low, high = 0, cutoffs[0]
    elif bucket == 7:
        low, high = cutoffs[6], cutoffs[6] * 2
    else:
        low, high = cutoffs[bucket-1], cutoffs[bucket]
    return rng.randint(low, high)