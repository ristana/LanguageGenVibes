"""
Base transformer class for language transformations.

This module provides the base class that all language transformers should inherit from.
It defines the interface that all transformers must implement.
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Optional


class BaseTransformer(ABC):
    """Base class for all language transformers."""

    def __init__(self):
        """Initialize the base transformer."""
        self.consonant_mappings: Dict[str, List[str]] = {}
        self.vowel_mappings: Dict[str, List[str]] = {}
        self.prefixes: List[str] = []
        self.suffixes: List[str] = []
        self.word_symbols: List[str] = []
        self.particles: List[str] = []

    @abstractmethod
    def transform(self, text: str) -> str:
        """Transform text from English to the target language.
        
        Args:
            text: The English text to transform
            
        Returns:
            The transformed text in the target language
        """
        pass

    @abstractmethod
    def reverse_transform(self, text: str) -> str:
        """Transform text from the target language back to English.
        
        Args:
            text: The text in the target language
            
        Returns:
            The transformed text in English
        """
        pass 