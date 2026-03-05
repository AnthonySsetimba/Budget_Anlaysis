class Expense:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def display(self):
        print(f"  == {self.name}: UGX {self.amount:.2f}")