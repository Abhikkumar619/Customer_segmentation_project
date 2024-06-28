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



class ModelTainer:
    def __init__(self, config=ModelTrainerConfig) -> None:
        self.config=config

        self.model={
            'kmean': KMeans(n_clusters=4, init='k-means++')
        }

    def model_evaluation(self, x_train, x_test, y_train, y_test, Model):
        report={}
        dim_red=PCA(n_components=2)
        x_train_scaled=dim_red.fit_transform(x_train)
        x_test_scaled=dim_red.transform(x_test)

        for mod in range(len(Model)): 
            model= list(Model.values())[mod]

            model= model.fit(x_train_scaled)

            y_pred=model.predict(x_test_scaled)

            logger.info(f"Y perdication: {y_pred}")

            score=confusion_matrix(y_test, y_pred)
            # precision_sc=precision_score(y_test, y_pred, average='weighted')

            acc_score=accuracy_score(y_test, y_pred)
            # logger.info(f"Accuracy score: {acc_score}")

            class_report=classification_report(y_test, y_pred)
            # logger.info(f"Classification report\n\n: {class_report}")
            
            # mae=mean_absolute_error(x_test, y_pred)

            logger.info(f"Accuracy Score\n\n: {score}")
            # logger.info(f"precision_score: {precision_score}")

            report[list(Model.keys())[mod]]=acc_score
            # report[list(Model.keys())[mod]]=score
        return (report, model, dim_red)





    def inititate_model_trainer(self):
        train_data=self.config.train_data
        train_not_scaled=self.config.train_not_scaled
        test_not_scaled=self.config.test_not_scaled
        test_data=self.config.test_data

        x= pd.read_csv(train_data)
        x1=pd.read_csv(train_not_scaled)
        x1['Segmentation']=x1['Segmentation'].map({'A':1, 'B':2, 'C':3, 'D':4})

        y1=pd.read_csv(test_not_scaled)
        y1['Segmentation']=y1['Segmentation'].map({'A':1, 'B':2, 'C':3, 'D':4})

        y=pd.read_csv(test_data)

        x_train=x.iloc[:,:-1]
        y_train=x1.iloc[:,-1]

        x_test=y.iloc[:,:-1]
        y_test=y1.iloc[:,-1]

        # logger.info(f"x_: {x_test}")
        # logger.info(f"{y_test}")

        logger.info(f"Model list :{self.model}")

        report, model, dim_red=self.model_evaluation(x_train, x_test, y_train, y_test, self.model)
        logger.info(f"Report of model: {report}")

        save_object(file_path=Path(self.config.best_model_path), obj=model)
        save_object(file_path=Path(self.config.dim_red_model), obj=dim_red)
        

        
        
        
        




