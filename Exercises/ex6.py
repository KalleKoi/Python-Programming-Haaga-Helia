try:
    price = float(input("Enter price: "))
except ValueError:
    print("Invalid price")
else:
    print(f"The price with VAT is {price * 1.24:.2f}")
