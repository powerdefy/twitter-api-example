from flask import Flask, request, Response, jsonify
from werkzeug.exceptions import abort
from settings import PORT, CONSUMER_API_KEY, CONSUMER_API_SECRET_KEY, AUTH_URL, SEARCH_URL, USER_TIMELINE_URL
import requests, json
import urllib.parse

app = Flask(__name__)


def get_access_token():
    params = {'grant_type': 'client_credentials'}
    r = requests.post(url=AUTH_URL, params=params, auth=(
        CONSUMER_API_KEY, CONSUMER_API_SECRET_KEY))
    if r.status_code != 200:
        abort(Response(response=json.dumps(r.json()), status=r.status_code, mimetype='application/json'))
    else:
        return r.json().get("access_token")


@app.route('/hashtags/<q>')
def hashtags_search(q):
    limit = request.args.get('limit', 30)
    params = {'count': limit, 'q': '#' + q}
    headers = {'Authorization': 'Bearer ' + get_access_token()}
    r = requests.get(url=SEARCH_URL, params=params, headers=headers)
    return jsonify(r.json())


@app.route('/users/<user>')
def user_timeline(user):
    limit = request.args.get('limit', 30)
    params = {'count': limit, 'screen_name': user}
    headers = {'Authorization': 'Bearer ' + get_access_token()}
    r = requests.get(url=USER_TIMELINE_URL, params=params, headers=headers)
    return jsonify(r.json())


if __name__ == '__main__':
    app.run('0.0.0.0', PORT)
