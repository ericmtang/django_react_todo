from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
import pytest
from todo.models import Todo

# Create your tests here.

# def test_homepage_access():
#     url = reverse(views.Todo)
#     print(url)
#     assert url == "/api/"

@pytest.fixture
def new_todo(db):
    todo = Todo.objects.create(
        title = "Test To-Do",
        description = "Automated To-Do",
        completed = True,
    )
    return todo

def test_search_todo(new_todo):
    assert Todo.objects.filter(title='Test To-Do').exists()

def test_update_todo(new_todo):
    new_todo.title = 'Change To-Do'
    new_todo.save()
    assert Todo.objects.filter(title='Change To-Do').exists()

def test_api_get_todo(new_todo):
    client = APIClient()
    response = client.get(path='/api/todos/', format='json')
    print(response.data)
    assert response.status_code == 200

def test_api_post_todo(new_todo):
    client = APIClient()
    response = client.post(path='/api/todos/', data={
        'title': 'Test To-Do 2',
        'description': 'Automated To-Do 2',
        'completed': False,
    }, format='json')
    print(response.data)
    assert response.status_code == 201
