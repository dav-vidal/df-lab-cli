import argparse
from dflab_cli.commands import generate as cmd_generate
from dflab_cli.commands import validate as cmd_validate

def main(argv=None):
    # Create main perser
    p = argparse.ArgumentParser(prog="dflab", description="DF Lab CLI")
    sub = p.add_subparsers(dest="cmd", required=True)

    # generate subcommand
    p_gen = sub.add_parser("generate", help="Generate one unit")
    p_gen.add_argument("--creature", required=True) # which creature to use
    p_gen.add_argument("--caste") # optional caste choice
    p_gen.add_argument("--seed", type=int)  # optional rng seed
    p_gen.add_argument("--save", action="store_true") # whether to save output
    p_gen.set_defaults(func=cmd_generate.main) # handler

    # validate subcommand
    p_val = sub.add_parser("validate", help="Validate configs")
    p_val.set_defaults(func=cmd_validate.main)

    # dispatch chosencommand
    args = p.parse_args(argv)
    return args.func(args)

