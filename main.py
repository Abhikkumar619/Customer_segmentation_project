from src.Customer_segementation.pipeline.stage_1_data_ingestion import DataIngestionPipeline
from src.Customer_segementation.logger import logger

stage_name="DataIngestion"

if __name__ =="__main__":
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> stage {stage_name} started>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    obj=DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> stage {stage_name} Completed >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

