from sqlalchemy import MetaData, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

from database import Base


# class Base(DeclarativeBase):
#     metadata = MetaData()


class Post(Base):
    __tablename__ = "post"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    title: Mapped[str] = mapped_column(nullable=False)
    number_of_likes: Mapped[int] = mapped_column(default=0)
    owner_id: Mapped[int] = mapped_column(
        ForeignKey("user.id", ondelete="CASCADE"), nullable=False
    )
