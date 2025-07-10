import questionary

def language_choice():
    language = {
        "US Inglés": "en",
        "ES Español": "es",
        "FR Francés": "fr",
        "DE Alemán": "de",
        "IT Italiano": "it",
        "PT Portugués": "pt",
        "RU Ruso": "ru",
        "JP Japonés": "ja",
        "CN Chino Simplificado": "ch_sim",
        "SA Árabe": "ar"
    }

    selected = questionary.select(
        "Selecciona el idioma que usará EasyOCR:",
        choices=list(language.keys())
    ).ask()

    return language[selected]