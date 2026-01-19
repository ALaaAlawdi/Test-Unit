class CalculationError(Exception):
    pass


class CalculatorService:
    async def add(self, a: int, b: int) -> int:
        if a < 0 or b < 0:
            raise CalculationError("Negative numbers not allowed")
        return a + b


def get_calculator() -> CalculatorService:
    return CalculatorService()
