"""
Necrotic Undead language transformer.

This module implements a transformer that converts English text into a necrotic undead language.
The language features decayed-looking text with irregular symbols and dark thematic elements.
"""

import random
from typing import Dict, List, Optional
from .base import BaseTransformer

class NecroticTransformer(BaseTransformer):
    """Implements the Necrotic language transformation."""

    def __init__(self):
        """Initialize the Necrotic transformer."""
        # Necrotic consonant mappings with decayed patterns
        self.consonant_mappings = {
            'b': 'ɓ',
            'c': 'ç',
            'd': 'ɗ',
            'f': 'ɸ',
            'g': 'ɠ',
            'h': 'ɦ',
            'j': 'ʝ',
            'k': 'ʞ',
            'l': 'ɬ',
            'm': 'ɱ',
            'n': 'ɳ',
            'p': 'ƥ',
            'q': 'ʠ',
            'r': 'ɽ',
            's': 'ʂ',
            't': 'ʈ',
            'v': 'ʋ',
            'w': 'ʍ',
            'x': 'χ',
            'y': 'ʎ',
            'z': 'ʐ',
        }

        # Necrotic vowel mappings with elongated patterns
        self.vowel_mappings = {
            'a': 'ɑ',
            'e': 'ɘ',
            'i': 'ɨ',
            'o': 'ɤ',
            'u': 'ʉ',
        }

        # Add uppercase mappings
        self.consonant_mappings.update({k.upper(): v.upper() for k, v in self.consonant_mappings.items()})
        self.vowel_mappings.update({k.upper(): v.upper() for k, v in self.vowel_mappings.items()})

        # Necrotic word separator
        self.word_separator = '̥'

    def transform(self, text: str) -> str:
        """Transform text into Necrotic.
        
        Args:
            text: The input text to transform.
            
        Returns:
            The transformed text in Necrotic language.
        """
        if not text:
            return ""
            
        result = text
        
        # Apply consonant mappings
        for eng, nec in sorted(self.consonant_mappings.items(), key=lambda x: len(x[0]), reverse=True):
            result = result.replace(eng, nec)
            
        # Apply vowel mappings
        for eng, nec in sorted(self.vowel_mappings.items(), key=lambda x: len(x[0]), reverse=True):
            result = result.replace(eng, nec)
            
        return result

    def reverse_transform(self, text: str) -> str:
        """Transform Necrotic text back to English.
        
        Args:
            text: The Necrotic text to transform back.
            
        Returns:
            The original English text.
        """
        if not text:
            return ""
            
        result = text
        
        # Create reverse mappings
        reverse_consonants = {v: k for k, v in self.consonant_mappings.items()}
        reverse_vowels = {v: k for k, v in self.vowel_mappings.items()}
        
        # Combine all reverse mappings
        reverse_map = {**reverse_consonants, **reverse_vowels}
        
        # Apply reverse mappings
        for nec, eng in sorted(reverse_map.items(), key=lambda x: len(x[0]), reverse=True):
            result = result.replace(nec, eng)
            
        return result 