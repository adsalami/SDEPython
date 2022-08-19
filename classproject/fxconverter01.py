#!/usr/bin/python3

# Gathering information needed for the conversion
# From which currency: USD
# To which currency: GBP
# How much is the amount?

# API Calls
from forex_python.converter import CurrencyRates
c = CurrencyRates()

# Prompt user to enter Currency they'd like to convert from
from_currency = input("Enter currency you'd like to convert from: ")).upper()

# Prompt user to enter Currency they'd like to convert to
to_currency = input("Enter currency you'd like to convert to: ")).uppper()

# Prompt user to enter amount
amount = int(input("Enter in the amount of money: "))

# Print result
print(from_currency, "To", to_currency, amount)
result = c.convert(from_currency, to_currency, amount)

print(result)
