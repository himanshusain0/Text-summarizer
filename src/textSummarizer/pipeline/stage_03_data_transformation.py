from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_transformation import DataTransformation
from textSummarizer.logging import logger


class DataTransformationTrainingPipeline:
    def main(self):
        try:
            logger.info("Stage 03: Data Transformation started")

            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()

            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.convert()

            logger.info("Stage 03: Data Transformation completed ✅")

        except Exception as e:
            logger.exception(e)
            raise e