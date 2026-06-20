import sys
from pathlib import Path

# Allow `python src/textSummarizer/pipeline/stage_01_data_ingestion.py`
sys.path.append(str(Path(__file__).resolve().parents[3]))

from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_ingestion import DataIngestion
from textSummarizer.logging import logger


class DataIngestionTrainingPipeline:
    def main(self):
        try:
            logger.info("Stage 01: Data Ingestion started")

            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()

            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()

            logger.info("Stage 01: Data Ingestion completed ✅")

        except Exception as e:
            logger.exception(e)
            raise e