from .. import db
from sqlalchemy import Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
import validators

# Association table for the many-to-many relationship
event_tag_association = Table(
    'event_tag_association',
    db.Model.metadata,
    db.Column('event_id', ForeignKey('events.id'), primary_key=True),
    db.Column('tag_id', ForeignKey('eventTags.id'), primary_key=True)  # Updated to match the table name
)

# Event model
class Event(db.Model):
    __tablename__ = 'events'
    id: Mapped[int] = mapped_column(primary_key=True)
    Title: Mapped[str] = mapped_column(nullable=False)
    Host: Mapped[str] = mapped_column(nullable=False)
    Location: Mapped[str] = mapped_column(nullable=False)
    Description: Mapped[str] = mapped_column(nullable=False)
    Date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    Picture: Mapped[str] = mapped_column(nullable=False)
    WebOrig: Mapped[str] = mapped_column(nullable=False)

    # Use a string-based reference to the Tag model
    tags: Mapped[list['EventTag']] = relationship(
        "EventTag",  # Updated to match the correct class name
        secondary="event_tag_association",  # Association table
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


# EventTag model
class EventTag(db.Model):
    __tablename__ = 'eventTags'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)

    # Use a string-based reference to the Event model
    events: Mapped[list['Event']] = relationship(
        "Event",  # Updated to match the correct class name
        secondary="event_tag_association",  # Association table
        back_populates="tags"
    )

    def __repr__(self) -> str:
        return f"<Tag(id={self.id}, name='{self.name}')>"
