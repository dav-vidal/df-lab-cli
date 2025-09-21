import sys
from dflab_cli.core import loader, validator

def main(args):
    try:
        idx = loader.load_creature_index()
        mp = idx.get("MAP", {})
        if not mp:
            raise ValueError("CreatureIndex missing MAP")
        errors = []
        for creature, relpath in mp.items():
            try:
                data = loader.load_creature_raw(creature)
                validator.validate_creature_dict(data)
                print(f"[OK] {creature} ({relpath})")
            except Exception as e:
                errors.append((creature, str(e)))
                print(f"[ERR] {creature}: {e}")
        if errors:
            print(f"Failed: {len(errors)} creature(s).")
            sys.exit(1)
        print("\nAll good.")
    except Exception as e:
        print(f"[FATAL] {e}")
        sys.exit(2)

