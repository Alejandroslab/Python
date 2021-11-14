#Create a dictionary:

dict = {1: 'one', 2: 'two'}
print(dict)

#to clear :

dict.clear()
print(dict)

#if you want to delete all the dict just type:

#del dict

#to get the corresponding value:
dict = {1: 'one', 2: 'two'}
dict.get(1)
print(dict.get(1))

#to check if an element is present:

print(1 in dict)

#return the pairs as tuples:

dict.items()
print(dict.items

#return the values:

print(dict.values())

#if you want to get the keys:

print(dict.keys())

#to check the number of pairs:

print(len(dict))

#to add another dicitionary to the preexisting(note that duplicates will be removed)

dict2 = {1: 'one', 3: 'three'}
dict.update(dict2)
print(dict)
#the second dictionary will not change
print(dict2)
