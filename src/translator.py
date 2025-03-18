"""
Core translation functionality for converting English to fictional languages.
"""
from typing import Dict, Optional

from pydantic import BaseModel

from .languages.phonetics import PhoneticTransformer


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
    
    def __init__(self, rules: Dict[str, str] = None):
        """Initialize the translator.
        
        Args:
            rules: Optional dictionary of special case translations
        """
        self.transformer = PhoneticTransformer()
    
    def translate(self, text: str) -> str:
        """Translate a full text from English to the fictional language.
        
        Args:
            text: The English text to translate
            
        Returns:
            The translated text
        """
        return self.transformer.transform(text)


# Special case translations are now handled by the transformer
DEFAULT_RULES = {} 