mylist = []
lim = int(input("Enter how many elements to push into list: "))
for _ in range(lim):
    var = input("enter what you want: ").lower()
    if var not in mylist:
        mylist.append(var)
print(mylist)