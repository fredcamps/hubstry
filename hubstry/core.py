import json
import requests
from .settings import Conf


class RegistryNotFound(BaseException):
    pass


class RegistryUnexpectedResponse(BaseException):
    pass


class Request(object):

    @staticmethod
    def get_response_content(response):
        if response.status_code != 200:
            error_msg = "Returned status code %d, Body %s" % \
                (response.status_code, json.dumps(response.json()))
            raise RegistryUnexpectedResponse(error_msg)
        content = response.json()
        return content

    @staticmethod
    def get(url):
        response = requests.get(url)
        return Request.get_response_content(response)

    @staticmethod
    def delete(url):
        response = requests.delete(url)
        return Request.get_response_content(response)


class Registry(object):

    def __init__(self):
        self.api_url = "%s/%s" % (Conf.Registry.URL, Conf.Registry.API_VERSION)

    def healthcheck(self):
        url = '%s/' % self.api_url
        Request.get(url=url)
        return {'status': 200, 'message': 'Ok'}

    def _all_images(self):
        url = '%s/_catalog' % self.api_url
        content = Request.get(url=url)
        if not content.get('repositories'):
            raise RegistryNotFound('No image(s) found at catalog.')

        return content.get('repositories')

    def images(self, limit=20, last_image=None):
        last = '' if not last_image else '&last={0}'.format(last_image)
        url = '%s/_catalog?n=%s%s' % (self.api_url, limit, last)
        content = Request.get(url)
        repositories = content.get('repositories')
        if not repositories:
            raise RegistryNotFound('No image(s) found at catalog.')

        return {
            'images': repositories,
            'last': repositories[-1],
        }

    def find_image(self, name_to_find, limit=20, offset=0):
        images = self._all_images()
        filtereds = [image for image in images if name_to_find in image]
        if not filtereds:
            raise RegistryNotFound("Image not found!")

        return {
            'last': None if len(filtereds) < limit else filtereds[-1],
            'images': filtereds[offset:limit-1],
        }

    def get_image_tags(self, name):
        url = '{0}/{1}/tags/list'.format(self.api_url, name)
        content = Request.get(url=url)
        if not content.get('tags'):
            raise RegistryNotFound(
                'Using clean node image instead image from registry'
            )

        return content.get('tags')

    def get_tag_layers(self, name, tag):
        url = '{0}/{1}/manifests/{2}'.format(self.api_url, name, tag)
        content = Request.get(url=url)
        error_msg = \
            'No manifests found for image {0} and tag {1}'.format(name, tag)

        if not content.get('fsLayers'):
            raise RegistryNotFound(error_msg)

        return content.get('fsLayers')

    def delete_tag(self, name, tag):
        url = '{0}/{1}/manifests/{2}'.format(self.api_url, name, tag)
        Request.delete(url=url)

    def delete_layer(self, name, digest):
        url = '{0}/{1}/blobs/{2}'.format(self.api_url, name, digest)
        Request.delete(url=url)
