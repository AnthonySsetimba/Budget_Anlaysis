#command-line utility for personal financial management
# track financial transactions, maintain a real-time
#account of cumulative spending
#  and provide essential feedback to the user regarding their fiscal status. 
# The final output will be a comprehensive summary of the user's financial activity.





class prices:
    def get_positive_price(firstPrice):
        #get a non-negative digit from user
        while True:
            try:
                value = float(input(firstPrice))
                if value < 0:
                    print("Please enter a non-negative number.")
                else:
                    return value
            except ValueError:
                print("Please enter a valid number ")


def main():
    price = prices(firstprice)
print("Enter your details for your weekly Budget:")

# Get user's name
name = input("Enter your name: ")

# Get user's class
budget_name = input("Budget name: ")

# Get initial amount of money 
initial_money = get_positive_price(f"Enter your initial amount of money for :{budget_name}: ")

#how many iteams user has to enter


# Display initial information
print("\n--- User Information ---")
print(f"Name: {name}")
print(f"Class: {budget_name}")
print(f"Initial Money: UGX{initial_money:.0f}\n")

print(f"--- Enter  {budget_name} Expenses ---")

current_balance = initial_money

# Ask for 5 expenses and subtract each one
for i in range(1, 6):
    print(f"\nExpense :{i}")
    print(f"Current balance: UGX: {current_balance:.0f}")
    
    expense_Name = input("enter the name of the expense: ")
    expense = get_positive_price("Enter expense amount: ")

    
    # Check if expense is greater than current balance
    if expense > current_balance:
        print("Warning: This expense exceeds your current balance!")
    
    current_balance -= expense
    print("==New Iteam== ", expense_Name)
    print(f"Remaining balance: UGX{current_balance:.2f}")


    #DISPLAYING AN EXPENSS SAMARY

  

#ask user to enter 5 inputs(expenes and for each expense, subtract its cost from the initial price while reculaculting the initial price every after an input )
