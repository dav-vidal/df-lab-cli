# DF Lab CLI

Lightweight CLI tool to **generate** and **store** units from YAML specs.  
Focus: keep it simple — just generation, storage, and viewing.

---

## Features

- Define creatures with YAML specs
- Merge defaults + creature data into an attribute profile
- Generate random units with reproducible seeds
- Save units as YAML in `Store/`
- Keep an index of created units
- List and show saved units from the CLI

---

## Install

```bash
git clone https://github.com/yourname/df-lab-cli.git
cd df-lab-cli
python -m venv .venv
source .venv/bin/activate
pip install -e .
