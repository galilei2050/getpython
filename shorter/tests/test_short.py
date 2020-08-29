import pytest
from shortcut.models import ShortUrl


def verify_short_in_db(url):
    assert ShortUrl.objects.count() == 1
    assert ShortUrl.objects.get(url=url) is not None


@pytest.mark.django_db
def test_short(client, url):
    request = client.post('/s/', data={'url': url})
    assert request.status_code == 200
    verify_short_in_db(url)


@pytest.mark.django_db
def test_short_get_not_allowed(client):
    request = client.get('/s/')
    assert request.status_code == 405
