from django.urls import reverse


class TestIndex:
    def test_unauthenticated(self, client):
        """An Unauthenticated user gets a valid response"""
        response = client.get(reverse('index'))
        assert response.context['hello'] == 'world'
        assert response.status_code == 200
