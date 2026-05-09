from transformers import pipeline
import torch

MODEL_NAME = "philschmid/bart-large-cnn-samsum"

class PredictionPipeline:
    def __init__(self):
        device = 0 if torch.cuda.is_available() else -1
        self.summarizer = pipeline(
            "summarization",
            model=MODEL_NAME,
            device=device
        )

    def predict(self, text: str) -> str:
        text = text.strip()
        result = self.summarizer(
            text,
            max_length=150,
            min_length=30,
            do_sample=False,
            no_repeat_ngram_size=3
        )
        return result[0]["summary_text"]