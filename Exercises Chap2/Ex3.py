apples = input("How many apples? ")
children = input("How many children? ")

result = int(apples) // int(children)
leftover = int(apples) % int(children)
print()
print(f"Each child will get {result} apples.")
print(f"There will be {leftover} leftover apples.")