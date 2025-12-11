import pytest
from django.shortcuts import reverse

@pytest.mark.django_db
def test_login_get(client):
    response = client.get(reverse("login"))
    assert response.status_code == 200
    assert response.context['form']


@pytest.mark.django_db
def test_login_success(client, user):
    response = client.post(reverse('login'),{
        'username': user.username,
        'password': 'testpassword',
    })
    #print(response.context['form'].errors)
    assert response.status_code == 302
    assert '_auth_user_id' in client.session

@pytest.mark.django_db
def test_login_post_fail(client, user):
    response = client.post(reverse('login'),{
        'username': 'wrong',
        'password': 'data',
    })
    #print(response.context['form'].errors)
    assert response.status_code == 200
    assert '__all__' in response.context['form'].errors
