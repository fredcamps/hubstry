import os
from urllib import request


class Registry(object):

    def __init__(self):
        self.api_url = "%s/%s" % ('v2', os.environ.get('REGISTRY_URL'))

    def repositories(self, limit=20, last_image=None):
        method = 'GET'
        headers = ''
        last = '' if not last_image else '&last=' % last_image
        url = '%s/_catalog?n=%s%s' % (self.api_url, limit, last)
        response = request.Request(url=url, headers=headers, method=method)
        return response
