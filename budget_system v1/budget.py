from expense import Expense

class Budget:
    def __init__(self, initial_amount):
        self.initial_amount = initial_amount
        self.balance = initial_amount
        self.expenses = []

    def add_expense(self, expense: Expense):
        if expense.amount > self.balance:
            print("Warning: This expense exceeds your current balance!")
        self.expenses.append(expense)
        self.balance -= expense.amount

    def display_summary(self):
        print("\n*****")
        print("   EXPENSE SUMMARY    ")
        print("******")
        print(f"{'Item':<20} {'Cost (UGX)':>10}")
        print("-" * 32)
        for e in self.expenses:
            print(f"{e.name:<20} {e.amount:>10.2f}")
        print("-" * 32)
        print(f"{'Initial amount:':<20} {self.initial_amount:>10.2f}")
        print(f"{'Total spent:':<20} {self.initial_amount - self.balance:>10.2f}")
        print(f"{'Remaining balance:':<20} {self.balance:>10.2f}")
        print("*****")
