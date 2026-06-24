subject = []
mark = 0
name = input("Enter your name: ")
count = int(input("Enter no. of subjects: "))
for i in range(count):
    sub = input("Enter subject name: ",)
    subject.append(sub)

for sub in subject:
    mark += int(input(f"Enter {sub} mark: "))

print("your total mark is: ", mark)
print("Your average is: ", mark/count)
