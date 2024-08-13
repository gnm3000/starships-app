import json
from chalice.test import Client
import pytest
from app import app as chalice_app


@pytest.fixture
def client():
    with Client(chalice_app) as client:
        yield client


@pytest.fixture
def jwt_token(client):
    response = client.http.post(
        "/login",
        headers={"Content-Type": "application/json"},
        body=json.dumps({"username": "user1", "password": "12345"}),
    )
    assert response.status_code == 200
    print(f"Login Response: {response.json_body}")  
    return response.json_body["token"]


def test_get_starships_not_auth(client):
    response = client.http.get("/starships")
    assert response.status_code == 401


def test_get_starship(client, jwt_token):
    response = client.http.get(
        "/starships", headers={"Authorization": f"Bearer {jwt_token}"}
    )
    print(f"Starships Response: {response.json_body}")  
    assert response.status_code == 200
    assert "starships" in response.json_body


def test_get_starship_with_manufacturer(client, jwt_token):
    response = client.http.get(
        "/starships?manufacturer=Kuat Drive Yards", headers={"Authorization": f"Bearer {jwt_token}"}
    )
    print(f"Starships Response: {response.json_body}")  
    assert response.status_code == 200
    assert "starships" in response.json_body
    starships_response = response.json_body
    print(starships_response["starships"])
    filtered = [x for x in starships_response["starships"] if x["manufacturer"]!="Kuat Drive Yards"]
    assert len(filtered) == 0
