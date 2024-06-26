from src.Customer_segementation.config.configuration import configurationManager
from src.Customer_segementation.components.data_transformation import DataTransformation
from src.Customer_segementation.logger import logger

stage_name="DataTransformation"

class DataTransformationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        try: 
            configmanager=configurationManager()
            transformation_config=configmanager.get_data_transformation_config()
            # logger.info(f"{transformation_config}")
            data_transformation=DataTransformation(transformation_config)
            data_transformation.initate_data_transformation()

        except Exception as e: 
            raise e
        
if __name__ == "__main__":
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> stage {stage_name} started>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    obj=DataTransformationPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> stage {stage_name} Completed >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

