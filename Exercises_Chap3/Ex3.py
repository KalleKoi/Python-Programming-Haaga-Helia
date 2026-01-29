userinput = int(input("Enter an integer: "))
sum = 0

if userinput <= 0:
    print("Nothing to be printed")
else:
    for i in range(userinput, 0, -1):
        sum += i
        print(i, end=" ")
    print("\nThe sum is", sum)
    