# config file

class MainConfiguration(object):
    """ Main configuration class"""
    DEBUG = False
    CSRF_ENABLED = True


class DevelopmentEnvironment(MainConfiguration):
    """ Configurations for development"""
    DEBUG = True