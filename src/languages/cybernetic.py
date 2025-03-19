"""
Cybernetic Binary language transformer.

This module implements a transformer that converts English text into a cybernetic binary language.
The language features binary and hexadecimal patterns with symbolic glyphs.
"""

import random
from typing import Dict, List, Optional
from .base import BaseTransformer

class CyberneticTransformer(BaseTransformer):
    """Implements the Cybernetic language transformation."""

    def __init__(self):
        """Initialize the Cybernetic transformer."""
        # Binary and hex mappings
        self.consonant_mappings = {
            'b': '0b01',
            'c': '0c10',
            'd': '0d11',
            'f': '0f00',
            'g': '0g01',
            'h': '0h10',
            'j': '0j11',
            'k': '0k00',
            'l': '0l01',
            'm': '0m10',
            'n': '0n11',
            'p': '0p00',
            'q': '0q01',
            'r': '0r10',
            's': '0s11',
            't': '0t00',
            'v': '0v01',
            'w': '0w10',
            'x': '0x11',
            'y': '0y00',
            'z': '0z01',
        }

        # Vowel mappings with circuit symbols
        self.vowel_mappings = {
            'a': '1a01',
            'e': '1e10',
            'i': '1i11',
            'o': '1o00',
            'u': '1u01',
        }

        # Add uppercase mappings
        self.consonant_mappings.update({k.upper(): v.upper() for k, v in self.consonant_mappings.items()})
        self.vowel_mappings.update({k.upper(): v.upper() for k, v in self.vowel_mappings.items()})

    def transform(self, text: str) -> str:
        """Transform text into Cybernetic.
        
        Args:
            text: The input text to transform.
            
        Returns:
            The transformed text in Cybernetic language.
        """
        if not text:
            return ""
            
        result = text
        
        # Apply consonant mappings
        for eng, cyb in sorted(self.consonant_mappings.items(), key=lambda x: len(x[0]), reverse=True):
            result = result.replace(eng, cyb)
            
        # Apply vowel mappings
        for eng, cyb in sorted(self.vowel_mappings.items(), key=lambda x: len(x[0]), reverse=True):
            result = result.replace(eng, cyb)
            
        return result

    def reverse_transform(self, text: str) -> str:
        """Transform Cybernetic text back to English.
        
        Args:
            text: The Cybernetic text to transform back.
            
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
        for cyb, eng in sorted(reverse_map.items(), key=lambda x: len(x[0]), reverse=True):
            result = result.replace(cyb, eng)
            
        return result 