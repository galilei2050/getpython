import pytest
from shortcut.models import ShortUrl


@pytest.fixture()
def domain():
    return 'com'


@pytest.fixture()
def short_key(url):
    su = ShortUrl(url=url, key=hash(url))
    su.save()
    return su


@pytest.mark.django_db
def test_long(client, short_key):
    response = client.get(f'/s/{short_key.key}')
    assert response.status_code == 302
    assert response.url == short_key.url
