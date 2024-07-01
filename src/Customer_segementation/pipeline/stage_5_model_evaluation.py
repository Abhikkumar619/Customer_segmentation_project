from src.Customer_segementation.config.configuration import configurationManager
from src.Customer_segementation.components.model_evaluation import ModelEvaluation
from src.Customer_segementation.logger import logger

stage_name="ModelEvaluation"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        try: 
            configmanager=configurationManager()
            evaluation_config=configmanager.get_model_evaluation_config()
            model_evaluation=ModelEvaluation(evaluation_config)
            model_evaluation.inititate_model_evaluation()
            
        except Exception as e:
            raise e
        
if __name__ =="__main__": 
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> stage {stage_name} started>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    obj=ModelEvaluationPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> stage {stage_name} Completed >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

