from service import CalculationError


def test_add_endpoint_negative_numbers(client, mock_calculator):
    mock_calculator.add.side_effect = CalculationError(
        "Negative numbers not allowed"
    )

    response = client.get("/add?a=-1&b=5")

    assert response.status_code == 400
    assert response.json()["detail"] == "Negative numbers not allowed"
