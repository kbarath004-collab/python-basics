''' Arithametic operations ''' 
x = 10
y = 5

print(x + y)
#Adds x and y -- 15

print(x - y)
#Subtracts y from x -- 5

print(x * y)
#Multiplies x and y -- 50

print(x / y)
#Divides x by y  -- 2.0

print(x % y)
#Returns the remainder of x divided by y  -- 0

print(x ** y)
#Returns x raised to the power of y  -- 100000

print(x // y)
#Returns an integer division of x by y  -- 2

__________________________________________________________________________________________________________

''' Assignment Operators '''
x = 5
x += 3  # Equivalent to x = x + 3
print(x)  # Output: 8

x = 8
x -= 2  # Equivalent to x = x - 2
print(x)  # Output: 6


x = 6
x *= 4  # Equivalent to x = x * 4
print(x)  # Output: 24


x = 24
x /= 3  # Equivalent to x = x / 3
print(x)  # Output: 8.0


x = 8
x %= 3  # Equivalent to x = x % 3 
print(x)  # Output: 2


x = 2
x **= 3  # Equivalent to x = x ** 3
print(x)  # Output: 8


x = 8
x //= 2  # Equivalent to x = x // 2
print(x)  # Output: 4

________________________________________________________________________________________

''' Comparison Operators '''

x = 10
y = 5

print(x == y) #Checks if x is equal to y
# Output: False


print(x != y) #Checks if x is not equal to y
# Output: True


print(x > y) #Checks if x is greater than y
# Output: True


print(x < y) #Checks if x is less than y
# Output: False


print(x >= y) #Checks if x is greater than or equal to y
# Output: True


print(x <= y)
# Output: False

________________________________________________________________________________

''' Logical Operators '''

x = 6
y = 8
if x > 5 and y < 10:
    print("true") # Checks if both conditions are true
    #Output: true
if x > 5 or y < 10:
    print("true") # Checks if at least one condition is true
    #Output: true
    
    
if not(x > 5 and y < 10):
    print("false") # Checks if the condition is false
    #Output: false

______________________________________________________________________________________

''' Membership Operators '''

x = "Hello, World!"

print("Hello" in x) # Checks if "Hello" is present in x
# Output: True  


print("hello" not in x) # Checks if "hello" is not present in x
# Output: True

_______________________________________________________________________________________

''' Identity Operators '''

x = 5
y = 5

print(x is y) # Checks if x and y refer to the same object
# Output: True

print(x is not y) # Checks if x and y do not refer to the same object
# Output: False 

______________________________________________________________________________________