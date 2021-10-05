#An empty list:

mylist = []
#To fill it you will need the append() method

#A full list:

myages = [19, 20, 21, 22, 23]


#The index is always zero
To recall the first value of the list:

myages[0] = 19

#It is possible also to acces the values from the last one:

#In this case the last has an index of '-1'
#Therefore:

myages[-1] = 23

'''
You can also assign a list to a variable

'''

myvariable = myages

#Then the myvariable will become: [20, 21, 22, 23]
#You can also assign a portion of the list like:

mynewvariable = myages[2:4]
#This means that will be retrieved the values in position (or index) number 2 and for
#that is:

mynewvariable = [21, 23]

#This notation is called slice
#The item at the start index is always included 
#There is also the stepper that will retrieve ever n number from index x:y
#example:

mynewvariable2 = myages[1:5:2]

#With this you will get a sublist with every second number from index 1 to index 5-1

#Other notations:

myages[ :4]
#Will retriev values from index 0 to index 4-1
