class CalculatorService:
    async def add(self, a: int, b: int) -> int:
        return a + b


def get_calculator() -> CalculatorService:

    return CalculatorService()
