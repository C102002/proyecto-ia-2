import warnings
import time
import questionary

from app.common.farewell_panel import FAREWELL_PANEL
from app.extra.info import info_about_us, info
from app.extra.instrucctions import instrucctions
from app.extra.language import language_choice
from app.extra.image import image_choice, get_test_path
from app.models.str import transcription
from app.models.sam import configs

from rich.console import Console
from rich.panel import Panel
from rich import box

console = Console()

warnings.filterwarnings(
    "ignore",
    message=".*pin_memory.*",
    category=UserWarning,
    module="torch.utils.data.dataloader"
)

def menu():
    # 1) Spinner de carga
    with console.status("[bold green]Cargando menú...[/bold green]", spinner="dots"):
        time.sleep(1)
    console.clear()

    # 1.1) Instrucciones de navegación
    console.print(
        "[bold cyan]🡅 🡇 Usa las flechas arriba/abajo y presiona Enter para navegar el menú[/bold cyan]\n"
    )

    # 2) Menú interactivo
    while True:
        option = questionary.select(
            "Bienvenido, ¿qué desea hacer?",
            choices=[
                "1. Cargar imagen",
                "2. Probar con un ejemplo",
                "3. Instrucciones",
                "4. ¿Quiénes somos?",
                "5. Información de los modelos",
                "6. Salir"
            ],
        ).ask()

        if option is None or option == "6. Salir":
            console.print(
                FAREWELL_PANEL
            )
            break

        elif option == "5. Información de los modelos":
            console.print(info())

        elif option == "4. ¿Quiénes somos?":
            console.print(info_about_us())

        elif option == "3. Instrucciones":
            console.print(instrucctions())

        elif option == "2. Probar con un ejemplo":
            test_path = get_test_path()
            console.print(f"Ejemplo: {test_path}")
            text = transcription(test_path, 'es')
            configs(text)

        elif option == "1. Cargar imagen":
            language = language_choice()
            path = image_choice()
            console.print(f"Ruta seleccionada: {path}")
            text = transcription(path, language)
            configs(text)

if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        console.print(
            Panel(
                "[bold yellow]Interrupción con Ctrl+C detectada.\nCerrando programa.[/bold yellow]",
                title="[yellow]⏸️ Interrupción[/yellow]",
                border_style="yellow",
                box=box.ROUNDED,
                padding=(1, 2)
            )
        )
    except Exception as e:
        console.print(
            Panel(
                f"❌  [bold red]Ocurrió un error:[/bold red]\n{e}",
                title="[red]Error[/red]",
                border_style="red",
                box=box.SQUARE,
                padding=(1, 2)
            )
        )
