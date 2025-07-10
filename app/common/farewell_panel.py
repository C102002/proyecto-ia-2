from rich.console import Console
from rich.panel import Panel
from rich import box

FAREWELL_PANEL = Panel(
    "[bold white]Saliendo del Sistema de Reconocimiento de Texto en Imágenes\n"
    "y Análisis de Sentimiento.[/bold white]\n\n"
    "[bold cyan]¡Hasta pronto! 👋[/bold cyan]",
    title="[bold green]🚀 Adiós[/bold green]",
    border_style="green",
    box=box.ROUNDED,
    padding=(1, 2)
)