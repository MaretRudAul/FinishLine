from flask import (
    Blueprint, Response, jsonify
)

from FinishLineApp.models import Event, EventTag

api_bp = Blueprint('api_bp', __name__)


@api_bp.route('/api/fetch-events', methods=['GET'])
def health():
    """API endpoint to return all events with their associated tags."""
    try:
        # Query all events and their tags
        events = Event.query.all()

        # Convert the events into a list of dictionaries
        event_list = []
        for event in events:
            event_data = {
                'id': event.id,
                'Title': event.Title,
                'Host': event.Host,
                'Location': event.Location,
                'Description': event.Description,
                'Date': event.Date.strftime('%Y-%m-%d %H:%M:%S'),  # Convert datetime to string
                'Picture': event.Picture,
                'WebOrig': event.WebOrig,
                'Tags': [tag.name for tag in event.tags]  # List of tag names
            }
            event_list.append(event_data)

        # Return the list of events as JSON
        return jsonify({'events': event_list}), 200

    except Exception as e:
        # Handle any exceptions and return an error message
        return jsonify({'error': str(e)}), 500

