num = int(input("Enter a number: "))
fibanocci = [0, 1]
result = 0
for _ in range(num):
    result = fibanocci[-1] + fibanocci[-2]
    fibanocci.append(result)
    
print(fibanocci[:num])