#!flask/bin/python
from flask import Flask, jsonify, request, make_response, abort
from flask_httpauth import HTTPBasicAuth
from dateutil.parser import parse
from datetime import datetime, timedelta
from models import Progress, db
from sqlalchemy import func
from mailer import Mailer


app = Flask(__name__)
auth = HTTPBasicAuth()
mailer = Mailer()


@auth.get_password
def get_password(username):  # Not great security, best for 1 hour of time.
    if username == 'mightiest':
        return 'howvery'
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


@app.route('/progress/<player_id>/game/<game_id>', methods=['GET'])
@auth.login_required
def progress_get(player_id, game_id):
    try:
        player = parse(request.args['player'])
        device_id = parse(request.args['deviceId'])
        if (start_time > end_time):
            raise
    except:
        abort(400)
    progresses = Progress.query.filter(
        Progress.player_id == player_id,
        Progress.game_id == game_id
    ).all()
    result = {
        "player": player_id,
        "progresses": []
    }
    for progress in progresses:
        result["progresses"].append(progress.to_dicitonary())
    return jsonify(result)


@app.route('/progress/<player_id>/game/<game_id>', methods=['POST'])
@auth.login_required
def progress_post(player_id, game_id):
    try:
        player = request.data.get("player")
        device_id = request.data.get("deviceId")
        progress = request.data.get("progress")
    except:
        abort(400)
    if player_id != player:
        abort(400)
    elif game_id != progress['gameId']:
        abort(400)

    entry = Progress(
        player_id,
        game_id,
        progress['timeStamp'],
        progress['level'],
        progress['score']
    )
    db.session.add(entry)
    db.session.commit()

    max_score = Progress.query(func.max(Progress.score)).filter(
        Progress.player_id == player_id,
        Progress.game_id == game_id
    ).all()
    if (max_score < progress['score']):
        mailer.notify_parent_hi_score(child_id, game_id, score) # This would assume a mailer object, which would tie into an SMTP server, or use a transactional e-mail service like MailGun.
        return 'New High Score!'
    else:
        return 'Success!'


@app.route('rollingAverages', methods=['GET'])
@auth.login_required
def rolling_average_get():
    try:
        week = request.args['week']
        player_id = request.args['player_id']
    except:
        abort(400)
    start_date = datetime.now() - timedelta(days = 7 * (week + 3)
    end_date = datetime.now() - timedelta(days = 7 * week)

    progresses = Progress.query(
        Progress.game_id, func.avg(Progress.score).label('rolling_average')
    ).filter(
        Progress.player_id == player_id,
        Progress.timestamp >= start_date,
        Progress.timestamp <= end_date,
    ).group_by(
        Progress.game_id
    ) # Let the ORM construct a query to gather the average of scores for progress entries from 3+n to n weeks ago. Then group them by game_id.
    result = {}
    for progress in progresses:
        game_id = progress.game_id
        rolling_average = progress.rolling_average
        result[game_id] = rolling_average

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
