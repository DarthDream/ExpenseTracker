from exception import*


CATEGORIES=[
    "Food"
    "Shohping"
    "Education"
    "Health"
    "Entertainment"
    "Other"
]

def validate_titlr(title):
    title=title.strip()

    if not title:
        invalidExpense("Title cannot emptty!!!")
    return title
def validate_amount(amount):
    try:
        amount=float(amount)
    except ValueError:
        invalidExpense("Amount must be number")
    if amount<=0:
        invalidExpense("Amout must be grader 0")