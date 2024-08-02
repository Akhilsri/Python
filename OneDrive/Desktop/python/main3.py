list = [98.3, 88.5, 92.5, 78.9, "Akhil"];
list[4] = 17; #lists are mutable
print(list)
print(type(list))

print(list[1:3])

# List Methods
list.append(85.0);
list.sort()
list.sort(reverse=True)
list.reverse()
list.insert(2,50.9)
list.remove(92.5)
list.pop(2)

print(list)


# Tuple

tup = (22,43,1,9,55,1,1)

tup1 = () #Empty tuple

tup2 = (1,) #Single value tuple     

tup3 = (1) #Here type is integer

print(tup.index(43))
print(tup.count(1))

print(type(tup))