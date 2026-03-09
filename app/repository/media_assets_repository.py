from sqlalchemy.orm import Session
from ..models.t_media_asset import TMediaAsset

def get_media_assets(
    db: Session    
):
    return db.query(TMediaAsset).all()
