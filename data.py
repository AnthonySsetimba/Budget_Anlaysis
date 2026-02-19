# 1. Budget Initialization 
print("--- Welcome to your Mukono Financial Assistant ---")
try:
    budget = float(input("Enter your initial budget for the period: "))
    if budget < 0:
        print("Error: Budget cannot be negative. Setting to 0.")
        budget = 0
except ValueError:
    print("Invalid input. Please enter a numerical value.")
    budget = 0

# 2. Variable Setup [cite: 33, 38]
total_expenses = 0.0
transaction_log = [] # To store descriptions and amounts
transaction_count = 0

# 3. Transactional Logging Loop [cite: 30, 31]
# We use a loop to ensure at least 5 transactions are captured
while True:
    print(f"\n--- Recording Transaction #{transaction_count + 1} ---")
    
    description = input("Enter transaction description (e.g., Lunch at Bobics): ") [cite: 32]
    try:
        amount = float(input("Enter the amount: ")) [cite: 32]
    except ValueError:
        print("Invalid amount. Please enter a number.")
        continue

    # Update cumulative total and log [cite: 33, 38]
    total_expenses += amount
    transaction_log.append({"desc": description, "amt": amount})
    transaction_count += 1

    # Real-time fiscal oversight 
    if total_expenses > budget:
        print("!!! WARNING: You have breached your budget ceiling !!!")

    # Check if user wants to stop after the minimum requirement [cite: 31, 36]
    if transaction_count >= 5:
        choice = input("\nWould you like to add another transaction? (y/n): ")
        if choice.lower() != 'y':
            break

# 4. Final Financial Summary Report [cite: 36, 37]
print("\n" + "="*40)
print("FINAL FINANCIAL REPORT")
print("="*40)
print(f"Initial Budget:    {budget:,.2f} UGX")
print(f"Total Expenses:    {total_expenses:,.2f} UGX")

# Calculate financial position 
balance = budget - total_expenses
if balance >= 0:
    print(f"Remaining Balance: {balance:,.2f} UGX (Status: Under Budget)")
else:
    print(f"Deficit Amount:    {abs(balance):,.2f} UGX (Status: Overspent)")

# Itemized Log 
print("\nItemized Transaction Log:")
for item in transaction_log:
    print(f"- {item['desc']}: {item['amt']:,.2f} UGX")
print("="*40)
