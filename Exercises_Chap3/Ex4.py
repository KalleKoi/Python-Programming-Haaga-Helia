total = 0
count = 0
value = float(input("Enter first number: "))

if value == 0:
    print("Nothing to be calculated")
else: 
    total += value
    count += 1

    while True:
    
        value = float(input("Enter next number: "))
        if value == 0:
            break
        total += value
        count += 1

    if count == 0:
        print("Nothing to be calculated")
    else:
        average = total / count
        print("The average is", f"{average:.2f}")