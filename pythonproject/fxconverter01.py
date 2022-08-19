#!/usr/bin/python3

# Gathering information needed for the conversion
# From which currency: USD
# To which currency: GBP
# How much is the amount?


# But first of all.let's explore the 'if, elif, else' conditionals to make a decision."""

message = 'Happy to earn your business today...  '

# wrap connection in a float() to accept decimals as numbers
amount = float(input("Welcome to TLG_FX. Please enter the amount you want to send today?"))


# if input value was higher or equal to 1000
if amount >= 1000:
    message = message + 'your conversion fee will be 5%.'

# if input was higher or equal to 500
elif amount >= 500:
    message = message + 'your conversion fee equals to 7.5%'

# if input was higher or equal to 100
elif amount >= 100:
    message = message + 'your comversion fee equals to 10%.'
else:    
    message = message + 'Unfortunately, the weight is below our minimum threshold, please go to USPS.'
print(message)


from forex_python.converter import CurrencyRates
c = CurrencyRates()

# Prompt user to enter Currency they'd like to convert from
from_currency = input("Enter currency you'd like to convert from: ")

# Prompt user to enter Currency they'd like to convert to
to_currency = input("Enter currency you'd like to convert to: ")

# Prompt user to enter amount
amount = int(input("Enter in the amount of money: "))

# Print result
print(from_currency, "To", to_currency, amount)
result = c.convert(from_currency, to_currency, amount)

print(result)


