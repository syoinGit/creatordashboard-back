import uuid

from ..db.base import Base
from sqlalchemy import String, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime, timezone


class MUser(Base):
    __tablename__ = "m_users"

    user_id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        comment="ユーザーID(UUID)",
    )

    name: Mapped[str] = mapped_column(String(50), nullable=False, comment="ユーザー名")

    email: Mapped[str] = mapped_column(
        String(255), nullable=True, comment="メールアドレス"
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        comment="作成日",
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        comment="更新日",
    )

    is_deleted: Mapped[bool] = mapped_column(
        Boolean, default=False, comment="削除フラグ"
    )
