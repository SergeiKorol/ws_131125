# создать задачу, удалить созданную задачу,
# проверить что гет по удалённой задаче == 404
import pytest
import requests

@pytest.mark.xfail(reason = 'bug')
def test_add_and_delete_task():
    ''' Cоздает задачу, удаляет задачу, проверяет статус код = 404'''
    body = {"title":"Новая задача", "completed":False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    id = response.json()["id"]

    requests.delete(f'https://todo-app-sky.herokuapp.com/{id}')
    response = requests.get(f'https://todo-app-sky.herokuapp.com/{id}')
    assert response.status_code == 404