from decimal import Decimal

firstnumber = Decimal(input("Enter first number: "))    
secondnumber = Decimal(input("Enter second number: "))
print()

result = firstnumber + secondnumber
print(f"{firstnumber} + {secondnumber} = {result}")
