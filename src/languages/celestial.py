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
            'b': ['♭', '♮', '♯'],
            'c': ['☽', '☾', '☪'],
            'd': ['♈', '♉', '♊'],
            'f': ['♋', '♌', '♍'],
            'g': ['♎', '♏', '♐'],
            'h': ['♑', '♒', '♓'],
            'j': ['☉', '☼', '☀'],
            'k': ['⚡', '⚢', '⚣'],
            'm': ['⚧', '⚨', '⚩'],
            'p': ['⚭', '⚮', '⚯'],
            'q': ['⚰', '⚱', '⚲'],
            'w': ['⚿', '⛀', '⛁'],
            'x': ['⛂', '⛃', '⛄'],
            'y': ['⛅', '⛆', '⛇'],
            'z': ['⛈', '⛉', '⛊'],
        }

        # Celestial vowel mappings with gentle curves
        self.vowel_mappings = {
            'a': ['☉', '☼', '☀'],
            'e': ['☽', '☾', '☪'],
            'i': ['⚡', '⚢', '⚣'],
            'o': ['⚤', '⚥', '⚦'],
            'u': ['⚧', '⚨', '⚩'],
        }

        # Celestial prefixes with divine patterns
        self.prefixes = [
            '☉', '☽', '⚡', '⚤',
            '☼', '☾', '⚢', '⚥',
            '☀', '☪', '⚣', '⚦'
        ]

        # Celestial suffixes with harmonious endings
        self.suffixes = [
            '☉', '☽', '⚡', '⚤',
            '☼', '☾', '⚢', '⚥',
            '☀', '☪', '⚣', '⚦'
        ]

        # Celestial word separators
        self.word_symbols = [
            '❀', '❁', '✿', '❃',
            '❅', '❆', '❉', '❊'
        ]

    def transform(self, text: str) -> str:
        """Transform text into Celestial."""
        result = text.lower()
        
        # Apply consonant mappings
        for eng, cel in self.consonant_mappings.items():
            result = result.replace(eng, random.choice(cel))
            
        # Apply vowel mappings
        for eng, cel in self.vowel_mappings.items():
            result = result.replace(eng, random.choice(cel))
            
        # Add random prefix and suffix
        if result:
            result = random.choice(self.prefixes) + result + random.choice(self.suffixes)
            
        return result

    def reverse_transform(self, text: str) -> str:
        """Transform Celestial text back to English."""
        result = text.lower()
        
        # Remove prefixes and suffixes
        for prefix in self.prefixes:
            if result.startswith(prefix):
                result = result[len(prefix):]
        for suffix in self.suffixes:
            if result.endswith(suffix):
                result = result[:-len(suffix)]
                
        # Reverse consonant mappings
        for eng, cel_list in self.consonant_mappings.items():
            for cel in cel_list:
                result = result.replace(cel, eng)
                
        # Reverse vowel mappings
        for eng, cel_list in self.vowel_mappings.items():
            for cel in cel_list:
                result = result.replace(cel, eng)
                
        return result 