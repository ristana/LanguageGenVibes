# LanguageGenVibes

A fun Python application that translates English text into fictional languages. Convert your boring regular text into something more interesting!

## Features

- Convert English words to fictional language equivalents
- Command-line interface with beautiful output
- Easy to extend with new translations
- Preserves text formatting and punctuation
- Case-insensitive matching

## Example

```bash
$ python -m src translate "Hello my friend, how are you?"
╭─── Translation Result ────╮
│ English: Hello my friend, how are you? │
│ Translated: henlo my fren, how r u?    │
╰──────────────────────────╯
```

## Project Structure

```
project-root/
├── src/
│   ├── __init__.py      # Package initialization
│   ├── __main__.py      # Entry point
│   ├── translator.py    # Core translation logic
│   └── cli.py          # Command-line interface
├── tests/              # Test files
└── docs/              # Documentation
```

## Quick Start

1. Clone the repository:
   ```bash
   git clone https://github.com/ristana/LanguageGenVibes.git
   cd LanguageGenVibes
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Translate text:
   ```bash
   python -m src translate "Hello friend"
   ```

2. List available translations:
   ```bash
   python -m src list-rules
   ```

## Development

- Follow PEP 8 style guide
- Add type hints to all new code
- Write tests for new features
- Update documentation as needed

## Testing

Run tests with pytest:
```bash
pytest
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Add your translations to `src/translator.py`
4. Commit your changes (`git commit -m 'Add new translations'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 