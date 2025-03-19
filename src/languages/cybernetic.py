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
            'b': ['1010', '0xA', 'β'],
            'c': ['1100', '0xC', 'ψ'],
            'd': ['1101', '0xD', 'δ'],
            'f': ['1111', '0xF', 'φ'],
            'g': ['0111', '0x7', 'γ'],
            'h': ['1000', '0x8', 'η'],
            'j': ['1010', '0xA', 'θ'],
            'k': ['1011', '0xB', 'κ'],
            'l': ['1100', '0xC', 'λ'],
            'm': ['1101', '0xD', 'μ'],
            'n': ['1110', '0xE', 'ν'],
            'p': ['1111', '0xF', 'π'],
            'q': ['0001', '0x1', 'χ'],
            'r': ['0010', '0x2', 'ρ'],
            's': ['0011', '0x3', 'σ'],
            't': ['0100', '0x4', 'τ'],
            'v': ['0101', '0x5', 'υ'],
            'w': ['0110', '0x6', 'ω'],
            'x': ['0111', '0x7', 'ξ'],
            'y': ['1000', '0x8', 'ψ'],
            'z': ['1001', '0x9', 'ζ'],
        }

        # Vowel mappings with circuit symbols
        self.vowel_mappings = {
            'a': ['1010', '⚡', 'α'],
            'e': ['1110', '⚢', 'ε'],
            'i': ['1001', '⚣', 'ι'],
            'o': ['1111', '⚤', 'ο'],
            'u': ['1011', '⚥', 'υ'],
        }

        # Circuit prefixes
        self.prefixes = [
            '0x', '0b', '0o', '0d',
            '⚡', '⚢', '⚣', '⚤', '⚥',
            '⟺', '⟹', '⟸', '⟷'
        ]

        # Binary suffixes
        self.suffixes = [
            '01', '10', '11', '00',
            '0x', '0b', '0o', '0d',
            '⟺', '⟹', '⟸', '⟷'
        ]

        # Circuit symbols between words
        self.word_symbols = [
            '⟺', '⟹', '⟸', '⟷',
            '⚡', '⚢', '⚣', '⚤', '⚥',
            '0x', '0b', '0o', '0d'
        ]

    def transform(self, text: str) -> str:
        """Transform text into Cybernetic."""
        result = text.lower()
        
        # Apply consonant mappings
        for eng, cyb in self.consonant_mappings.items():
            result = result.replace(eng, random.choice(cyb))
            
        # Apply vowel mappings
        for eng, cyb in self.vowel_mappings.items():
            result = result.replace(eng, random.choice(cyb))
            
        # Add random prefix and suffix
        if result:
            result = random.choice(self.prefixes) + result + random.choice(self.suffixes)
            
        return result

    def reverse_transform(self, text: str) -> str:
        """Transform Cybernetic text back to English."""
        result = text.lower()
        
        # Remove prefixes and suffixes
        for prefix in self.prefixes:
            if result.startswith(prefix):
                result = result[len(prefix):]
        for suffix in self.suffixes:
            if result.endswith(suffix):
                result = result[:-len(suffix)]
                
        # Reverse consonant mappings
        for eng, cyb_list in self.consonant_mappings.items():
            for cyb in cyb_list:
                result = result.replace(cyb, eng)
                
        # Reverse vowel mappings
        for eng, cyb_list in self.vowel_mappings.items():
            for cyb in cyb_list:
                result = result.replace(cyb, eng)
                
        return result 