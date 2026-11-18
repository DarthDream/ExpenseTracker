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
          print("Expense ID:", expense["ID"])


          return expense
       elif choice==2:
          show_expenses()
       elif choice==3:
          Title=input("Enter Title:")
          Amount=input("Enter Amount:")
          Categories=input("Enter Category:")

          expense=update_exspenses(Title,Amount,Categories)
          print("Expense Updateded Succsesfuly")
       elif choice==4:
          Id=int(input("ID daxil et:"))
          expenses=load_expenses
          for a in expenses:
             if Id in a["ID"]:
                expenses=delete_expense(Title,Amount,Categories)
             else:
                print("ID not Found")
       elif choice==5:
          Titlee=input("Enter title:")
          expenses=load_expenses
          for ab in expenses:
             if Titlee in expenses:
                ab[show_expenses(Title,Amount,Categories)]
             else:
                print("Title not found")
       elif choice==6:
        total = sum(float(expense["Amount"]) for expense in expenses)
        print("Total Expenses:", total)  
    except:
       print("There Have Problem")