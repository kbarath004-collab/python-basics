''' Sets '''

#Sets are unordered and unindexed. And they do not allow duplicate values, can add or remove items but cannot change existing items.


myset = {"apple", "banana", "cherry"}
print(myset) # Output: {'banana', 'cherry', 'apple'}
#sets are written with curly brackets.


#Does not allow duplicate values:
myset = {"apple", "banana", "cherry", "apple"}
print(myset) # Output: {'banana', 'cherry', 'apple'}


myset = {"apple", "banana", "cherry"}
#len() method returns the number of items in a set.
print(len(myset)) # Output: 3

_________________________________________________________________________________________________________________________________________________


''' Set Methods '''

myset = {"apple", "banana", "cherry"}
# add() method adds an item to a set.
myset.add("orange")
print(myset) # Output: {'banana', 'cherry', 'apple', 'orange'}


myset = {"apple", "banana", "cherry"} 
# remove() method removes the specified item from the set.
myset.remove("banana")
print(myset) # Output: {'cherry', 'apple'}


myset = {"apple", "banana", "cherry"}
# discard() method removes the specified item from the set.
myset.discard("banana")
print(myset) # Output: {'cherry', 'apple'}  


myset = {"apple", "banana", "cherry"}
# pop() method removes the last item from the set.
myset.pop()
print(myset) # Output: {'banana', 'cherry'}  (Note: The output may vary since sets are unordered)


myset = {"apple", "banana", "cherry"}
# clear() method removes all items from the set.
myset.clear()
print(myset) # Output: set()  (An empty set)


myset = {"apple", "banana", "cherry"}
# del keyword deletes the set completely.   
del myset
print(myset) # Output: NameError: name 'myset' is not defined (since the set has been deleted)


myset = {"apple", "banana", "cherry"}
# copy() method returns a copy of the set.
newset = myset.copy()
print(newset) # Output: {'banana', 'cherry', 'apple'}


myset = {"apple", "banana", "cherry"}
# union() method returns a new set with all items from both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"orange", "kiwi", "melon"}
set3 = set1.union(set2)
print(set3) # Output: {'banana', 'cherry', 'kiwi', 'apple', 'melon', 'orange'}


myset = {"apple", "banana", "cherry"}
# intersection() method returns a new set with items that are present in both sets.
set1 = {"apple", "banana", "cherry"}  
set2 = {"banana", "kiwi", "melon"}
set3 = set1.intersection(set2)
print(set3) # Output: {'banana'}


myset = {"apple", "banana", "cherry"}
# difference() method returns a new set with items that are present in the first set but not in the second set.
set1 = {"apple", "banana", "cherry"}   
set2 = {"banana", "kiwi", "melon"}
set3 = set1.difference(set2)
print(set3) # Output: {'cherry', 'apple'}

__________________________________________________________________________________________________________________________________________