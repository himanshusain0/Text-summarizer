import os
from textSummarizer.logging import logger
from textSummarizer.entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_files_exist(self) -> bool:
        try:
            data_path = os.path.join("artifacts", "data_ingestion", "samsum_dataset")
            all_files = os.listdir(data_path)

            validation_status = all(
                file in all_files for file in self.config.ALL_REQUIRED_FILES
            )

            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation status: {validation_status}")

            logger.info(f"Validation status: {validation_status}")
            return validation_status
        
        except Exception as e:
            raise e