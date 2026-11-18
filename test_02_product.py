def test_get_product_and_validate_content(api_session, base_url):
    product_id = 1
    response = api_session.get(f"{base_url}/products/{product_id}", timeout=10)
    assert response.status_code == 200
    product = response.json()

    assert product["id"] == product_id
    assert isinstance(product.get("title"), str) and product["title"].strip()
    assert isinstance(product.get("description"), str) and product["description"].strip()
    assert isinstance(product.get("price"), (int, float)) and product["price"] > 0
    assert isinstance(product.get("discountPercentage"), (int, float))
    assert 0 <= product["discountPercentage"] <= 100
    assert isinstance(product.get("rating"), (int, float))
    assert 0 <= product["rating"] <= 5
    assert isinstance(product.get("stock"), int) and product["stock"] >= 0
    assert isinstance(product.get("category"), str) and product["category"].strip()
    assert isinstance(product.get("images"), list) and product["images"]
