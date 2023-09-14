class category:
    deposit = 0.0
    expenses = {}
    total_expense_amount = 0.0
    
    def __init__(self, category_name) -> None:
        self.category_name = category_name.upper()
      
        
    def set_deposit(self,value:float) -> None:
        if self.__is_valid_amount(value):
            self.deposit = float(value)
        else:
            print("Invalid deposit amount")


    def add_expense(self, name:str, amount:float):
        name = name.lower()
        if self.__is_valid_amount(amount):
            if name in self.expenses:
                self.expenses[name] += float(amount)
            else:
                self.expenses[name] = float(amount)
            self.total_expense_amount += float(amount)
            self.total_expense_amount = round(self.total_expense_amount, 2)
        else:
            print("Invalid expense amount.")


    def print_expenses(self):
        print(self.category_name)

        print("-"*(15)) #print dash bar
        str_income = self.__append_zero(self.deposit)
        print(f"Deposit:        ${str_income}")

        for category in self.expenses:
            str_amount = self.__append_zero(self.expenses[category])
            print("{:<15}".format(category), '-'+str_amount)
        print("-"*(15))

        str_total_amount = self.__append_zero(self.total_expense_amount)
        print(f"Total expenses:    ${str_total_amount}")

        remaining_income = self.deposit - self.total_expense_amount
        remaining_income = round(remaining_income,2)
        str_remaining_income = self.__append_zero(remaining_income)
        print(f"Remaining Deposit: ${str_remaining_income}")


    def __append_zero(self, amount:float):
        '''appends a zero to a numerical string if needed'''
        str_amount = str(amount)
        second_to_last = len(str_amount) - 2
        if str_amount[second_to_last] == '.': #if the second to last index is a decimal then append a 0
            str_amount += '0'
        return str_amount
        

    def __is_valid_amount(self,value:float) -> bool:
        '''check if a floating point value has no more than 2 digits after the decimal point'''
        str_value = str(float(value))
        after_decimal = str_value.find('.') + 1 #find the index that is after the decimal

        return len(str_value[after_decimal:]) <= 2


class budget:
    income = 0.0
    category_dict = {}

    def __init__(self, first_name:str, last_name:str) -> None:
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()


    def set_income(self, income:float):
        if self.__is_valid_amount(income):
            self.income = float(income)
        else:
            print("Invalid income amount")


    def add_category_info(self, category_name:str, expense_name:str, expense_amount:float):
        category_name = category_name.upper()
        if category_name not in self.category_dict:
            self.category_dict[category_name] = category(category_name)

        self.category_dict[category_name].add_expense(expense_name, expense_amount)

    def print_categories(self):
        print(self.first_name, self.last_name)
        print(f"Income: ${self.income}")
        for cat in self.category_dict:
            self.category_dict[cat].print_expenses()
            print("*"*(15))

    def get_category_count(self):
        return len(self.category_dict)
        

    def __is_valid_amount(self,value:float) -> bool:
        '''check if a floating point value has no more than 2 digits after the decimal point'''
        str_value = str(float(value))
        after_decimal = str_value.find('.') + 1 #find the index that is after the decimal

        return len(str_value[after_decimal:]) <= 2
    