from fastapi.testclient import TestClient
from app import app
from unittest.mock import create_autospec
from service import CalculatorService, get_calculator
import pytest


client = TestClient(app)

@pytest.mark.asyncio
async def test_add_endpoint():
    mock_calc = create_autospec(CalculatorService, instance=True , spec_set=True)
    mock_calc.add.return_value = 10

    app.dependency_overrides[get_calculator] = lambda: mock_calc

    with TestClient(app) as client:
        response = client.get("/add?a=3&b=7")

    assert response.status_code == 200
    assert response.json() == {"result": 10}
    mock_calc.add.assert_called_once_with(3, 7)

    app.dependency_overrides.clear()


