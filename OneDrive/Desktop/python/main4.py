dict = {
    'name' : "Akhil Srivastava",
    'age' : 19,
    'percent' : 98.5,
    'friends' : ["Akshat", "Sahil", "Ravi"],
    'tuple' : (23,32,52,53),
}

# dict["age"] = 18

# print(dict)
# print(dict["name"])


# print(dict.get('name'))

print(dict.keys())
print(dict.values())
print(dict.items())
print(dict.get("name")) # It gives no error when key is not present
dict.update({"watch" : "Rolex"})

# Sets

collection = {1,2,3,"Akhil"}

print(collection)

collection1 = set() # Empty Set
collection1.add(44) # We cannot add list in a set
collection1.add(45)
collection1.add(46)
collection1.add(47)
collection1.remove(46)
collection1.pop() #Remove random value
# collection1.clear()

print(collection1)

collection1.union(collection)
collection1.intersection(collection)