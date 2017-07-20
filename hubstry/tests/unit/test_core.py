import unittest
from hubstry.core import Registry


class TestRegistry(unittest.TestCase):

    def test_images_should_make_request(self):
        registry = Registry()
        registry.images()
