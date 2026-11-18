# Test Report – DummyJSON Python API Automation

## Scope

The suite contains five scenario groups and six pytest test functions.

| Scenario | Endpoint(s) | Method(s) | Expected result |
|---|---|---|---|
| Successful login | `/auth/login`, `/auth/me` | POST, GET | HTTP 200; valid tokens and same authenticated user |
| Product retrieval | `/products/1` | GET | HTTP 200; valid product fields, types and ranges |
| Cart creation | `/auth/login`, `/carts/add` | POST | HTTP 201; same user, 3 products, quantity 4, valid totals |
| Cart deletion | `/auth/login`, `/carts/add`, `/carts/{id}` | POST, DELETE | HTTP 200; matching IDs, `isDeleted=true`, valid timestamp |
| Negative: invalid login | `/auth/login` | POST | HTTP 400; error message and no access token |
| Negative: missing product | `/products/999999` | GET | HTTP 404; error message and no product data |

## Execution

Install dependencies:

```bash
pip install -r requirements.txt
```

Run all tests:

```bash
pytest
```

Run a specific module:

```bash
pytest tests/test_05_negative_scenarios.py
```

## Expected test functions

- `test_successful_login_and_authenticated_user`
- `test_get_product_and_validate_content`
- `test_create_cart_with_three_products`
- `test_delete_created_cart`
- `test_login_rejects_invalid_password`
- `test_get_non_existing_product_returns_not_found`

## Execution status

**Not executed during ZIP creation.** This report describes test design and expected outcomes, not actual run results. Run the suite in an internet-connected environment to obtain real results. If DummyJSON changes its public API contract, review the official documentation and update the relevant assertions.

## Limitations

- DummyJSON is a public demo API and depends on network availability.
- Cart creation and deletion are simulated; they do not represent durable database persistence.
- Public test data and endpoint behavior may change.
- The sample account credentials are public demo credentials, not real-user credentials.

## References

- https://dummyjson.com/docs
- https://dummyjson.com/docs/auth
- https://dummyjson.com/docs/products
- https://dummyjson.com/docs/carts
