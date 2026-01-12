# Python Vocabulary Census

Extract vocabulary frequency statistics from GitHub Top Python projects
for Rosetta Map allocation reference.

## Quick Start

```bash
# Clone demo projects (shallow clone)
git clone --depth 1 https://github.com/pallets/flask.git /tmp/flask
git clone --depth 1 https://github.com/psf/requests.git /tmp/requests
git clone --depth 1 https://github.com/pandas-dev/pandas.git /tmp/pandas
git clone --depth 1 https://github.com/python/cpython.git /tmp/cpython
git clone --depth 1 https://github.com/scikit-learn/scikit-learn.git /tmp/sklearn

# Analyze each project
python census.py analyze /tmp/flask -o output/projects/flask.json
python census.py analyze /tmp/requests -o output/projects/requests.json
python census.py analyze /tmp/pandas -o output/projects/pandas.json
python census.py analyze /tmp/cpython -o output/projects/cpython.json
python census.py analyze /tmp/sklearn -o output/projects/sklearn.json

# Generate aggregated report
python census.py aggregate

# View results
head -50 output/vocab_report.json
```

## Output

- `output/projects/{name}.json` - Per-project vocabulary statistics
- `output/vocab_report.json` - Aggregated report with all unique words
- `output/sources.lock.json` - Version lock file (create manually)

## Verification

```bash
# Check hash for reproducibility
sha256sum output/vocab_report.json
```

## LICENSE

- Tool code: MIT
- Output data: CC0 (Public Domain)
