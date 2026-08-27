total = 0

while True:
    expense = input("Enter expense (or 'done' to finish): ")

    if expense.lower() == "done":
        break

    total = total + float(expense)

print("Total Spent:", total)