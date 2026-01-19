import pytest
from service import CalculatorService, CalculationError


@pytest.mark.asyncio
async def test_add_success():
    service = CalculatorService()
    result = await service.add(2, 3)
    assert result == 5


@pytest.mark.asyncio
async def test_add_negative_numbers():
    service = CalculatorService()
    with pytest.raises(CalculationError):
        await service.add(-1, 5)
