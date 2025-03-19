"""Language module initialization."""
from typing import List

from .elvish import ElvishTransformer
from .cybernetic import CyberneticTransformer
from .dwarvish import DwarvishTransformer
from .insectoid import InsectoidTransformer
from .celestial import CelestialTransformer
from .necrotic import NecroticTransformer

LANGUAGE_TRANSFORMERS = {
    'elvish': ElvishTransformer,
    'cybernetic': CyberneticTransformer,
    'dwarvish': DwarvishTransformer,
    'insectoid': InsectoidTransformer,
    'celestial': CelestialTransformer,
    'necrotic': NecroticTransformer,
}

__all__ = ['LANGUAGE_TRANSFORMERS', 'get_available_languages']

def get_available_languages() -> List[str]:
    """Get a list of all available language transformers.
    
    Returns:
        List[str]: List of language names that can be used for translation.
    """
    return list(LANGUAGE_TRANSFORMERS.keys()) 