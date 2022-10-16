from unittest.mock import Mock

from libdevpro import github_api


def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {
        'login': 'thiago-garcia', 'id': 13400040,
        'avatar_url': 'https://avatars.githubusercontent.com/u/13400040?v=4',
    }
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('thiago-garcia')
    assert 'https://avatars.githubusercontent.com/u/13400040?v=4' == url
