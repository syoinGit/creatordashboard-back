import uuid
from .base  import Base
 
from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime, timezone

class MUser (Base):
    __tablename__ = "m_users"
    
    user_id: Mapped[str] = mapped_column(
    String(36),
    primary_key=True,
    default=lambda: str(uuid.uuid4()),
    comment="ユーザーID(UUID)"
    )
    
    name: Mapped[str] = mapped_column(
    String(50),
    nullable=False,
    comment="ユーザー名"
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
    