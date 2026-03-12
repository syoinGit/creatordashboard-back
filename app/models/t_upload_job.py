import uuid

from ..core.base import Base
from sqlalchemy import String, DateTime, ForeignKey, Boolean, func
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime


class TUploadJob(Base):
    __tablename__ = "t_upload_jobs"

    job_id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        comment="アップロードジョブID",
    )
    
    file_name: Mapped[str] = mapped_column(
        String(100), nullable=False, comment="登録ファイル名"
    )

    storage_path: Mapped[str] = mapped_column(
        String(1000), nullable=False, comment="保存ストレージパス"
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
