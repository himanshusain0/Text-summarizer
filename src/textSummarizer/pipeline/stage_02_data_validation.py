import sys
from pathlib import Path

# Allow `python src/textSummarizer/pipeline/stage_02_data_validation.py`
sys.path.append(str(Path(__file__).resolve().parents[3]))

from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_validation import DataValidation
from textSummarizer.logging import logger


class DataValidationTrainingPipeline:
    def main(self):
        try:
            logger.info("Stage 02: Data Validation started")

            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()

            data_validation = DataValidation(config=data_validation_config)
            status = data_validation.validate_all_files_exist()

            logger.info(f"Validation Status: {status}")

            logger.info("Stage 02: Data Validation completed ✅")

        except Exception as e:
            logger.exception(e)
            raise e