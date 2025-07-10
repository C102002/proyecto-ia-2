def info_about_us():
    return (
        "\n"
        "📌 **¿Quiénes somos?**\n"
        "\n"
        "Somos estudiantes del último semestre de Ingeniería Informática, apasionados por la tecnología y la inteligencia artificial.\n"
        "Nuestro equipo está conformado por:\n\n"
        "  👤 Alfredo Fung\n"
        "  👤 Daniel Bortot\n"
        "  👤 Hualong Chan\n"
        "  👤 Gabriela Martínez\n"
        "  👤 Juan Perdomo\n"
        "\n"
        "Nos une el interés por desarrollar soluciones innovadoras y accesibles con impacto real en el mundo digital.\n"
    )

def info():
    return (
        "\n📚 **Resumen de los modelos utilizados:**\n\n"

        "🔠 **1. EasyOCR**\n"
        "EasyOCR es una biblioteca de código abierto para el reconocimiento óptico de caracteres (OCR), "
        "basada en modelos de deep learning con PyTorch. Permite extraer texto de imágenes en más de 80 idiomas.\n\n"
        "🛠️ ¿Cómo funciona?\n"
        "- Utiliza un detector de texto (como CRAFT) para encontrar regiones con texto.\n"
        "- Luego aplica un modelo de reconocimiento (usualmente un CRNN: Convolutional Recurrent Neural Network) "
        "para decodificar las letras dentro de cada región.\n\n"

        "🔍 **2. Modelo de análisis de sentimientos**\n"
        "Este modelo evalúa si un texto refleja una emoción positiva, negativa o neutral.\n"
        "Dependiendo de la implementación, puede ser:\n"
        "- Utiliza fine tunning con el moedelo Roberta, que se basa en el analisis de sentimientos\n"
        "- **Transformers**: modelos preentrenados de lenguaje natural que entienden el contexto de las palabras.\n\n"

        "🛠️ ¿Cómo funciona el análisis de sentimientos?\n"
        "- Convierte el texto a vectores numéricos (tokenización y embeddings).\n"
        "- El modelo evalúa el tono emocional con base en el entrenamiento previo (millones de textos).\n"
        "- Devuelve una etiqueta: positiva, negativa o neutral (a veces también un porcentaje o puntuación).\n\n"

        "💡 Estos dos modelos se complementan: EasyOCR convierte imágenes en texto, y el modelo de sentimientos analiza el contenido textual.\n"
    )