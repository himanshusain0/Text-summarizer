import sys
from pathlib import Path

# Allow `python src/textSummarizer/pipeline/stage_04_model_trainer.py`
sys.path.append(str(Path(__file__).resolve().parents[3]))

from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.model_trainer import ModelTrainer
from textSummarizer.logging import logger


class ModelTrainerTrainingPipeline:
    def main(self):
        try:
            logger.info("Stage 04: Model Training started")

            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()

            model_trainer = ModelTrainer(config=model_trainer_config)
            model_trainer.train()

            logger.info("Stage 04: Model Training completed ✅")

        except Exception as e:
            logger.exception(e)
            raise e