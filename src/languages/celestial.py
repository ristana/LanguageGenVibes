"""
Ethereal Celestial language transformer.

This module implements a transformer that converts English text into an ethereal celestial language.
The language features smooth, flowing text with celestial symbols and gentle curves.
"""

import random
from typing import Dict, List, Optional
from .base import BaseTransformer

class CelestialTransformer(BaseTransformer):
    """Implements the Celestial language transformation."""

    def __init__(self):
        """Initialize the Celestial transformer."""
        # Celestial consonant mappings with flowing patterns
        self.consonant_mappings = {
            'b': '♭',
            'c': '☽',
            'd': '♈',
            'f': '♋',
            'g': '♎',
            'h': '♑',
            'j': '☉',
            'k': '⚡',
            'l': '⚤',
            'm': '⚧',
            'n': '⚪',
            'p': '⚭',
            'q': '⚰',
            'r': '⚸',
            's': '⚹',
            't': '⚺',
            'v': '⚻',
            'w': '⚿',
            'x': '⛂',
            'y': '⛅',
            'z': '⛈',
        }

        # Celestial vowel mappings with gentle curves
        self.vowel_mappings = {
            'a': '✧',
            'e': '✦',
            'i': '✥',
            'o': '✤',
            'u': '✣',
        }

        # Add uppercase mappings
        self.consonant_mappings.update({k.upper(): v.upper() for k, v in self.consonant_mappings.items()})
        self.vowel_mappings.update({k.upper(): v.upper() for k, v in self.vowel_mappings.items()})

        # Celestial word separator
        self.word_separator = '❀'

    def transform(self, text: str) -> str:
        """Transform text into Celestial.
        
        Args:
            text: The input text to transform.
            
        Returns:
            The transformed text in Celestial language.
        """
        if not text:
            return ""
            
        result = text
        
        # Apply consonant mappings
        for eng, cel in sorted(self.consonant_mappings.items(), key=lambda x: len(x[0]), reverse=True):
            result = result.replace(eng, cel)
            
        # Apply vowel mappings
        for eng, cel in sorted(self.vowel_mappings.items(), key=lambda x: len(x[0]), reverse=True):
            result = result.replace(eng, cel)
            
        return result

    def reverse_transform(self, text: str) -> str:
        """Transform Celestial text back to English.
        
        Args:
            text: The Celestial text to transform back.
            
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
        for cel, eng in sorted(reverse_map.items(), key=lambda x: len(x[0]), reverse=True):
            result = result.replace(cel, eng)
            
        return result 