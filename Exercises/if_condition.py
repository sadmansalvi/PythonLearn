price_house = 1000000

credit_good = True

if credit_good:
    down_payment = 0.1 * price_house
else:
    down_payment = 0.2 * price_house

print(f"Down Payment: ${down_payment}")