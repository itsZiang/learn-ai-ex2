# Ex3: Write a NumPy program to find the indices of the maximum and minimum values along the given axis of an array
# Input Array [1,6,4,8,9,-4,-2,11]

import numpy as np

x = np.array([1, 6, 4, 8, 9, -4, -2, 11])
print("Original array: ", x)
print("Maximum Values: ", np.argmax(x))
print("Minimum Values: ", np.argmin(x))
