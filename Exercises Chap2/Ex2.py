price = int(input("Enter the car's selling price: "))

if price < 50000:
    bonus = 0.01 * price
else:
    bonus = 0.015 * price

if bonus < 200:
    bonus = 200
print(f"The bonus is {bonus:.2f} euros.")
