from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json, os
from datetime import datetime

app = FastAPI()
FILE = "expenses.json"

class Expense(BaseModel):
    amount: float
    category: str = "Другое"
    desc: str = ""

def load():
    if os.path.exists(FILE):
        with open(FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save(data):
    with open(FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

@app.get("/")
def root():
    return {
        "message": "Перейдите в /docs для управления расходами",
        "docs_url": "http://127.0.0.1:8000/docs"
    }

@app.post("/expenses")
def add_expense(exp: Expense):
    data = load()
    new_id = len(data) + 1
    record = {
        "id": new_id,
        "date": datetime.now().strftime("%d.%m.%Y %H:%M"),
        "category": exp.category,
        "desc": exp.desc or "Без описания",
        "amount": exp.amount
    }
    data.append(record)
    save(data)
    return record

@app.get("/expenses")
def get_expenses():
    return load()

@app.delete("/expenses/{item_id}")
def delete_expense(item_id: int):
    data = load()
    new_data = [x for x in data if x.get('id') != item_id]
    if len(new_data) == len(data):
        raise HTTPException(status_code=404, detail="Не найдено")
    save(new_data)
    return {"message": f"Удалили запись {item_id}"}

@app.get("/total")
def get_total():
    data = load()
    return {"total": sum(x['amount'] for x in data)}