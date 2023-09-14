from budget import budget

my_budget = budget("Marco", "Dominguez")
my_budget.set_income(1000)
file = open("expense.txt")
for line in file:
    info = line.split(" ")
    category_name = info[0]
    expense_name = info[1]
    amount = float(info[2])
    my_budget.add_category_info(category_name, expense_name, amount)

my_budget.print_categories()
#print(my_budget.get_category_count())
print(my_budget.category_dict['FOOD'].expenses)
file.close()
