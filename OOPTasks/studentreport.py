class Student:
    def __init__(self):
        self.name = input("Enter your name: ").title()
        self.age = int(input("Enter your age: "))
        self.dept = input("Enter your department: ").upper()
        self.mark = []
        
    def info(self):
        subs = int(input("Enter the number of subjects: "))
        for x in range(subs):
            mark = int(input(f"Enter your mark {x+1}: "))
            self.mark.append(mark)
        
    def display(self):   
        print("\nyour name       :", self.name)
        print("your age        : ", self.age)
        print("your department : ", self.dept)
        print("Your total is   : ", sum(self.mark))
        print("Your average is : ", sum(self.mark)/len(self.mark))
        
stu1 = Student()
stu1.info()
stu1.display()