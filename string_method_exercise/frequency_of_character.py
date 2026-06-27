var = []
string = input("Enter a string: ").lower()
for ch in string:
    if ch not in var:
        var.append(ch)
        print(ch, ":", string.count(ch))