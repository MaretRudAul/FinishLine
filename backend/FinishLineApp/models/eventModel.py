from .. import db
from sqlalchemy import Integer, String, ForeignKey, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship
import validators

event_tag_association = Table(
    'event_tag_association',
    db.Model.metadata,
    db.Column('event_id', ForeignKey('events.id'), primary_key=True),
    db.Column('tag_id', ForeignKey('eventTags.id'), primary_key=True)
)


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

    tags: Mapped[list['EventTag']] = relationship(
        "EventTag",
        secondary="event_tag_association",
        back_populates="events"
    )

    @property
    def image_url(self):
        return self._image_url

    @image_url.setter
    def image_url(self, value: str):
        if not validators.url(value):
            raise ValueError(f"Invalid URL: {value}")
        self._image_url = value


class EventTag(db.Model):
    __tablename__ = 'eventTags'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)

    events: Mapped[list['Event']] = relationship(
        "Event",
        secondary="event_tag_association",
        back_populates="tags"
    )

    def __repr__(self) -> str:
        return f"<Tag(id={self.id}, name='{self.name}')>"
