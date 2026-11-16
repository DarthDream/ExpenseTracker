from exspenses import*
from validation import*
from reports import*

def show_menu():
    print("="*40)
    print("            EXPENSE TRACKER           ")
    print("="*40)

    print('''
    
    1.Add Expense
    2.Show All Expenses
    3.Edit Expense
    4.Delete Expense
    5.Search Expense
    6.Show Total Expenses
    7.Show Category
    8.Export to CSV
    
       0.Exit

    ''')
    print("="*40)

def app():
   while True:
    show_menu()
    choice=int(input("Secim et:"))

    try:
       if choice==1:
          Title=input("Enter Title:")
          Amount=input("Enter Amount:")
          Categories=input("Enter Category:")

          expense=add_exspenses(Title,Amount,Categories)
          print("Expense Added Succsesfuly")
          print(show_expenses "ID")

          return expense
    except:
       print("There Have Problem")