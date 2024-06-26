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