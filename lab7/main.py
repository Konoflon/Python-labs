import typer
from modules import lab4, lab5, lab6

app = typer.Typer()

@app.command("lab4")
def task4():
    lab4.run()

@app.command("lab5")
def task5():
    lab5.run()

@app.command("lab6")
def task6(city: str = "Сургут", days: int = 5):
    lab6.run(city, days)

@app.command("all")
def all_tasks(city: str = "Сургут", days: int = 5):
    lab4.run()
    print()
    lab5.run()
    print()
    lab6.run(city, days)

if __name__ == "__main__":
    app()