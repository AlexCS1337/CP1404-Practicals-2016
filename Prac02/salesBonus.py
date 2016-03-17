"""
if sales are under $1,000, the user gets a 10% bonus
if sales are $1,000 or over, the bonus is 15%
"""

sales = float(input("Enter sales: $"))
while sales > 0:
    if sales < 1000:
        bonus = sales * 0.1
    else:
        bonus = sales * 0.15
    sales = float(input("Enter sales: $"))
    print("Bonus is $", bonus, sep="")