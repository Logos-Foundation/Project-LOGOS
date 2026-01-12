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

## Algorithm

### Extracted AST Nodes

| AST Node | Content | Example |
|:--|:--|:--|
| `ast.Name` | Variable/function references | `print`, `data` |
| `ast.FunctionDef.name` | Function definition names | `def process():` |
| `ast.ClassDef.name` | Class definition names | `class User:` |
| `ast.Attribute.attr` | Attribute access | `obj.name` → `name` |
| `ast.Constant` (str) | String constants | `"GET"` |
| `ast.Import` / `ast.ImportFrom` | Module names | `import pandas` |
| `ast.keyword.arg` | Keyword arguments | `func(timeout=10)` → `timeout` |
| `ast.Call.func.attr` | Decorator calls | `@app.route` → `route` |
| `ast.annotation` | Type annotations | `def foo(x: str)` → `str` |

### Filter Rules

**Excluded:**
- Docstrings
- Comments  
- Single-character identifiers (`i`, `j`, `x`)
- Pure digits

**Included:**
- All identifiers ≥2 characters

### Normalization Rules

| Rule | Setting | Description |
|:--|:--|:--|
| Case | **preserve** | Keep original case, `GET` ≠ `get` |
| Dedup Key | `(word, type)` | Same word in different types counted separately |

### Word Types

| Type | Description | Example |
|:--|:--|:--|
| `keyword` | Python keywords | `def`, `class` |
| `builtin` | Built-in functions | `len`, `print` |
| `magic` | Magic methods | `__init__` |
| `identifier` | User-defined | `request`, `data` |
| `string_constant` | String constants | `"GET"` |

## Version Scheme

`v{major}.{minor}.{patch}.{build}`

| Trigger | Version Change |
|:--|:--|
| Add new projects | minor +1 |
| Project version update | patch +1 |
| Fix statistics bug | patch +1 |
| Algorithm improvement | major +1 |

## Verification

```bash
# Check hash for reproducibility
sha256sum output/vocab_report.json
```

## LICENSE

- Tool code: MIT
- Output data: CC0 (Public Domain)
