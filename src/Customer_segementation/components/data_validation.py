from src.Customer_segementation.entity.config_entity import DataValidationConfig
from src.Customer_segementation.logger import logger
import pandas as pd



class DataValidation:
    def __init__(self, config=DataValidationConfig):
        self.config=config

    def validation_all_columns(self):
        """
        Method_name: validation all  columns
        Description: This method validate all columns like data comming from database and columns use for model.

        output: function return txt file, it columns all right than return True otherwise false.
        on failure: write exception log and raise exception.
        """
        logger.info(f"Data validation started in data validation class")
        try: 
            validation_satus=None
            data=pd.read_csv(self.config.data_dir)
            logger.info(f"Customer segemntaion data: {data.head()}")

            all_columns=list(data.columns)
            logger.info(f"All Columns of data {all_columns}")

            logger.info(f"All schema data: {self.config.all_schema}")

            schema=list(self.config.all_schema.keys())

            logger.info(f"Actual schema : {schema}")

            for col in all_columns: 
                if col not in schema:
                    validation_satus=False
                    with open(self.config.status_file,'w') as f: 
                        f.write(f"Validation status: {validation_satus}")

                else: 
                    validation_satus=True
                with open(self.config.status_file,'w') as f: 
                    f.write(f"Validation status: {validation_satus}")

        except Exception as e: 
            raise e