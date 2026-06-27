numbers = []
lim = int(input("How many numbers would you like to compare?: "))
for x in range(lim):
    numbers.append(int(input(f"enter your number{x+1}: ")))
print(max(numbers))