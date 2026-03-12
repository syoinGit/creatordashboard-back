import uuid
from pathlib import Path

from fastapi import UploadFile
from sqlalchemy.orm import Session
import shutil

TEMP_DIR = Path("temp")

def generate_temp_file_path(filename: str, uuid: str) -> Path:
    safe_filename = Path(filename).name
    return TEMP_DIR / str(uuid) / safe_filename

def save_upload_file_to_temp(file: UploadFile, file_path: Path):
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)