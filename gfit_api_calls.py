import requests
import json
from utils import get_config


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
        'Authorization': 'Bearer ' + config['TOKENS']['janek']
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

    return response.json()


if __name__ == '__main__':

    result = get_user_distance_interval(1564272000, 1564704000)
    print(result)
