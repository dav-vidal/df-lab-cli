import argparse
from dflab_cli.commands import generate as cmd_generate

def _build_parser():
    p = argparse.ArgumentParser(prog="dflab")
    sub = p.add_subparsers(dest="cmd", required=True)

    g = sub.add_parser("generate", help="Generate one unit")
    g.add_argument("--creature", required=True)
    g.add_argument("--caste")
    g.add_argument("--seed", type=int)
    g.add_argument("--save", action="store_true")
    return p

def main():
    args = _build_parser().parse_args()
    if args.cmd == "generate":
        cmd_generate.run(args)
    else:
        print(f"[DF Lab] Unknown command: {args.cmd}")

if __name__ == "__main__":
    main()
