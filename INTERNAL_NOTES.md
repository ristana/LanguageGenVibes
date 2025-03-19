# Internal Development Notes

## Pre-commit Testing
Before committing any changes to the repository:
1. Run the test suite: `pytest tests/`
2. Ensure all tests pass
3. If tests fail, fix the issues before committing
4. The pre-commit hook will automatically run tests, but it's good practice to run them manually first

## Test Coverage
The test suite covers:
- All language transformers
- Various text input types
- Edge cases and special characters
- Unicode handling
- Whitespace handling
- Case sensitivity
- Empty input handling
- Repeated characters

## Running Tests
```bash
# Run all tests
pytest tests/

# Run tests with coverage report
pytest --cov=src tests/

# Run specific test file
pytest tests/test_languages.py
``` 