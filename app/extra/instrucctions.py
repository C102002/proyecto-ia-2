from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich import box

console = Console()

def instrucctions():
    """Muestra las instrucciones de uso en un panel estilizado con Rich."""
    content = Markdown(
        """
📋 **Instrucciones para usar la aplicación OCR:**

1. Mueve la imagen que deseas analizar a la carpeta `images` dentro del proyecto.  
2. En el menú principal, selecciona la opción **1. Cargar imagen** y sigue los pasos en pantalla.  
3. Asegúrate de que el idioma seleccionado **coincida con el idioma del texto en la imagen**.  
        """
    )
    panel = Panel(
        content,
        title="📋 Cómo usar",
        border_style="yellow",
        box=box.ROUNDED,
        padding=(1, 2)
    )
    console.print(panel)
