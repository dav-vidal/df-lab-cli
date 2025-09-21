# Use laoder to load creature and resolve caste, then call generator
from dflab_cli.core import loader, generator

def main(args):
    # Load raw creature dict and select caste or default first caste.
    caste_block, caste_name = loader.load_creature_caste(args.creature, args.caste)

    # Generate a unit from the already-narrowed caste bloack
    unit = generator.generate_unit(caste_block, seed=args.seed)

    # Minimal pretty print
    print("== Unit ==")
    print(f"creature: {args.creature}")
    if args.seed is not None:
        print(f"seed: {args.seed}")
    for k, v in unit.items():
        print(f"{k}: {v}")

