x = 'hello world'
print(x.upper()) #this will print the string in uppercase
''' output: HELLO WORLD '''


x = 'HELLO WORLD'
print(x.lower()) #this will print the string in lowercase
''' output: hello world '''


x = 'hello world' 
print(x.capitalize()) #this will print the string with the first character capitalized
''' output: Hello world '''


x = 'hello world'
print(x.title()) #this will print the string with the first character of each word capitalized
''' output: Hello World '''


x = '   hello world   '
print(x.strip()) #this will print the string without any leading or trailing whitespace
''' output: hello world '''


x = 'hello world'
print(x.replace('h', 'H')) #this will replace all occurrences of "h" with "H"
''' output: Hello world '''


x = 'hello world'
print(x.split(' ')) #this will split the string into a list of words based on the space character
''' output: ['hello', 'world'] '''


x = 'hello world'
print(x.find('world')) #this will return the index of the first occurrence of "world" in the string
''' output: 6 '''


x = 'hello world'
print(x.count('l')) #this will return the number of occurrences of "l" in the string
''' output: 3 '''


x = 'hello world'
print(x.index('o')) #this will return the index of the first occurrence of "o" in the string
''' output: 4 '''


x = 'hello world'
print(x.isdecimal()) #this will return True if all characters in the string are decimal characters, otherwise False
''' output: False '''


x = 'hello world'
print(x.isalnum()) #this will return True if all characters in the string are alphanumeric, otherwise False
''' output: False '''


x = 'hello world'
print(x.isalpha()) #this will return True if all characters in the string are alphabetic, otherwise False
''' output: False '''