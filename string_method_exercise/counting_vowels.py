vowel = 0
consonent = 0
vowels = ("a", "e", "i", "o", "u")
var = input("Enter your sentence: ").lower().strip()
for x in var:
    if x in vowels:
        vowel+=1
    else:
        consonent+=1
print(f"Vowel: {vowel}")
print(f"Consonent: {consonent}")