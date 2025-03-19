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
    def _setup_transformations(self) -> None:
        """Set up the transformation rules for the language.
        
        This method should be implemented by subclasses to define their specific
        transformation rules.
        """
        pass

    @abstractmethod
    def transform(self, text: str) -> str:
        """Transform text from English to the target language.
        
        Args:
            text: The English text to transform.
            
        Returns:
            The transformed text in the target language.
        """
        pass

    @abstractmethod
    def reverse_transform(self, text: str) -> str:
        """Attempt to reverse transform text back to English.
        
        Note: This may be an approximate reverse transformation due to the
        complexity of the transformations.
        
        Args:
            text: The text in the target language to reverse transform.
            
        Returns:
            An approximate English text.
        """
        pass 