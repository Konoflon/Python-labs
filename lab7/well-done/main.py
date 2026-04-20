from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import time
from modules import lab4, lab5, lab6

app = FastAPI(title="Python Labs")

class SplitReq(BaseModel):
    lst: List[int]
    n: int

class CalcReq(BaseModel):
    i: int

class ValidateReq(BaseModel):
    min_val: float
    max_val: float
    values: List[float]

class DivideReq(BaseModel):
    a: float
    b: float

class WeatherReq(BaseModel):
    city: Optional[str] = "Сургут"
    days: Optional[int] = 3
    parallel: Optional[bool] = False

@app.get("/")
def root():
    return {"status": "ok", "docs": "/docs"}

@app.post("/lab4/split")
def split(req: SplitReq):
    return {"iter": lab4.split_iter_opt(req.lst, req.n), "rec": lab4.split_rec_opt(req.lst, req.n)}

@app.post("/lab4/calc")
def calc(req: CalcReq):
    return {"iter": lab4.calc_v_iter_opt(req.i), "rec": lab4.calc_v_rec_opt(req.i)}

@app.post("/lab5/validate")
def validate(req: ValidateReq):
    res = lab5.check_values(req.min_val, req.max_val, req.values)
    if isinstance(res, str) and "Error" in res:
        raise HTTPException(400, res)
    return {"result": res}

@app.post("/lab5/divide")
def divide(req: DivideReq):
    res = lab5.divide(req.a, req.b)
    if isinstance(res, str) and "Error" in res:
        return {"error": res}
    return {"result": res}

@app.post("/lab6/weather")
def weather(req: WeatherReq):
    func = lab6.parallel if req.parallel else lab6.sequential
    return {"forecast": func([req.city], req.days)}

@app.get("/lab6/benchmark")
def benchmark(days: int = 3):
    cities = list(lab6.CITIES.keys())
    t1 = time.time(); lab6.sequential(cities, days); seq = time.time() - t1
    t2 = time.time(); lab6.parallel(cities, days); par = time.time() - t2
    return {"seq_sec": round(seq, 2), "par_sec": round(par, 2), "speedup": round(seq/par, 2) if par > 0 else 0}