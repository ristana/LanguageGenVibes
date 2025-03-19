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