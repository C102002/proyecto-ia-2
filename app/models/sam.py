from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import numpy as np 
import os

def configs(text):
    loaded_model_path = r"../../modelo_sentimientos"

    tokenizer = AutoTokenizer.from_pretrained(loaded_model_path)
    model = AutoModelForSequenceClassification.from_pretrained(loaded_model_path)

    if torch.cuda.is_available():
        model.to('cuda')

    id_to_label = model.config.id2label
    if id_to_label:
        sentiment_labels = [id_to_label[i] for i in sorted(id_to_label.keys())]
    else:
        print("\nAdvertencia: No se encontró id_to_label en la configuración del modelo. Las predicciones serán IDs numéricos.")

    return predict_sentiment(text, model, tokenizer, sentiment_labels)

def predict_sentiment(text, model, tokenizer, sentiment_labels):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)

    if torch.cuda.is_available():
        inputs = {key: value.to('cuda') for key, value in inputs.items()}

    model.eval() 
    with torch.no_grad():
        outputs = model(**inputs)

    logits = outputs.logits
    probabilities = torch.softmax(logits, dim=1)[0].cpu().numpy()
    predicted_class_id = torch.argmax(logits, dim=1).item()
    predicted_sentiment = sentiment_labels[predicted_class_id] if sentiment_labels else f"ID: {predicted_class_id}"

    print(f"\nTexto: '{text}'")
    print("Probabilidades:")
    if sentiment_labels:
        for i, prob in enumerate(probabilities):
            print(f"  {sentiment_labels[i]}: {prob:.4f}")
    else:
        print(f"  {probabilities}") 

    print(f"Sentimiento Predicho: {predicted_sentiment}")

    return {
        "text": text,
        "probabilities": probabilities.tolist(),
        "predicted_id": predicted_class_id,
        "predicted_sentiment": predicted_sentiment
    }

