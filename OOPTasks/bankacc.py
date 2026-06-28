#ATM using functions#
import string, random

gen_amount = random.randint(1000,10000)

balance = gen_amount

pool = string.digits

password = None
user_password = None

def avail_balance():
    global balance
    print(f"Your balance is: {balance}")

def deposit():
    global balance
    while True:
        try:
            amount = int(input("enter your deposit: "))
            if amount > 0:
                balance += amount
                print(f"\nYour balance after depositing is: {balance}")
                break
            else:
                print("Please enter something valid")
        except ValueError:
            print("Please enter a valid amount")

def withdraw():
    global balance
    while True:
        try:
            withdraw_amount = int(input("enter your withdraw amount: "))
            if withdraw_amount <= balance:
                balance -= withdraw_amount
                print(f"Rs.{withdraw_amount} is Withdrawn!! ")
                print(f"\nYour balance after withdraw is: {balance}")
                break
            else:
                print("Please enter a valid amount")
        except ValueError:
            print("Please enter something valid")

def atm_menu():
    global password, user_password
    while True:
        verification = (input("enter your PIN: "))

        if verification in [user_password, password]:
            print("PIN is correct! ")
            print("Please Select choice you want to do (1,2,3,4): ")
            print("\n1. to check balance" "\n2. to deposit" "\n3. to withdraw" "\n4. to quit: ")

            # use cases#
            while True:
                options = input("\nenter your choice: ")

                if options == "1":
                    avail_balance()
                    continue
                elif options == "2":
                    deposit()
                    continue
                elif options == "3":
                    withdraw()
                    continue
                elif options == "4":
                    print("Thank you for your visit!")
                    quit()
                else:
                    print("Please enter a valid number")
                    continue
                # to this end#

        else:
            print("PIN is incorrect! ")
            continue
while True:

    options = input("1.Generate PIN  2.Choose your own!: ")

    if options.lower() == "1":
        password = random.choices(pool,k=4)
        password = "".join(password)
        print(f"Your PIN is: {password}")
        atm_menu()
    elif options == "2":
        user_password = input("Enter your PIN(only four numbers): ")
        while len(user_password) != 4:
            print("please enter four numbers")
            user_pass = input("Enter your PIN(only four numbers): ")
            continue
        print(f"Your PIN is Set: {user_password}")
        atm_menu()

    else:
        print("Please enter a valid option")
        continue