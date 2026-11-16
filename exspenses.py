import uuid
from datetime import*
from storage import*
from validation import*
from exception import* 

def add_exspenses(title,amount,category):
    exspenses=load_expenses()

    exspense={
       "ID":str(uuid.uuid4())[:8],
       "Title":validate_title(title),
       "Amount":validate_amount(amount),
       "Category":validate_category(category),
       "Date":date.today().isoformat()
    }

    exspenses.append(exspense)
    save_expenses(exspenses)

    return exspense

def show_expenses():
    return load_expenses()

def search_expenses(exspenseID):
    exspenses=load_expenses()
    for e in exspenses:
     if e["ID"]==exspenseID:
        return e
    expensesNotFound()

def update_exspenses(exspenseID,title,amount,category):
   expenses=load_expenses()
   for e in expenses:
     if e["ID"]==exspenseID:
        e["Title"]=validate_title(title)
        e["Amount"]=validate_amount(amount)
        e["Category"]=validate_category(category)

        save_expenses(expenses)

   expensesNotFound()
def delete_expense(exspenseID):
   exspenses=load_expenses
   for e in exspenses:
     if e["ID"]==exspenseID:
        exspenses.remove(e)

        save_expenses

        return True
   expensesNotFound()