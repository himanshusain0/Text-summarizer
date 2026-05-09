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