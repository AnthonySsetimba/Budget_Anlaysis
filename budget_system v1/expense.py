
# EXPENSE CLASS
# Represents a single expense with a name and amount


class Expense:

    def __init__(self, name, amount):
        """
        Constructor — called when a new Expense object is created.
        Stores the name and cost of a single expense.
        """
        self.name = name      # The name of the expense (e.g. "Rent", "Food")
        self.amount = amount  # The cost of the expense in UGX

    def display(self):
        """Prints a single formatted line showing the expense name and amount."""
        print(f"  == {self.name}: UGX {self.amount:.2f}")