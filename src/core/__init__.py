"""Core package for business logic and shared functionality."""

from .config import settings
from .logger import setup_logging

__all__ = ["settings", "setup_logging"] 