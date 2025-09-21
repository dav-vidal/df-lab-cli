#!/usr/bin/env python3
import os, sys

EXCLUDE_DIRS = {
    ".git", "__pycache__", ".venv", "venv", "myenv", "env", "build", 
    "dist", ".idea", ".vscode", ".tox", ".pytest_cache" 
}
EXCLUDE_EXTS = {".pyc", ".pyo", ".pyd", ".so", ".egg", ".whl"}

def human(n):
    for u in ["B", "KB", "MB", "GB", "TB"]:
        if n < 1024:
            return f"{n:.1f}{u}"
        n /= 1024
    return f"{n:.2f} PB"

def main(root="."):
    total = 0
    # prune excluded dirs
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]
        for f in filenames:
            _, ext = os.path.splitext(f)
            if ext in EXCLUDE_EXTS:
                continue
            fp = os.path.join(dirpath, f)
            try:
                total += os.path.getsize(fp)
            except OSError:
                pass
    print(human(total))
    
if __name__ == "__main__":
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    main(root)