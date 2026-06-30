numbers = []
num = int(input("Enter the end term number to print prime number: "))

for number in range(2, num + 1):
    for divisor in range(2, number):
        if number % divisor == 0:
            break
    else:
        numbers.append(number)
print(numbers)