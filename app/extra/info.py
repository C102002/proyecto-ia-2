from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.table import Table
from rich import box

console = Console()

def info_about_us():
    """Imprime información del equipo en un panel estilizado."""
    content = Markdown(
        """
**Somos estudiantes del último semestre de Ingeniería Informática**, apasionados por la tecnología y la inteligencia artificial.

**Nuestro equipo está conformado por:**
- 👤 Alfredo Fung
- 👤 Daniel Bortot
- 👤 Hualong Chan
- 👤 Gabriela Martínez
- 👤 Juan Perdomo

Nos une el interés por **desarrollar soluciones innovadoras y accesibles** con impacto real en el mundo digital.
        """
    )
    panel = Panel(
        content,
        title="📌 ¿Quiénes somos?",
        border_style="blue",
        box=box.ROUNDED,
        padding=(1, 2)
    )
    console.print(panel)


def info():
    """Imprime un resumen de los modelos OCR y de Sentimiento en un panel con tabla."""
    table = Table.grid(padding=1)
    table.add_column("🔍 Modelo", style="bold")
    table.add_column("Descripción", style="")

    table.add_row(
        "🔠 EasyOCR (OCR)",
        "- Extrae texto de imágenes en **80+ idiomas**.\n"
        "- Usa detector (CRAFT) + CRNN para transcribir regiones de texto."
    )
    table.add_row(
        "💬 Sentiment Analysis",
        "- Clasifica textos como **😊 positivo**, **😞 negativo** o **😐 neutral**.\n"
        "- Basado en Transformers (p.ej. RoBERTa) con tokenización y embeddings."
    )

    panel = Panel(
        table,
        title="📚 Resumen de los modelos utilizados",
        border_style="magenta",
        box=box.ROUNDED,
        padding=(1, 2)
    )
    console.print(panel)