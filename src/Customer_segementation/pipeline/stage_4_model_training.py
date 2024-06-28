from src.Customer_segementation.config.configuration import configurationManager
from src.Customer_segementation.components.model_training import ModelTainer
from src.Customer_segementation.logger import logger

stage_name="ModelTraining"

class ModelTraningPipeline: 
    def __init__(self) -> None:
        pass
    def main(self):
        try: 
            config_manager=configurationManager()
            model_trainer_config=config_manager.get_model_trainer_config()
            model_trainer=ModelTainer(model_trainer_config)
            model_trainer.inititate_model_trainer()
        except Exception as e:
            raise e
        
if __name__ =="__main__": 
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> stage {stage_name} started>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    obj=ModelTraningPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> stage {stage_name} Completed >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

