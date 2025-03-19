"""Test suite for language transformers."""

import pytest
from src.languages import LANGUAGE_TRANSFORMERS

# Test cases with different types of text
TEST_CASES = [
    "Hello world",
    "The quick brown fox jumps over the lazy dog",
    "123 numbers and special chars !@#$%^&*()",
    "Mixed case TeXt",
    "Multiple   spaces   between   words",
    "Punctuation, marks! and? other. symbols;",
    "Short text",
    "Very long text that should test the transformer's ability to handle longer strings and ensure it doesn't break with extended input",
]

@pytest.mark.parametrize("language_name,transformer_class", LANGUAGE_TRANSFORMERS.items())
@pytest.mark.parametrize("test_text", TEST_CASES)
def test_language_transformation(language_name, transformer_class, test_text):
    """Test that each language transformer can transform and reverse transform text.
    
    Args:
        language_name: Name of the language being tested
        transformer_class: The transformer class to test
        test_text: The text to transform and reverse transform
    """
    # Create transformer instance
    transformer = transformer_class()
    
    # Test forward transformation
    transformed = transformer.transform(test_text)
    assert transformed is not None, f"{language_name} transform returned None"
    assert isinstance(transformed, str), f"{language_name} transform returned non-string type"
    assert len(transformed) > 0, f"{language_name} transform returned empty string"
    
    # Test reverse transformation
    reversed_text = transformer.reverse_transform(transformed)
    assert reversed_text is not None, f"{language_name} reverse_transform returned None"
    assert isinstance(reversed_text, str), f"{language_name} reverse_transform returned non-string type"
    assert len(reversed_text) > 0, f"{language_name} reverse_transform returned empty string"

@pytest.mark.parametrize("language_name,transformer_class", LANGUAGE_TRANSFORMERS.items())
def test_language_empty_input(language_name, transformer_class):
    """Test that each language transformer handles empty input correctly.
    
    Args:
        language_name: Name of the language being tested
        transformer_class: The transformer class to test
    """
    transformer = transformer_class()
    
    # Test empty string
    empty_result = transformer.transform("")
    assert empty_result is not None, f"{language_name} transform returned None for empty input"
    assert isinstance(empty_result, str), f"{language_name} transform returned non-string type for empty input"
    
    # Test reverse transform of empty string
    empty_reversed = transformer.reverse_transform("")
    assert empty_reversed is not None, f"{language_name} reverse_transform returned None for empty input"
    assert isinstance(empty_reversed, str), f"{language_name} reverse_transform returned non-string type for empty input"

@pytest.mark.parametrize("language_name,transformer_class", LANGUAGE_TRANSFORMERS.items())
def test_language_special_characters(language_name, transformer_class):
    """Test that each language transformer handles special characters correctly.
    
    Args:
        language_name: Name of the language being tested
        transformer_class: The transformer class to test
    """
    transformer = transformer_class()
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    # Test forward transformation
    transformed = transformer.transform(special_chars)
    assert transformed is not None, f"{language_name} transform returned None for special characters"
    assert isinstance(transformed, str), f"{language_name} transform returned non-string type for special characters"
    
    # Test reverse transformation
    reversed_text = transformer.reverse_transform(transformed)
    assert reversed_text is not None, f"{language_name} reverse_transform returned None for special characters"
    assert isinstance(reversed_text, str), f"{language_name} reverse_transform returned non-string type for special characters"

@pytest.mark.parametrize("language_name,transformer_class", LANGUAGE_TRANSFORMERS.items())
def test_language_unicode_characters(language_name, transformer_class):
    """Test that each language transformer handles Unicode characters correctly.
    
    Args:
        language_name: Name of the language being tested
        transformer_class: The transformer class to test
    """
    transformer = transformer_class()
    unicode_text = "Hello 世界 and 🌍"
    
    # Test forward transformation
    transformed = transformer.transform(unicode_text)
    assert transformed is not None, f"{language_name} transform returned None for Unicode characters"
    assert isinstance(transformed, str), f"{language_name} transform returned non-string type for Unicode characters"
    
    # Test reverse transformation
    reversed_text = transformer.reverse_transform(transformed)
    assert reversed_text is not None, f"{language_name} reverse_transform returned None for Unicode characters"
    assert isinstance(reversed_text, str), f"{language_name} reverse_transform returned non-string type for Unicode characters"

@pytest.mark.parametrize("language_name,transformer_class", LANGUAGE_TRANSFORMERS.items())
def test_language_whitespace_handling(language_name, transformer_class):
    """Test that each language transformer handles whitespace correctly.
    
    Args:
        language_name: Name of the language being tested
        transformer_class: The transformer class to test
    """
    transformer = transformer_class()
    whitespace_text = "   multiple   spaces   and\nnewlines\nand\ttabs\t"
    
    # Test forward transformation
    transformed = transformer.transform(whitespace_text)
    assert transformed is not None, f"{language_name} transform returned None for whitespace"
    assert isinstance(transformed, str), f"{language_name} transform returned non-string type for whitespace"
    
    # Test reverse transformation
    reversed_text = transformer.reverse_transform(transformed)
    assert reversed_text is not None, f"{language_name} reverse_transform returned None for whitespace"
    assert isinstance(reversed_text, str), f"{language_name} reverse_transform returned non-string type for whitespace"

@pytest.mark.parametrize("language_name,transformer_class", LANGUAGE_TRANSFORMERS.items())
def test_language_case_handling(language_name, transformer_class):
    """Test that each language transformer handles case correctly.
    
    Args:
        language_name: Name of the language being tested
        transformer_class: The transformer class to test
    """
    transformer = transformer_class()
    case_text = "MiXeD cAsE tExT"
    
    # Test forward transformation
    transformed = transformer.transform(case_text)
    assert transformed is not None, f"{language_name} transform returned None for mixed case"
    assert isinstance(transformed, str), f"{language_name} transform returned non-string type for mixed case"
    
    # Test reverse transformation
    reversed_text = transformer.reverse_transform(transformed)
    assert reversed_text is not None, f"{language_name} reverse_transform returned None for mixed case"
    assert isinstance(reversed_text, str), f"{language_name} reverse_transform returned non-string type for mixed case"

@pytest.mark.parametrize("language_name,transformer_class", LANGUAGE_TRANSFORMERS.items())
def test_language_repeated_characters(language_name, transformer_class):
    """Test that each language transformer handles repeated characters correctly.
    
    Args:
        language_name: Name of the language being tested
        transformer_class: The transformer class to test
    """
    transformer = transformer_class()
    repeated_text = "aaaa bbbb cccc dddd"
    
    # Test forward transformation
    transformed = transformer.transform(repeated_text)
    assert transformed is not None, f"{language_name} transform returned None for repeated characters"
    assert isinstance(transformed, str), f"{language_name} transform returned non-string type for repeated characters"
    
    # Test reverse transformation
    reversed_text = transformer.reverse_transform(transformed)
    assert reversed_text is not None, f"{language_name} reverse_transform returned None for repeated characters"
    assert isinstance(reversed_text, str), f"{language_name} reverse_transform returned non-string type for repeated characters" 