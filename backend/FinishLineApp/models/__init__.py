from .eventModel import Event, EventTag, event_tag_association
from datetime import datetime
from .. import db

def db_fill_samples():
    # Clear existing data, including the association table
    db.session.query(event_tag_association).delete()  # Clear the association table
    db.session.query(Event).delete()
    db.session.query(EventTag).delete()
    db.session.commit()

    # Sample Event objects
    events = [
        Event(
            Title="Hackathon 2024",
            Host="Tech University",
            Location="Tech University Campus",
            Description="A 48-hour coding competition for students around the world.",
            Date=datetime(2024, 11, 1, 9, 0, 0),
            Picture="https://example.com/images/hackathon2024.jpg",
            WebOrig="https://hackathon2024.tech.edu"
        ),
        Event(
            Title="AI Conference",
            Host="AI Society",
            Location="Downtown Conference Center",
            Description="A conference discussing the latest advancements in artificial intelligence.",
            Date=datetime(2024, 12, 5, 10, 0, 0),
            Picture="https://example.com/images/ai_conference.jpg",
            WebOrig="https://ai-society.org/conference"
        ),
        Event(
            Title="Startup Pitch Night",
            Host="Entrepreneur Network",
            Location="City Innovation Hub",
            Description="An event for startups to pitch their ideas to investors.",
            Date=datetime(2024, 10, 20, 18, 0, 0),
            Picture="https://example.com/images/pitch_night.jpg",
            WebOrig="https://entrepreneurnetwork.org/pitchnight"
        )
    ]

    # Sample Tag objects
    tags = [
        EventTag(name="Technology"),
        EventTag(name="Artificial Intelligence"),
        EventTag(name="Entrepreneurship"),
        EventTag(name="Competition"),
        EventTag(name="Conference"),
        EventTag(name="Networking"),
        EventTag(name="Education")
    ]

    # Add tags to the session
    db.session.add_all(tags)
    db.session.commit()  # Commit to ensure tags have IDs

    # Associate events with tags, ensuring no duplicates
    events[0].tags = [tags[0], tags[3]]  # "Hackathon 2024" -> "Technology", "Competition"
    events[1].tags = [tags[0], tags[1], tags[4]]  # "AI Conference" -> "Technology", "AI", "Conference"
    events[2].tags = [tags[2], tags[5]]  # "Startup Pitch Night" -> "Entrepreneurship", "Networking"

    # Add events and associate tags
    db.session.add_all(events)
    db.session.commit()  # Commit all changes to the database

def db_verify_sample_data():
    all_events = Event.query.all()
    for event in all_events:
        print(f"Event: {event.Title}")
        print(f"Tags: {[tag.name for tag in event.tags]}")
