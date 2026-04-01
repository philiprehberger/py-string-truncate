# philiprehberger-string-truncate

[![Tests](https://github.com/philiprehberger/py-string-truncate/actions/workflows/publish.yml/badge.svg)](https://github.com/philiprehberger/py-string-truncate/actions/workflows/publish.yml)
[![PyPI version](https://img.shields.io/pypi/v/philiprehberger-string-truncate.svg)](https://pypi.org/project/philiprehberger-string-truncate/)
[![Last updated](https://img.shields.io/github/last-commit/philiprehberger/py-string-truncate)](https://github.com/philiprehberger/py-string-truncate/commits/main)

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

| Function / Class | Description |
|------------------|-------------|
| `truncate(text, max_length, suffix="…", break_words=False)` | Word-boundary truncation |
| `truncate_middle(text, max_length, separator="…")` | Keep start and end |
| `truncate_path(path, max_length, separator="/", placeholder="...")` | Path-aware truncation |

## Development

```bash
pip install -e .
python -m pytest tests/ -v
```

## Support

If you find this project useful:

⭐ [Star the repo](https://github.com/philiprehberger/py-string-truncate)

🐛 [Report issues](https://github.com/philiprehberger/py-string-truncate/issues?q=is%3Aissue+is%3Aopen+label%3Abug)

💡 [Suggest features](https://github.com/philiprehberger/py-string-truncate/issues?q=is%3Aissue+is%3Aopen+label%3Aenhancement)

❤️ [Sponsor development](https://github.com/sponsors/philiprehberger)

🌐 [All Open Source Projects](https://philiprehberger.com/open-source-packages)

💻 [GitHub Profile](https://github.com/philiprehberger)

🔗 [LinkedIn Profile](https://www.linkedin.com/in/philiprehberger)

## License

[MIT](LICENSE)
