
from sklearn.metrics import silhouette_score
import dagshub
import mlflow
from urllib.parse import urlparse
from pathlib import Path
from src.Customer_segementation.utils.common import load_object
from src.Customer_segementation.config.configuration import ModelEvaluationConfig
import pandas as pd

class ModelEvaluation:
    def __init__(self, config=ModelEvaluationConfig):
        self.config=config

    def evluation_matrix_for_mlflow(self, model, train_data): 
        dagshub.init(repo_owner='Abhikkumar619', repo_name='Customer_segmentation_project', mlflow=True)
        mlflow.set_registry_uri('https://dagshub.com/Abhikkumar619/Customer_segmentation_project.mlflow')
        tracking_url_type_store=urlparse(mlflow.get_tracking_uri()).scheme
        print(tracking_url_type_store)


        with mlflow.start_run():
            prediction=model.predict(train_data)
            sil_score=silhouette_score(train_data ,model.labels_)
            mlflow.log_metric("silhouette_score",sil_score)

            if tracking_url_type_store !='file': 
                    mlflow.sklearn.log_model(model, "model", registered_model_name="ml_model")
            else: 
                mlflow.sklearn.log_model(model, "model")


    def inititate_model_evaluation(self):
        try: 
            # Load model from artifacts.
            model=load_object(Path(self.config.model_path))
            dim_model=load_object(Path(self.config.dim_red_model))
            
            x=pd.read_csv(self.config.data)

            dim_train=dim_model.transform(x)

            self.evluation_matrix_for_mlflow(model, dim_train)

           
        except Exception as e: 
            raise


