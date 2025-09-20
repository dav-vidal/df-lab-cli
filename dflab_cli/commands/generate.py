def run(args):
    creature = args.creature.upper()
    caste = args.caste.upper() if args.caste else None
    seed = args.seed
    save = bool(args.save)

    print("[DF Lab] generate")
    print(f" creature   = {creature}")
    print(f" caste      = {caste or '(auto)'} ")
    print(f" seed       = {seed or '(auto)'}")
    print(f" save       = {save}")
