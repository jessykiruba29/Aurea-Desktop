import os
import torch
from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification

MODEL_PATH = os.path.join(os.path.dirname(__file__), "intent_model")

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model folder not found: {MODEL_PATH}")

tokenizer = DistilBertTokenizerFast.from_pretrained(MODEL_PATH)
model = DistilBertForSequenceClassification.from_pretrained(MODEL_PATH)

INTENTS = ["open_url", "scroll_down", "open_app"]

def get_intent(text: str) -> dict:
    """Predicts intent and extracts simple slots from text."""
    inputs = tokenizer(text, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    pred = torch.argmax(outputs.logits).item()
    intent = INTENTS[pred]

    slots = {}

    if intent == "open_url":
        if "youtube" in text.lower():
            slots["url"] = "https://youtube.com"
        elif "google" in text.lower():
            slots["url"] = "https://google.com"

    elif intent == "open_app":
        if "notepad" in text.lower():
            slots["app_name"] = "notepad.exe"
        elif "calculator" in text.lower():
            slots["app_name"] = "calc.exe"

    return {"intent": intent, "slots": slots}
