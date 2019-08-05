from flask import Flask, make_response, jsonify, render_template
from flask_httpauth import HTTPBasicAuth

from data_processing import create_table
from gfit_api import get_user_distance_interval
from utils import get_config, ApiException, get_week_frame
from flask_table import Table, Col


app = Flask(__name__)
auth = HTTPBasicAuth()
config = get_config()
DATE_FORMAT = '%d. %B'


@app.route('/')
# @auth.login_required
def hello_world():
    try:

        week_frame = get_week_frame()
        users = ['Janek']
        data = [{'user': user, 'days': get_user_distance_interval(week_frame[0].timestamp().__round__(),
                                                                  week_frame[1].timestamp().__round__())} for user in users]

        table = create_table(data)

        return render_template('tracker.html',
                               week_start=week_frame[0].strftime(DATE_FORMAT),
                               week_end=week_frame[1].strftime(DATE_FORMAT),
                               km_target=config['CHALLENGE']['start_kilometers'],
                               table=table)

    except ApiException as e:
        return make_response(jsonify({'error': e.message}), e.code)


# route error handling
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': error.description}), 404)


# securing
@auth.get_password
def get_password(username):
    if username == config['PAGE']['username']:
        return config['PAGE']['password']
    return None


# authorization error handling
@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)


if __name__ == '__main__':
    app.run(debug=True)
