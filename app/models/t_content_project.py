import uuid

from ..db.base import Base
from sqlalchemy import String, DateTime, Text, Boolean, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime


class TContentProject(Base):
    __tablename__ = "t_content_projects"

    project_id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        comment="動画企画ID",
    )

    project_name: Mapped[str] = mapped_column(
        String(50), nullable=False, comment="動画企画名"
    )

    project_summry: Mapped[str] = mapped_column(Text, nullable=True, comment="企画概要")

    created_user_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("m_users.user_id"), nullable=False, comment="作成者"
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
