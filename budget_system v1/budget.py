from expense import Expense

# -------------------------------------------------------
# BUDGET CLASS
# Handles all financial logic — tracks the running balance,
# stores expenses, and displays the final summary
# -------------------------------------------------------

class Budget:

    def __init__(self, initial_amount):
        """
        Constructor — called when a Budget object is created.
        Sets the starting amount and prepares an empty list for expenses.
        """
        self.initial_amount = initial_amount  # The original amount the user started with
        self.balance = initial_amount         # Running balance, decreases as expenses are added
        self.expenses = []                    # List that stores all Expense objects added

    def add_expense(self, expense: Expense):
        """
        Adds an expense to the budget.
        Warns the user if the expense exceeds the current balance,
        then deducts the amount from the running balance regardless.
        """
        # Warn the user but still allow the transaction
        if expense.amount > self.balance:
            print("Warning: This expense exceeds your current balance!")

        # Add the expense object to the list for later display in the summary
        self.expenses.append(expense)

        # Deduct the expense amount from the current balance
        self.balance -= expense.amount

    def display_summary(self):
        """
        Prints a formatted table of all expenses at the end of the session.
        Shows each item and its cost, then totals at the bottom.
        """
        print("\n*****")
        print("   EXPENSE SUMMARY    ")
        print("******")

        # Column headers — left-aligned item name, right-aligned cost
        print(f"{'Item':<20} {'Cost (UGX)':>10}")
        print("-" * 32)

        # Loop through every expense and print its name and amount
        for e in self.expenses:
            print(f"{e.name:<20} {e.amount:>10.2f}")

        print("-" * 32)

        # Footer totals
        print(f"{'Initial amount:':<20} {self.initial_amount:>10.2f}")
        print(f"{'Total spent:':<20} {self.initial_amount - self.balance:>10.2f}")  # Calculated on the fly
        print(f"{'Remaining balance:':<20} {self.balance:>10.2f}")
        print("*****")