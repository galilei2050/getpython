import pytest
import random
from shortcut.models import ShortUrl


@pytest.mark.django_db
@pytest.fixture()
def shortcut(url):
    short_url = ShortUrl(url=url, key=hash(url))
    short_url.save()
    return short_url


@pytest.mark.django_db
def test_long(client, shortcut):
    response = client.get(f'/s/{shortcut.key}')
    assert response.status_code == 302
    assert response.url == shortcut.url