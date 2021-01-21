import numpy as np
#All zeros matirx
print(np.zeros((2,3))) #Creates an array of 2X3 with all zeros

#All ones matirx
print(np.ones((4,2,3))) #Creates an array of 4 2X3 with all ones

#Create non zero or 1 matrix
print(np.full((2,2), 10))

#Create non zero or 1 matrix
print(np.full((2,2), 10))

#Create matrix of same shape of another array
ref_array = np.array([1,2,2,4])
print(np.full_like(ref_array, 30))

#Random decimal numbers
print(np.random.rand(4,2))
#Random integer numbers
print(np.random.randint(3, size=(4,2)))#start number 3
#identity matrix
print(np.identity(4))
# repeat
arr= np.array([[1,2,3]])
r1 = np.repeat(arr, 3, axis=0) #3 is no.of repetitions, axis repeat row or column
print(r1)

ones_array = np.ones((5,5))
zeros_array = np.zeros((3,3))
zeros_array[1,1] = 9
ones_array[1:4, 1:4] = zeros_array #ones_array[1:-1, 1:-1] = zeros_array
print(ones_array)

## Array copy
a= np.array([1,2,3])
b=a.copy()
b[0]=12
print(a)
print(b)
