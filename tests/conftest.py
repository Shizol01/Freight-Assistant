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
