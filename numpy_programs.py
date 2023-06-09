# -*- coding: utf-8 -*-
"""Numpy programs.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gLOG08ggBNi1kg9NwAq160V8VLZA656y
"""

import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)
print(type(arr))

import numpy as np
x=np.array([6,7,8,9])
print(x)
print(type(x))

import numpy as np
arr=np.array(44)
print(arr)
print(type(arr))

import numpy as np
x=np.array([[1,2,3],
            [4,5,6]])
print(type(x))
print(x)

import numpy as np
x=np.array([1,2,3],ndmin=7)
print(x)

array=[20,30,40,50]
x=array[0]
print(x)

import numpy as np
my_array = np.array([10, 20, 30, 40, 50])
first = my_array[0]
print(first)

import numpy as np
my_arr=np.array([1,2,3])
firstx=my_arr[0]
print(firstx)

import numpy as np
arr=np.array([9,8,7,6])
x=arr.copy()
arr[0]=42
print(x)
print(arr)

import numpy as np
arr=np.array([6,7,8,99,-2])
x=np.max(arr)
y=np.min(arr)
print(x)
print(y)

import numpy as np
arr=np.array([22,66,55,44,33])
x=np.sort(arr)
print(x)

import numpy as np

# Create a list of 1D arrays
array_list = [np.array([10, 20, 30]), np.array([40, 50, 60]), np.array([70, 80, 90])]

# Find the mean of each array
for arr in array_list:
    mean = np.mean(arr)
    print(mean)

import numpy as np

# Create a 3x3 NumPy array
my_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Create a new row and append it to the array
new_row = np.array([10, 11, 12])
my_array = np.vstack((my_array, new_row))

# Create a new column and append it to the array
new_col = np.array([13, 14, 15, 16])
my_array = np.column_stack((my_array, new_col))

print(my_array)

import numpy as np
a=np.array(42)
b=np.array([1,2,3,4,5])
c=np.array([[1,2,3],[4,5,6]])
d=np.array([[[1,2,3],[4,5,6]],[[1,2,3][4,5,6]]])

print(a.ndim)
print(b.ndim)

print(c.ndim)
print(d.ndim)