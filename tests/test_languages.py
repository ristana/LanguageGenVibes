"""Test suite for language transformers."""

import pytest
import random
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
    "Very long text that should test the transformer's ability to handle longer strings",
]

@pytest.mark.parametrize("language_name,transformer_class", LANGUAGE_TRANSFORMERS.items())
@pytest.mark.parametrize("test_text", TEST_CASES)
def test_language_transformation(language_name, transformer_class, test_text):
    """Test basic transformation and reverse transformation."""
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
    
    # Test that the reversed text matches the original (case-insensitive)
    assert reversed_text.lower() == test_text.lower(), f"{language_name} reverse_transform did not match original text"

@pytest.mark.parametrize("language_name,transformer_class", LANGUAGE_TRANSFORMERS.items())
def test_language_empty_input(language_name, transformer_class):
    """Test empty input handling."""
    transformer = transformer_class()
    
    # Test empty string
    empty_result = transformer.transform("")
    assert empty_result == "", f"{language_name} transform should return empty string for empty input"
    
    # Test reverse transform of empty string
    empty_reversed = transformer.reverse_transform("")
    assert empty_reversed == "", f"{language_name} reverse_transform should return empty string for empty input"

@pytest.mark.parametrize("language_name,transformer_class", LANGUAGE_TRANSFORMERS.items())
def test_language_special_characters(language_name, transformer_class):
    """Test special character handling."""
    transformer = transformer_class()
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    # Test forward transformation
    transformed = transformer.transform(special_chars)
    assert transformed is not None
    assert special_chars in transformed, f"{language_name} should preserve special characters"
    
    # Test reverse transformation
    reversed_text = transformer.reverse_transform(transformed)
    assert reversed_text is not None
    assert special_chars in reversed_text, f"{language_name} should preserve special characters in reverse"

@pytest.mark.parametrize("language_name,transformer_class", LANGUAGE_TRANSFORMERS.items())
def test_language_whitespace_handling(language_name, transformer_class):
    """Test whitespace preservation."""
    transformer = transformer_class()
    whitespace_text = "  Multiple  Spaces  And\tTabs\nAnd\rReturns  "
    
    # Test forward transformation
    transformed = transformer.transform(whitespace_text)
    assert len(transformed.split()) == len(whitespace_text.split()), f"{language_name} should preserve word boundaries"
    
    # Test reverse transformation
    reversed_text = transformer.reverse_transform(transformed)
    assert len(reversed_text.split()) == len(whitespace_text.split()), f"{language_name} should preserve word boundaries in reverse"

@pytest.mark.parametrize("language_name,transformer_class", LANGUAGE_TRANSFORMERS.items())
def test_language_mapping_consistency(language_name, transformer_class):
    """Test that character mappings are consistent within a single transformation."""
    transformer = transformer_class()
    test_text = "test test test"  # Same word repeated
    
    # Transform the text
    transformed = transformer.transform(test_text)
    
    # Split into words
    transformed_words = transformed.split()
    
    # If the transformer has prefixes/suffixes, remove them for comparison
    if hasattr(transformer, 'prefixes') and hasattr(transformer, 'suffixes'):
        cleaned_words = []
        for word in transformed_words:
            cleaned = word
            for prefix in transformer.prefixes:
                if cleaned.startswith(prefix):
                    cleaned = cleaned[len(prefix):]
            for suffix in transformer.suffixes:
                if cleaned.endswith(suffix):
                    cleaned = cleaned[:-len(suffix)]
            cleaned_words.append(cleaned)
        transformed_words = cleaned_words
    
    # Check that all transformed instances of the same word are identical
    assert all(word == transformed_words[0] for word in transformed_words), \
        f"{language_name} should transform the same word consistently within a single transformation"

@pytest.mark.parametrize("language_name,transformer_class", LANGUAGE_TRANSFORMERS.items())
def test_language_character_sets(language_name, transformer_class):
    """Test that all character mappings work correctly."""
    transformer = transformer_class()
    
    # Test consonants if the transformer has consonant mappings
    if hasattr(transformer, 'consonant_mappings'):
        for consonant in transformer.consonant_mappings.keys():
            transformed = transformer.transform(consonant)
            reversed_text = transformer.reverse_transform(transformed)
            assert reversed_text.lower() == consonant.lower(), \
                f"{language_name} failed to correctly transform/reverse consonant '{consonant}'"
    
    # Test vowels if the transformer has vowel mappings
    if hasattr(transformer, 'vowel_mappings'):
        for vowel in transformer.vowel_mappings.keys():
            transformed = transformer.transform(vowel)
            reversed_text = transformer.reverse_transform(transformed)
            assert reversed_text.lower() == vowel.lower(), \
                f"{language_name} failed to correctly transform/reverse vowel '{vowel}'"

@pytest.mark.parametrize("language_name,transformer_class", LANGUAGE_TRANSFORMERS.items())
def test_language_prefix_suffix(language_name, transformer_class):
    """Test prefix and suffix handling."""
    transformer = transformer_class()
    test_text = "test"
    
    # Only run this test if the transformer has prefixes and suffixes
    if hasattr(transformer, 'prefixes') and hasattr(transformer, 'suffixes'):
        transformed = transformer.transform(test_text)
        
        # Check that either a prefix or suffix is present
        has_prefix = any(transformed.startswith(prefix) for prefix in transformer.prefixes)
        has_suffix = any(transformed.endswith(suffix) for suffix in transformer.suffixes)
        
        assert has_prefix or has_suffix, \
            f"{language_name} should add either a prefix or suffix to transformed text"
        
        # Test reverse transformation
        reversed_text = transformer.reverse_transform(transformed)
        assert reversed_text.lower() == test_text.lower(), \
            f"{language_name} should correctly handle prefixes and suffixes in reverse transformation"

@pytest.mark.parametrize("language_name,transformer_class", LANGUAGE_TRANSFORMERS.items())
def test_language_random_elements(language_name, transformer_class):
    """Test that random elements (if any) don't break reversibility."""
    transformer = transformer_class()
    test_text = "test"
    
    # Transform the same text multiple times
    results = [transformer.transform(test_text) for _ in range(5)]
    
    # Results might be different due to random choice
    all_same = all(result == results[0] for result in results)
    if not all_same:
        # If results are different (random elements used), ensure they all reverse correctly
        for transformed in results:
            reversed_text = transformer.reverse_transform(transformed)
            assert reversed_text.lower() == test_text.lower(), \
                f"{language_name} random elements broke reversibility" 