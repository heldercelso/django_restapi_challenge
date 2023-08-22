import pytest
from django.urls import reverse

pytestmark = pytest.mark.django_db()


def test_get_user(client, new_user):
    response = client.get(reverse('client_api:client', kwargs={'pk': new_user.pk}))
    assert response.status_code == 200
    assert response.json() == {'id': new_user.pk, 'cpf': '553.396.320-08', 'nome': 'Fulano', 'email': 'fulano@example.com', 'dataDeNascimento': '2000-01-15', 'sexo': 'H', 'rendaMensal': '3000.00'}


def test_update_user(client, new_user):
    response = client.put(reverse('client_api:client', kwargs={'pk': new_user.pk}),
                          data={'cpf': '553.396.320-08', 'nome': 'Ciclano', 'email': 'fulano@example.com', 'dataDeNascimento': '2000-01-15', 'sexo': 'H', 'rendaMensal': '5000.00'},
                          content_type='application/json;')
    assert response.status_code == 200
    assert response.json() == {'id': new_user.pk}

    response = client.get(reverse('client_api:client', kwargs={'pk': new_user.pk}))
    assert response.status_code == 200
    assert response.json() == {'id': new_user.pk, 'cpf': '553.396.320-08', 'nome': 'Ciclano', 'email': 'fulano@example.com', 'dataDeNascimento': '2000-01-15', 'sexo': 'H', 'rendaMensal': '5000.00'}


def test_create_user(client):
    response1 = client.post(reverse('client_api:clients'),
                            data={'cpf': '821.380.370-10', 'nome': 'Fulano', 'email': 'fulano@example.com', 'dataDeNascimento': '2000-01-15', 'sexo': 'H', 'rendaMensal': '3000.00'},
                            content_type='application/json;')
    assert response1.status_code == 201
    assert response1.json() == {'id': 3}

    response = client.get(reverse('client_api:client', kwargs={'pk': response1.json()['id']}))
    assert response.status_code == 200
    assert response.json() == {'id': response1.json()['id'], 'cpf': '821.380.370-10', 'nome': 'Fulano', 'email': 'fulano@example.com', 'dataDeNascimento': '2000-01-15', 'sexo': 'H', 'rendaMensal': '3000.00'}


def test_delete_user(client, new_user):
    response = client.delete(reverse('client_api:client', kwargs={'pk': new_user.pk}))
    assert response.status_code == 204

    response = client.get(reverse('client_api:client', kwargs={'pk': new_user.pk}))
    assert response.status_code == 404