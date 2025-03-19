"""
Dwarvish Runic language transformer.

This module implements a transformer that converts English text into a dwarven runic language.
The language features angular rune-like symbols and consonant-heavy patterns.
"""

import random
from typing import Dict, List, Optional
from .base import BaseTransformer

class DwarvishTransformer(BaseTransformer):
    """Implements the Dwarvish language transformation."""

    def __init__(self):
        """Initialize the Dwarvish transformer."""
        self.consonant_map = {
            'th': 'ð',
            'ch': 'ᚳ',
            'sh': 'ᛋ',
            'kh': 'ᚻ',
            'ph': 'ᚠ',
        }
        self.vowel_map = {
            'a': 'ᚪ',
            'e': 'ᛖ',
            'i': 'ᛁ',
            'o': 'ᚩ',
            'u': 'ᚢ',
        }

    def transform(self, text: str) -> str:
        """Transform text into Dwarvish."""
        result = text.lower()
        
        # Replace consonant combinations first
        for eng, dwa in self.consonant_map.items():
            result = result.replace(eng, dwa)
            
        # Then replace vowels
        for eng, dwa in self.vowel_map.items():
            result = result.replace(eng, dwa)
            
        return result

    def reverse_transform(self, text: str) -> str:
        """Transform Dwarvish text back to English."""
        result = text.lower()
        
        # Reverse consonant mappings
        for eng, dwa in self.consonant_map.items():
            result = result.replace(dwa, eng)
            
        # Reverse vowel mappings
        for eng, dwa in self.vowel_map.items():
            result = result.replace(dwa, eng)
            
        return result 