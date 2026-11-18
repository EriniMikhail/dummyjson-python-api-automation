def test_login_rejects_invalid_password(api_session, base_url):
    response = api_session.post(
        f"{base_url}/auth/login",
        json={"username": "emilys", "password": "WrongPassword123"},
        timeout=10,
    )
    assert response.status_code == 400
    error_data = response.json()
    assert isinstance(error_data.get("message"), str)
    assert error_data["message"].strip()
    assert "accessToken" not in error_data


def test_get_non_existing_product_returns_not_found(api_session, base_url):
    response = api_session.get(f"{base_url}/products/999999", timeout=10)
    assert response.status_code == 404
    error_data = response.json()
    assert isinstance(error_data.get("message"), str)
    assert error_data["message"].strip()
    assert "id" not in error_data
    assert "title" not in error_data
