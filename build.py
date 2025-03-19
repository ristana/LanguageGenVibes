"""Build script for creating the executable using PyInstaller."""
import os
import sys
import shutil
from pathlib import Path
import PyInstaller.__main__

def build_executable():
    """Build the executable using PyInstaller."""
    # Get the absolute path to the project root
    project_root = Path(__file__).parent.absolute()
    
    # Define paths
    src_dir = project_root / "src"
    assets_dir = project_root / "assets"
    dist_dir = project_root / "dist"
    
    # Clean previous builds
    if dist_dir.exists():
        shutil.rmtree(dist_dir)
    
    # Prepare PyInstaller arguments
    args = [
        "src/__main__.py",  # Entry point
        "--name=FictionalTranslator",
        "--onefile",  # Create a single executable
        "--windowed",  # Don't show console window on Windows
        f"--add-data={assets_dir};assets",  # Include assets directory
        "--icon=assets/app_icon.ico",  # Application icon
        "--clean",  # Clean PyInstaller cache
        "--noconfirm",  # Replace output directory without confirmation
    ]
    
    # Add platform-specific options
    if sys.platform.startswith("win"):
        args.append("--noconsole")  # Hide console on Windows
    
    # Run PyInstaller
    PyInstaller.__main__.run(args)
    
    print("\nBuild completed! Executable created in the 'dist' directory.")
    print("You can still run the app in development mode using 'python -m src'")

if __name__ == "__main__":
    build_executable() 