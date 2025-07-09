from app.models.str import transcription
from app.models.sam  import configs
from pathlib import Path

def analysis_of_sentiments():
    extensiones_image = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'}
    
    image_path = input('Load your image path: ')
    archivo = Path(image_path).expanduser().resolve()

    if not archivo.exists():
        print(f"File not found: {archivo}")
        return

    if archivo.suffix.lower() in extensiones_image:
        text = transcription(image_path)
        result = configs(text)
        return result
    else:
        print("The file is not a supported image format.")

    return

analysis_of_sentiments()