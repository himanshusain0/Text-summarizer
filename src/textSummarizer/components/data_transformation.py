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

        # ✅ Input tokenization
        input_encodings = self.tokenizer(
            example_batch['dialogue'],
            max_length=1024,
            truncation=True,
            padding="max_length"
        )

        # ✅ Target tokenization (FIXED - new transformers way)
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
        logger.info("Loading dataset from disk...")
        dataset_samsum = load_from_disk(self.config.data_path)

        logger.info("Starting data transformation...")
        dataset_samsum_pt = dataset_samsum.map(
            self.convert_examples_to_features,
            batched=True
        )

        output_path = os.path.join(self.config.root_dir, "samsum_dataset")

        logger.info(f"Saving transformed dataset at {output_path} ...")
        dataset_samsum_pt.save_to_disk(output_path)

        logger.info("Data transformation completed successfully ✅")