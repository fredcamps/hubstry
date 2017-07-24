import unittest
import pytest
from hubstry.core import (
    Registry,
    RegistryNotFound,
    RegistryUnexpectedResponse
)


class TestRegistry(unittest.TestCase):

    def test_healthcheck_should_return_ok(self):
        registry = Registry()
        result = registry.healthcheck()
        self.assertEqual(result.get('status'), 200)
        self.assertEqual(result.get('message'), 'Ok')

    @pytest.mark.skip('not implemented yet')
    def test_healthcheck_should_raise_exception(self):
        registry = Registry()
        self.assertRaises(RegistryUnexpectedResponse, registry.healthcheck)

    @pytest.mark.skip('not implemented yet')
    def test_images_should_make_request(self):
        registry = Registry()
        registry.images()

    @pytest.mark.skip('not implemente yet')
    def test_get_image_by_name_should_retrieve_result(self):
        registry = Registry()
        registry.get_image_by_name('python')
