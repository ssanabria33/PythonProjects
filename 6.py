"""
Challenge: Allow the user to choose from multiple currency pairs and implement appropriate error handling for invalid currency inputs.
==============================================
Input: Ask the user to enter an amount in one currency (e.g., USD).
Processing: Convert the amount to another currency (e.g., EUR) using a fixed exchange rate.
Output: Display the converted amount in the target currency.
"""

# Fixed exchange rates
exchange_rates = {
    ("USD", "EUR"): 0.85,
    ("EUR", "USD"): 1.18
}
# list of available currency pairs
print("Available currency pairs:")
for (from_currency, to_currency) in exchange_rates:
    print (f"{from_currency} -> {to_currency}")

# Get user input
from_currency = input("\nEnter the currency you are converting from (e.g., USD): ").upper()
to_currency = input("Enter the currency you are converting to (e.g., EUR): ").upper()

# Check if the currency pair is valid
if (from_currency, to_currency) not in exchange_rates:
    print("Error: Invalid currency pair. Please try again.")
else:
    try:
        amount = float(input(f"Enter the amount in {from_currency}: "))
        rate = exchange_rates[(from_currency, to_currency)]
        converted_amount = amount * rate
        print(f"{amount:.2f} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    except ValueError:
        print("Error: Please enter a valid number for the amount.")
