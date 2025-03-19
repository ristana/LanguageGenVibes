"""Elvish language transformer implementation."""
from .base import BaseTransformer


class ElvishTransformer(BaseTransformer):
    """Implements the Elvish language transformation."""

    def __init__(self):
        """Initialize the Elvish transformer."""
        # Using unique runes for each character to avoid conflicts
        self.char_map = {
            'a': 'ᚨ',  # Ansuz
            'b': 'ᛒ',  # Berkanan
            'c': 'ᚳ',  # Anglo-Saxon Cen
            'd': 'ᛞ',  # Dagaz
            'e': 'ᛖ',  # Ehwaz
            'f': 'ᚠ',  # Fehu
            'g': 'ᚷ',  # Gebo
            'h': 'ᚻ',  # Anglo-Saxon Haegl
            'i': 'ᛁ',  # Isa
            'j': 'ᛃ',  # Jera
            'k': 'ᚴ',  # Younger Futhark Kaun
            'l': 'ᛚ',  # Laguz
            'm': 'ᛗ',  # Mannaz
            'n': 'ᚾ',  # Nauthiz
            'o': 'ᛟ',  # Othala
            'p': 'ᛈ',  # Perthro
            'q': 'ᛩ',  # Q-rune
            'r': 'ᚱ',  # Raidho
            's': 'ᛋ',  # Sowilo
            't': 'ᛏ',  # Tiwaz
            'u': 'ᚢ',  # Uruz
            'v': 'ᚡ',  # Younger Futhark Fe
            'w': 'ᚹ',  # Wunjo
            'x': 'ᛪ',  # X-rune
            'y': 'ᚤ',  # Yr
            'z': 'ᛉ',  # Algiz
            # Special digraphs
            'th': 'ᚦ',  # Thurisaz
            'ch': 'ᚳᚻ',  # Combination of Cen and Haegl
            'sh': 'ᛋᚻ',  # Combination of Sowilo and Haegl
            'ph': 'ᛈᚻ',  # Combination of Perthro and Haegl
            'ng': 'ᛝ',  # Ing
        }

    def transform(self, text: str) -> str:
        """Transform text into Elvish.
        
        Args:
            text: The input text to transform.
            
        Returns:
            The transformed text in Elvish runes.
        """
        if not text:
            return ""
            
        result = []
        i = 0
        while i < len(text):
            # Try digraphs first
            matched = False
            if i < len(text) - 1:
                digraph = text[i:i+2].lower()
                if digraph in ['th', 'ch', 'sh', 'ph', 'ng']:
                    if text[i:i+2].isupper():
                        result.append(self.char_map[digraph].upper())
                    elif text[i].isupper() and text[i+1].islower():
                        # Handle mixed case in digraphs
                        result.append(self.char_map[digraph][0].upper() + self.char_map[digraph][1:])
                    else:
                        result.append(self.char_map[digraph])
                    i += 2
                    matched = True
            
            if not matched:
                char = text[i]
                lower_char = char.lower()
                if lower_char in self.char_map:
                    if char.isupper():
                        result.append(self.char_map[lower_char].upper())
                    else:
                        result.append(self.char_map[lower_char])
                else:
                    result.append(char)
                i += 1
            
        return ''.join(result)

    def reverse_transform(self, text: str) -> str:
        """Transform Elvish text back to English.
        
        Args:
            text: The Elvish text to transform back.
            
        Returns:
            The original English text.
        """
        if not text:
            return ""
            
        # Create reverse mapping
        reverse_map = {v: k for k, v in self.char_map.items()}
        
        # Sort patterns by length for proper matching
        patterns = sorted(reverse_map.items(), key=lambda x: len(x[0]), reverse=True)
        
        result = []
        i = 0
        while i < len(text):
            matched = False
            # Try each pattern
            for pattern, replacement in patterns:
                if text[i:].startswith(pattern):
                    result.append(replacement)
                    i += len(pattern)
                    matched = True
                    break
                elif text[i:].startswith(pattern.upper()):
                    result.append(replacement.upper())
                    i += len(pattern)
                    matched = True
                    break
                # Handle mixed case in digraphs
                elif len(pattern) > 1 and text[i:].startswith(pattern[0].upper() + pattern[1:]):
                    result.append(replacement[0].upper() + replacement[1:])
                    i += len(pattern)
                    matched = True
                    break
            
            if not matched:
                result.append(text[i])
                i += 1
            
        return ''.join(result)
