#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Install pre-commit hooks
pre-commit install

# Run tests to verify setup
pytest tests/

echo "Setup complete! Pre-commit hooks are installed and tests are configured." 