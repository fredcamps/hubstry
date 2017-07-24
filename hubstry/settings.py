import os


class Conf(object):
    class Flask(object):
        DEBUG = True if os.environ.get('HUBSTRY_DEBUG', False) else False

    class Registry(object):
        URL = os.environ.get('REGISTRY_URL')
        API_VERSION = 'v2'
