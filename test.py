class Budget:
    def __init__(self, name, budget_name, initial_amount):
        # Encapsulated attributes
        self._user_name = name
        self._budget_name = budget_name
        self._initial_amount = initial_amount
        self._current_balance = initial_amount
        self._expenses = []
    
    # Getter methods (controlled access to private attributes)
    def get_user_name(self):
        return self._user_name
    
    def get_budget_name(self):
        return self._budget_name
    
    def get_initial_amount(self):
        return self._initial_amount
    
    def get_current_balance(self):
        return self._current_balance
    
    def get_expenses(self):
        # Return a copy to prevent external modification
        return self._expenses.copy()
    
    # Setter methods with validation
    def set_user_name(self, new_name):
        if new_name and new_name.strip():
            self._user_name = new_name.strip()
        else:
            print("Error: User name cannot be empty")
    
    def set_budget_name(self, new_budget_name):
        if new_budget_name and new_budget_name.strip():
            self._budget_name = new_budget_name.strip()
        else:
            print("Error: Budget name cannot be empty")
    
    # Business logic methods
    def add_expense(self, expense_name, amount):
        """Add an expense with validation and update balance"""
        if amount < 0:
            print("Error: Expense amount cannot be negative")
            return False
        
        # Check if expense exceeds balance
        warning = ""
        if amount > self._current_balance:
            warning = f" Warning: This expense (UGX{amount:.2f}) exceeds your current balance!"
            print(warning)
        
        # Record expense
        expense = {
            'name': expense_name,
            'amount': amount,
            'balance_before': self._current_balance
        }
        
        # Update balance
        self._current_balance -= amount
        
        expense['balance_after'] = self._current_balance
        if warning:
            expense['warning'] = True
            
        self._expenses.append(expense)
        return True
    
    def display_info(self):
        """Display user and budget information"""
        print("\n" + "=" * 40)
        print(" BUDGET INFORMATION")
        print("=" * 40)
        print(f"User: {self._user_name}")
        print(f"Budget: {self._budget_name}")
        print(f"Initial Amount: UGX{self._initial_amount:.2f}")
        print(f"Current Balance: UGX{self._current_balance:.2f}")
        print("=" * 40)
    
    def display_expense_summary(self):
        """Display all expenses and final summary"""
        print("\n" + "=" * 50)
        print(" EXPENSE SUMMARY")
        print("=" * 50)
        
        if not self._expenses:
            print("No expenses recorded.")
            return
        
        total_spent = 0
        for i, expense in enumerate(self._expenses, 1):
            print(f"\nExpense #{i}:")
            print(f"  Name: {expense['name']}")
            print(f"  Amount: UGX{expense['amount']:.2f}")
            print(f"  Balance before: UGX{expense['balance_before']:.2f}")
            print(f"  Balance after: UGX{expense['balance_after']:.2f}")
            if expense.get('warning'):
                print(f"   Exceeded available balance!")
            total_spent += expense['amount']
        
        print("\n" + "-" * 30)
        print("FINAL TOTALS:")
        print(f"  Initial Budget: UGX{self._initial_amount:.2f}")
        print(f"  Total Spent: UGX{total_spent:.2f}")
        print(f"  Final Balance: UGX{self._current_balance:.2f}")
        print(f"  Remaining: {((self._current_balance/self._initial_amount)*100):.1f}% of budget")
        print("=" * 50)


def get_positive_price(prompt):
    """Helper function to get non-negative numbers from user"""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print(" Please enter a non-negative number.")
            else:
                return value
        except ValueError:
            print(" Please enter a valid number")


def main():
    print(" PERSONAL BUDGET TRACKER")
    print("=" * 40)
    
    # Get user details (encapsulated in Budget class)
    name = input("Enter your name: ")
    budget_name = input("Enter budget name: ")
    initial_amount = get_positive_price("Enter initial budget amount (UGX): ")
    
    # Create budget object (encapsulation at work)
    my_budget = Budget(name, budget_name, initial_amount)
    
    # Display initial information using encapsulated method
    my_budget.display_info()
    
    # Record 5 expenses
    print(f"\n Enter your 5 expenses for {budget_name}:")
    
    for i in range(1, 6):
        print(f"\n--- Expense #{i} ---")
        print(f" Current Balance: UGX{my_budget.get_current_balance():.2f}")
        
        expense_name = input("Expense name: ")
        expense_amount = get_positive_price("Expense amount (UGX): ")
        
        # Add expense using encapsulated method
        my_budget.add_expense(expense_name, expense_amount)
    
    # Show final summary using encapsulated method
    my_budget.display_expense_summary()
    
    # Example of controlled access through getters
    print("\nBudget tracking complete!")
    print(f"Thank you {my_budget.get_user_name()} for using the Budget Tracker!")


if __name__ == "__main__":
    main()