# Design Principles

## Code Structure
- Use modular design with clear separation of concerns
- Follow the Single Responsibility Principle
- Implement dependency injection where appropriate
- Keep functions small and focused

## Naming Conventions
- Classes: PascalCase (e.g., `UserService`)
- Functions/Methods: snake_case (e.g., `get_user_by_id`)
- Variables: snake_case (e.g., `user_count`)
- Constants: UPPER_SNAKE_CASE (e.g., `MAX_CONNECTIONS`)

## Documentation
- Use Google-style docstrings
- Include type hints for all function parameters and return values
- Document exceptions that may be raised
- Add inline comments for complex logic

## Error Handling
```python
# Example error handling pattern
try:
    result = operation()
except SpecificError as e:
    logger.error(f"Operation failed: {str(e)}")
    raise CustomError("Friendly error message") from e
```

## Logging
```python
# Example logging pattern
import logging

logger = logging.getLogger(__name__)

def some_function():
    logger.info("Starting operation")
    try:
        # operation
        logger.debug("Operation details")
    except Exception as e:
        logger.error("Operation failed", exc_info=True)
```

## Testing
- Write unit tests for all business logic
- Use pytest fixtures for test setup
- Mock external dependencies
- Aim for high test coverage

## API Design
- Use RESTful principles
- Version your APIs
- Use consistent response formats
- Handle errors gracefully with proper status codes 