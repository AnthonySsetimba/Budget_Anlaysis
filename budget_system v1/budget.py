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
        print("\n--- Expense Summary ---")
        for e in self.expenses:
            e.display()
        print(f"\nInitial amount:  UGX {self.initial_amount:.2f}")
        print(f"Total spent:     UGX {self.initial_amount - self.balance:.2f}")
        print(f"Remaining:       UGX {self.balance:.2f}")