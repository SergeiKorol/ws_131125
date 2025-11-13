import requests

def test_add():
    """Описание теста"""
    body = {"title":"enjetest","completed":False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    id = response.json()["id"]
    print("id1", id)


    body = {"title":"enjetest1"}
    response = requests.patch(f'https://todo-app-sky.herokuapp.com/{id}', json=body)
    id2 = response.json()["id"]
    print("id2", id2)
    assert id == id2
    assert response.status_code == 200


test_add()
