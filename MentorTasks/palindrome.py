num = str(int(input("Enter a number: ")))
print("palindrome" if num == num[::-1] else "not palindrome")