"""Elvish language transformation system.

This module implements a complex phonetic transformation system for the Elvish language,
with multiple layers of transformation and encryption-like features.
"""

from typing import Dict, List, Optional
import random
from .phonetics import PhoneticTransformer

class ElvishTransformer(PhoneticTransformer):
    """Implements the Elvish language transformation system."""

    def __init__(self):
        """Initialize the Elvish transformer with complex transformation rules."""
        super().__init__()
        self._initialize_elvish_rules()

    def _initialize_elvish_rules(self) -> None:
        """Initialize complex Elvish transformation rules."""
        # Base phonetic mappings with multiple layers
        self.phonetic_mappings = {
            # Layer 1: Basic consonant transformations
            'b': ['v', 'f', 'w'],
            'c': ['k', 'ch', 'kh'],
            'd': ['dh', 'th', 'z'],
            'f': ['ph', 'v', 'w'],
            'g': ['gh', 'k', 'ng'],
            'h': ['ch', 'kh', 'h'],
            'j': ['y', 'zh', 'dj'],
            'k': ['c', 'kh', 'k'],
            'l': ['ll', 'l', 'lh'],
            'm': ['mm', 'm', 'mh'],
            'n': ['nn', 'n', 'nh'],
            'p': ['ph', 'p', 'b'],
            'q': ['kw', 'qu', 'k'],
            'r': ['rr', 'r', 'rh'],
            's': ['ss', 's', 'sh'],
            't': ['th', 't', 'd'],
            'v': ['w', 'v', 'f'],
            'w': ['v', 'w', 'u'],
            'x': ['ks', 'x', 'kh'],
            'y': ['i', 'y', 'j'],
            'z': ['zh', 'z', 's'],
            
            # Layer 2: Vowel transformations with context
            'a': ['á', 'ä', 'â'],
            'e': ['é', 'ë', 'ê'],
            'i': ['í', 'ï', 'î'],
            'o': ['ó', 'ö', 'ô'],
            'u': ['ú', 'ü', 'û'],
            
            # Layer 3: Special combinations
            'th': ['þ', 'ð', 'th'],
            'sh': ['š', 'ş', 'sh'],
            'ch': ['č', 'ç', 'ch'],
            'ng': ['ŋ', 'ng', 'n'],
            'ph': ['φ', 'ph', 'f'],
        }

        # Complex transformation rules
        self.transformation_rules = [
            # Rule 1: Consonant doubling based on position
            lambda word: self._double_consonants(word),
            
            # Rule 2: Vowel elongation in stressed syllables
            lambda word: self._elongate_vowels(word),
            
            # Rule 3: Add mystical suffixes based on word length
            lambda word: self._add_mystical_suffix(word),
            
            # Rule 4: Insert random elvish particles
            lambda word: self._insert_particles(word),
            
            # Rule 5: Transform word endings based on context
            lambda word: self._transform_endings(word),
        ]

        # Elvish particles for random insertion
        self.particles = [
            'el', 'il', 'al', 'ol', 'ul',
            'en', 'in', 'an', 'on', 'un',
            'eth', 'ith', 'ath', 'oth', 'uth'
        ]

    def _double_consonants(self, word: str) -> str:
        """Double consonants in specific positions."""
        result = list(word)
        for i in range(len(result) - 1):
            if result[i] in 'bcdfghjklmnprstvwxz' and random.random() < 0.3:
                result[i] = result[i] * 2
        return ''.join(result)

    def _elongate_vowels(self, word: str) -> str:
        """Elongate vowels in stressed syllables."""
        vowels = 'aeiou'
        result = list(word)
        for i in range(len(result)):
            if result[i] in vowels and random.random() < 0.4:
                result[i] = result[i] + '̄'
        return ''.join(result)

    def _add_mystical_suffix(self, word: str) -> str:
        """Add mystical suffixes based on word length."""
        if len(word) < 4:
            return word + random.choice(['el', 'il', 'al'])
        elif len(word) < 8:
            return word + random.choice(['eth', 'ith', 'ath'])
        else:
            return word + random.choice(['ion', 'ian', 'ien'])

    def _insert_particles(self, word: str) -> str:
        """Insert random elvish particles."""
        if random.random() < 0.3:
            particle = random.choice(self.particles)
            return word + particle
        return word

    def _transform_endings(self, word: str) -> str:
        """Transform word endings based on context."""
        endings = {
            'ing': ['ion', 'ien', 'ian'],
            'ed': ['eth', 'ith', 'ath'],
            'er': ['or', 'ar', 'ur'],
            'ly': ['li', 'lë', 'lï']
        }
        for end, replacements in endings.items():
            if word.endswith(end):
                return word[:-len(end)] + random.choice(replacements)
        return word

    def transform(self, text: str) -> str:
        """Transform text into Elvish with multiple layers of complexity."""
        # Apply base phonetic transformations
        result = super().transform(text)
        
        # Apply each transformation rule
        for rule in self.transformation_rules:
            words = result.split()
            transformed_words = [rule(word) for word in words]
            result = ' '.join(transformed_words)
        
        # Add final mystical touches
        if random.random() < 0.2:
            result = result + ' ' + random.choice(self.particles)
        
        return result

    def reverse_transform(self, text: str) -> str:
        """Reverse transform Elvish text back to English.
        
        Note: Due to the complexity of the transformation rules,
        this is an approximation and may not perfectly restore the original text.
        """
        # This is a simplified reverse transformation
        # In practice, the complex rules make perfect reversal difficult
        result = text
        for original, variants in self.phonetic_mappings.items():
            for variant in variants:
                result = result.replace(variant, original)
        return result
