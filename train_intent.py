import pandas as pd
from datasets import Dataset
from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification, Trainer, TrainingArguments
import torch


df = pd.read_csv("backend/data.csv")  
intent_mapping = {"open_url": 0, "open_app": 1, "scroll_down": 2}
df["intent"] = df["intent"].map(intent_mapping)


dataset = Dataset.from_pandas(df)

tokenizer = DistilBertTokenizerFast.from_pretrained("distilbert-base-uncased")

def tokenize(batch):
    return tokenizer(batch["text"], padding=True, truncation=True)

dataset = dataset.map(tokenize, batched=True)


dataset = dataset.rename_column("intent", "labels")


def cast_labels(example):
    example["labels"] = int(example["labels"])
    return example

dataset = dataset.map(cast_labels)


dataset.set_format("torch", columns=["input_ids", "attention_mask", "labels"])


num_labels = len(intent_mapping)
model = DistilBertForSequenceClassification.from_pretrained(
    "distilbert-base-uncased",
    num_labels=num_labels,
    problem_type="single_label_classification"
)


training_args = TrainingArguments(
    output_dir="./backend/intent_model", 
    num_train_epochs=5,
    per_device_train_batch_size=8,
    logging_dir="./logs",
    logging_steps=1,
    save_strategy="epoch",
    report_to="none",          
)


trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
)


trainer.train()


model.save_pretrained("./backend/intent_model")
tokenizer.save_pretrained("./backend/intent_model")

print("Training complete! Model saved to backend/intent_model")
