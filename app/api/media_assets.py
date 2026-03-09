from fastapi import APIRouter, Depends
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
