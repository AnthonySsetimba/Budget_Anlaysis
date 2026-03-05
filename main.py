from user import User
from budget import Budget
from expense import Expense

def get_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a non-negative number.")
            else:
                return value
        except ValueError:
            print("Please enter a valid number.")

def main():
    print("Enter your details for your weekly budget:")
    name = input("Enter your name: ")
    budget_name = input("Budget name: ")
    initial_amount = get_positive_number(f"Enter your initial amount for {budget_name}: UGX ")

    user = User(name, budget_name)
    budget = Budget(initial_amount)

    user.display()
    print(f"Initial Money: UGX {initial_amount:.2f}\n")
    print(f"--- Enter {budget_name} Expenses ---")

    for i in range(1, 6):
        print(f"\nExpense {i} | Current balance: UGX {budget.balance:.2f}")
        expense_name = input("Expense name: ")
        amount = get_positive_number("Expense amount: UGX ")
        budget.add_expense(Expense(expense_name, amount))

    budget.display_summary()

if __name__ == "__main__":
    main()