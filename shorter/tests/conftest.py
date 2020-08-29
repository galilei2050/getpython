import pytest


@pytest.fixture(params=['http://google.com', 'http://yandex.ru'])
def url(request):
    return request.param
