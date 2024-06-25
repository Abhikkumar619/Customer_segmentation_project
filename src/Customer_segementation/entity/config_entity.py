from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig: 
    root_dir: Path
    data_path: Path
    mongodb_url: str
    database_name: str
    collection_name: str