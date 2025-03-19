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
            'b': ['ɓ', 'ɓ̥', 'ɓ̬'],
            'c': ['ç', 'ç̥', 'ç̬'],
            'd': ['ɗ', 'ɗ̥', 'ɗ̬'],
            'f': ['ɸ', 'ɸ̥', 'ɸ̬'],
            'g': ['ɠ', 'ɠ̥', 'ɠ̬'],
            'h': ['ɦ', 'ɦ̥', 'ɦ̬'],
            'j': ['ʝ', 'ʝ̥', 'ʝ̬'],
            'k': ['ʞ', 'ʞ̥', 'ʞ̬'],
            'l': ['ɬ', 'ɬ̥', 'ɬ̬'],
            'm': ['ɱ', 'ɱ̥', 'ɱ̬'],
            'n': ['ɳ', 'ɳ̥', 'ɳ̬'],
            'p': ['ɸ', 'ɸ̥', 'ɸ̬'],
            'q': ['ʠ', 'ʠ̥', 'ʠ̬'],
            'r': ['ɽ', 'ɽ̥', 'ɽ̬'],
            's': ['ʂ', 'ʂ̥', 'ʂ̬'],
            't': ['ʈ', 'ʈ̥', 'ʈ̬'],
            'v': ['ʋ', 'ʋ̥', 'ʋ̬'],
            'w': ['ʍ', 'ʍ̥', 'ʍ̬'],
            'x': ['χ', 'χ̥', 'χ̬'],
            'y': ['ʎ', 'ʎ̥', 'ʎ̬'],
            'z': ['ʐ', 'ʐ̥', 'ʐ̬'],
        }

        # Necrotic vowel mappings with elongated patterns
        self.vowel_mappings = {
            'a': ['ɑ', 'ɑ̥', 'ɑ̬'],
            'e': ['ɘ', 'ɘ̥', 'ɘ̬'],
            'i': ['ɨ', 'ɨ̥', 'ɨ̬'],
            'o': ['ɤ', 'ɤ̥', 'ɤ̬'],
            'u': ['ʉ', 'ʉ̥', 'ʉ̬'],
        }

        # Necrotic prefixes with decayed patterns
        self.prefixes = [
            'ɓ̥', 'ɗ̥', 'ɠ̥', 'ʞ̥',
            'ɬ̥', 'ɱ̥', 'ɳ̥', 'ɸ̥',
            'ʠ̥', 'ɽ̥', 'ʂ̥', 'ʈ̥'
        ]

        # Necrotic suffixes with decayed patterns
        self.suffixes = [
            'ɓ̥', 'ɗ̥', 'ɠ̥', 'ʞ̥',
            'ɬ̥', 'ɱ̥', 'ɳ̥', 'ɸ̥',
            'ʠ̥', 'ɽ̥', 'ʂ̥', 'ʈ̥'
        ]

        # Necrotic word separators
        self.word_symbols = [
            '̥', '̬', '̩', '̯',
        ]

    def transform(self, text: str) -> str:
        """Transform text into Necrotic."""
        result = text.lower()
        
        # Apply consonant mappings
        for eng, nec in self.consonant_mappings.items():
            result = result.replace(eng, random.choice(nec))
            
        # Apply vowel mappings
        for eng, nec in self.vowel_mappings.items():
            result = result.replace(eng, random.choice(nec))
            
        # Add random prefix and suffix
        if result:
            result = random.choice(self.prefixes) + result + random.choice(self.suffixes)
            
        return result

    def reverse_transform(self, text: str) -> str:
        """Transform Necrotic text back to English."""
        result = text.lower()
        
        # Remove prefixes and suffixes
        for prefix in self.prefixes:
            if result.startswith(prefix):
                result = result[len(prefix):]
        for suffix in self.suffixes:
            if result.endswith(suffix):
                result = result[:-len(suffix)]
                
        # Reverse consonant mappings
        for eng, nec_list in self.consonant_mappings.items():
            for nec in nec_list:
                result = result.replace(nec, eng)
                
        # Reverse vowel mappings
        for eng, nec_list in self.vowel_mappings.items():
            for nec in nec_list:
                result = result.replace(nec, eng)
                
        return result 