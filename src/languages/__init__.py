"""
Language definitions and transformations.
"""

from .phonetics import PhoneticTransformer, get_example_transformations
from .vybix import (EXAMPLE_WORDS, LETTER_COMBINATIONS, NUMBERS,
                   PHONETIC_MAPPING, SPECIAL_RULES, VOWEL_HARMONY_EXAMPLES,
                   WORD_ENDINGS)

__all__ = [
    'PhoneticTransformer',
    'get_example_transformations',
    'EXAMPLE_WORDS',
    'LETTER_COMBINATIONS',
    'NUMBERS',
    'PHONETIC_MAPPING',
    'SPECIAL_RULES',
    'VOWEL_HARMONY_EXAMPLES',
    'WORD_ENDINGS',
] 