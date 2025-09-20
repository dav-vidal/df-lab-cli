from dflab_cli.core import loader, generator

def run(args):
    creature = args.creature.upper()
    caste_in = args.caste.upper() if args.caste else None
    seed = args.seed
    save = bool(args.save)
    
    caste_block, caste_name = loader.load_creature_caste(creature, caste_in)
    unit = generator.generate_unit(caste_block, seed=seed)

    print("[DF Lab] generate")
    print(f" creature   = {creature}")
    print(f" caste      = {caste_name}")
    print(f" seed       = {seed or '(random)'} save={save}")
    print(" PHYS:", unit["physical"])
    print(" MENT:", unit["mental"])
    print(" BODY:", unit["body_mods"])
