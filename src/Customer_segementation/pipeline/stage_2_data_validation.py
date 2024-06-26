from src.Customer_segementation.config.configuration import configurationManager
from src.Customer_segementation.components.data_validation import DataValidation
from src.Customer_segementation.logger import logger

stage_name="Data_validation"

class DataValidationPipeline: 
    def __init__(self) -> None:
        pass

    def main(self):
        try: 
            configmanger=configurationManager()
            data_validationConfig=configmanger.get_Data_validation_config()
            data_validation=DataValidation(data_validationConfig)
            data_validation.validation_all_columns()
        except Exception as e: 
            raise e

if __name__ == "__main__":
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> stage {stage_name} started>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    obj=DataValidationPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> stage {stage_name} Completed >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

