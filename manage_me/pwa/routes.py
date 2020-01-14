from flask import Blueprint, make_response, send_from_directory

pwa = Blueprint('pwa', __name__, url_prefix='')


@pwa.route('/manifest.json')
def manifest():
    return send_from_directory('static', 'manifest.json')
