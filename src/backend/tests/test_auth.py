import pytest
from fastapi.testclient import TestClient
from src.backend.main import app

client = TestClient(app)

def test_register_success():
    response = client.post(
        "/api/v1/auth/register",
        json={"username": "testuser", "email": "test@example.com", "password": "password123"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["code"] == 0
    assert data["data"]["username"] == "testuser"
    assert data["data"]["email"] == "test@example.com"

def test_register_duplicate_username():
    # First registration
    client.post(
        "/api/v1/auth/register",
        json={"username": "dupuser", "email": "dup1@example.com", "password": "password123"}
    )
    # Second registration with same username
    response = client.post(
        "/api/v1/auth/register",
        json={"username": "dupuser", "email": "dup2@example.com", "password": "password123"}
    )
    assert response.status_code == 200 # Since we return BaseResponse.error with code 400 inside 200
    data = response.json()
    assert data["code"] == 400
    assert "Username already registered" in data["message"]

def test_register_invalid_email():
    response = client.post(
        "/api/v1/auth/register",
        json={"username": "user3", "email": "not-an-email", "password": "password123"}
    )
    # Pydantic validation error will return 422
    assert response.status_code == 422

def test_login_success():
    # Register first
    client.post(
        "/api/v1/auth/register",
        json={"username": "loginuser", "email": "login@example.com", "password": "password123"}
    )
    # Login with username
    response = client.post(
        "/api/v1/auth/login",
        json={"account": "loginuser", "password": "password123"}
    )
    assert response.status_code == 200
    assert response.json()["code"] == 0
    assert response.json()["data"]["username"] == "loginuser"

def test_login_fail_wrong_password():
    # Login with wrong password
    response = client.post(
        "/api/v1/auth/login",
        json={"account": "loginuser", "password": "wrongpassword"}
    )
    assert response.status_code == 200
    assert response.json()["code"] == 401
