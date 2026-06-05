from transformers import pipeline
import torch

MODEL_NAME = "sshleifer/distilbart-cnn-12-6"

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

        word_count = len(text.split())
        if word_count < 20:
            return "Text too short. Please provide at least 20 words."

        max_len = min(150, max(30, word_count // 2))
        min_len = min(30, word_count // 4)

        result = self.summarizer(
            text,
            max_length=max_len,
            min_length=min_len,
            do_sample=False
        )
        return result[0]["summary_text"]