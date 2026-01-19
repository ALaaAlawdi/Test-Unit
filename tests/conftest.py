import pytest
from fastapi.testclient import TestClient
from unittest.mock import create_autospec
from app import app
from service import CalculatorService, get_calculator


@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client


@pytest.fixture
def mock_calculator():
    mock = create_autospec(
        CalculatorService,
        instance=True,
        spec_set=True
    )
    app.dependency_overrides[get_calculator] = lambda: mock
    yield mock
    app.dependency_overrides.clear()
