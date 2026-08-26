# Cheminformatics Tutorials

Notebooks and scripts for learning cheminformatics with RDKit.

## Setup

```bash
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Running

```bash
jupyter lab
```

Then open `class_1.ipynb`. Sample data used by the notebooks lives in `example_compounds.sdf`.

## Notes

- `venv/` and `.ipynb_checkpoints/` are gitignored — don't commit them.
- If you add new dependencies, remember to update `requirements.txt` (e.g. `pip freeze > requirements.txt`).
