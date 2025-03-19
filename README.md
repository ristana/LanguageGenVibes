# LanguageGenVibes

A fun Python application that translates English text into fictional languages. Convert your boring regular text into something more interesting!

## Features

- Convert English words to fictional language equivalents
- Modern GUI interface with real-time translation
- Easy to extend with new translations
- Preserves text formatting and punctuation
- Case-insensitive matching
- Comprehensive test suite
- Multiple fictional languages:
  - Elvish (Elegant and flowing script with accented vowels)
  - Cybernetic Binary (Futuristic binary and hex patterns with circuit symbols)
  - Dwarvish Runic (Angular rune-like symbols with Norse influence)
  - Alien Insectoid (Chittering patterns with insect-like sounds)
  - Ethereal Celestial (Flowing celestial symbols with divine patterns)
  - Necrotic Undead (Decayed-looking text with irregular symbols)

## Example Usage

The application provides a graphical interface where you can:
1. Select your desired fictional language from the dropdown
2. Enter your English text in the input field
3. See the translation update in real-time
4. View the translation history for all languages

## Project Structure

```
project-root/
├── src/
│   ├── __init__.py      # Package initialization
│   ├── __main__.py      # Entry point
│   ├── translator.py    # Core translation logic
│   ├── gui.py          # Graphical user interface
│   └── languages/      # Language transformers
│       ├── __init__.py
│       ├── base.py     # Base transformer class
│       ├── elvish.py   # Elvish language
│       ├── cybernetic.py # Cybernetic language
│       ├── dwarvish.py # Dwarvish language
│       ├── insectoid.py # Insectoid language
│       ├── celestial.py # Celestial language
│       └── necrotic.py # Necrotic language
├── tests/              # Test files
│   └── test_languages.py  # Comprehensive test suite
└── README.md          # This file
```

## Quick Start

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/LanguageGenVibes.git
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

4. Run the application:
   ```bash
   python -m src
   ```

## Development

### Adding a New Language

To add a new language transformer:

1. Create a new file in `src/languages/` (e.g., `mylanguage.py`)
2. Implement a class that inherits from `BaseTransformer`
3. Define the language's character mappings in `__init__`
4. Implement the `transform` and `reverse_transform` methods
5. Add the language to `LANGUAGE_TRANSFORMERS` in `src/languages/__init__.py`

Example:
```python
from .base import BaseTransformer

class MyLanguageTransformer(BaseTransformer):
    def __init__(self):
        """Initialize the transformer."""
        self.consonant_mappings = {...}  # Define consonant mappings
        self.vowel_mappings = {...}      # Define vowel mappings
        self.prefixes = [...]            # Optional prefixes
        self.suffixes = [...]            # Optional suffixes
        self.word_symbols = [...]        # Optional word separators

    def transform(self, text: str) -> str:
        """Transform text into your language."""
        result = text.lower()
        # Apply your transformations
        return result

    def reverse_transform(self, text: str) -> str:
        """Transform back to English."""
        result = text.lower()
        # Apply reverse transformations
        return result
```

### Testing

The project includes a comprehensive test suite that verifies:
- Basic transformation and reverse transformation
- Empty input handling
- Special character handling
- Unicode character support
- Whitespace preservation
- Case sensitivity
- Repeated character handling
- Prefix and suffix handling
- Consonant and vowel mappings

Run the tests with:
```bash
pytest tests/
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 