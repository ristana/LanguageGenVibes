"""Elvish language transformation system.

This module implements a complex phonetic transformation system for the Elvish language,
with multiple layers of transformation and encryption-like features.
"""

from typing import Dict, List, Optional
import random
import re
from .phonetics import PhoneticTransformer

class ElvishTransformer(PhoneticTransformer):
    """Implements the Elvish language transformation system."""

    def __init__(self):
        """Initialize the Elvish transformer with complex transformation rules."""
        super().__init__()
        self._initialize_elvish_rules()
        self._initialize_encryption_rules()

    def _initialize_elvish_rules(self) -> None:
        """Initialize complex Elvish transformation rules."""
        # Base phonetic mappings with multiple layers
        self.phonetic_mappings = {
            # Layer 1: Basic consonant transformations
            'b': ['v', 'f', 'w'],
            'c': ['k', 'ch', 'kh'],
            'd': ['dh', 'th', 'z'],
            'f': ['ph', 'v', 'w'],
            'g': ['gh', 'k', 'ng'],
            'h': ['ch', 'kh', 'h'],
            'j': ['y', 'zh', 'dj'],
            'k': ['c', 'kh', 'k'],
            'l': ['ll', 'l', 'lh'],
            'm': ['mm', 'm', 'mh'],
            'n': ['nn', 'n', 'nh'],
            'p': ['ph', 'p', 'b'],
            'q': ['kw', 'qu', 'k'],
            'r': ['rr', 'r', 'rh'],
            's': ['ss', 's', 'sh'],
            't': ['th', 't', 'd'],
            'v': ['w', 'v', 'f'],
            'w': ['v', 'w', 'u'],
            'x': ['ks', 'x', 'kh'],
            'y': ['i', 'y', 'j'],
            'z': ['zh', 'z', 's'],
            
            # Layer 2: Vowel transformations with context
            'a': ['á', 'ä', 'â'],
            'e': ['é', 'ë', 'ê'],
            'i': ['í', 'ï', 'î'],
            'o': ['ó', 'ö', 'ô'],
            'u': ['ú', 'ü', 'û'],
            
            # Layer 3: Special combinations
            'th': ['þ', 'ð', 'th'],
            'sh': ['š', 'ş', 'sh'],
            'ch': ['č', 'ç', 'ch'],
            'ng': ['ŋ', 'ng', 'n'],
            'ph': ['φ', 'ph', 'f'],
        }

        # Complex transformation rules
        self.transformation_rules = [
            # Rule 1: Consonant doubling based on position
            lambda word: self._double_consonants(word),
            
            # Rule 2: Vowel elongation in stressed syllables
            lambda word: self._elongate_vowels(word),
            
            # Rule 3: Add mystical suffixes based on word length
            lambda word: self._add_mystical_suffix(word),
            
            # Rule 4: Insert random elvish particles
            lambda word: self._insert_particles(word),
            
            # Rule 5: Transform word endings based on context
            lambda word: self._transform_endings(word),
        ]

        # Elvish particles for random insertion
        self.particles = [
            'el', 'il', 'al', 'ol', 'ul',
            'en', 'in', 'an', 'on', 'un',
            'eth', 'ith', 'ath', 'oth', 'uth'
        ]

    def _initialize_encryption_rules(self) -> None:
        """Initialize encryption-like transformation rules."""
        # Mystical symbols for special transformations
        self.mystical_symbols = {
            'light': ['☀', '☼', '☉'],
            'dark': ['☽', '☾', '☪'],
            'magic': ['⚡', '⚢', '⚣'],
            'nature': ['❀', '❁', '✿'],
            'time': ['⌛', '⏳', '⌚']
        }

        # Word encryption patterns
        self.encryption_patterns = [
            # Pattern 1: Insert mystical symbols between vowels
            lambda word: self._insert_mystical_symbols(word),
            
            # Pattern 2: Shift consonants based on word position
            lambda word: self._shift_consonants(word),
            
            # Pattern 3: Add magical prefixes based on word meaning
            lambda word: self._add_magical_prefix(word),
            
            # Pattern 4: Transform based on word length and position
            lambda word: self._transform_by_length(word),
        ]

        # Magical prefixes for different word types
        self.magical_prefixes = {
            'noun': ['Ael', 'Eld', 'Ilm', 'Ond', 'Uth'],
            'verb': ['Mae', 'Nae', 'Pae', 'Rae', 'Sae'],
            'adjective': ['Cal', 'Del', 'Fel', 'Gel', 'Hel'],
            'adverb': ['Wen', 'Xen', 'Yen', 'Zen', 'Aen']
        }

    def _double_consonants(self, word: str) -> str:
        """Double consonants in specific positions."""
        result = list(word)
        for i in range(len(result) - 1):
            if result[i] in 'bcdfghjklmnprstvwxz' and random.random() < 0.3:
                result[i] = result[i] * 2
        return ''.join(result)

    def _elongate_vowels(self, word: str) -> str:
        """Elongate vowels in stressed syllables."""
        vowels = 'aeiou'
        result = list(word)
        for i in range(len(result)):
            if result[i] in vowels and random.random() < 0.4:
                result[i] = result[i] + '̄'
        return ''.join(result)

    def _add_mystical_suffix(self, word: str) -> str:
        """Add mystical suffixes based on word length."""
        if len(word) < 4:
            return word + random.choice(['el', 'il', 'al'])
        elif len(word) < 8:
            return word + random.choice(['eth', 'ith', 'ath'])
        else:
            return word + random.choice(['ion', 'ian', 'ien'])

    def _insert_particles(self, word: str) -> str:
        """Insert random elvish particles."""
        if random.random() < 0.3:
            particle = random.choice(self.particles)
            return word + particle
        return word

    def _transform_endings(self, word: str) -> str:
        """Transform word endings based on context."""
        endings = {
            'ing': ['ion', 'ien', 'ian'],
            'ed': ['eth', 'ith', 'ath'],
            'er': ['or', 'ar', 'ur'],
            'ly': ['li', 'lë', 'lï']
        }
        for end, replacements in endings.items():
            if word.endswith(end):
                return word[:-len(end)] + random.choice(replacements)
        return word

    def _insert_mystical_symbols(self, word: str) -> str:
        """Insert mystical symbols between vowels."""
        vowels = 'aeiou'
        result = list(word)
        for i in range(len(result) - 1):
            if result[i] in vowels and result[i + 1] in vowels:
                symbol_type = random.choice(list(self.mystical_symbols.keys()))
                symbol = random.choice(self.mystical_symbols[symbol_type])
                result.insert(i + 1, symbol)
        return ''.join(result)

    def _shift_consonants(self, word: str) -> str:
        """Shift consonants based on word position."""
        consonants = 'bcdfghjklmnprstvwxz'
        result = list(word)
        for i in range(len(result)):
            if result[i] in consonants:
                shift = (i * 3) % len(consonants)
                new_pos = (consonants.index(result[i]) + shift) % len(consonants)
                result[i] = consonants[new_pos]
        return ''.join(result)

    def _add_magical_prefix(self, word: str) -> str:
        """Add magical prefixes based on word meaning."""
        # Simple heuristic for word type detection
        if word.endswith(('ing', 'ed', 's')):
            prefix = random.choice(self.magical_prefixes['verb'])
        elif word.endswith(('ly', 'y', 'ic')):
            prefix = random.choice(self.magical_prefixes['adverb'])
        elif word.endswith(('er', 'or', 'ar')):
            prefix = random.choice(self.magical_prefixes['adjective'])
        else:
            prefix = random.choice(self.magical_prefixes['noun'])
        return prefix + word

    def _transform_by_length(self, word: str) -> str:
        """Transform based on word length and position."""
        if len(word) < 3:
            return word + random.choice(['ë', 'ï', 'ü'])
        elif len(word) < 6:
            return word + random.choice(['ion', 'ian', 'ien'])
        else:
            return word + random.choice(['eth', 'ith', 'ath'])

    def transform(self, text: str) -> str:
        """Transform text into Elvish with multiple layers of complexity."""
        # Apply base phonetic transformations
        result = super().transform(text)
        
        # Apply each transformation rule
        for rule in self.transformation_rules:
            words = result.split()
            transformed_words = [rule(word) for word in words]
            result = ' '.join(transformed_words)
        
        # Apply encryption patterns
        for pattern in self.encryption_patterns:
            words = result.split()
            transformed_words = [pattern(word) for word in words]
            result = ' '.join(transformed_words)
        
        # Add final mystical touches
        if random.random() < 0.2:
            result = result + ' ' + random.choice(self.particles)
        
        return result

    def reverse_transform(self, text: str) -> str:
        """Reverse transform Elvish text back to English.
        
        Note: Due to the complexity of the transformation rules,
        this is an approximation and may not perfectly restore the original text.
        """
        # Remove mystical symbols
        for symbols in self.mystical_symbols.values():
            for symbol in symbols:
                text = text.replace(symbol, '')
        
        # Remove magical prefixes
        for prefixes in self.magical_prefixes.values():
            for prefix in prefixes:
                text = re.sub(f'^{prefix}', '', text)
        
        # Basic phonetic reversal
        result = text
        for original, variants in self.phonetic_mappings.items():
            for variant in variants:
                result = result.replace(variant, original)
        
        return result
