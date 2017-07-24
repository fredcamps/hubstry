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
    def test_images_should_retrieve_result(self):
        registry = Registry()
        registry.images()

    @pytest.mark.skip('not implemented yet')
    def test_images_should_raise_exception(self):
        registry = Registry()
        registry.images()

    @pytest.mark.skip('not implemented yet')
    def test_get_image_by_name_should_retrieve_result(self):
        registry = Registry()
        registry.get_image_by_name('python')

    @pytest.mark.skip('not implemented yet')
    def test_get_image_by_name_should_raise_exception(self):
        pass

    @pytest.mark.skip('not implemented yet')
    def test_get_tag_manifests_should_retrieve_results(self):
        pass

    @pytest.mark.skip('not implemented yet')
    def test_get_tag_manifests_should_raise_exception(self):
        pass

    @pytest.mark.skip('not implemented yet')
    def test_delete_tag_should_succesful(self):
        pass

    @pytest.mark.skip('not implemented yet')
    def test_delete_tag_should_raise_exception_when_get_non_200_status(self):
        pass

    @pytest.mark.skip('not implemented yet')
    def test_delete_tag_should_raise_exception_when_not_found_manifest(self):
        pass

    @pytest.mark.skip('not implemented yet')
    def test_find_image_should_retrieve_results(self):
        pass

    @pytest.mark.skip('not implemented yet')
    def test_find_image_should_not_retrieve_results(self):
        pass
