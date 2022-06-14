import numpy as np

list1 = [1, 2, 3]
array1 = np.array(list1)
print('array1 type: ', type(array1))
print('array1 array 형태: ', array1.shape)

array2 = np.array([[1, 2, 3], [2, 3, 4]])
print('array2 type: ', type(array2))
print('array2 array 형태: ', array2.shape)

array3 = np.array([[1, 2, 3], [2, 3, 4], [3, 4, 5]])
print('array3 type: ', type(array3))
print('array3 array 형태: ', array3.shape)

print(f'array1: {array1.ndim}차원, array2: {array2.ndim}차원, array3: {array3.ndim}차원')
print(f'array1: {array1.dtype}, array2: {array2.dtype}, array3: {array3.dtype}')
