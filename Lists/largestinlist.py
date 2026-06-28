mylist = []
lim = int(input("How many numbers you wanna compare: "))
for i in range(lim):
    num = int(input(f"enter number {i+1}: "))
    mylist.append(num)
    
print(max(mylist))