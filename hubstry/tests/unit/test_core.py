import unittest
from hubstry.core import Registry


class TestRegistry(unittest.TestCase):

    def test_images_should_make_request(self):
        registry = Registry()
        registry.images()

    def test_get_image_by_name_should_retrieve_result(self):
        registry = Registry()
        registry.get_image_by_name('python')
