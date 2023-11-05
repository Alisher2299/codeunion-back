import pytest
from django.test import Client
from users.models import User


@pytest.mark.django_db
def test_request_to_get_currencies(db):
    User.objects.create_user(username="user1", password="admin1admin1", email="user1@mail.com")

    client = Client()

    login_response = client.post(
        "/v0/api/users/login/",
        {"email": "user1@mail.com", "password": "admin1admin1"},
        content_type="application/json"
    )

    access_token = login_response.json().get("access")

    response = client.get(
        "/v0/api/currencies",
        content_type="application/json",
        HTTP_AUTHORIZATION=f'Bearer {access_token}'
    )

    assert response.status_code == 200
