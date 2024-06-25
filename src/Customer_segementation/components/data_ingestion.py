from src.Customer_segementation.config.configuration import DataIngestionConfig
from pymongo.mongo_client import MongoClient
from src.Customer_segementation.logger import logger
import pandas as pd


class DataIngestion: 
    def __init__(self,config=DataIngestionConfig):
        self.config=config


    def import_collection_as_DataFrame(self, database_name: str,
                                        collection_name: str, mongodb_uri: str):
        try: 
            client=MongoClient(mongodb_uri)

            collection_name=client[database_name][collection_name]

            data=pd.DataFrame(list(collection_name.find()))
            
            for col in data.columns: 
                if col =='_id':
                    data.drop('_id', axis=1, inplace=True)
            
            return data


        except Exception as e:
            raise e

    def import_data_into_feature_store_file_system(self):
        """
        Method_name: Import data into feature store file.
        Description: This method import data from mongodb and save into artifacts folder.

        outPut: data return as DataFrame
        onfailure: Write exception log and raise exception.
        """

        try: 
            logger.info("Importing DataFrame from Mongodb")
            data=self.import_collection_as_DataFrame(database_name=self.config.database_name,
                                                collection_name=self.config.collection_name,
                                                mongodb_uri=self.config.mongodb_url
                                                )
            
            data.to_csv(self.config.data_path, header=True, index=False)

        except Exception as e: 
            raise e
