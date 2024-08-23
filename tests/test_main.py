from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_book_image_success():
    response = client.post("/get_book_image/", json={"title": "Harry Potter & the Prisoner of Azkaban"})
    assert response.status_code == 200
    assert "image" in response.json()

def test_get_book_image_not_found():
    response = client.post("/get_book_image/", json={"title": "Libro No Existente"})
    assert response.status_code == 404
    assert response.json() == {"detail": "Book or user not found"}

def test_get_book_image_success():
    response = client.post("/get_book_image/", json={"title": "Harry Potter & the Prisoner of Azkaban"})
    assert response.status_code == 200
    assert "image" in response.json()


def test_get_similar_books_not_found():
    response = client.post("/get_similar_books/", json={"title": "Libro No Existente"})
    assert response.status_code == 200
    assert response.json() == {"similar_books": []}


