import configparser
from datetime import datetime, timedelta


class ApiException(Exception):

    def __init__(self, code, message):
        """
        creates exception with a message
        :param code: response error code
        :param message: custom error message
        """
        super(ApiException, self).__init__(message)
        self.code = code
        self.message = message


def get_config(config_path='config.ini'):
    """
    creates and returns an config parser object of a .ini file
    :param config_path: path of config file
    :return: config parser object
    """
    config = configparser.ConfigParser()
    config.read(config_path)
    return config


def get_week_frame():
    """
    returns tupel of week start and end
    :return: datetime tupel
    """
    now = datetime.now()

    week_start = now - timedelta(days=now.weekday(),
                                 hours=now.hour,
                                 minutes=now.minute,
                                 seconds=now.second)
    week_end = now + timedelta(days=6 - now.weekday(),
                               hours=23 - now.hour,
                               minutes=59 - now.minute,
                               seconds=59 - now.second)

    return week_start, week_end


def get_week_kilometers():
    """
    returns the current weeks kilometer goal
    :return: int kilometers
    """
    config = get_config()

    now = datetime.now()
    challenge_start = datetime.fromtimestamp(int(config['CHALLENGE']['start_timestamp']))
    monday_current_week = now - timedelta(days=now.weekday())
    monday_challenge_start = challenge_start - timedelta(days=challenge_start.weekday())

    passed_weeks = int((monday_current_week - monday_challenge_start).days / 7)
    return int(config['CHALLENGE']['start_kilometers']) + passed_weeks


if __name__ == '__main__':
    print(get_week_kilometers())
