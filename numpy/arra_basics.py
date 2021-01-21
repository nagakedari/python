import numpy as np

#array initialization
a= np.array([1,2,3], dtype='int32')
print(a)
#2 dimensional array
b= np.array([[9.0,6.0,7.0],[5.0,4.3,5.8]])
print(b)

#3 dimensional array
c= np.array([[[9.0,6.0,7.0],[5.0,4.3,5.8],[3.2,4.2,5.2]]])
print(c)

# get dimension
print(a.ndim)
print(b.ndim)
print(c.ndim)

#get shape
print(a.shape)
print(b.shape)
print(c.shape)

#get type
print(a.dtype)
print(b.dtype)
print(a.itemsize)# number of bytes of single element
print(a.nbytes)# total number of bytes of the entire array

d = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
#Get a specific element
print(d[1,3]) # d[r, c] d[2nd row, 4th column]

#Get a specific row
print(d[1, :]) # d[r: ] d[2nd row elements]

#Get a specific column
print(d[:, 0]) # d[: c] d[1st column elements]

#[startindex:endindex:stepsize]
#if we have to get every other elements starting from element 2 to 6
print(d[0, 1:6:2])

#Changing values
d[1,4] = 20
d[:, 2] = [6,9]
print(d)

#3d- arrays
e=np.array([[[1,2], [3,4]],[[5,6], [7,8]]])
print(e)
print(e.shape)
print(e[0,1,1])#First section 2nd row, 2nd column