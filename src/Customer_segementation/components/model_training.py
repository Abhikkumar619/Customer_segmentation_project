from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA
import pandas as pd
from src.Customer_segementation.logger import logger
from sklearn.metrics import confusion_matrix, precision_score, accuracy_score, classification_report
from src.Customer_segementation.utils.common import save_object
from pathlib import Path
from src.Customer_segementation.entity.config_entity import ModelTrainerConfig
from sklearn.metrics import silhouette_score


class ModelTainer:
    def __init__(self, config=ModelTrainerConfig) -> None:
        self.config=config

        self.model={
            'kmean': KMeans(n_clusters=4, init='k-means++')
        }

    def model_evaluation(self, x_train, x_test, Model):
        report={}
        dim_red=PCA(n_components=2)
        x_train_scaled=dim_red.fit_transform(x_train)
        x_test_scaled=dim_red.transform(x_test)

        save_object(file_path=Path(self.config.dim_red_model), obj=dim_red)
        
        for mod in range(len(Model)): 
            model= list(Model.values())[mod]

            model= model.fit(x_train_scaled)

            logger.info(f"Labels: {model.labels_}")
            sil_score=silhouette_score(x_train,model.labels_)

            logger.info(f"silhouette_score of kmean: {sil_score}")

           
            report[list(Model.keys())[mod]]=silhouette_score
            # report[list(Model.keys())[mod]]=score
        return (report,model)
        
    def inititate_model_trainer(self):
        train_data=self.config.train_data
        test_data=self.config.test_data

        train= pd.read_csv(train_data)
        test=pd.read_csv(test_data)


        # logger.info(f"x_: {train}")
        # logger.info(f"{test}")

        # logger.info(f"Model list :{self.model}")

        (report,model)=self.model_evaluation(train, test, self.model)
        logger.info(f"Report of model: {report}")

        save_object(file_path=Path(self.config.best_model_path), obj=model)
        # save_object(file_path=Path(self.config.dim_red_model), obj=dim_red)
        
