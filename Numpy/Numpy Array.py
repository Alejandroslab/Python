import numpy as np
myarray = np.array([1,2,3])

print(myarray)

print(myarray.ndim)
myarray.shape

len(myarray)

a = np.arange(10)
print(a)

#start,end, step
b = np.arange(1,9,2)
print(b)

#the first one is the number of rows , the second argument is the number of columns
one = np.ones((5, 2))
print(one)


zeros = np.zeros((2,5))
print(zeros)

#identity matrix. to see it, it should have 2 rows and 2 columns

id = np.eye(2,2)
print(id)

empty = np.empty((3,3))
print(empty)

#creates a matrix 3x3 with a random number between 0 and 10
integers1 = np.random.randint(0,10,(3,3))
print(integers1)


#Each numpy array requires that the data contained is of the same type
a = np.arange(10)
print(a)
#slice: it will show the first 4 elements of the array
print(a[:4])

#start,end, step
print(a[::2])
