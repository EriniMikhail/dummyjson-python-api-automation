import math


def test_create_cart_with_three_products(api_session, base_url, logged_in_user):
    user_id = logged_in_user["id"]
    payload = {
        "userId": user_id,
        "products": [
            {"id": 1, "quantity": 2},
            {"id": 2, "quantity": 1},
            {"id": 3, "quantity": 1},
        ],
    }
    response = api_session.post(f"{base_url}/carts/add", json=payload, timeout=10)
    assert response.status_code == 201
    cart = response.json()

    assert cart.get("id") is not None
    assert cart["userId"] == user_id
    assert cart["totalProducts"] == 3
    assert cart["totalQuantity"] == 4
    assert len(cart["products"]) == 3

    expected_quantities = {1: 2, 2: 1, 3: 1}
    returned_ids = set()
    for item in cart["products"]:
        product_id = item["id"]
        returned_ids.add(product_id)
        assert product_id in expected_quantities
        assert item["quantity"] == expected_quantities[product_id]
        assert isinstance(item["price"], (int, float)) and item["price"] > 0
        expected_line_total = item["price"] * item["quantity"]
        assert math.isclose(item["total"], expected_line_total, rel_tol=0, abs_tol=0.02)

    assert returned_ids == {1, 2, 3}
    assert sum(item["quantity"] for item in cart["products"]) == cart["totalQuantity"]
    calculated_total = sum(item["total"] for item in cart["products"])
    assert math.isclose(cart["total"], calculated_total, rel_tol=0, abs_tol=0.05)
    assert isinstance(cart.get("discountedTotal"), (int, float))
    assert 0 <= cart["discountedTotal"] <= cart["total"]
