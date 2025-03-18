# Contributing to LanguageGenVibes

## Quick Reference

### Common Git Commands
```bash
# Check status
git status

# Pull latest changes
git pull origin main

# Create and switch to new branch
git checkout -b feature/new-feature

# Discard local changes
git checkout -- .

# View commit history
git log --oneline

# Update remote URL if needed
git remote set-url origin https://github.com/ristana/LanguageGenVibes.git
```

### Common Issues & Solutions

1. **Git not found**: Make sure Git is installed and in your PATH
2. **Permission denied**: Check your GitHub credentials
3. **Merge conflicts**: 
   ```bash
   git status  # See conflicting files
   # Edit files to resolve conflicts
   git add .
   git commit -m "Resolve merge conflicts"
   ```

## Development Setup

1. Clone the repository:
```bash
git clone https://github.com/ristana/LanguageGenVibes.git
cd LanguageGenVibes
```

2. Set up your Python environment:
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Unix or MacOS:
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Making Changes

1. Create a new branch for your feature:
```bash
git checkout -b feature/your-feature-name
```

2. Make your changes to the code

3. Test your changes:
```bash
python -m pytest
```

4. Stage your changes:
```bash
git add .
```

5. Commit your changes:
```bash
git commit -m "Description of your changes"
```

6. Push to GitHub:
```bash
git push origin feature/your-feature-name
```

## Code Style Guidelines

- Follow PEP 8 style guide
- Use type hints for all function parameters and return values
- Add docstrings in Google style format
- Keep lines under 88 characters (Black formatter default)
- Use meaningful variable and function names

## Project Structure

```
LanguageGenVibes/
├── src/
│   ├── languages/
│   │   ├── __init__.py
│   │   ├── phonetics.py
│   │   └── vybix.py
│   ├── __init__.py
│   ├── __main__.py
│   └── cli.py
├── tests/
├── requirements.txt
└── README.md
```

## Testing

- Write tests for new features
- Run tests before committing:
```bash
python -m pytest
```

## Pull Request Process

1. Create a new branch for your feature
2. Make your changes
3. Run tests
4. Push to GitHub
5. Create a Pull Request on GitHub
6. Wait for review and address any feedback
7. Merge once approved

## Contact

For questions or issues, please open an issue on GitHub or contact the maintainers. 