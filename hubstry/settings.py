import os


class Conf(object):
    class Flask(object):
        pass

    class Registry(object):
        URL = 'http://%s' % os.environ.get('REGISTRY_URL')
        API_VERSION = 'v2'
