from unittest import (
    mock,
    TestCase,
)
import pytest

from hubstry.core import (
    Registry,
    RegistryNotFound,
    RegistryUnexpectedResponse
)


class TestRegistry(TestCase):

    def setUp(self):
        super().setUp()

    @pytest.mark.skip('not implemented yet')
    @mock.patch('hubstry.core.requests.get')
    def test_healthcheck_should_return_ok(self, mocked_request):
        class Response(object):
            status_code = 200

        mocked_request.return_value = Response
        registry = Registry()
        result = registry.healthcheck()
        mocked_request.assert_called_once_with(url='%s/' % registry.api_url)
        self.assertEqual(result.get('status'), 200)
        self.assertEqual(result.get('message'), 'Ok')
        mocked_request.reset_mock()

    @pytest.mark.skip('not implemented yet')
    @mock.patch('hubstry.core.requests.get')
    def test_healthcheck_should_raises_unexpected_response(self, mock_request):
        class Response(object):
            status_code = 502

            @staticmethod
            def json():
                return {
                    'error': 'Service Indisponible'
                }

        mock_request.return_value = Response
        registry = Registry()
        self.assertRaises(RegistryUnexpectedResponse, registry.healthcheck)

    @pytest.mark.skip('not implemented yet')
    @mock.patch('hubstry.core.requests.get')
    def test_images_without_last_param_should_retrieve_result(self, m_request):
        class Response(object):
            status_code = 200

            @staticmethod
            def json():
                return {
                    'repositories': ['hubstry', 'nginx', 'python'],
                }

        m_request.return_value = Response
        registry = Registry()
        images = registry.images()
        expected = {'images': ['hubstry', 'nginx', 'python'], 'last': 'python'}
        m_request.assert_called_once_with(
            '%s/_catalog?n=20' % registry.api_url
        )
        self.assertEqual(expected, images)

    @pytest.mark.skip('not implemented yet')
    @mock.patch('hubstry.core.requests.get')
    def test_images_with_last_param_should_retrieve_result(self, m_request):

        class Response(object):
            status_code = 200

            @staticmethod
            def json():
                return {
                    'repositories': ['nginx', 'python']
                }

        m_request.return_value = Response
        expected = {'images': ['nginx', 'python'], 'last': 'python'}
        registry = Registry()
        images = registry.images(limit=2, last_image='hubstry')
        m_request.assert_called_with(
            '%s/_catalog?n=2&last=hubstry' % registry.api_url
        )
        self.assertEqual(expected, images)

    @pytest.mark.skip('not implemented yet')
    @mock.patch('hubstry.core.requests.get')
    def test_images_should_raise_registry_not_found(self, m_request):

        class Response(object):
            status_code = 200

            @staticmethod
            def json():
                return {'repositories': []}

        m_request.return_value = Response

        registry = Registry()
        self.assertRaises(RegistryNotFound, registry.images)

    @pytest.mark.skip('not implemented yet')
    @mock.patch('hubstry.core.requests.get')
    def test_get_image_tags_should_retrieve_result(self, m_request):
        class Response(object):
            status_code = 200

            @staticmethod
            def json():
                return {'tags': ['latest']}

        m_request.return_value = Response
        registry = Registry()
        tags = registry.get_image_tags('python')
        url = '{0}/{1}/tags/list'.format(registry.api_url, 'python')
        m_request.assert_called_once_with(url)

        self.assertEqual(['latest'], tags)

    @pytest.mark.skip('not implemented yet')
    @mock.patch('hubstry.core.requests.get')
    def test_get_image_tags_should_raise_registry_not_found(self, m_request):
        class Response(object):
            status_code = 200

            @staticmethod
            def json():
                return {'tags': []}

        m_request.return_value = Response
        registry = Registry()

        self.assertRaises(RegistryNotFound, registry.get_image_tags, 'myball')

    @pytest.mark.skip('not implemented yet')
    @mock.patch('hubstry.core.requests.get')
    def test_get_tag_layers_should_retrieve_results(self, m_request):
        class Response(object):
            status_code = 200

            @staticmethod
            def json():
                return {
                    'fsLayers': [
                        {'blobSum': 'sha256:a3ed95caeb02'},
                    ]
                }
        m_request.return_value = Response

        registry = Registry()
        manifests = registry.get_tag_layers('python', 'latest')

        self.assertEqual([{'blobSum': 'sha256:a3ed95caeb02'}], manifests)
        m_request.assert_called_once_with(
            '{0}/{1}/manifests/{2}'.format(registry.api_url,
                                           'python',
                                           'latest')
        )

    @pytest.mark.skip('not implemented yet')
    @mock.patch('hubstry.core.requests.get')
    def test_get_tag_layers_should_raise_registry_not_found(self, m_request):
        class Response(object):
            status_code = 200

            @staticmethod
            def json():
                return {
                    'fsLayers': [
                    ]
                }
        m_request.return_value = Response
        registry = Registry()

        self.assertRaises(RegistryNotFound,
                          registry.get_tag_layers,
                          'python',
                          'latest')

    @mock.patch('hubstry.core.requests.get')
    def test_find_image_should_retrieve_results(self):
        registry = Registry()
        result = registry.find_image('yth')
        self.assertEqual('python', result.get('images')[0])
        result = registry.find_image('ython')
        self.assertEqual('python', result.get('images')[0])
        result = registry.find_image('pyth')
        self.assertEqual('python', result.get('images')[0])
        result = registry.find_image('python')
        self.assertEqual('python', result.get('images')[0])


    @pytest.mark.skip('not implemented yet')
    def test_find_image_should_not_retrieve_results(self):
        pass


    @pytest.mark.skip('not implemented yet')
    def test_delete_tag_should_succesful(self):
        pass

    @pytest.mark.skip('not implemented yet')
    def test_delete_tag_should_raise_exception_when_not_tag_layers(self):
        pass
