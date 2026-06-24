''' Dictionary '''

#Dictionaries are stored values in key:value pairs, with no duplicates

dictionary = {
    
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(dictionary) # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}


dictionary = {
    
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(dictionary["brand"]) # Output: Ford

__________________________________________________________________________________________________________

#get key of a value uing 'get' keyword

dictionary = {
    
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(dictionary.get("brand")) #output "Ford"



# The 'keys()' keyword is used to get all keys of a dictionary

dictionary = {
    
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(dictionary.keys()) #output ['brand', 'model', 'year'] 


# The values() keyword is used to get all values of a dictionary

dictionary = {
    
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(dictionary.values()) #output ['Ford', 'Mustang', '1964']



# item() returns all items in a dictionary as a tuple

dictionary = {
    
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(dictionary.items()) #output 


__________________________________________________________________________________________________________________________________________#

#Update a dictionary

dictionary = {
    
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(dictionary.update({"year": 1990})) #output "year": 1990


___________________________________________________________________________________________________________________________