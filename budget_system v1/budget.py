from expense import Expense


# BUDGET CLASS
# Handles all financial logic — tracks the running balance,
# stores expenses, and displays the final summary


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
       
        # add an expense to the budget.
        #Rejects the expense entirely if it would exceed the current balance.
        #Returns True if the budget is now exactly zero (exhausted),
        #False if there is still remaining balance.
        #Returns None if the expense was rejected.
       
        # Block the expense if it exceeds the available balance
        if expense.amount > self.balance:
            print(f"\nExpense rejected. UGX {expense.amount:.2f} exceeds "
                  f"your remaining balance of UGX {self.balance:.2f}.")
            print("Please enter a smaller amount.")
            return None  # tells main  that the expense was not added

        # Add the expense object to the list for later display in the summary
        self.expenses.append(expense)

        # Deduct the expense amount from the current balance
        self.balance -= expense.amount

        # Signal that the budget is now fully exhausted
        if self.balance == 0:
            print("\nYour budget is now fully used up.")
            return True  # Tells main to stop the loop

        return False  # Budget still has funds, loop can continue

    def display_summary(self):
        
        #Prints a table of all expenses at the end of the program.
        
        #Shows each item and its cost, then totals at the bottom.
        
        print("\n*****")
        print("   EXPENSE SUMMARY    ")
        print("******")

       

        # Loop through every expense and print its name and amount
        for e in self.expenses:
            print(f"{e.name:<20} {e.amount:>10.2f}")

        print("-" * 32)

        # Footer totals
        print(f"{'Initial amount:':<20} {self.initial_amount:>10.2f}")
        print(f"{'Total spent:':<20} {self.initial_amount - self.balance:>10.2f}")
        print(f"{'Remaining balance:':<20} {self.balance:>10.2f}")
        print("*****")