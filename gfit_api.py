import requests
import json
from utils import get_config, ApiException


def get_user_distance_interval(start_timestamp, end_timestamp, user='me'):
    """
    perform api call to get a users the delta distance in an interval
    :param start_timestamp: interval start
    :param end_timestamp: interval end
    :param user: user
    :return: http response as json
    """
    config = get_config()

    # prepare uri
    uri = config['API']['aggregate_dataset_url']
    uri = uri.replace('<1>', user)

    # prepare headers
    headers = {
        'Content-Type': 'application/json',
        'Authorization': config['API']['authorization_type'] + ' ' + config['TOKENS']['janek']
    }

    # prepare POST Request body
    body_dict = {
        "aggregateBy": [{
            "dataTypeName": config['DISTANCE']['dataTypeName'],
            "dataSourceId": config['DISTANCE']['dataSourceId']
        }],
        "bucketByTime": {"durationMillis": 86400000},
        "startTimeMillis": start_timestamp * 1000,
        "endTimeMillis": end_timestamp * 1000
    }
    body_json = json.dumps(body_dict)

    # perform request
    response = requests.post(uri,
                             data=body_json,
                             headers=headers)

    # handle results
    if response.status_code == 200:
        return extract_relevant_data(response.json())
    elif response.status_code == 401:
        raise ApiException(response.status_code, 'Invalid access token for user \'' + user + '\'')
    else:
        raise ApiException(response.status_code, 'Undefined Exception')


def extract_relevant_data(result):
    """
    extracts the interval and distance from all entries of the requested data
    :param result: response result in json format
    :return: list of dictionaries with start_timestamp, end_timestamp and distance
    """
    return [{'start_timestamp': int(entry['startTimeMillis']) / 1000,
             'end_timestamp': int(entry['endTimeMillis']) / 1000,
             'distance': entry['dataset'][0]['point'][0]['value'][0]['fpVal'] if len(entry['dataset'][0]['point']) > 0 else 0}
            for entry in result['bucket']]


if __name__ == '__main__':

    response_json = get_user_distance_interval(1564272000, 1564704000)

    for day in extract_relevant_data(response_json):
        print(day)
