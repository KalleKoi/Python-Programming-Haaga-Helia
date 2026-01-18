female = input("Enter the number of female students: ")
male = input("Enter the number of male students: ")
total = int(female) + int(male)
print()

if total == 0:
    percentagefemale = 0
    percentagemale = 0
else:
    percentagefemale = (int(female) / total) * 100
    percentagemale = (int(male) / total) * 100

print(f"Female: {percentagefemale:.1f} %")
print(f"Male: {percentagemale:.1f} %")