class User:
    def __init__(self, name, budget_name):
        self.name = name
        self.budget_name = budget_name

    def display(self):
        print("\n--- User Information ---")
        print(f"Name: {self.name}")
        print(f"Budget: {self.budget_name}")