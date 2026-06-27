string1 = input("Enter 1st word to see if its an anagram: ").lower()
string2 = input("Enter 2nd word to see if its an anagram: ").lower()

if sorted(string1) == sorted(string2):
    print("anagram")
else:
    print("not an anagram")