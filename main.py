from src.incomeClassifier import logger
from src.incomeClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

logger.info("Logging has started")

STAGE_NAME = "Data Ingestion stage"

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e