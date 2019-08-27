from decimal import *

dollarAmount = 8.69

piggyBank = {
    "pennies": 0,
    "nickels": 0,
    "dimes": 0,
    "quarters": 0
}

def convert_to_change(dollarAmount, quarters, dimes, nickels, pennies):
    piggyBank["pennies"] = Decimal(dollarAmount - (dollarAmount - pennies*.01))/.01
    piggyBank["nickels"] = (dollarAmount - (dollarAmount - nickels*.05))/.05
    piggyBank["dimes"] = (dollarAmount - (dollarAmount - dimes*.1))/.1
    piggyBank["quarters"] = (dollarAmount - (dollarAmount - quarters*.25))/.25

    print(piggyBank)

convert_to_change(dollarAmount, 34, 1, 1, 4)
