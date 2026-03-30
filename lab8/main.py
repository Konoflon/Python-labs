import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

DATA_FILE = "expenses.json"

class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Трекер расходов")
        self.root.geometry("700x500")
        
        self.expenses = []
        self.load_data()
        
        self.create_ui()
        self.refresh_table()
        
    def create_ui(self):
        frame_input = tk.Frame(self.root)
        frame_input.pack(pady=10)
        
        tk.Label(frame_input, text="Сумма:").grid(row=0, column=0)
        self.entry_amount = tk.Entry(frame_input)
        self.entry_amount.grid(row=0, column=1)
        
        tk.Label(frame_input, text="Категория:").grid(row=0, column=2)
        self.combo_category = ttk.Combobox(frame_input, values=["Еда", "Транспорт", "Жилье", "Развлечения", "Другое"])
        self.combo_category.current(0)
        self.combo_category.grid(row=0, column=3)
        
        tk.Label(frame_input, text="Описание:").grid(row=0, column=4)
        self.entry_desc = tk.Entry(frame_input)
        self.entry_desc.grid(row=0, column=5)
        
        btn_add = tk.Button(frame_input, text="Добавить", command=self.add_expense)
        btn_add.grid(row=0, column=6, padx=10)
        
        columns = ("date", "category", "desc", "amount")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")
        self.tree.heading("date", text="Дата")
        self.tree.heading("category", text="Категория")
        self.tree.heading("desc", text="Описание")
        self.tree.heading("amount", text="Сумма")
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        frame_bottom = tk.Frame(self.root)
        frame_bottom.pack(pady=5)
        
        self.label_total = tk.Label(frame_bottom, text="Всего: 0 руб.", font=("Arial", 12, "bold"))
        self.label_total.pack(side=tk.LEFT, padx=20)
        
        btn_del = tk.Button(frame_bottom, text="Удалить", command=self.delete_expense)
        btn_del.pack(side=tk.RIGHT, padx=20)
        
    def add_expense(self):
        amount = self.entry_amount.get().replace(',', '.')
        desc = self.entry_desc.get()
        category = self.combo_category.get()
        
        try:
            amount = float(amount)
        except:
            messagebox.showerror("Ошибка", "Введите число в сумму!")
            return
            
        if amount <= 0:
            messagebox.showerror("Ошибка", "Сумма должна быть больше 0")
            return
            
        from datetime import datetime
        date = datetime.now().strftime("%d.%m.%Y %H:%M")
        
        self.expenses.append({
            "date": date,
            "category": category,
            "desc": desc if desc else "Нет описания",
            "amount": amount
        })
        
        self.save_data()
        self.refresh_table()
        self.entry_amount.delete(0, tk.END)
        self.entry_desc.delete(0, tk.END)
        
    def delete_expense(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Внимание", "Выберите строку для удаления")
            return
            
        item = self.tree.item(selected[0])
        val = item['values']
        self.expenses = [e for e in self.expenses if not (e['date'] == val[0] and e['amount'] == val[3])]
        
        self.save_data()
        self.refresh_table()
        
    def refresh_table(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
            
        total = 0
        for exp in self.expenses:
            self.tree.insert("", tk.END, values=(exp['date'], exp['category'], exp['desc'], exp['amount']))
            total += exp['amount']
            
        self.label_total.config(text=f"Всего: {total:.2f} руб.")
        
    def save_data(self):
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(self.expenses, f, ensure_ascii=False)
            
    def load_data(self):
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, 'r', encoding='utf-8') as f:
                    self.expenses = json.load(f)
            except:
                self.expenses = []

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()