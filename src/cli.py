"""
Command-line interface for the language translator.
"""
import click
from rich.console import Console
from rich.panel import Panel
from rich.layout import Layout
from rich.text import Text
from src.languages.phonetics import PhoneticTransformer

from .translator import DEFAULT_RULES, Translator
from .languages import get_example_transformations

console = Console()


@click.group()
def cli():
    """CLI for the language translation tool."""
    pass


@cli.command()
@click.argument('text')
def translate(text: str) -> None:
    """Translate English text to Vybix."""
    transformer = PhoneticTransformer()
    try:
        vybix_text = transformer.transform(text)
        result = Text()
        result.append("English: ", style="blue bold")
        result.append(text)
        result.append("\nVybix: ", style="green bold")
        result.append(vybix_text)
        console.print(Panel(result, title="Translation Result", expand=True))
    except Exception as e:
        console.print(f"[red]Error during translation: {str(e)}[/red]")


@cli.command()
def list_rules():
    """List all available translation rules."""
    # Create a formatted list of rules
    rules_text = "\n".join(
        f"[blue]{english}[/blue] → [green]{translated}[/green]"
        for english, translated in sorted(DEFAULT_RULES.items())
    )
    
    console.print(Panel.fit(
        rules_text,
        title="Available Translations",
        border_style="bright_blue"
    ))


@cli.command()
def examples():
    """Show example translations demonstrating the language features."""
    examples = get_example_transformations()
    
    # Create a formatted list of examples
    examples_text = "\n".join(
        f"[blue]{eng}[/blue]\n→ [yellow]{ipa}[/yellow]\n→ [green]{vyb}[/green]\n"
        for eng, ipa, vyb in examples
    )
    
    console.print(Panel.fit(
        examples_text,
        title="Example Translations",
        border_style="bright_blue"
    ))


if __name__ == '__main__':
    cli() 