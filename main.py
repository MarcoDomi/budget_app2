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
file.close()

category_list = my_budget.get_categories()
percentage = 100.0
for ca in category_list: #TODO ADD ERROR HANDLING FOR PERCENTS  
    print(f"{percentage}% of income remaining")
    p = float(input(f"Enter {ca} category percentage:"))
    percentage -= p
    my_budget.set_category_deposit(ca, p)

my_budget.print_statement()
