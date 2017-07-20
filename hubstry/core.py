from .settings import Conf
from urllib import request


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
        response = request.Request(url=url, headers=headers, method=method)
        import ipdb;ipdb.set_trace()
        return response
