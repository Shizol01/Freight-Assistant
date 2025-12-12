import pytest
from django.contrib.auth.models import User
from django.test import Client

from apps.company.models import Carrier


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


@pytest.fixture
def profile(user):
    profile = user.profile

    profile.about_me = 'lorem ipsum dolor sit amet'
    profile.job = 'test_job'
    profile.country = 'test_country'
    profile.address = 'test_address'
    profile.phone = '111222333'
    profile.twitter = 'test_twitter.com'
    profile.facebook = 'test_facebook.com'
    profile.instagram = 'test_instagram.com'
    profile.linkedin = 'test_linkedin.com'
    profile.save()

    return profile


@pytest.fixture
def carrier_list():
    carriers = [
        Carrier(
            name=f"test_carrier{i}",
            nip=f"123456789{i}",
            address=f"test_carrier_address{i}",
            email=f"test_carrier{i}@mail.com",
            phone=f"12345678{i}",
        )
        for i in range(1, 6)
    ]
    Carrier.objects.bulk_create(carriers)
    return carriers


@pytest.fixture
def carrier(carrier_list):
    return carrier_list[0]
