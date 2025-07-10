import easyocr

def transcription(image_path):
    try: 
        reader = easyocr.Reader(['es', 'en'])
        results = reader.readtext(image_path)

        text_detected = []  

        for bbox, text, condifdence in results:
            text_detected.append(text) 
            print(f'text detectado: "{text}" - Confianza: {condifdence:.2f}')

        all_text = ' '.join(text_detected)
        return all_text

    except Exception as e:
        print("Ocurrió un error:", e)
