import json

DATA_FILE="data/expenses.json"

def load_expenses():
    try:
      with open(DATA_FILE,"r",encoding="utf-8") as file:
         expenses=json.load(file)
    except FileNotFoundError:
         return []
    except json.JSONDecodeError:
        raise ValueError("JSON file is corrupted")
def save_expenses(expenses):
      with open(DATA_FILE,"w",encoding="utf-8") as file:
         json.dump(expenses,file,indent=4,ensure_ascii=False)