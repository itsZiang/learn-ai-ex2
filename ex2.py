# Ex2: Write a NumPy program to test whether each element of a 1-D array is also present in a second array
# Input Array1: [ 0 10 20 40 60]
#       Array2: [10, 30, 40]

import numpy as np

array1 = np.array([0, 10, 20, 40, 60])
print("Array1: ", array1)
array2 = [10, 30, 40]
print("Array2: ", array2)
print("Compare each element of array1 and array2")
print(np.in1d(array1, array2))
