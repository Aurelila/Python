''' Author: Nancy McCoy
    Description: Practicing NumPy with arrays.
'''

# Import numpy
import numpy as np

# Make an array
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

print(arr)

# Turn odd numbers in the array with -1
arr[arr % 2 == 1] = -1

print(arr)

# Sort the array from lowest to highest number
arr.sort(axis=0)

print(arr)

# Put array in columns
arr = np.arange(9).reshape(3,3)

print(arr)

# Add the sums of the rows
arr = arr.sum(axis=1)

print(arr)

# Add all numbers together
arr = arr.sum(axis=0)

print(arr)


