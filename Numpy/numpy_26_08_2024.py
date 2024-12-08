import numpy as np

# create 1D array
arr1 = np.array([1,2,3,4,5])
print(arr1)
print(type(arr1))
print(arr1.shape) # Its an 1 dimensional array

arr2 = np.array([1,2,3,4,5])
print(arr2.reshape(1,5))
print(arr2.shape)

arr3 = np.array([[1,2,3,4,5]])
print(arr3.shape)

arr4 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr4)

print(np.arange(0,10,2))
print(np.arange(0,10,2).reshape(5,1))

print(np.ones((4,5)))   # because its a 2D array
print(np.ones(1,))

print(np.eye(3))

"""Attributes of numpy array"""

arr = np.array([[1,2,4],[5,6,7]])
print('Array :\n ',arr)
print('Shape :', arr.shape)
print('Number of dimension :', arr.ndim)
print('size of number of elements :', arr.size)
print('Data type :', arr.dtype)
print('Item size (In bytes) :', arr.itemsize)


"""numpy vectorized operation"""
a = np.array([1,2,3,4,5])
b = np.array([10,20,30,40,50])

"""Element wise operation"""
print('Addition :', a + b)
print('subraction :', a - b)


"""Universal Function"""
arr = np.array([1,2,3,4,5])

""" square root function"""
print(np.sqrt(arr))

"""Exponential"""
print(np.exp(arr))

"""Sine"""
print(np.sin(arr))

"""natural log"""
print(np.log(arr))


"""Array slicing and indexing"""
arr = np.array([[1,2,3,4],
                [4,5,6,7],
                [7,8,9,20]])
print(arr)
print(arr[0])

print(arr[0][1])

print(arr[1:,2:])    # to get [6,7][9,20]
print()
print(arr[0:2, 1:-1]) # to get [2,3][5,6]
print()
print(arr[0:2, 2:]) # to get [3,4][6,7]
print()
print(arr[1:, 1:-1]) # to get [5,6][8,9]


"""Modify array elements"""
arr[0,0] = 50
print(arr)


"""Statistical concepts - Normalization"""
"""To have mean as 0 and standard deviation as 1 """

data = np.array([1,2,3,4,5])

mean = np.mean(data)
std_dev = np.std(data)
median = np.median(data)
variance = np.var(data)

"""Normalize data (It is like converting our data in a way that mean is 0 and std_dev is 1)"""
Normalized_data = (data - mean)/std_dev
print(Normalized_data)


"""Logical operation"""
data = np.array([1,2,3,4,5,6,7,8,9,10])
print(data > 5)  # it is in boolean
print(data[(data > 5) & (data < 8)]) # it will give numbers