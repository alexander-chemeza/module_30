from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_item():
    response = client.get("/recipes/1")
    assert response.status_code == 200
    assert response.json() == {
        "name": "Tunets",
        "views": 2,
        "time": 1,
        "ingredients": "tunets, salt",
        "description": "cook tunets",
        "id": 1
    }


def test_read_items():
    response = client.get("/recipes")
    assert response.status_code == 200
    assert response.json() == [
        {
            "name": "Fish",
            "views": 1,
            "time": 1,
            "id": 3
        },
        {
            "name": "Tunets",
            "views": 2,
            "time": 1,
            "id": 1
        },
        {
            "name": "Heck",
            "views": 2,
            "time": 2,
            "id": 2
        },
        {
            "name": "Crisps",
            "views": 2,
            "time": 3,
            "id": 4
        }
    ]