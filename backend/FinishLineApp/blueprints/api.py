from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify, send_from_directory,
    current_app, Response, copy_current_request_context, send_file, make_response
)

api_bp = Blueprint('website', __name__)


@api_bp.route('/api/v1/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})

