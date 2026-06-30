year = int(input("Enter a year to check if its a leap year: "))
if year % 400 == 0:
    print(f"{year} is a leap year")
elif year % 100 == 0:
    print(f"{year} not leap year")
elif year % 4 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")