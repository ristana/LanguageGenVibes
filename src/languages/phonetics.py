"""
Phonetic transformation utilities for language conversion.
"""
import re
from typing import Dict, List, Optional, Tuple
import string

import epitran

from .vybix import (EXAMPLE_WORDS, LETTER_COMBINATIONS, NUMBERS,
                   PHONETIC_MAPPING, SPECIAL_RULES, VOWEL_HARMONY_EXAMPLES, WORD_ENDINGS)


class PhoneticTransformer:
    """Handles phonetic transformations between languages."""

    def __init__(self):
        """Initialize the transformer."""
        try:
            self.epi = epitran.Epitran('eng-Latn')
        except:
            # Fallback if epitran fails to load
            self.epi = None
            print("Warning: IPA conversion not available")

        # Print loaded rules for debugging
        print("Loaded rules:")
        print(f"Letter combinations: {len(LETTER_COMBINATIONS)}")
        print(f"Word endings: {len(WORD_ENDINGS)}")
        print(f"Modern substitutions: {len(SPECIAL_RULES['modern_substitutions'])}")
        print(f"Example modern substitutions: {list(SPECIAL_RULES['modern_substitutions'].items())[:5]}")

        # Compile regex patterns for efficiency
        self.letter_pattern = self._compile_patterns(LETTER_COMBINATIONS)
        self.ending_pattern = self._compile_patterns(WORD_ENDINGS, is_suffix=True)
        self.number_pattern = re.compile(r'\d')
        
        # Compile patterns for special rules
        self.modern_pattern = self._compile_patterns(
            SPECIAL_RULES["modern_substitutions"], 
            is_word=True
        )
        self.emoji_pattern = self._compile_patterns(
            SPECIAL_RULES["emoji_text"]
        )
        self.emphasis_pattern = self._compile_patterns(
            SPECIAL_RULES["emphasis"],
            is_word=True
        )

    def _compile_patterns(
        self, 
        mapping: Dict[str, str], 
        is_suffix: bool = False,
        is_word: bool = False
    ) -> re.Pattern:
        """Compile regex patterns for transformations.
        
        Args:
            mapping: Dictionary of patterns to replacements
            is_suffix: Whether patterns should match at end of words
            is_word: Whether patterns should match whole words
            
        Returns:
            Compiled regex pattern
        """
        # Sort combinations by length (longest first) to avoid partial matches
        sorted_combinations = sorted(
            mapping.items(), 
            key=lambda x: len(x[0]), 
            reverse=True
        )
        
        # Create pattern string
        patterns = []
        for k, _ in sorted_combinations:
            pattern = re.escape(k)
            if is_suffix:
                pattern += '$'
            if is_word:
                pattern = fr'\b{pattern}\b'
            patterns.append(pattern)
            
        return re.compile('|'.join(patterns))

    def english_to_ipa(self, text: str) -> str:
        """Convert English text to IPA.
        
        Args:
            text: English text
            
        Returns:
            IPA representation
        """
        if self.epi is None:
            return "IPA not available"
        try:
            return self.epi.transliterate(text)
        except:
            return "IPA conversion failed"

    def ipa_to_vybix(self, ipa: str) -> str:
        """Convert IPA notation to Vybix script.
        
        Args:
            ipa: IPA text to convert
            
        Returns:
            Vybix representation of the text
        """
        result = ipa
        
        # Apply phonetic mappings
        for _, ipa_sound, vybix_sound in PHONETIC_MAPPING:
            result = result.replace(ipa_sound, vybix_sound)
            
        return result

    def apply_letter_combinations(self, text: str) -> str:
        """Apply Vybix letter combination rules.
        
        Args:
            text: Text to transform
            
        Returns:
            Text with letter combinations applied
        """
        return self.letter_pattern.sub(
            lambda m: LETTER_COMBINATIONS[m.group(0)],
            text
        )

    def apply_word_endings(self, text: str) -> str:
        """Apply Vybix word ending rules.
        
        Args:
            text: Text to transform
            
        Returns:
            Text with word endings applied
        """
        return self.ending_pattern.sub(
            lambda m: WORD_ENDINGS[m.group(0)],
            text
        )

    def apply_number_substitution(self, text: str) -> str:
        """Apply Vybix number substitution rules.
        
        Args:
            text: Text to transform
            
        Returns:
            Text with numbers transformed
        """
        return self.number_pattern.sub(
            lambda m: NUMBERS[m.group(0)],
            text
        )

    def apply_modern_substitutions(self, text: str) -> str:
        """Apply modern internet-speak substitutions.
        
        Args:
            text: Text to transform
            
        Returns:
            Text with modern substitutions applied
        """
        return self.modern_pattern.sub(
            lambda m: SPECIAL_RULES["modern_substitutions"][m.group(0)],
            text
        )

    def apply_emoji_substitutions(self, text: str) -> str:
        """Apply emoji text substitutions.
        
        Args:
            text: Text to transform
            
        Returns:
            Text with emoji substitutions applied
        """
        return self.emoji_pattern.sub(
            lambda m: SPECIAL_RULES["emoji_text"][m.group(0)],
            text
        )

    def apply_emphasis(self, text: str) -> str:
        """Apply emphasis word substitutions.
        
        Args:
            text: Text to transform
            
        Returns:
            Text with emphasis substitutions applied
        """
        return self.emphasis_pattern.sub(
            lambda m: SPECIAL_RULES["emphasis"][m.group(0)],
            text
        )

    def _get_vowel_group(self, vowel: str) -> Optional[str]:
        """Determine which vowel group a vowel belongs to.
        
        Args:
            vowel: The vowel to check
            
        Returns:
            The vowel group name or None if not found
        """
        vowel_groups = SPECIAL_RULES["vowel_harmony"]["groups"]
        for group_name, vowels in vowel_groups.items():
            if vowel in vowels:
                return group_name
        return None

    def _get_last_vowel(self, word: str) -> Optional[str]:
        """Find the last vowel in a word.
        
        Args:
            word: The word to check
            
        Returns:
            The last vowel found or None if no vowels
        """
        all_vowels = []
        for group in SPECIAL_RULES["vowel_harmony"]["groups"].values():
            all_vowels.extend(group)
            
        # Find all vowels in word
        vowels = [c for c in word if c in all_vowels]
        return vowels[-1] if vowels else None

    def apply_vowel_harmony(self, text: str) -> str:
        """Apply Vybix vowel harmony rules.
        
        Args:
            text: Text to transform
            
        Returns:
            Text with vowel harmony applied
        """
        words = text.split()
        result = []
        
        for word in words:
            # Check if word is in exceptions list
            if word in SPECIAL_RULES["vowel_harmony"]["exceptions"]:
                result.append(word)
                continue
                
            # Get the last vowel and its group
            last_vowel = self._get_last_vowel(word)
            if not last_vowel:
                result.append(word)
                continue
                
            vowel_group = self._get_vowel_group(last_vowel)
            if not vowel_group or vowel_group == "neutral":
                result.append(word)
                continue
            
            # Apply transformations based on vowel group
            transformed = word
            if vowel_group in ["front", "back"]:
                transformations = SPECIAL_RULES["vowel_harmony"]["transformations"][vowel_group]
                for vowel, replacement in transformations.items():
                    transformed = re.sub(f"({vowel})(?![aeiouyw])", replacement, transformed)
            
            # Apply suffix harmony if word ends with a known suffix
            suffix_harmony = SPECIAL_RULES["vowel_harmony"]["suffix_harmony"]
            for suffix, harmony in suffix_harmony.items():
                if transformed.endswith(suffix):
                    transformed = transformed[:-len(suffix)] + harmony[vowel_group]
            
            result.append(transformed)
        
        return " ".join(result)

    def apply_special_rules(self, text: str) -> str:
        """Apply Vybix-specific special rules.
        
        Args:
            text: Text to transform
            
        Returns:
            Text with special rules applied
        """
        words = text.split()
        result = []
        
        for word in words:
            # Drop final consonants if in the list
            for cons in SPECIAL_RULES["final_consonants_dropped"]:
                if word.endswith(cons):
                    word = word[:-1]
                    break
            
            # Handle double letters
            for letter in SPECIAL_RULES["double_letter_allowed"]:
                if letter * 2 in word:
                    # Keep the double letter
                    pass
                else:
                    # Remove other doubled consonants
                    word = re.sub(r'([^' + ''.join(SPECIAL_RULES["double_letter_allowed"]) + r'])\1+', r'\1', word)
            
            # Apply vowel harmony (simplified)
            result.append(word)
        
        return " ".join(result)

    def transform(self, text: str) -> str:
        """Transform English text into Vybix."""
        if not text:
            return text

        print("Loaded rules:")
        print(f"Letter combinations: {len(LETTER_COMBINATIONS)}")
        print(f"Word endings: {len(WORD_ENDINGS)}")
        print(f"Modern substitutions: {len(SPECIAL_RULES['modern_substitutions'])}")
        print(f"Example modern substitutions: {list(SPECIAL_RULES['modern_substitutions'].items())[:5]}\n")

        # Split text into words while preserving punctuation
        words = text.split()
        transformed_words = []

        for word in words:
            print(f"\nProcessing word: {word}")
            # Store punctuation to reattach later
            punctuation = ''
            while word and word[-1] in string.punctuation:
                punctuation = word[-1] + punctuation
                word = word[:-1]

            # Apply transformations
            transformed = word.lower()

            # Check for modern substitutions first
            if transformed in SPECIAL_RULES["modern_substitutions"]:
                transformed = SPECIAL_RULES["modern_substitutions"][transformed]
                print(f"Found modern substitution: {word} -> {transformed}")
            else:
                # Apply letter combinations
                for old, new in LETTER_COMBINATIONS.items():
                    if old in transformed:
                        transformed = transformed.replace(old, new)
                        print(f"Applied letter combination: {old} -> {new}")

                # Apply word endings
                for ending, replacement in WORD_ENDINGS.items():
                    if transformed.endswith(ending):
                        transformed = transformed[:-len(ending)] + replacement
                        print(f"Applied word ending: {ending} -> {replacement}")

                # Apply special rules
                for pattern, replacement in SPECIAL_RULES.items():
                    if pattern != "modern_substitutions":  # Skip modern_substitutions as we handled it earlier
                        if pattern in transformed:
                            transformed = transformed.replace(pattern, replacement)
                            print(f"Applied special rules: {word} -> {transformed}")

            # Reattach punctuation
            transformed = transformed + punctuation
            print(f"Final result: {word}{punctuation} -> {transformed}")
            transformed_words.append(transformed)

        # Join words back together
        result = ' '.join(transformed_words)
        print(f"\nFinal translation: {text} -> {result}\n")
        return result


def get_example_transformations() -> List[Tuple[str, str, str]]:
    """Get example transformations for testing and demonstration.
    
    Returns:
        List of tuples (english, ipa, vybix) and vowel harmony examples
    """
    transformer = PhoneticTransformer()
    examples = []
    
    # Regular examples
    for eng, (ipa, vyb) in EXAMPLE_WORDS.items():
        examples.append((eng, ipa, transformer.transform(eng)))
    
    # Add vowel harmony examples
    for eng, vyb in VOWEL_HARMONY_EXAMPLES.items():
        transformed = transformer.transform(eng)
        examples.append((eng, "N/A", transformed))
    
    return examples 