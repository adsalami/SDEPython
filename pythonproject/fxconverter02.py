#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   Conditionals - FX Conversion using a while True loop."""


round = 0         # integer round initiated to 0
while True:       # sets up an infinite loop condition
    round = round + 1   # increase the round counter
    print('Welcome to TLG_FX.')

    amount = input("Please enter amount --> ")     # string ans collected from user

    if amount >= 1000:      # logic to check if amount is equal or greater than 1000
    print('your fee will be 5%')
        break              # break statement escapes the while loop

    if amount >= 500:      # logic to check if amount is equal or greater than 500
    print('your fee will be 7.5%')
        break              # break statement escapes the while loop

    elif round == 3:          # logic to ensure round has not yet reached 3
        print("Sorry, our minimum threshold is $500.")
        break               # break statement escapes the while loop

    else:                   # if amount was wrong, and round is not yet equal to 3
        print("Sorry! Try again!")


