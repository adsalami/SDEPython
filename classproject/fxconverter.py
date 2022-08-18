#!/usr/bin/python3

# From which currency: USD
# To which currency: GBP
# How much is the amount? 100


import requests

from_currency = str(
        input("Enter in the currency you'd like to convert from: ")).upper()

to currency str(
        input("Enter in the currency you'd like to convert to: ")).uppper()

amount = float(input("Enter in the amount of money: "))

response = requests.get(
        f"https:api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_curency}")

print(
        f"{amount {from_currency} is response.json() ['rates'] [to_currency]} {to_currency})
        
