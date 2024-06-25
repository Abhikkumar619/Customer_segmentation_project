from src.Customer_segementation.constant import *
from src.Customer_segementation.entity.config_entity import DataIngestionConfig
from src.Customer_segementation.utils.common import read_yaml, create_directories


class configurationManager:
    def __init__(self, config_file_path=CONFIG_FILE_PATH, 
                 params_file_path=PARAMS_FILE_PATH):
        self.config=read_yaml(config_file_path)
        self.params=read_yaml(params_file_path)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self)-> DataIngestionConfig:
        config=self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            mongodb_url=config.mongodb_url,
            database_name=config.DATABASE_NAME,
            collection_name=config.COLLECTION_NAME

        )
        return data_ingestion_config