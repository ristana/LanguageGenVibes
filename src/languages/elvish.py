"""Elvish language transformer implementation."""
from .base import BaseTransformer


class ElvishTransformer(BaseTransformer):
    """Implements the Elvish language transformation."""

    def __init__(self):
        """Initialize the Elvish transformer."""
        self.vowel_map = {
            'a': 'á',
            'e': 'é',
            'i': 'í',
            'o': 'ó',
            'u': 'ú',
        }
        self.consonant_map = {
            'th': 'þ',
            'ch': 'ç',
            'sh': 'š',
            'ph': 'φ',
            'ng': 'ŋ',
        }

    def transform(self, text: str) -> str:
        """Transform text into Elvish."""
        result = text.lower()
        
        # Replace consonant combinations first
        for eng, elv in self.consonant_map.items():
            result = result.replace(eng, elv)
            
        # Then replace vowels
        for eng, elv in self.vowel_map.items():
            result = result.replace(eng, elv)
            
        return result

    def reverse_transform(self, text: str) -> str:
        """Transform Elvish text back to English."""
        result = text.lower()
        
        # Reverse consonant mappings
        for eng, elv in self.consonant_map.items():
            result = result.replace(elv, eng)
            
        # Reverse vowel mappings
        for eng, elv in self.vowel_map.items():
            result = result.replace(elv, eng)
            
        return result
