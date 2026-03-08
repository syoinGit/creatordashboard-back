import uuid
from .base  import Base
 
from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime, timezone

class T_media_asset (Base):
    __tablename__ = "t_media_asset"


media_asset_id: Mapped[str] = mapped_column(
    String(36),
    primary_key=True,
    default=lambda: str(uuid.uuid4()),
    comment="動画素材ID"
    )

media_type_id: Mapped[str] = mapped_column(
    String(36),
    ForeignKey("media_type_id"),
    nullable=True,
    comment="素材タイプID"
    )

original_file_name: Mapped[str] = mapped_column(
    String(100),
    nullable=True,
    comment="アップロードファイル名"
    )

saved_file_name: Mapped[str] = mapped_column(
    String(100),
    nullable=True,
    comment="登録ファイル名"
    )

storage_path: Mapped[str] = mapped_column(
    String(1000),
     nullable=True,
    comment="保存ストレージパス"
    )

file_size: Mapped[str] = mapped_column(
    String(100),
    nullable=True,
    comment="ファイルサイズ"
)

file_size: Mapped[str] = mapped_column(
    String(100),
    nullable=True,
    comment="ファイルサイズ"
)

memo: Mapped[str] = mapped_column(
    String(1000),
    comment="メモ"
)

created_user_id: Mapped[str] = mapped_column(
        String(36),
        nullable=True,
        comment='作成者'
        )

updated_user_id: Mapped[str] = mapped_column(
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
