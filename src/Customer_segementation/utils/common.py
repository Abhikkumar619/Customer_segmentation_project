from box import ConfigBox
from ensure import ensure_annotations
from pathlib import Path
from src.Customer_segementation.logger import logger
import yaml
import os
import pickle

@ensure_annotations
def read_yaml(yaml_path: Path)->ConfigBox: 
    with open(yaml_path) as yaml_file: 
        content=yaml.safe_load(yaml_file)
    logger.info(f"Yaml file read {yaml_path} successfully") 
        
    return ConfigBox(content)

@ensure_annotations
def create_directories(dir_path: list):
    for path in dir_path: 
        os.makedirs(path, exist_ok=True) 
        logger.info(f"Directories created {dir_path}")

@ensure_annotations
def save_object(file_path: Path, obj: object):
    try:
        with open(file_path, 'wb') as file_path: 
            pickle.dump(obj, file_path)
            logger.info(f"Object save at: {file_path}")
    except Exception as e: 
        raise e
    
@ensure_annotations
def load_object(file_path:Path): 
    try: 
        with open(file_path, 'rb') as file_obj: 
            model=pickle.load(file_obj)
            logger.info(f"object load sucessfully from path: {file_path}")
            return model

    except Exception as e:
        raise e

        