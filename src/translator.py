"""
Core translation functionality for converting English to fictional languages.
"""
from typing import Dict, Optional

from pydantic import BaseModel

from .languages import LANGUAGE_TRANSFORMERS


class TranslationRule(BaseModel):
    """A rule for translating words or phrases.
    
    Attributes:
        english: The English word or phrase
        translation: The corresponding translation
        context: Optional context where this translation applies
    """
    english: str
    translation: str
    context: Optional[str] = None


class Translator:
    """Main translator class for converting English to fictional languages."""
    
    def __init__(self):
        """Initialize the translator with available language transformers."""
        self.transformers = {
            name.lower(): transformer_class()
            for name, transformer_class in LANGUAGE_TRANSFORMERS.items()
        }
    
    def translate(self, text: str, language: str) -> str:
        """Translate a full text from English to the specified fictional language.
        
        Args:
            text: The English text to translate
            language: The target fictional language
            
        Returns:
            The translated text
            
        Raises:
            ValueError: If the specified language is not supported
        """
        language = language.lower()
        if language not in self.transformers:
            raise ValueError(f"Unsupported language: {language}")
            
        return self.transformers[language].transform(text)

    def reverse_translate(self, text: str, language: str) -> str:
        """Convert text from a fictional language back to English.
        
        Args:
            text: The text in the fictional language to convert back
            language: The source fictional language
            
        Returns:
            The original English text
            
        Raises:
            ValueError: If the specified language is not supported
        """
        language = language.lower()
        if language not in self.transformers:
            raise ValueError(f"Unsupported language: {language}")
            
        return self.transformers[language].reverse_transform(text)


# Special case translations are now handled by the transformer
DEFAULT_RULES = {} 