"""
Alien Insectoid language transformer.

This module implements a transformer that converts English text into an insectoid alien language.
The language features chittering and clicking patterns with segmented characters.
"""

import random
from typing import Dict, List, Optional
from .base import BaseTransformer

class InsectoidTransformer(BaseTransformer):
    """Implements the Insectoid language transformation."""

    def __init__(self):
        """Initialize the Insectoid transformer."""
        # Consonant mappings with chittering patterns
        self.consonant_mappings = {
            'b': 'bzz',
            'c': 'czz',
            'd': 'dzz',
            'f': 'fzz',
            'g': 'gzz',
            'h': 'hzz',
            'j': 'jzz',
            'k': 'kzz',
            'l': 'lzz',
            'm': 'mzz',
            'n': 'nzz',
            'p': 'pzz',
            'q': 'qzz',
            'r': 'rzz',
            's': 'szz',
            't': 'tzz',
            'v': 'vzz',
            'w': 'wzz',
            'x': 'xzz',
            'y': 'yzz',
            'z': 'zzz',
        }

        # Vowel mappings with clicking patterns
        self.vowel_mappings = {
            'a': 'akk',
            'e': 'ekk',
            'i': 'ikk',
            'o': 'okk',
            'u': 'ukk',
        }

        # Special digraph mappings
        self.digraph_mappings = {
            'th': 'thkk',
            'ch': 'chkk',
            'sh': 'shkk',
            'ph': 'phkk',
            'wh': 'whkk',
            'qu': 'qukk',
        }

        # Add uppercase mappings
        self.consonant_mappings.update({k.upper(): v.upper() for k, v in self.consonant_mappings.items()})
        self.vowel_mappings.update({k.upper(): v.upper() for k, v in self.vowel_mappings.items()})
        self.digraph_mappings.update({k.upper(): v.upper() for k, v in self.digraph_mappings.items()})

    def transform(self, text: str) -> str:
        """Transform text into Insectoid.
        
        Args:
            text: The input text to transform.
            
        Returns:
            The transformed text in Insectoid language.
        """
        if not text:
            return ""
            
        result = []
        i = 0
        while i < len(text):
            # Try digraphs first
            matched = False
            if i < len(text) - 1:
                digraph = text[i:i+2]
                if digraph.lower() in self.digraph_mappings:
                    if digraph.isupper():
                        result.append(self.digraph_mappings[digraph.upper()])
                    else:
                        result.append(self.digraph_mappings[digraph.lower()])
                    i += 2
                    matched = True
            
            if not matched:
                char = text[i]
                if char.lower() in self.consonant_mappings:
                    if char.isupper():
                        result.append(self.consonant_mappings[char.upper()])
                    else:
                        result.append(self.consonant_mappings[char.lower()])
                elif char.lower() in self.vowel_mappings:
                    if char.isupper():
                        result.append(self.vowel_mappings[char.upper()])
                    else:
                        result.append(self.vowel_mappings[char.lower()])
                else:
                    result.append(char)
                i += 1
            
        return ''.join(result)

    def reverse_transform(self, text: str) -> str:
        """Transform Insectoid text back to English.
        
        Args:
            text: The Insectoid text to transform back.
            
        Returns:
            The original English text.
        """
        if not text:
            return ""
            
        # Create reverse mappings
        reverse_digraphs = {v: k for k, v in self.digraph_mappings.items()}
        reverse_consonants = {v: k for k, v in self.consonant_mappings.items()}
        reverse_vowels = {v: k for k, v in self.vowel_mappings.items()}
        
        # Combine all reverse mappings and sort by length for proper matching
        all_patterns = sorted(
            list(reverse_digraphs.items()) + 
            list(reverse_consonants.items()) + 
            list(reverse_vowels.items()),
            key=lambda x: len(x[0]),
            reverse=True
        )
        
        result = []
        i = 0
        while i < len(text):
            matched = False
            # Try to match patterns starting from longest
            for pattern, replacement in all_patterns:
                if text[i:].startswith(pattern):
                    result.append(replacement)
                    i += len(pattern)
                    matched = True
                    break
            
            if not matched:
                result.append(text[i])
                i += 1
            
        return ''.join(result)