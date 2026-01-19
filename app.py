from fastapi import FastAPI, Depends, HTTPException
from service import CalculatorService, get_calculator, CalculationError

app = FastAPI()


@app.get("/add")
async def add_endpoint(
    a: int,
    b: int,
    calc: CalculatorService = Depends(get_calculator),
):
    try:
        result = await calc.add(a, b)
        return {"result": result}
    except CalculationError as e:
        raise HTTPException(status_code=400, detail=str(e))
