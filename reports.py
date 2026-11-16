import csv
from exspenses import*
def total_exspenses():
    exspenses=show_expenses()

    total=0
    for e in exspenses:
       total+=e["Amount"]

    return total
def export_to_CSV():
    exspenses=show_expenses

    file_path="data/expenses.csv"
    field_names=["ID","Title","Amount","Category","Date"]

    with open(file_path,"w",newline="",encoding="utf-8") as file:
        writer=csv.DictWriter(file,fieldnames=field_names)
        writer.writeheader()
        writer.writerows(exspenses)

    return file_path