from .eventModel import Event
from datetime import datetime
from .. import db
from FinishLineApp.tasks import scrape_anchorlink
import re

events = [
    Event(
        Title="Hackathon 2024",
        Host="Tech University",
        Location="Tech University Campus",
        Description="A 48-hour coding competition for students around the world.",
        Link='RandomLinkA',
        Date="RandomDate1",
        Picture="https://example.com/images/hackathon2024.jpg",
        WebOrig="https://hackathon2024.tech.edu"
    ),
    Event(
        Title="AI Conference",
        Host="AI Society",
        Location="Downtown Conference Center",
        Description="A conference discussing the latest advancements in artificial intelligence.",
        Link='RandomLinkB',
        Date="RandomDate2",
        Picture="https://example.com/images/ai_conference.jpg",
        WebOrig="https://ai-society.org/conference"
    ),
    Event(
        Title="Startup Pitch Night",
        Host="Entrepreneur Network",
        Location="City Innovation Hub",
        Description="An event for startups to pitch their ideas to investors.",
        Link='RandomLinkC',
        Date="RandomDate3",
        Picture="https://example.com/images/pitch_night.jpg",
        WebOrig="https://entrepreneurnetwork.org/pitchnight"
    )
]

def db_fill_samples():
    db.session.query(Event).delete()
    db.session.commit()

    db.session.add_all(events)
    db.session.commit()

def db_verify_sample_data():
    all_events = Event.query.all()
    for event in all_events:
        print(f"Event: {event.Title}")

def convert_to_custom_format(date_string: str) -> str:
    try:
        cleaned_string = re.sub(r"\s+to\s*$", "", date_string)
        cleaned_string = re.sub(r"\s\w{3}$", "", cleaned_string)
        dt = datetime.strptime(cleaned_string, "%A, %B %d %Y at %I:%M %p")
        formatted_string = dt.strftime("%I:%M %A, %m/%d/%Y")
        formatted_string = re.sub(r'^0', '', formatted_string)

        return formatted_string
    except:
        return str

def is_career_related(description):
    career_keywords = [
    "job",
    "career",
    "employ",
    "network",
    "growth",
    "opportunit",
    "skill",
    "resume",
    "interview",
    "planning",
    "remote",
    "freelance",
    "salar",
    "advancement",
    "search",
    "balance",
    "develop",
    "leadership",
    "transition",
    "industr"
]

    for word in career_keywords:
        if word in description.lower():
            return True


def db_fill_with_scrape():
    data = scrape_anchorlink()
    for item in data:

        if not is_career_related(item['desc']):
            continue

        event = Event(
            Title=item['title'],
            Host=item['host'],
            Location=item['location'],
            Description=item['desc'],
            Link=item['link'],
            Date=convert_to_custom_format(item['date']),
            Picture=item['image_url'],
            WebOrig=item['origin'],
        )

        db.session.add(event)

    db.session.commit()