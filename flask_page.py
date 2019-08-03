from flask import Flask, make_response, jsonify
from flask_httpauth import HTTPBasicAuth
from gfit_api import get_user_distance_interval
from utils import get_config, ApiException

app = Flask(__name__)
auth = HTTPBasicAuth()


@app.route('/')
# @auth.login_required
def hello_world():
    try:
        return str(get_user_distance_interval(1564272000, 1564704000))
    except ApiException as e:
        return make_response(jsonify({'error': e.message}), e.code)


# route error handling
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': error.description}), 404)


# securing
@auth.get_password
def get_password(username):
    config = get_config()
    if username == config['PAGE']['username']:
        return config['PAGE']['password']
    return None


# authorization error handling
@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)


if __name__ == '__main__':
    app.run(debug=True)
