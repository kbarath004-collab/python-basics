string = input("Enter a word to see whether its Palindrome: ")
if string == string[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")