''' Tuple '''

#Tuples are immutable, meaning that you cannot change, add, or remove items after the tuple has been created.
mytuple = ("apple", "banana", "cherry")
print(mytuple)



#Tuples allow duplicate values:
mytuple = ("apple", "banana", "cherry", "apple", "cherry")
print(mytuple) # Output: ('apple', 'banana', 'cherry', 'apple', 'cherry')


''' ALL same as list but tuple is immutable '''

____________________________________________________________________________________________________________________________

''' Tuple Methods '''  


mytuple = ("apple", "banana", "cherry", "apple")
# count() method returns the number of times a specified value appears in the tuple.
print(mytuple.count("apple")) # Output: 2



# index() method returns the index of the first occurrence of the specified value.
print(mytuple.index("banana")) # Output: 1  



mytuple = ("apple", "banana", "cherry")
# len() method returns the number of items in a tuple.  
print(len(mytuple)) # Output: 3



mytuple = ("apple", "banana", "cherry")
# max() method returns the item with the highest value in a tuple. 
print(max(mytuple)) # Output: cherry



mytuple = ("apple", "banana", "cherry")
# min() method returns the item with the lowest value in a tuple.
print(min(mytuple)) # Output: apple



mytuple = ("apple", "banana", "cherry")
# sorted() method returns a new sorted list from the items in a tuple.
print(sorted(mytuple)) # Output: ['apple', 'banana', 'cherry']



mytuple = ("apple", "banana", "cherry")
# sum() method returns the sum of all items in a tuple.
mytuple = (1, 2, 3, 4, 5)
print(sum(mytuple)) # Output: 15



mytuple = ("apple", "banana", "cherry")
# tuple() method converts an iterable (e.g., list, string) into a tuple.
mylist = ["apple", "banana", "cherry"]
mytuple = tuple(mylist)
print(mytuple) # Output: ('apple', 'banana', 'cherry')



mytuple = ("apple", "banana", "cherry")
print(mytuple.index("banana")) # Output: 1



mytuple = ("apple", "banana", "cherry")
# You can use the in keyword to check if an item exists in a tuple.
if "apple" in mytuple:
    print("Yes, 'apple' is in the tuple") # Output: Yes, 'apple' is in the tuple 
    


mytuple = ("apple", "banana", "cherry")
# You can use the not in keyword to check if an item does not exist in a tuple.
if "orange" not in mytuple:
    print("No, 'orange' is not in the tuple") # Output: No, 'orange' is not in the tuple
    

    
mytuple = ("apple", "banana", "cherry")
# You can use the + operator to concatenate two tuples.
mytuple1 = ("apple", "banana", "cherry")
mytuple2 = ("orange", "kiwi", "melon")
mytuple3 = mytuple1 + mytuple2
print(mytuple3) # Output: ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon')



mytuple = ("apple", "banana", "cherry")
# You can use the * operator to repeat a tuple a specified number of times.
mytuple = ("apple", "banana", "cherry")
print(mytuple * 2) # Output: ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')

_________________________________________________________________________________________________________________