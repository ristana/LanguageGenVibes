"""
Sci-fi lizard language transformer.

This module implements a transformer that converts English text into a sci-fi lizard language.
The language features reptilian characteristics like hissing sounds and sci-fi elements.
"""

import random
from typing import Dict, List, Optional

from .base import BaseTransformer


class LizardTransformer(BaseTransformer):
    """Transforms text into a sci-fi lizard language."""

    def __init__(self):
        """Initialize the lizard language transformer."""
        super().__init__()
        self._setup_transformations()

    def _setup_transformations(self) -> None:
        """Set up the transformation rules for the lizard language."""
        # Reptilian consonant mappings
        self.consonant_mappings = {
            's': ['ss', 'sz', 'zz', 'z'],
            'z': ['zz', 'sz', 'ss', 'z'],
            'f': ['ff', 'ph', 'f'],
            'v': ['vv', 'vh', 'v'],
            't': ['tt', 'th', 't'],
            'd': ['dd', 'dh', 'd'],
            'k': ['kk', 'kh', 'k'],
            'g': ['gg', 'gh', 'g'],
            'p': ['pp', 'ph', 'p'],
            'b': ['bb', 'bh', 'b'],
            'm': ['mm', 'mh', 'm'],
            'n': ['nn', 'nh', 'n'],
            'l': ['ll', 'lh', 'l'],
            'r': ['rr', 'rh', 'r'],
            'h': ['hh', 'h'],
            'w': ['ww', 'wh', 'w'],
            'y': ['yy', 'yh', 'y'],
            'x': ['xx', 'ks', 'x'],
            'c': ['kk', 'kh', 'k'],
            'q': ['kk', 'kh', 'k'],
        }

        # Sci-fi vowel mappings
        self.vowel_mappings = {
            'a': ['aa', 'ae', 'ai'],
            'e': ['ee', 'ei', 'ey'],
            'i': ['ii', 'iy', 'ie'],
            'o': ['oo', 'ou', 'ow'],
            'u': ['uu', 'uw', 'ue'],
        }

        # Sci-fi prefixes and suffixes
        self.prefixes = [
            'Zz', 'Ss', 'Kk', 'Xx', 'Vv', 'Qq', 'Rr', 'Tt',
            'Zzss', 'Sszz', 'Kkxx', 'Xxkk', 'Vvqq', 'Qqvv', 'Rrtt', 'Ttrr'
        ]
        self.suffixes = [
            'ss', 'zz', 'xx', 'kk', 'qq', 'tt', 'rr', 'hh',
            'sszz', 'zzss', 'xxkk', 'kkxx', 'qqvv', 'vvqq', 'ttrr', 'rrtt'
        ]

        # Sci-fi symbols between words (using simple separators)
        self.word_symbols = ['--', '~~', '.:', ':.', '-~-', '~-~', '::', '..']

        # Reptilian particles
        self.particles = ['ss', 'zz', 'xx', 'kk', 'qq', 'tt', 'rr', 'hh']

    def transform(self, text: str) -> str:
        """Transform English text into lizard language.

        Args:
            text: The English text to transform.

        Returns:
            The transformed lizard language text.
        """
        # Split text into words
        words = text.split()
        transformed_words = []

        for i, word in enumerate(words):
            # Add random prefix
            prefix = random.choice(self.prefixes)
            
            # Transform consonants and vowels
            transformed = ''
            for char in word.lower():
                if char in self.consonant_mappings:
                    transformed += random.choice(self.consonant_mappings[char])
                elif char in self.vowel_mappings:
                    transformed += random.choice(self.vowel_mappings[char])
                else:
                    transformed += char

            # Add random suffix
            suffix = random.choice(self.suffixes)
            transformed_word = f"{prefix}{transformed}{suffix}"

            # Add word symbol if not the last word
            if i < len(words) - 1:
                transformed_word += random.choice(self.word_symbols)

            transformed_words.append(transformed_word)

        # Add random particles at the end
        num_particles = random.randint(1, 3)
        particles = [random.choice(self.particles) for _ in range(num_particles)]
        
        return ' '.join(transformed_words + particles)

    def reverse_transform(self, text: str) -> str:
        """Attempt to reverse transform lizard language text back to English.

        Note: This is an approximate reverse transformation due to the complexity
        of the transformations.

        Args:
            text: The lizard language text to reverse transform.

        Returns:
            An approximate English text.
        """
        # Remove prefixes, suffixes, and particles
        words = text.split()
        cleaned_words = []
        
        for word in words:
            # Remove prefix (first 2-4 characters)
            word = word[2:] if len(word) > 2 else word
            
            # Remove suffix (last 2-4 characters)
            word = word[:-2] if len(word) > 2 else word
            
            # Remove sci-fi symbols
            for symbol in self.word_symbols:
                word = word.replace(symbol, '')
            
            cleaned_words.append(word)
        
        # Remove particles at the end
        while cleaned_words and cleaned_words[-1] in self.particles:
            cleaned_words.pop()
        
        return ' '.join(cleaned_words) 