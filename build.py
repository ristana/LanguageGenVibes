"""Build script for creating the executable."""
import os
import sys
import PyInstaller.__main__

def build_executable():
    """Build the executable using PyInstaller."""
    # Define PyInstaller arguments
    args = [
        "src/__main__.py",  # Main script
        "--name=FictionalTranslator",  # Name of the executable
        "--onefile",  # Create a single executable file
        "--windowed",  # Don't show console window
        "--clean",  # Clean PyInstaller cache
        "--add-data=src/languages;languages",  # Include language modules
    ]
    
    # Run PyInstaller
    PyInstaller.__main__.run(args)

if __name__ == "__main__":
    build_executable() 