# Technical Documentation

## Project Overview
This project is built using Python with a focus on maintainability, scalability, and clean code practices. It implements a modular system for transforming text into various fictional languages.

## Technology Stack
- **Language:** Python 3.9+
- **Testing:** 
  - pytest (test framework)
  - pytest-cov (coverage reporting)
  - pre-commit (git hooks)
- **Code Quality:** 
  - Black (formatting)
  - flake8 (linting)
  - mypy (type checking)
- **Documentation:** Sphinx

## Project Structure
```
src/
├── __init__.py      # Package initialization
├── __main__.py      # Entry point
├── translator.py    # Core translation logic
├── cli.py          # Command-line interface
└── languages/      # Language transformers
    ├── __init__.py
    ├── base.py     # Base transformer class
    ├── vybix.py    # Modern internet slang
    ├── elvish.py   # Elegant and flowing
    ├── lizard.py   # Hiss-like patterns
    ├── cybernetic.py  # Futuristic binary
    ├── dwarven.py  # Angular rune-like
    ├── insectoid.py   # Chittering patterns
    ├── celestial.py   # Flowing celestial
    └── necrotic.py    # Decayed-looking text

tests/
└── test_languages.py  # Comprehensive test suite
```

## Setup Instructions
1. Create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
2. Install dependencies and set up pre-commit hooks:
   ```bash
   ./setup.sh  # On Windows: python setup.py
   ```

## Development Guidelines
- Follow PEP 8 style guide
- Use type hints
- Write unit tests for new features
- Document functions using Google style docstrings
- Run tests before committing changes
- See INTERNAL_NOTES.md for detailed guidelines

## Language Transformer Architecture
Each language transformer:
- Inherits from BaseTransformer
- Implements transform() and reverse_transform() methods
- Defines unique mappings for consonants and vowels
- Includes language-specific prefixes, suffixes, and particles
- Handles special characters and formatting

## Testing Strategy
The project uses a comprehensive test suite that covers:
- All language transformers
- Various text input types
- Edge cases and special characters
- Unicode handling
- Whitespace handling
- Case sensitivity
- Empty input handling
- Repeated characters

Test commands:
```bash
# Run all tests
pytest tests/

# Run tests with coverage report
pytest --cov=src tests/

# Run specific test file
pytest tests/test_languages.py
```

## Pre-commit Hooks
- Automatically runs tests before each commit
- Prevents commits if tests fail
- Ensures code quality and consistency

## Error Handling
- Custom exceptions for transformation errors
- Proper handling of invalid input
- Graceful fallbacks for unsupported characters
- Detailed error messages for debugging

## Performance Considerations
- Efficient string manipulation
- Caching of transformation rules
- Optimized regex patterns
- Memory-efficient processing of large texts 

## Translation System

### Core Components

1. **Translator Class**
- Main interface for translation operations
- Manages language transformer instances
- Provides both forward and reverse translation capabilities
- Thread-safe implementation

2. **BaseTransformer Class**
- Abstract base class for all language transformers
- Defines required interface methods:
  - `transform(text: str) -> str`
  - `reverse_transform(text: str) -> str`
- Provides common utility methods

3. **Language Transformers**
Each language transformer implements:
- Character mappings (consonants, vowels)
- Special character handling
- Bidirectional translation logic
- Language-specific formatting

### Translation Process

1. **Forward Translation (English to Fictional)**
```python
def translate(self, text: str, language: str) -> str:
    """
    1. Validate language selection
    2. Get appropriate transformer
    3. Apply transformation rules
    4. Return translated text
    """
```

2. **Reverse Translation (Fictional to English)**
```python
def reverse_translate(self, text: str, language: str) -> str:
    """
    1. Validate language selection
    2. Get appropriate transformer
    3. Apply reverse transformation rules
    4. Return original English text
    """
```

## GUI System

### Components

1. **Main Window**
- Language selection dropdown with custom styling
- Dynamic background textures
- Semi-transparent input/output areas
- Translation history display

2. **Controls**
- Translate button
- Untranslate button
- Copy history button
- Clear button

3. **Asset Management**
- Background textures for each language
- Custom dropdown arrow
- Application icon

### Event Handling

1. **Translation Events**
- Real-time input validation
- Error handling and user feedback
- History management
- Background updates

2. **UI Updates**
- Dynamic texture loading
- Theme consistency
- Responsive layout

## Build System

### Development Build
- Python environment setup
- Dependency management
- Test execution

### Production Build
1. **PyInstaller Configuration**
- Single-file executable
- Asset bundling
- Icon integration
- Version information

2. **Release Process**
- Version tagging
- Asset compression
- Distribution packaging

## Testing Framework

### Unit Tests
- Individual transformer tests
- Core functionality verification
- Edge case handling

### Integration Tests
- Full translation pipeline
- GUI functionality
- Asset loading

### Test Categories
1. **Translation Tests**
- Basic transformation
- Reverse transformation
- Character mapping
- Special cases

2. **GUI Tests**
- Event handling
- Asset loading
- State management

## Performance Considerations

1. **Memory Management**
- Efficient texture loading
- History size limits
- Resource cleanup

2. **Processing Optimization**
- Cached transformers
- Efficient string operations
- Background processing for long operations 