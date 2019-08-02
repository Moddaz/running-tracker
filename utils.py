import configparser


def get_config(config_path='config.ini'):
    """
    creates and returns an config parser object of a .ini file
    :param config_path: path of config file
    :return: config parser object
    """
    config = configparser.ConfigParser()
    config.read(config_path)
    return config
