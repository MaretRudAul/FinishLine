from flask import (
    Blueprint, Response, jsonify
)

from FinishLineApp.models import Event, EventTag

api_bp = Blueprint('api_bp', __name__)


@api_bp.route('/api/fetch-events', methods=['GET'])
def health():
    """API endpoint to return all events with their associated tags."""
    try:
        events = Event.query.all()

        event_list = []

        for event in events:
            event_data = {
                'id': event.id,
                'title': event.Title,
                'host': event.Host,
                'location': event.Location,
                'description': event.Description,
                'link': event.Link,
                'datetime': event.Date.strftime('%Y-%m-%d %H:%M:%S'),
                'pictureUrl': event.Picture,
                'websiteOrigin': event.WebOrig,
                'tag': [tag.name for tag in event.tags]
            }
            event_list.append(event_data)

        return jsonify(event_list), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

