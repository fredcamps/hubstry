
from .settings import Conf
import json
import requests


class RegistryNotFound(BaseException):
    pass


class Registry(object):

    def __init__(self):
        self.api_url = "%s/%s" % (Conf.Registry.URL, Conf.Registry.API_VERSION)

    def images(self, limit=20, last_image=None):
        if not last_image:
            last = ''
        else:
            last = '&last=' % last_image
        url = '%s/_catalog?n=%s%s' % (self.api_url, limit, last)

        response = requests.get(url)
        content = json.loads(response.content.decode())

        if not content or not content.get('repositories'):
            raise RegistryNotFound("No image(s) have been pushed!")

        return content.get('repositories')

    def get_image_by_name(self, name):

        url = '%s/%s' % (self.api_url, name)

        response = requests.get(url)
