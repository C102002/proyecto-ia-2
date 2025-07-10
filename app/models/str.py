from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box
import easyocr
import torch

console = Console()

def transcription(image_path: str, language: str) -> str:
    """
    Performs OCR on the given image and prints results with Rich.
    Returns the concatenated text or an empty string on error.
    """
    try:
        reader = easyocr.Reader([language], gpu=torch.cuda.is_available())
        results = reader.readtext(image_path)

        # Build a table of detections
        table = Table(
            title="🖼️  OCR Transcription",
            box=box.ROUNDED,
            border_style="cyan"
        )
        table.add_column("Detected Text", style="bold white")
        table.add_column("Confidence", justify="right", style="magenta")

        for _, text, confidence in results:
            table.add_row(f"🔍  {text}", f"{confidence:.2f}")

        console.print(table)

        # Concatenate all detected fragments
        all_text = " ".join(text for _, text, _ in results)
        return all_text

    except Exception as e:
        console.print(
            Panel(
                f"❌  [bold red]Ocurrió un error:[/bold red]\n{e}",
                title="[red]Error[/red]",
                border_style="red",
                box=box.SQUARE
            )
        )
        return ""
