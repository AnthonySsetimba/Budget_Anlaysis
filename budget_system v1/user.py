# -------------------------------------------------------
# USER CLASS
# Stores the user's personal details and displays them
# -------------------------------------------------------

class User:

    def __init__(self, name, budget_name):
        """
        Constructor — called when a User object is created.
        Stores the user's name and the name of their budget.
        """
        self.name = name              # The user's full name
        self.budget_name = budget_name  # The name given to this budget (e.g. "Weekly Budget")

    def display(self):
        """Prints a formatted summary of the user's basic information."""
        print("\n--- User Information ---")
        print(f"Name: {self.name}")
        print(f"Budget: {self.budget_name}")