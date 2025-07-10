import os
import questionary

def image_choice():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    from_folder = os.path.join(base_dir, "..", "images") 
    from_folder = os.path.normpath(from_folder) 

    valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp')
    try:
        files = [
            f for f in os.listdir(from_folder)
            if f.lower().endswith(valid_extensions)
        ]
    except FileNotFoundError:
        print(f"⚠️ La carpeta '{from_folder}' no existe.")
        return None

    if not files:
        print(f"⚠️ No se encontraron imágenes en la carpeta '{from_folder}'.")
        return None

    option = questionary.select(
        "Selecciona una imagen:",
        choices=files
    ).ask()

    return os.path.join(from_folder, option)

def get_test_path():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    ruta_imagen = os.path.join(base_dir, "..", "images", "test.jpg")
    return os.path.normpath(ruta_imagen)  