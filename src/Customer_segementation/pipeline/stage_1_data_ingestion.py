from src.Customer_segementation.config.configuration import configurationManager
from src.Customer_segementation.components.data_ingestion import DataIngestion
from src.Customer_segementation.logger import logger

stage_name="DataIngestion"

class DataIngestionPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        try: 
            configmanger=configurationManager()
            dataingestion_config=configmanger.get_data_ingestion_config()
            data_ingestion=DataIngestion(dataingestion_config)
            data_ingestion.import_data_into_feature_store_file_system()
        except Exception as e:
            raise e
        
    
if __name__ =="__main__":
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> stage {stage_name} started>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    obj=DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> stage {stage_name} Completed >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

