import random

MAX_INCREASE = 0.1 # 10%
MAX_DECREASE = 0.175 # 5%
MIN_PRICE = 1.0
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0

price = INITIAL_PRICE
day = 0
print("Starting Price: ${:,.2f}".format(price))

while price >= MIN_PRICE and price <= MAX_PRICE:
    priceChange = 0
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        priceChange = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_INCREASE and 0
        priceChange = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + priceChange)
    day += 1
    print("On day", day, "${:,.2f}".format(price))