import configparser


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
