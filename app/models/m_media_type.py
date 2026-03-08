import uuid

from ..db.base  import Base
from sqlalchemy import String, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime, timezone

class MMediaType (Base):
    __tablename__ = "m_media_types"
    
    media_type_id: Mapped[str] = mapped_column(
    String(36),
    primary_key=True,
    default=lambda: str(uuid.uuid4()),
    comment="素材タイプID"
    )
    
    media_type_name: Mapped[str] = mapped_column(
    String(50),
    nullable=False,
    unique=True,
    comment="素材タイプ名"
    )
    
    description: Mapped[str] = mapped_column(
    String(100),
    comment="素材タイプの説明"
    )
    
    created_user_id: Mapped[str] = mapped_column(
        String(36),
        nullable=False,
        comment='作成者'
        )
    
    updated_user_id: Mapped[str] = mapped_column(
        String(36),
        nullable=False,
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
