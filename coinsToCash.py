

def calc_dollars():
     piggybank = {
         "quarters": 6,
         "dimes": 15,
         "nickels": 36,
         "pennies": 250
     }

     total_quarter = piggybank["quarters"] * .25
     total_dimes = piggybank["dimes"] * .10
     total_nickels = piggybank["nickels"] * .05
     total_pennies = piggybank["pennies"] * .01

     dollaramount = total_pennies + total_nickels + total_dimes + total_quarter

     print('$',dollaramount)

calc_dollars()

