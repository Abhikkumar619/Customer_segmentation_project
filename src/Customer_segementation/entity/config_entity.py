from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig: 
    root_dir: Path
    data_path: Path
    mongodb_url: str
    database_name: str
    collection_name: str

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    data_dir: Path
    status_file: Path
    all_schema: dict

@dataclass(frozen=True)
class DataTransformationConfig: 
    root_dir: Path
    data_dir: Path
    train_data__scaled_path: Path
    test_data_scaled_path: Path
    test_size: int
    random_state: int
    train_data_path: Path
    test_data_path: Path
    preprocessor_path: Path


@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    train_data: Path
    test_data: Path
    best_model_path: Path  
    train_not_scaled: Path
    test_not_scaled: Path  
    dim_red_model: Path
    
@dataclass(frozen=True)
class ModelEvaluationConfig:
    data: Path
    model_path: Path
    dim_red_model: Path
