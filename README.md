# philiprehberger-string-truncate

Truncate strings intelligently without cutting words.

## Installation

```bash
pip install philiprehberger-string-truncate
```

## Usage

```python
from philiprehberger_string_truncate import truncate, truncate_middle, truncate_path

truncate("Hello beautiful world", max_length=15)
# "Hello…"

truncate("Hello beautiful world", max_length=15, suffix="...")
# "Hello..."

truncate_middle("Hello beautiful world of code", max_length=20)
# "Hello bea…l of code"

truncate_path("/very/long/path/to/some/file.txt", max_length=25)
# "/very/long/.../file.txt"
```

## API

- `truncate(text, max_length, suffix="…", break_words=False)` — Word-boundary truncation
- `truncate_middle(text, max_length, separator="…")` — Keep start and end
- `truncate_path(path, max_length, separator="/", placeholder="...")` — Path-aware truncation

## License

MIT
