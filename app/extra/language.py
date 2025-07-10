import sys
import questionary
from rich.console import Console

from app.common.farewell_panel import FAREWELL_PANEL

console = Console()

def language_choice():
    language = {
        "🇺🇸 English":       "en",
        "🇪🇸 Español":       "es",
        "🇫🇷 Français":      "fr",
        "🇩🇪 Deutsch":       "de",
        "🇮🇹 Italiano":      "it",
        "🇵🇹 Português":     "pt",
        "🇷🇺 Русский":       "ru",
        "🇯🇵 日本語":         "ja",
        "🇨🇳 中文":           "ch_sim",
        "🇸🇦 العربية":       "ar"
    }

    selected = questionary.select(
        "Selecciona el idioma que usará EasyOCR:",
        choices=list(language.keys()),
        qmark="🌐"
    ).ask()

    # Si el usuario pulsa Esc o Ctrl+C, ask() devuelve None
    if selected is None:
        console.print(FAREWELL_PANEL)
        sys.exit(0)

    return language[selected]
