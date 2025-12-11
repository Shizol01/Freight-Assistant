import pytest
from django.contrib.auth.models import User
from django.test import Client

@pytest.fixture
def client():
    return Client()

@pytest.fixture
def user():
    user = User.objects.create_user(
        username="test",
        email="test@mail.com",
    )
    user.set_password("testpassword")
    user.save()
    return user