#!/usr/bin/python3

# Gathering information needed for the conversion
# How much is user converting?
# How much is the amount?

# But first of all.let's explore the 'if, elif, else' conditionals to make a decision."""


message = 'Happy to earn your business today...  '

# wrap connection in a float() to accept decimals as numbers
amount = float(input("Welcome to TLG_FX. Please enter the amount you want to convert today?"))

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
    message = message + 'Unfortunately, the amount is below our minimum threshold, please go to WesterUnion.'
print(message)





