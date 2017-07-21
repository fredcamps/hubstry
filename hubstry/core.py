
from .settings import Conf
import requests


class Registry(object):

    def __init__(self):
        self.api_url = "%s/%s" % (Conf.Registry.URL, Conf.Registry.API_VERSION)

    def images(self, limit=20, last_image=None):
        method = 'GET'
        headers = {}
        if not last_image:
            last = ''
        else:
            last = '&last=' % last_image
        url = '%s/_catalog?n=%s%s' % (self.api_url, limit, last)

        response = requests.get(url, auth=('admin', 'admin'))

        import ipdb;ipdb.set_trace()

        return response
