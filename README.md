# demo_test

Demo repository used to validate GitHub + Linear connector behavior.

## Structure
- rel_notes/rel_notes_v1.txt: lightweight release notes
- src/config/global_config.py: configuration helpers
- src/config/entities.py: small data entities used by the app
- src/libraries/common_utils.py: utility helpers (logging/formatting)

## Quick start
Set optional environment variables:
- ENV (default: dev)
- MODE (default: standard)

## Notes
This repository is used for connector QA scenarios (GitHub + Linear).

## Output

`process(rows)` returns a dictionary:

```json
{
  "total_revenue": 1234.5,
  "valid_rows": 10
}
```

Run a quick smoke test in python:

```bash
python -c "from src.config.global_config import get_runtime_context; print(get_runtime_context())"
```
