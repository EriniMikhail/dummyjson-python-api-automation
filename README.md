# DummyJSON Python API Automation

Python API automation suite using `requests` and `pytest` for https://dummyjson.com/.

## Test coverage

1. Successful login (`POST /auth/login`) and authenticated-user verification (`GET /auth/me`).
2. Retrieve product 1 (`GET /products/1`) and validate its content.
3. Create a cart for the logged-in user with products 1, 2 and 3; validate quantities and totals.
4. Create and delete a cart; validate the delete response.
5. Two negative scenarios: invalid login (`POST /auth/login`) and non-existing product (`GET /products/999999`).

## Structure

```text
dummyjson-python-api-automation/
├── README.md
├── requirements.txt
├── pytest.ini
├── report/TEST_REPORT.md
└── tests/
    ├── __init__.py
    ├── conftest.py
    ├── test_01_login.py
    ├── test_02_product.py
    ├── test_03_create_cart.py
    ├── test_04_delete_cart.py
    └── test_05_negative_scenarios.py
```

## Setup

Python 3.9+ is recommended.

```bash
python -m venv .venv
```

Activate the environment:

- Windows PowerShell: `.venv\Scripts\Activate.ps1`
- macOS/Linux: `source .venv/bin/activate`

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run tests

```bash
pytest
```

Run one module:

```bash
pytest tests/test_01_login.py
pytest tests/test_05_negative_scenarios.py
```

## Demo credentials

DummyJSON public sample account:
- Username: `emilys`
- Password: `emilyspass`

These are public demo credentials, not private account credentials.

## Notes

DummyJSON is a demo API. Cart create/delete operations are simulated and do not persist as ordinary database changes. The suite validates the returned API responses. Public API data or behavior can change; consult the official docs if an assertion needs updating.

## Publish to GitHub

1. Create a new repository on GitHub (for example `dummyjson-python-api-automation`).
2. Extract this ZIP and open a terminal in the extracted folder.
3. Run the following commands, replacing the placeholder with your GitHub username:

```bash
git init
git add .
git commit -m "Add DummyJSON Python API automation tests"
git branch -M main
git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/dummyjson-python-api-automation.git
git push -u origin main
```

Authenticate with GitHub when prompted.

## Suggested GitHub description

Python API automation suite using requests and pytest to test DummyJSON authentication, products, carts, deletion, and negative scenarios.
