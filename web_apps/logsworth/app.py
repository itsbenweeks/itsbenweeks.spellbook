#!flask/bin/python
from flask import Flask, jsonify, request, make_response, abort
from flask.ext.httpauth import HTTPBasicAuth
from dateutil.parser import parse
from models import Log, db


app = Flask(__name__)
auth = HTTPBasicAuth()


@auth.get_password
def get_password(username):  # Not great security, best for 1 hour of time.
    if username == 'logsworth':
        return 'welldonesir'
    return None


@auth.error_handler
def unauthorized(err):
    return make_response(jsonify({'error': 'You Shall Not Pass'}), 403)


@app.errorhandler(400)
def bad_request(err):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


@app.errorhandler(404)
def not_found(err):
    return make_response(jsonify({'error': 'Nothing to see here'}), 404)


@app.route('/api/v1/logs.json', methods=['GET'])
@auth.login_required
def logs_get():
    try:
        start_time = parse(request.args['start_time'])
        end_time = parse(request.args['end_time'])
        if (start_time > end_time):
            raise
    except:
        abort(400)
    logs = Log.query.filter(
        Log.timestamp >= start_time,
        Log.timestamp <= end_time
    ).all()
    if (len(logs) == 0):
        abort(400)
    result = {"logs": []}
    for log in logs:
        result["logs"].append(str(log))
    return jsonify(result)


@app.route('/api/v1/logs.json', methods=['POST'])
@auth.login_required
def logs_post():
    try:
        timestamp = parse(request.data[:request.data.find(' ')],
                          fuzzy_with_tokens=False),
        message = request.data[request.data.find(' ') + 1:]
    except:
        abort(400)
    entry = Log(timestamp[0], message)
    db.session.add(entry)
    db.session.commit()
    return 'Success!'

if __name__ == '__main__':
    app.run(debug=True)
