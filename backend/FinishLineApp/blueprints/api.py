from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify, send_from_directory,
    current_app, Response, copy_current_request_context, send_file, make_response
)

website_bp = Blueprint('website', __name__)