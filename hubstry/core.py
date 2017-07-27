import json
import requests
from .settings import Conf


class RegistryNotFound(BaseException):
    pass


class RegistryUnexpectedResponse(BaseException):
    pass


class Request(object):

    @staticmethod
    def validate_response_status(response):
        if response.status_code != 200:
            error_msg = "Returned status code %d, Body %s" % \
                (response.status_code, json.dumps(response.json()))
            raise RegistryUnexpectedResponse(error_msg)

    @staticmethod
    def get(url, index, error_msg):
        response = requests.get(url)
        Request.validate_response_status(response)
        content = response.json()

        if not content.get(index):
            raise RegistryNotFound(error_msg)

        return content.get(index)

    @staticmethod
    def delete(url):
        response = requests.delete(url)
        Request.validate_response_status(response)


class Registry(object):

    def __init__(self):
        self.api_url = "%s/%s" % (Conf.Registry.URL, Conf.Registry.API_VERSION)

    def healthcheck(self):
        url = '%s/' % self.api_url
        response = requests.get(url=url)
        Request.validate_response_status(response)
        return {'status': 200, 'message': 'Ok'}

    def _all_images(self):
        url = '%s/_catalog' % self.api_url
        content = Request.get(url,
                              index='repositories',
                              error_msg='No image(s) found at catalog.')

        return content

    def images(self, limit=20, last_image=None):
        if not last_image:
            last = ''
        else:
            last = '&last=%s' % last_image
        url = '%s/_catalog?n=%s%s' % (self.api_url, limit, last)
        content = Request.get(url=url,
                              index='repositories',
                              error_msg='No image(s) found at catalog.')
        return {
            'images': content,
            'last': content[-1],
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
        url = '%s/%s/tags/list' % (self.api_url, name)
        error_msg = 'No tag(s) found at image %s' % name
        content = Request.get(url=url,
                              index='tags',
                              error_msg=error_msg)
        return content

    def get_tag_layers(self, name, tag):
        url = '{0}/{1}/manifests/{2}'.format(self.api_url, name, tag)

        error_msg = \
            'No manifests found for image {0} and tag {1}'.format(name, tag)
        content = Request.get(url=url,
                              index='fsLayers',
                              error_msg=error_msg)
        return content

    def delete_tag(self, name, tag):
        url = '{0}/{1}/manifests/{2}'.format(self.api_url, name, tag)

        Request.delete(url=url)

    def delete_layer(self, name, digest):
        url = '{0}/{1}/blobs/{2}'.format(self.api_url, name, digest)

        Request.delete(url=url)
