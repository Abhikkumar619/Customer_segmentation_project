from src.Customer_segementation.constant import *
from src.Customer_segementation.entity.config_entity import (DataIngestionConfig,
                                                             DataValidationConfig)
from src.Customer_segementation.utils.common import read_yaml, create_directories


class configurationManager: 
    def __init__(self,config_file_path=CONFIG_FILE_PATH,
                 schema_file_path=SCHEMA_FILE_PATH,
                 params_file_path=PARAMS_FILE_PATH):
        self.config=read_yaml(config_file_path)
        self.schema=read_yaml(schema_file_path)
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
    
    def get_Data_validation_config(self)->DataValidationConfig:
        config=self.config.data_validation
        schema=self.schema.COLUMNS
        create_directories([config.root_dir])

        data_validation_config=DataValidationConfig(
            root_dir=config.root_dir,
            data_dir=config.data_dir,
            status_file=config.status_file,
            all_schema=schema
            )
        return data_validation_config
        