#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   if, elif, else - A simple program using conditionals to make a decision."""


message = 'Happy to earn your business...  '

# wrap connection in a float() to accept decimals as numbers
weight = float(input("Welcome to Alta3Express. What is the weight of the package you want to ship?"))

# if input value was higher or equal to 50
if weight >= 25:
    message = message + 'your post rate equals to $100.'
elif weight >= 15:
    message = message + 'your post rate equals to $50.'
elif weight >= 5:
    message = message + 'your post rate equals  to $25.'
else:
    message = message + 'Unfortunately, the weight is below our minimum threshold, please go to USPS.'
print(message)

