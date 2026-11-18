from datetime import datetime


def test_delete_created_cart(api_session, base_url, logged_in_user):
    user_id = logged_in_user["id"]
    token = logged_in_user["accessToken"]

    create_response = api_session.post(
        f"{base_url}/carts/add",
        json={
            "userId": user_id,
            "products": [
                {"id": 1, "quantity": 2},
                {"id": 2, "quantity": 1},
                {"id": 3, "quantity": 1},
            ],
        },
        timeout=10,
    )
    assert create_response.status_code == 201
    cart_id = create_response.json()["id"]

    delete_response = api_session.delete(
        f"{base_url}/carts/{cart_id}",
        headers={"Authorization": f"Bearer {token}"},
        timeout=10,
    )
    assert delete_response.status_code == 200
    deleted_cart = delete_response.json()

    assert deleted_cart["id"] == cart_id
    assert deleted_cart["userId"] == user_id
    assert deleted_cart.get("isDeleted") is True

    deleted_on = deleted_cart.get("deletedOn")
    assert isinstance(deleted_on, str) and deleted_on.strip()
    datetime.fromisoformat(deleted_on.replace("Z", "+00:00"))
