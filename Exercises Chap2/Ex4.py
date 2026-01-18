gigs = int(input("Number of gigs: "))
gigstostrings = int(input("Gigs to be played with the same set of strings: "))
price = float(input("Price of a set of guitar strings: "))
print()
sets = (gigs + gigstostrings - 1) // gigstostrings

print(f"The guitarist needs {sets} new sets of guitar strings")
print(f"The total cost is {sets * price:.2f} euros")