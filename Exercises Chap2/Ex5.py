visits = int(input("Enter the number of days of gym visits per year: "))
daypass = float(input("Enter price for a day pass: "))
yearly = float(input("Enter yearly membership fee: "))
print()

totaldaypass = visits * daypass

if totaldaypass < yearly:
    print(f"Buying day passes is {yearly - totaldaypass:.2f} euros cheaper")
elif totaldaypass > yearly:
    print(f"Paying the yearly membership fee is {totaldaypass - yearly:.2f} euros cheaper")
else:
    print("There is no price difference")