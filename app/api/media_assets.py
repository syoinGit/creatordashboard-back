from fastapi import APIRouter, Depends, File, UploadFile, BackgroundTasks
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..models import TMediaAsset
from ..repository import media_assets_repository

router = APIRouter(prefix="/media-assets", tags=["media-assets"])

@router.get("/")
def get_media_assets(
    db: Session = Depends(get_db),    
):
    return media_assets_repository.get_media_assets(db)
                                     
                                            
@router.post("/register")
def register_media(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    job = media_assets_repository.upload_media_asset_job(file, db)
    background_tasks.add_task(media_assets_repository.register_media_asset,job)
    
    return {"message": "Media asset registration started", "job_id": job.job_id}


@router.get("/{job_id}")
def get_upload_job_status(
    job_id: str,
    db: Session = Depends(get_db)
):
    return media_assets_repository.get_upload_jobs(db, job_id)
