# LanguageGenVibes

A fun Python application that translates English text into fictional languages, featuring a modern GUI with dynamic background textures that change based on the selected language. Convert your boring regular text into something more interesting!

## Features

- Convert English words to fictional language equivalents
- Modern GUI interface with:
  - Real-time translation
  - Dynamic background textures for each language
  - Semi-transparent chat boxes
  - Themed buttons and controls
  - Copy and clear functionality
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

The application provides a stylish graphical interface where you can:
1. Select your desired fictional language from the dropdown
2. Watch as the background texture changes to match the selected language
3. Enter your English text in the semi-transparent input field
4. See the translation update in real-time
5. View the translation history with a themed display
6. Copy translations to clipboard or clear history as needed

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
├── assets/            # Graphical assets
│   ├── CyberneticBinary.png
│   ├── DwarvishRunic.png
│   ├── AlienInsectoid.png
│   ├── EtherealCelestial.png
│   ├── NecroticUndead.png
│   └── icon.ico
├── tests/            # Test files
│   └── test_languages.py  # Comprehensive test suite
└── README.md        # This file
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
6. Add a background texture in `assets/` (optional)

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
        # Apply consonant mappings
        for eng, my_list in self.consonant_mappings.items():
            result = result.replace(eng, random.choice(my_list))
        # Apply vowel mappings
        for eng, my_list in self.vowel_mappings.items():
            result = result.replace(eng, random.choice(my_list))
        # Add prefix and suffix
        if result:
            result = random.choice(self.prefixes) + result + random.choice(self.suffixes)
        return result

    def reverse_transform(self, text: str) -> str:
        """Transform back to English."""
        result = text.lower()
        # Remove prefixes and suffixes
        for prefix in self.prefixes:
            if result.startswith(prefix):
                result = result[len(prefix):]
        for suffix in self.suffixes:
            if result.endswith(suffix):
                result = result[:-len(suffix)]
        # Reverse consonant mappings
        for eng, my_list in self.consonant_mappings.items():
            for my in my_list:
                result = result.replace(my, eng)
        # Reverse vowel mappings
        for eng, my_list in self.vowel_mappings.items():
            for my in my_list:
                result = result.replace(my, eng)
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

### Styling

The application uses a themed UI with:
- Dynamic background textures for each language
- Semi-transparent chat boxes (rgba(128, 128, 128, 180))
- Light grey buttons and dropdown (#D3D3D3)
- White text for better contrast
- Rounded corners and borders
- Hover and pressed states for buttons

To add styling for a new language:
1. Add a background texture to `assets/`
2. Update the texture mapping in `gui.py`
3. Ensure the texture scales well at different resolutions

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

## Building the Executable

You can run the application in two modes:

### Development Mode
Run the application directly with Python for development and debugging:
```bash
python -m src
```

This mode provides:
- Real-time error messages
- Easy debugging
- Quick testing of changes
- Access to all development tools

### Executable Mode
Create a standalone executable for distribution:

1. Ensure all dependencies are installed:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the build script:
   ```bash
   python build.py
   ```

3. Find the executable in the `dist` directory:
   - Windows: `dist/FictionalTranslator.exe`
   - macOS: `dist/FictionalTranslator`
   - Linux: `dist/FictionalTranslator`

The executable includes:
- All required dependencies
- Background textures and assets
- Full GUI functionality
- No Python installation required

Notes:
- The executable is a single file that can be shared with users
- Background textures will work correctly from the executable
- Tests can still be run normally using `pytest tests/`
- Development mode remains fully functional after building

## License

This project is licensed under the MIT License - see the LICENSE file for details. 