from fastapi import FastAPI
from modules import lab4, lab5, lab6

app = FastAPI(title="Python Labs")

@app.get("/lab4")
def run_lab4():
    return {
        "split": lab4.split_iter_opt([1, 2, 3, 4, 5], 2),
        "calc": lab4.calc_v_iter_opt(10)
    }

@app.get("/lab5")
def run_lab5():
    return {
        "validate": lab5.check_values(0, 100, [10, 50, 150, -10]),
        "divide_ok": lab5.divide(10, 2),
        "divide_err": lab5.divide(10, 0)
    }

@app.get("/lab6")
def run_lab6(city: str = "Сургут", days: int = 3, parallel: bool = False):
    func = lab6.parallel if parallel else lab6.sequential
    return {"forecast": func([city], days)}

@app.get("/run_all")
def run_all():
    return {
        "lab4": run_lab4(),
        "lab5": run_lab5(),
        "lab6": run_lab6()
    }

@app.get("/")
def root():
    return {"status": "ok", "docs": "/docs"}