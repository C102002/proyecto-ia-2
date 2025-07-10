from app.extra.info import info_about_us, info
from app.extra.instrucctions import instrucctions
from app.extra.language import language_choice
from app.extra.image import image_choice, get_test_path
from app.models.str import transcription
from app.models.sam import configs
import questionary

def menu():
    while True:
        option = questionary.select(
            "Bienvenido, ¿qué desea hacer?",
            choices=[
                "1. Cargar imagen",
                "2. Probar con un ejemplo",
                "3. Instrucciones",
                "4. ¿Quiénes somos?",
                "5. Informacion de los modelos"
                "6. Salir"
            ]
        ).ask()

        if option == "6. Salir":
            print("Saliendo del programa. ¡Hasta pronto!")
            break
        elif option == "5. Informacion":
            print(info())
        elif option == "4. ¿Quiénes somos?":
            print(info_about_us())
        elif option == "3. Instrucciones":
            print(instrucctions())
        elif option == "2. Probar con un ejemplo":
            print(get_test_path())
            text = transcription(get_test_path(), 'es')
            result = configs(text)
        elif option == "1. Cargar imagen":
            language = language_choice()
            path = image_choice()
            print(path)
            text = transcription(path, language)
            configs(text)

if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print("\n\nInterrupción con Ctrl+C detectada. Cerrando programa.")
