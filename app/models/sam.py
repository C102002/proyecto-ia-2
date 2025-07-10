from pathlib import Path
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

console = Console()

def configs(text: str):
    # Ruta relativa al proyecto raíz
    base_dir = Path(__file__).resolve().parent.parent.parent
    loaded_model_path = base_dir / "modelo_sentimientos"

    # Cargar tokenizer y modelo
    tokenizer = AutoTokenizer.from_pretrained(loaded_model_path, local_files_only=True)
    model = AutoModelForSequenceClassification.from_pretrained(loaded_model_path, local_files_only=True)

    if torch.cuda.is_available():
        model.to("cuda")

    # Map IDs a etiquetas
    id_to_label = model.config.id2label or {}
    sentiment_labels = [id_to_label[i] for i in sorted(id_to_label.keys())]

    return predict_sentiment(text, model, tokenizer, sentiment_labels)


def predict_sentiment(text: str, model, tokenizer, sentiment_labels):
    # Mapping de etiquetas a emojis
    emoji_map = {
        "positivo": "😊",
        "negativo": "😞",
        "neutral": "😐"
    }

    # Tokenizar
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    if torch.cuda.is_available():
        inputs = {k: v.to("cuda") for k, v in inputs.items()}

    model.eval()
    with torch.no_grad():
        outputs = model(**inputs)

    # Obtener probabilidades y predicción
    logits = outputs.logits
    probs = torch.softmax(logits, dim=1)[0].cpu().numpy()
    pred_id = int(torch.argmax(logits, dim=1).item())
    base_label = sentiment_labels[pred_id] if sentiment_labels else f"ID {pred_id}"
    pred_label = f"{base_label} {emoji_map.get(base_label, '')}"

    # Mostrar texto extraído
    console.print(
        Panel(
            Text(text, justify="center"),
            title="[bold cyan]Extracted Text[/bold cyan]",
            border_style="cyan"
        )
    )

    # Mostrar tabla de probabilidades con emojis
    table = Table(title="[bold magenta]Probabilities[/bold magenta]", box=None)
    table.add_column("Sentiment", style="bold")
    table.add_column("Probability", justify="right")
    for idx, p in enumerate(probs):
        base = sentiment_labels[idx] if sentiment_labels else str(idx)
        label = f"{base} {emoji_map.get(base, '')}"
        table.add_row(label, f"{p:.4f}")
    console.print(table)

    # Mostrar predicción final con estilo
    console.print(
        Panel(
            Text(pred_label, style="bold green"),
            title="[bold green]Predicted Sentiment[/bold green]",
            border_style="green"
        )
    )

    return {
        "text": text,
        "probabilities": probs.tolist(),
        "predicted_id": pred_id,
        "predicted_sentiment": pred_label
    }
