from fastapi import FastAPI , Depends
from service import CalculatorService , get_calculator  

app = FastAPI()

@app.get("/add")
async def add_endpoint(a: int, b: int, calc: CalculatorService = Depends(get_calculator)):
    result = await calc.add(a, b)
    return {"result": result }

