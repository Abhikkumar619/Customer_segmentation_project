import os
from src.Customer_segementation.utils.common import load_object
from src.Customer_segementation.logger import logger


from src.Customer_segementation.utils.common import load_object
from src.Customer_segementation.logger import logger
from pathlib import Path
import pandas as pd


class PrediPipeline: 
    def __init__(self):
        pass
    def predict(self, user_dataframe):
        try: 
            
            preprocessor=load_object(Path('artifacts/data_transformation/preprocessor.pkl'))
            dim_red_model=load_object(Path('artifacts/model_trainer/dim_red.h5'))
            model=load_object(Path("artifacts/model_trainer/best_Model.h5"))

            # logger.info(f"Model load sucessfully: {preprocessor}")

            preprocess_data=preprocessor.transform(user_dataframe)
            data_for_dimred=pd.DataFrame(preprocess_data, columns=preprocessor.get_feature_names_out())

            logger.info(f"Data for dim reduction: {data_for_dimred}")

            dim_red_data=dim_red_model.transform(data_for_dimred)
            logger.info(f"Data after dimension reduction: {dim_red_data}")
            pred=model.predict(dim_red_data)
            
            return pred

        except Exception as e:
            raise e
        
class CustomData: 
    def __init__(self, Gender, 
                 Ever_Married, 
                 Age,
                 Graduated, 
                 Profession, 
                 Work_Experience,
                 Spending_Score,
                 Family_Size):
        self.Gender=Gender
        self.Ever_Married=Ever_Married
        self.Age=Age
        self.Graduated=Graduated
        self.Profession=Profession
        self.Work_Experience=Work_Experience
        self.Spending_Score=Spending_Score
        self.Family_Size=Family_Size

    def get_data_as_dataframe(self):
        try: 
            custom_data_input_dict={
                'Gender':[self.Gender],
                'Ever_Married':[self.Ever_Married],
                'Age':[self.Age],
                'Graduated':[self.Graduated],
                'Profession':[self.Profession],
                'Work_Experience':[self.Work_Experience],
                'Spending_Score': [self.Spending_Score],
                'Family_Size':[self.Family_Size]
                }
            
            df=pd.DataFrame(custom_data_input_dict)
            # df.to_csv('artifacts/data_ingestion/user_data.csv', index=False, header=True)
            logger.info(f"DataGather\n\n: {df}")

            return df
        except Exception as e:
            raise e


        
