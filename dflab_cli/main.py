import argparse
from dflab_cli.commands import generate as cmd_generate

def _build_parser():
    p = argparse.ArgumentParser(prog="dflab")
    sub = p.add_subparsers(dest="cmd", required=True)

    pg = sub.add_parser("generate", help="Generate one unit")
    pg = sub.add_parser("--creature", help="DWARF|HUMAN|ELF", required=True)
    pg = sub.add_parser("--caste", help="MALE|FEMALE")
    pg = sub.add_parser("--seed", help="RNG seed", type=int)
    pg = sub.add_parser("--save", help="Persist to Store/", action="store_true")
    return p

def main():
    args = _build_parser().parse_args()
    if args.cmd == "generate":
        cmd_generate.run(args)
    else:
        print(f"[DF Lab] Unknown command: {args.cmd}")

if __name__ == "__main__":
    main()
