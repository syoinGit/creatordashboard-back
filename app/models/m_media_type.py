import uuid

from ..core.base import Base
from sqlalchemy import String, DateTime, Boolean, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime


class MMediaType(Base):
    __tablename__ = "m_media_types"

    media_type_id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        comment="素材タイプID",
    )

    media_type_name: Mapped[str] = mapped_column(
        String(50), nullable=False, unique=True, comment="素材タイプ名"
    )

    description: Mapped[str] = mapped_column(
        String(100), nullable=True, comment="素材タイプの説明"
    )

    created_user_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("m_users.user_id"), nullable=False, comment="作成者"
    )

    updated_user_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("m_users.user_id"), nullable=False, comment="更新者"
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        comment="作成日",
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        comment="更新日",
    )

    is_deleted: Mapped[bool] = mapped_column(
        Boolean, default=False, index=True, comment="削除フラグ"
    )
