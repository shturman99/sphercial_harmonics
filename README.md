# sphercial_harmonics

Goal of this repo is to aggregate resources needed to effectively use spherical
harmonics of different kinds in cosmological and gravitational waves research.

## Development setup

Create a virtual environment and install the package in editable mode:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[test]"
```

## Run tests

```bash
pytest
```

## Check required TeX equation labels

```bash
python tools/check_tex_equations.py
```
