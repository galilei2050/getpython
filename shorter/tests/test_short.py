import pytest
from shortcut.models import ShortUrl


@pytest.mark.django_db
def test_create_short(client, url):
    response = client.post('/s/', data={'url': url})
    assert response.status_code == 200
    assert ShortUrl.objects.count() == 1
    shortcut = ShortUrl.objects.get(url=url)
    assert shortcut is not None

