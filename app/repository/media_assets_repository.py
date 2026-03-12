import shutil

from fastapi import UploadFile
from sqlalchemy.orm import Session

from ..service import service
from ..models import TMediaAsset, TUploadJob
from pathlib import Path


def get_media_assets(
    db: Session    
):
    return db.query(TMediaAsset).all()

def get_upload_jobs(
    db: Session,
    job_id: str
):
    return db.query(TUploadJob).filter(TUploadJob.job_id == job_id).first()

def upload_media_asset_job(
    file: UploadFile,
    db: Session
):
    
    job = TUploadJob(
        file_name=file.filename,
        storage_path="仮",
        created_user_id="a6272b14-092a-4663-8309-0503aed614e2",
        updated_user_id="a6272b14-092a-4663-8309-0503aed614e2"
    )
    
    db.add(job)
    db.flush()
    
    job.storage_path = str(service.generate_temp_file_path(job.file_name, str(job.job_id)))
    service.save_upload_file_to_temp(file, Path(job.storage_path))
    
    db.add(job)
    db.commit()
    db.refresh(job)
    
    return job

def register_media_asset(
    job,
):
    media_asset = TMediaAsset(
        original_file_name=job.file_name,
        storage_path=job.storage_path,
        saved_file_name="仮",
        mime_type="application/octet-stream",
        file_size=0,
        memo="",
        created_user_id="a6272b14-092a-4663-8309-0503aed614e2",
        updated_user_id="a6272b14-092a-4663-8309-0503aed614e2"
    )
    
    src_path = Path(job.storage_path)
    dest_path = Path("storage/media") / str(job.job_id) / media_asset.original_file_name
    
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(src_path), str(dest_path))

    return media_asset