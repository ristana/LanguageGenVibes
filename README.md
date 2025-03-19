# LanguageGenVibes

A fun Python application that translates English text into fictional languages. Convert your boring regular text into something more interesting!

## Features

- Convert English words to fictional language equivalents
- Command-line interface with beautiful output
- Easy to extend with new translations
- Preserves text formatting and punctuation
- Case-insensitive matching
- Comprehensive test suite with pre-commit hooks
- Multiple fictional languages:
  - Vybix (Modern internet slang)
  - Elvish (Elegant and flowing)
  - Lizard (Hiss-like patterns)
  - Cybernetic Binary (Futuristic binary patterns)
  - Dwarvish Runic (Angular rune-like symbols)
  - Alien Insectoid (Chittering patterns)
  - Ethereal Celestial (Flowing celestial symbols)
  - Necrotic Undead (Decayed-looking text)

## Example

```bash
$ python -m src translate "Hello my friend, how are you?" --language vybix
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
│   ├── cli.py          # Command-line interface
│   └── languages/      # Language transformers
│       ├── __init__.py
│       ├── base.py
│       ├── vybix.py
│       ├── elvish.py
│       ├── lizard.py
│       ├── cybernetic.py
│       ├── dwarven.py
│       ├── insectoid.py
│       ├── celestial.py
│       └── necrotic.py
├── tests/              # Test files
│   └── test_languages.py  # Comprehensive test suite
├── docs/              # Documentation
└── INTERNAL_NOTES.md  # Development guidelines
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

3. Install dependencies and set up pre-commit hooks:
   ```bash
   ./setup.sh  # On Windows: python setup.py
   ```

## Usage

1. Translate text:
   ```bash
   python -m src translate "Hello friend" --language vybix
   ```

2. List available languages:
   ```bash
   python -m src list-languages
   ```

## Development

- Follow PEP 8 style guide
- Add type hints to all new code
- Write tests for new features
- Update documentation as needed
- Run tests before committing changes
- See INTERNAL_NOTES.md for detailed guidelines

## Testing

The project includes a comprehensive test suite that covers:
- All language transformers
- Various text input types
- Edge cases and special characters
- Unicode handling
- Whitespace handling
- Case sensitivity
- Empty input handling
- Repeated characters

Run tests with:
```bash
# Run all tests
pytest tests/

# Run tests with coverage report
pytest --cov=src tests/

# Run specific test file
pytest tests/test_languages.py
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Add your language transformer to `src/languages/`
4. Add tests for your transformer in `tests/test_languages.py`
5. Run the test suite to ensure everything passes
6. Commit your changes (`git commit -m 'Add new language transformer'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 