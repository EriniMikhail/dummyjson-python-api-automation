import pytest
import requests

BASE_URL = "https://dummyjson.com"


@pytest.fixture
def api_session():
    session = requests.Session()
    session.headers.update({"Accept": "application/json"})
    yield session
    session.close()


@pytest.fixture
def base_url():
    return BASE_URL


@pytest.fixture
def logged_in_user(api_session, base_url):
    response = api_session.post(
        f"{base_url}/auth/login",
        json={
            "username": "emilys",
            "password": "emilyspass",
            "expiresInMins": 30,
        },
        timeout=10,
    )
    assert response.status_code == 200, (
        f"Login setup failed: HTTP {response.status_code}: {response.text}"
    )
    data = response.json()
    assert data.get("id") is not None
    assert data.get("accessToken")
    return data
