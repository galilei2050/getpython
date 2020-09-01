import pytest


@pytest.fixture(params=['com', 'ru', 'io'])
def domain(request):
    return request.param


@pytest.fixture(params=['http', 'https'])
def scheme(request):
    return request.param


@pytest.fixture(params=['google', 'ya'])
def url(request, domain, scheme):
    return f'{scheme}://{request.param}.{domain}'
