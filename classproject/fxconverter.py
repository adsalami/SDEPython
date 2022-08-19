#!/usr/bin/python3

# Gathering information needed for the conversion
# From which currency: USD
# To which currency: GBP
# How much is the amount?

# API Calls
from forex_python.converter import CurrencyRates
c = CurrencyRates()

# Promomix-list/         t user to enter Currency they'd like to convert from
from_cumyscript.sh*      rrency = str(
       no_shebang.py*     input("Enter currency you'd like to convert from: ")).upper()
       py3_shebang.py*   
to_currLICENSE           ency str(
       README.md          input("Enter currency you'd like to convert to: ")).uppper()

amount = float(input("Enter in the amount of money: "))

response = requests.get(
        f"https:api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_curency}")

print(
        f"{amount {from_currency} is response.json() ['rates'] [to_currency]} {to_currency})
        
