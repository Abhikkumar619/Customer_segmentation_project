from box import ConfigBox
from ensure import ensure_annotations
from pathlib import Path
from src.Customer_segementation.logger import logger
import yaml
import os

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
        