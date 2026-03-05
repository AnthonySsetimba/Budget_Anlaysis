from user import User
from budget import Budget
from expense import Expense


# INPUT FUNCTIONS


def get_positive_number(prompt):
    """Keeps asking until the user enters a valid non-negative number."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a non-negative number.")
            else:
                return value
        except ValueError:
            # Catches anything that can't be converted to a float (e.g. letters)
            print("Please enter a valid number.")

def get_positive_int(prompt):
    """Keeps asking until the user enters a valid positive whole number."""
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive whole number.")
            else:
                return value
        except ValueError:
            # Catches decimals and non-numeric input
            print("Please enter a valid whole number.")


# MAIN PROGRAM


def main():

    #Collect basic user and budget information 
    print("Enter your details for your weekly budget:")
    name = input("Enter your name: ")
    budget_name = input("Budget name: ")

    # Get the starting amount, must be a non-negative number
    initial_amount = get_positive_number(f"Enter your initial amount for {budget_name}: UGX ")

    # Create a User object to store and display user info
    user = User(name, budget_name)

    # Create a Budget object with the starting amount
    # This will track all expenses and the running balance
    budget = Budget(initial_amount)

    # Display the user's name and budget name
    user.display()
    print(f"Initial Money: UGX {initial_amount:.2f}\n")

    # Ask how many expenses the user wants to enter
    num_expenses = get_positive_int("How many expenses do you want to enter? ")

    print(f"\n--- Enter {budget_name} Expenses ---")

    # Expense entry loop 
    # Runs once for each expense the user wants to record
    for i in range(1, num_expenses + 1):

        print(f"\nExpense {i} of {num_expenses}")
        print(f"Current balance: UGX {budget.balance:.2f}")

        # Keep asking until a valid expense is accepted
        while True:
            expense_name = input("Expense name: ")
            amount = get_positive_number("Expense amount: UGX ")

            # Attempt to add the expense — may be rejected if it exceeds balance
            result = budget.add_expense(Expense(expense_name, amount))

            # None means the expense was rejected, ask the user to try again
            if result is None:
                print("Please try again.")
                continue

            # Expense was accepted, confirm and show updated balance
            print(f"✓ '{expense_name}' added.")
            print(f"Remaining balance: UGX {budget.balance:.2f}")
            break

        # True means budget is fully exhausted, stop accepting more expenses
        if result is True:
            break

    #  Display the full expense summary at the end 
    # Shows all items, total spent, and final remaining balance
    budget.display_summary()


# Entry point — only runs main() if this file is executed directly
# Prevents main() from running if this file is imported elsewhere
if __name__ == "__main__":
    main()