import requests

BASE_URL = "http://localhost:5000"  # Cambia este URL si tu API está en otro host/puerto

def test_home():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200
    assert "Bienvenido a la API de Libros" in response.json()["mensaje"]

def test_obtener_libros():
    response = requests.get(f"{BASE_URL}/api/libros")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_agregar_libro():
    nuevo_libro = {
        "titulo": "Nuevo Libro",
        "autor": "Autor Desconocido",
        "año": 2023
    }
    response = requests.post(f"{BASE_URL}/api/libros", json=nuevo_libro)
    assert response.status_code == 201
    data = response.json()
    assert data["titulo"] == nuevo_libro["titulo"]

def test_obtener_libro_por_id():
    response = requests.get(f"{BASE_URL}/api/libros/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1

def test_eliminar_libro():
    response = requests.delete(f"{BASE_URL}/api/libros/1")
    assert response.status_code == 200
    assert "Libro eliminado" in response.json()["mensaje"]
