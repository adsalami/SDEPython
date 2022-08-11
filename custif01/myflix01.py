#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   if, elif, else - A simple program using conditionals to make a decision."""


message = 'Welcome to Alta3 post office, how would you like to proceed '

# write a code for calculate postrate
connection = input("What is the weight of your package?)

# if input value was higher or equal to 25
if connection >= 25:
    message = message + 'cost is equal to $40.'
elif connection >= 5:
    message = message + 'cost is equal to $15.'
elif connection >= 2:
    message = message + ''cost is equal to $2.'
else:
    message = message + 'Go to UPS!.'
print(message)

