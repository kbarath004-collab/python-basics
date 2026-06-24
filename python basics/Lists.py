''' List '''

list = ["apple", "banana", "cherry"]
print(list)
# Output: ['apple', 'banana', 'cherry']

#List is mutable, can change the value of a list item and allows duplicate values
list[1] = "blackcurrant"
print(list)
# Output: ['apple', 'blackcurrant', 'cherry']

# Lists can contain different data types
list = ["apple", 1, True, 3.14]
print(list) # Output: ['apple', 1, True, 3.14]

#Use len() function to get the length of a list
list = ["apple", "banana", "cherry"]   
print(len(list)) # Output: 3

#List can be created using the list() constructor
mylist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(mylist) # Output: ['apple', 'banana', 'cherry']

_____________________________________________________________________________________________

''' List Methods '''


# List append() method
mylist = ["apple", "banana", "cherry"]
mylist.append("orange") # adds an item to the end of the list
print(mylist) # Output: ['apple', 'banana', 'cherry', 'orange']




# List insert() method
mylist = ["apple", "banana", "cherry"]
mylist.insert(1, "orange") # adds an item at the specified index
print(mylist) # Output: ['apple', 'orange', 'banana', 'cherry']




# List remove() method
mylist = ["apple", "banana", "cherry"]
mylist.remove("banana") # removes the specified item
print(mylist) # Output: ['apple', 'cherry']




# List pop() method
mylist = ["apple", "banana", "cherry"]
mylist.pop() # removes the last item in the list
print(mylist) # Output: ['apple', 'banana']




# List clear() method
mylist = ["apple", "banana", "cherry"]
mylist.clear() # removes all items from the list
print(mylist) # Output: []




# List index() method
mylist = ["apple", "banana", "cherry"]
print(mylist.index("banana")) # returns the index of the specified item




# List count() method
mylist = ["apple", "banana", "cherry", "banana"]
print(mylist.count("banana")) # returns the number of times the specified item appears in the list




# List sort() method
mylist = ["banana", "cherry", "apple"]
mylist.sort() # sorts the list in ascending order
print(mylist) # Output: ['apple', 'banana', 'cherry']




# List reverse() method
mylist = ["banana", "cherry", "apple"]
mylist.reverse() # reverses the order of the list
print(mylist) # Output: ['apple', 'cherry', 'banana']




# List copy() method
mylist = ["apple", "banana", "cherry"]
newlist = mylist.copy() # creates a copy of the list
print(newlist) # Output: ['apple', 'banana', 'cherry']




# List extend() method
mylist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
mylist.extend(tropical) # adds the items from the tropical list to the mylist
print(mylist) # Output: ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']




# List slicing
mylist = ["apple", "banana", "cherry", "mango", "pineapple", "papaya"]
print(mylist[2:5]) # prints items from index 2 to 4 (5 is not included)




# List comprehension
mylist = ["apple", "banana", "cherry", "mango", "pineapple", "papaya"]
newlist = [x for x in mylist if "a" in x] # creates a new list with items that contain the letter "a"
print(newlist) # Output: ['apple', 'banana', 'mango', 'papaya', 'pineapple']



# List comprehension with condition
mylist = ["apple", "banana", "cherry", "mango", "pineapple", "papaya"]
newlist = [x for x in mylist if x != "banana"] # creates a new list with items that are not "banana"
print(newlist) # Output: ['apple', 'cherry', 'mango', 'pineapple', 'papaya']



# List comprehension with expression
mylist = [1, 2, 3, 4, 5]
newlist = [x*2 for x in mylist] # creates a new list with each item multiplied by 2
print(newlist) # Output: [2, 4, 6, 8, 10]

____________________________________________________________________________________________________________