import pytest

from django.urls import reverse
from app.models import Provider


@pytest.fixture
def client():
    from rest_framework.test import APIClient
    return APIClient()


class TestProviderViewSet:
    @pytest.fixture()
    def provider(self, db):
        return Provider.objects.create(name="provider", email="provider@gmail.com", phone_number="(+216) 66 999 999",
                                       language="English", currency="Dollar")

    def test_create_provider_response(self, client, db):
        url = reverse("provider-list")
        response = client.post(url,
                               {'name': 'provider', 'email': 'provider@gmail.com', 'phone_number': '(+216) 66 999 999',
                                'language': 'English', 'currency': 'Dollar'}, format='json')
        assert 200 <= response.status_code < 300

        data = response.json()
        assert data == {
            'id': 1,
            'name': 'provider',
            'email': 'provider@gmail.com',
            'phone_number': '(+216) 66 999 999',
            'language': 'English',
            'currency': 'Dollar'
        }

    def test_create_provider_is_saved(self, client, db):
        url = reverse("provider-list")
        client.post(url, {'name': 'provider', 'email': 'provider@gmail.com', 'phone_number': '(+216) 66 999 999',
                          'language': 'English', 'currency': 'Dollar'}, format='json')
        provider = Provider.objects.all().first()
        assert provider is not None
        data = {
            'id': 1,
            'name': 'provider',
            'email': 'provider@gmail.com',
            'phone_number': '(+216) 66 999 999',
            'language': 'English',
            'currency': 'Dollar'
        }
        for field in data:
            assert data[field] == getattr(provider, field)

    def test_delete_provider(self, client, provider, db):
        assert Provider.objects.all().count() > 0
        url = reverse("provider-list")
        client.delete(url + f"{provider.id}/")
        assert Provider.objects.all().count() == 0
