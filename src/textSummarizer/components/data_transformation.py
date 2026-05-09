import os
from textSummarizer.logging import logger
from transformers import AutoTokenizer
from datasets import load_from_disk
from textSummarizer.entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)

    def convert_examples_to_features(self, example_batch):

        inputs = [
            "summarize: " + dialogue.replace("\n", " ")
            for dialogue in example_batch['dialogue']
        ]

        input_encodings = self.tokenizer(
            inputs,
            max_length=1024,
            truncation=True,
            padding="max_length"
        )

        target_encodings = self.tokenizer(
            text_target=example_batch['summary'],
            max_length=128,
            truncation=True,
            padding="max_length"
        )

        return {
            'input_ids': input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }

    def convert(self):
        dataset = load_from_disk(self.config.data_path)

        dataset = dataset.map(
            self.convert_examples_to_features,
            batched=True
        )

        output_path = os.path.join(self.config.root_dir, "samsum_dataset")
        dataset.save_to_disk(output_path)

        logger.info("Data transformation completed ✅")