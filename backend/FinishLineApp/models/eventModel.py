from .. import db
from sqlalchemy import Integer, String, ForeignKey, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship
import validators

class Event(db.Model):
    __tablename__ = 'events'
    id: Mapped[int] = mapped_column(primary_key=True)
    Title: Mapped[str] = mapped_column(nullable=False)
    Host: Mapped[str] = mapped_column(nullable=False)
    Location: Mapped[str] = mapped_column(nullable=False)
    Description: Mapped[str] = mapped_column(nullable=False)
    Link: Mapped[str] = mapped_column(nullable=False)
    Date: Mapped[str] = mapped_column(nullable=False)
    Picture: Mapped[str] = mapped_column(nullable=False)
    WebOrig: Mapped[str] = mapped_column(nullable=False)

    @property
    def image_url(self):
        return self._image_url

    @image_url.setter
    def image_url(self, value: str):
        if not validators.url(value):
            raise ValueError(f"Invalid URL: {value}")
        self._image_url = value