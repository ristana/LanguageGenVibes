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
        self.sound_map = {
            'a': 'zzt',
            'e': 'bzz',
            'i': 'tzz',
            'o': 'zzk',
            'u': 'kzz',
            'th': 'chkt',
            'ch': 'tzzk',
            'sh': 'szzk',
            'ph': 'fzzt',
        }

    def transform(self, text: str) -> str:
        """Transform text into Insectoid."""
        result = text.lower()
        for eng, ins in self.sound_map.items():
            result = result.replace(eng, ins)
        return result

    def reverse_transform(self, text: str) -> str:
        """Transform Insectoid text back to English."""
        result = text.lower()
        for eng, ins in self.sound_map.items():
            result = result.replace(ins, eng)
        return result 