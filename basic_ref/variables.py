x = 12 #an integer value inside x variable
y = 'hello' #a string value inside y variable
z = 1.254 #float value inside z variable

______________________________________________________________________________________


''' Casting '''

x = str(12)
y = int(12.2)
z = float(12)

''' casting means converting the data type of a variable to another data type '''

_______________________________________________________________________________________


''' Using the type() function to know the data type of a variable '''

print(type(x))

_______________________________________________________________________________________


''' Global and Local Variables '''

x = "Global variable"

def my_function():
    print(x) # this will print the global variable x

my_function()

_______________________________________________________________________________________


''' Local variable example '''

def my_function():
    x = "Local variable" 
    print(x) # this will print the local variable x

my_function()

_______________________________________________________________________________________