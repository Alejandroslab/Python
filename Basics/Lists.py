#Create a new empty list
newList = []
#add a new 'a' item (append method)
newList.append('a')

#print to see it
print(newList)

#now we can remove it knowing its position :
#REMEMBER that the list'position always starts with zero.
del newList[0]
print(newList)
 # now is empty

#extend the existing list with another list

newList = [1,2,3]
newList2 = ['a', 'b', 'c']

newList.extend(newList2)
print(newList)

#check if there is the element in the newList

print('c' in newList)

#You can also concatenate 2 lists with the + operator:
#but remember that this will not modify the list!

print(newList2 + ['d', 'e'])

#You can also concatenate multiple times with the * operator
#this will duplicate and concatenate

print(newList2*3)
#you will get newList2 with 'a','b','c','d','e'
#3 times 

#Add an item without overwriting the position

newList.insert(0, 'MyItem')
print(newList)

#check the number of items inside the newList

print(len(newList))

#get the value of an item and remove it

SelectedItem = newList.pop(0)
print(SelectedItem)

#now check your list and you will see that the item has been deleted
print(newList)

#you can also remove the last item leaving the parameter of the .pop method empty

#SelectedItem = newList.pop()

#You can also remove an item knowing its value

newList.remove('c')
print(newList)


#Finaly you can reverse the items in a list with .reverse() method

newList2.reverse()
print(newList2)

#or you can sort it alphabetically or numerically

newList2.sort()
print(newList2)

#you can also sort without having to sort the original list

newList3 = sorted(newList2)
#check it:
print(newList2)
print(newList3)
