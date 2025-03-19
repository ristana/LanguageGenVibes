"""Test script for the Elvish language translator."""

from src.languages.elvish import ElvishTransformer

def test_elvish_translation():
    """Test the Elvish language translation system."""
    transformer = ElvishTransformer()
    
    # Test cases with different types of words
    test_cases = [
        "Hello world",
        "The quick brown fox jumps over the lazy dog",
        "Magic is everywhere in this enchanted forest",
        "Ancient wisdom flows through the elven realms",
        "Stars twinkle in the night sky"
    ]
    
    print("\n=== Testing Elvish Language Translation ===\n")
    
    for text in test_cases:
        print(f"Original: {text}")
        translated = transformer.transform(text)
        print(f"Elvish:   {translated}")
        reversed_text = transformer.reverse_transform(translated)
        print(f"Reversed: {reversed_text}")
        print("-" * 80)

if __name__ == "__main__":
    test_elvish_translation() 