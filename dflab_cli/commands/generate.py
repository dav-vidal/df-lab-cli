# Use laoder to load creature and resolve caste, then call generator
from dflab_cli.core import loader, generator

def main(args):
    caste_block, caste_name = loader.load_creature_caste(args.creature, args.caste)
    unit = generator.generate_unit(caste_block, seed=args.seed)

    print("== Unit ==")
    print(f"creature: {args.creature}")
    print(f"caste: {caste_name}")
    if args.seed is not None:
        print(f"seed: {args.seed}")
    for k, v in unit.items():
        print(f"{k}: {v}")

    # if args.save:
    #     out = loader.save_unit(unit)
    #     print(f"saved: {out}")

    return 0


