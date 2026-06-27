name = input("Enter your name: ")
age= int(input("Enter your age: "))
math = int(input("Enter your math mark: "))
che = int(input("Enter your chemistry mark: "))
phy = int(input("Enter your physics mark: "))

age+=1
total = math + che + phy
avg = total/3

print("Next year you will be: ", age)
print("highest mark is: ", max(che,phy,math))
print("lowest mark is: ", min(che,phy,math))
print("average is: ", avg)
print("Your total is: ", total)