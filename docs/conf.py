"""Sphinx configuration file for project documentation."""

import os
import sys
from datetime import datetime

# Add source directory to path for autodoc
sys.path.insert(0, os.path.abspath("../src"))

# Project information
project = "Python Project"
copyright = f"{datetime.now().year}, Your Name"
author = "Your Name"
release = "0.1.0"

# Extensions
extensions = [
    "sphinx.ext.autodoc",  # Automatically include docstrings
    "sphinx.ext.napoleon",  # Support for Google-style docstrings
    "sphinx.ext.viewcode",  # Add links to source code
    "sphinx.ext.githubpages",  # Generate .nojekyll file
    "myst_parser",  # Support for Markdown
    "sphinxcontrib.mermaid",  # Support for Mermaid diagrams
]

# Templates
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# HTML output options
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = True
napoleon_use_ivar = True
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_type_aliases = None

# MyST settings
myst_enable_extensions = [
    "colon_fence",  # Support for ::: fences
    "deflist",      # Definition lists
    "dollarmath",   # Math in $$ blocks
    "fieldlist",    # Field lists
    "html_image",   # HTML image tags
    "linkify",      # Auto-link URLs
    "replacements", # Text replacements
    "smartquotes",  # Smart quotes
    "tasklist",     # Task lists
]

# AutoDoc settings
autodoc_default_options = {
    "members": True,
    "member-order": "bysource",
    "special-members": "__init__",
    "undoc-members": True,
    "exclude-members": "__weakref__"
} 