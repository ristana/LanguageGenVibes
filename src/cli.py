"""
Command-line interface for the language translator.
"""
import click
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

from .languages import LANGUAGE_TRANSFORMERS

console = Console()

@click.group()
def cli():
    """CLI for the language translation tool."""
    pass

@cli.command()
@click.argument('text')
@click.option('--language', '-l', default='elvish', help='Target language (elvish or vybix)')
def translate(text: str, language: str) -> None:
    """Translate English text to the target language."""
    if language not in LANGUAGE_TRANSFORMERS:
        console.print(f"[red]Error: Unknown language '{language}'. Available languages: {', '.join(LANGUAGE_TRANSFORMERS.keys())}[/red]")
        return

    try:
        # Create transformer for the selected language
        transformer_class = LANGUAGE_TRANSFORMERS[language]
        transformer = transformer_class()
        
        # Transform the text
        transformed_text = transformer.transform(text)
        
        # Display results
        result = Text()
        result.append("English: ", style="blue bold")
        result.append(text)
        result.append(f"\n{language.title()}: ", style="green bold")
        result.append(transformed_text)
        
        # Try to reverse transform
        reversed_text = transformer.reverse_transform(transformed_text)
        result.append("\nReversed: ", style="yellow bold")
        result.append(reversed_text)
        
        console.print(Panel(result, title="Translation Result", expand=True))
    except Exception as e:
        console.print(f"[red]Error during translation: {str(e)}[/red]")

@cli.command()
def list_languages():
    """List all available languages."""
    languages_text = "\n".join(
        f"[blue]{lang}[/blue]"
        for lang in sorted(LANGUAGE_TRANSFORMERS.keys())
    )
    
    console.print(Panel.fit(
        languages_text,
        title="Available Languages",
        border_style="bright_blue"
    ))

if __name__ == '__main__':
    cli() 