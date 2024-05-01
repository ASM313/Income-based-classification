from src.incomeClassifier import logger
from src.incomeClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.incomeClassifier.pipeline.stage_02_data_validation import  DataValidationTrainingPipeline

logger.info("Logging has started")



if __name__ == '__main__':
    STAGE_NAME = "Data Ingestion stage"
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e

    
    STAGE_NAME = "Data Validation stage"
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
        data_ingestion = DataValidationTrainingPipeline()
        data_ingestion.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e



    # STAGE_NAME = "Data Transformation stage"
    # try:
    # logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
    # data_ingestion = DataTransformationTrainingPipeline()
    # data_ingestion.main()
    # logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    # except Exception as e:
    #         logger.exception(e)
    #         raise e



    # STAGE_NAME = "Model Trainer stage"
    # try:
    # logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
    # data_ingestion = ModelTrainerTrainingPipeline()
    # data_ingestion.main()
    # logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    # except Exception as e:
    #         logger.exception(e)
    #         raise e



    # STAGE_NAME = "Model evaluation stage"
    # try:
    # logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
    # data_ingestion = ModelEvaluationTrainingPipeline()
    # data_ingestion.main()
    # logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    # except Exception as e:
    #         logger.exception(e)
    #         raise e