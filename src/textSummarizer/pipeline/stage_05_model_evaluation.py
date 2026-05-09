from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.model_evaluation import ModelEvaluation
from textSummarizer.logging import logger


class ModelEvaluationTrainingPipeline:
    def main(self):
        try:
            logger.info("Stage 05: Model Evaluation started")

            config = ConfigurationManager()
            model_eval_config = config.get_model_evaluation_config()

            model_eval = ModelEvaluation(config=model_eval_config)
            model_eval.evaluate()

            logger.info("Stage 05: Model Evaluation completed ✅")

        except Exception as e:
            logger.exception(e)
            raise e