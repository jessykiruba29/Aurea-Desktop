import torch
from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification

MODEL_PATH = "./intent_model" 
tokenizer = DistilBertTokenizerFast.from_pretrained(MODEL_PATH)
model = DistilBertForSequenceClassification.from_pretrained(MODEL_PATH)

INTENTS = ["open_url", "scroll_down", "open_app"]

def get_intent(text):
    inputs = tokenizer(text, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    pred = torch.argmax(outputs.logits).item()
    return {"intent": INTENTS[pred], "slots": {}}
