balance = 5000

def deposit():
    global balance
    deposit = int(input("Enter your deposit: "))
    balance += deposit
    print(f"{deposit} was deposited")

def withdraw():
    global balance
    withdraw = int(input("Enter your withdraw: "))
    if withdraw > balance:
        print("amount is too high")
    else:
        balance -= withdraw
        print(f"{withdraw} was withdrawn","\nAvailable balance is: ", balance)

deposit()
withdraw()
