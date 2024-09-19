# tests/conftest.py
import pytest
from app import create_app, db

@pytest.fixture(scope='module')
def test_client():
    app = create_app('testing')
    with app.app_context():
        db.create_all()  # Create tables in the test database
        yield app.test_client()
        db.drop_all()  # Drop tables after tests
