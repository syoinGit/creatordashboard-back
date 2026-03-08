import uuid

from ..db.base  import Base 
from sqlalchemy import String, Integer, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime, timezone

class TMediaAsset (Base):
    __tablename__ = "t_media_assets"
    
    media_asset_id: Mapped[str] = mapped_column(
    String(36),
    primary_key=True,
    default=lambda: str(uuid.uuid4()),
    comment="動画素材ID"
    )
    
    media_type_id: Mapped[str] = mapped_column(
    String(36),
    ForeignKey("m_media_types.media_type_id"),
    nullable=False,
    comment="素材タイプID"
    )
    
    original_file_name: Mapped[str] = mapped_column(
    String(100),
    nullable=False,
    comment="アップロードファイル名"
    )
    
    saved_file_name: Mapped[str] = mapped_column(
    String(100),
    nullable=False,
    comment="登録ファイル名"
    )
    
    storage_path: Mapped[str] = mapped_column(
    String(1000),
     nullable=False,
    comment="保存ストレージパス"
    )
    
    file_size: Mapped[int] = mapped_column(
    Integer,
    nullable=False,
    comment="ファイルサイズ"
    )
    
    memo: Mapped[str] = mapped_column(
    String(1000),
    nullable=True,
    comment="メモ"
    )
    
    created_user_id: Mapped[str] = mapped_column(
        String(36),
        nullable=True,
        comment='作成者'
        )
    
    pdated_user_id: Mapped[str] = mapped_column(
        String(36),
        nullable=True,
        comment='更新者'
        )
    
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        comment='作成日'
        )
    
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        comment='更新日'
        )
    
    is_deleted: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        comment="削除フラグ"
    )