
# ''' Create a function called calc_dollars. In the function body, define a dictionary and store it in a variable named piggyBank. The dictionary should have the following keys defined.
# 1. quarters
# 2. nickels
# 3. dimes
# 4. pennies
# Once you have given yourself a large stash of coins in your piggybank, look at each key and perform the appropriate math on the integer value to determine how much money you have in dollars. Store that value in a variable named dollarAmount and print it.
# '''

# def calc_dollars():
#     piggyBank = {
#         "pennies": 342,
#         "nickels": 9,
#         "dimes": 32,
#         "quarters": 65,
#     }
#     dollarAmount = piggyBank['pennies'] * .01 + piggyBank['nickels'] * .05 + piggyBank['dimes'] * .1 + piggyBank['quarters'] * .25
#     print(dollarAmount)

# calc_dollars()

def calc_dollars(**coins):
    # The function should look at each key (pennies, nickels, dimes and quarters) and perform the appropriate math on the integer value to determine how much money you have in dollars. Store that value in a variable named `dollarAmount` and print it.
    dollarAmount = {
        "p": 100,
        "n": 20,
        "d": 10,
        "q": 4,    
    }
    # print(dollarAmount['p'] * coins['pennies'] + dollarAmount['n'] * coins['nickels'] + dollarAmount['d'] * coins['dimes'] + dollarAmount['q'] * coins['quarters'])

    print(coins['pennies'] / dollarAmount['p'] + coins['nickels'] / dollarAmount['d'] + coins['dimes'] / dollarAmount['n'] + coins['quarters'] / dollarAmount['q'])

calc_dollars(pennies= 342, nickels=9, dimes=32, quarters=412)
calc_dollars(pennies= 1042, nickels=9, dimes=332, quarters=4)
calc_dollars(pennies= 212, nickels=439, dimes=32, quarters=44)