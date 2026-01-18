from fastapi import FastAPI , Depends
from logic import add
from service import CalculatorService , get_calculator  

app = FastAPI()

@app.get("/add")
def add_endpoint(a: int, b: int, calc: CalculatorService = Depends(get_calculator)):
    return {"result": calc.add(a, b)}