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
    returns list of week start and end
    :return: timestamp list
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

    return week_start.timestamp().__round__(), week_end.timestamp().__round__()