def test_successful_login_and_authenticated_user(api_session, base_url):
    response = api_session.post(
        f"{base_url}/auth/login",
        json={"username": "emilys", "password": "emilyspass", "expiresInMins": 30},
        timeout=10,
    )
    assert response.status_code == 200
    login_data = response.json()
    assert login_data.get("username") == "emilys"
    assert login_data.get("accessToken")
    assert login_data.get("refreshToken")
    assert login_data.get("id") is not None

    me_response = api_session.get(
        f"{base_url}/auth/me",
        headers={"Authorization": f"Bearer {login_data['accessToken']}"},
        timeout=10,
    )
    assert me_response.status_code == 200
    me_data = me_response.json()
    assert me_data.get("username") == login_data["username"]
    assert me_data.get("id") == login_data["id"]
