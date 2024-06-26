from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.impute import KNNImputer
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
import pandas as pd
from src.Customer_segementation.logger import logger
from src.Customer_segementation.config.configuration import DataTransformationConfig
from sklearn.model_selection import train_test_split

class DataTransformation: 
    def __init__(self, config=DataTransformationConfig) -> None:
        self.config=config

        Gender=['Male', 'Female']
        Ever_Married=['No', 'Yes']
        Graduated=['No', 'Yes']
        Profession=['Healthcare', 'Engineer', 'Lawyer', 'Entertainment', 'Artist','Executive', 'Doctor', 'Homemaker', 'Marketing']
        Spending_Score=['Low', 'Average', 'High']


    def train_test_data_split(self, data: pd.DataFrame):
        """
        method name: train test data split
        description: It divide data into training data and testing dataset.
        """
        data.drop('Var_1', inplace=True, axis=1)
        train_data, test_data=train_test_split(data, test_size=self.config.test_size, 
                                               random_state=self.config.random_state)
        
        # Save train data and test data.

        train_data.to_csv(self.config.train_data_path, index=False, header=True)
        test_data.to_csv(self.config.test_data_path, index=False, header=True)

        


    def get_data_preprocessing(self, cat_data:list, num_data:list):
        """
        method_name: get data preprocessing
        decription: In this method feature engineering pipeline created that handle the missing vlaue and scale data.
        """
        Gender=['Male', 'Female']
        Ever_Married=['No', 'Yes']
        Graduated=['No', 'Yes']
        Profession=['Healthcare', 'Engineer', 'Lawyer', 'Entertainment', 'Artist','Executive', 'Doctor', 'Homemaker', 'Marketing']
        Spending_Score=['Low', 'Average', 'High']

        num_pipeline=Pipeline(
            steps=[
        ("imputer",SimpleImputer()),
        ("scaler",StandardScaler())
        ])
        cat_pipeline=Pipeline([
            ('imputer',SimpleImputer(strategy='most_frequent')),
            ('onehot',OrdinalEncoder(categories=[Gender, Ever_Married, Graduated, Profession, Spending_Score]))])
        
        preprocessor=ColumnTransformer([
            ("num_pipeline",num_pipeline,num_data),
            ("cat_pipeline",cat_pipeline,cat_data)])
        
        return preprocessor
        

        


    def initate_data_transformation(self):
        data=pd.read_csv(self.config.data_dir)
        # logger.info(f"Customer segementation data: {data.head()}")
        
        # drop the Id columns from dataset
        data.drop('ID', inplace=True, axis=1)

        # logger(f"{self.config.test_size}")

        # self.start_preprocessing(data)

        self.train_test_data_split(data=data)

        categorical_data=[feature for feature in data.columns if data[feature].dtypes=='O']
        categorical_data=['Gender', 'Ever_Married', 'Graduated', 'Profession', 'Spending_Score']
        numerical_data=[feature for feature in data.columns if data[feature].dtypes !='O']

        logger.info(f"categorical_data : {categorical_data}")
        logger.info(f"Numerical data: {numerical_data}")

        preprocessing=self.get_data_preprocessing(cat_data=categorical_data, num_data=numerical_data)

        # logger.info(f"Preprocessing model created: {preprocessing}")

        x_train=pd.read_csv(self.config.train_data_path)
        x_test=pd.read_csv(self.config.test_data_path)
        x_train=x_train.iloc[:,:-1]
        x_test=x_test.iloc[:,:-1]
        # logger.info(f"x train remove segmentation: {x_train.head()}")

        x_train_scaled=pd.DataFrame(preprocessing.fit_transform(x_train), columns= preprocessing.get_feature_names_out())
        x_train_scaled.to_csv(self.config.train_data__scaled_path, index=False, header=True)

        x_test_scaled=pd.DataFrame(preprocessing.fit_transform(x_test),columns=preprocessing.get_feature_names_out())
        x_test_scaled.to_csv(self.config.test_data_scaled_path, index=False, header=True)

        # logger.info(f" x_train after scaled {x_train_scaled.head()}")
        logger.info(f" x_test after scaled {x_test_scaled.head()}")





        
        
        # logger.info(f"x_train: {x_train.shape}")
        # logger.info(f" x_test :{x_test.shape}")
        # logger.info(f"y_train: {y_train.shape}")
        # logger.info(f"y_test: {y_test.shape}")    