principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate: "))
time = float(input("Enter the time period in years: "))

# Calculate the compound interest
compound_interest = principal * ((1 + rate/100) ** time - 1)

# Calculate the total amount
total_amount = principal + compound_interest

# Display the result
print("Compound Interest is:", compound_interest)
print("Total Amount is:", total_amount)
