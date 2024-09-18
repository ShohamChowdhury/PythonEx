#numpy array can't store a inhomogeneous element
import numpy as np
arr1 = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9,10,11,12]])
def element(array, rowIndex, colIndex):
    if rowIndex-1 >= len(array) and colIndex-1 >= len(array[rowIndex-1]):
        print("Incorrect Index")
    else:
        print(arr1[rowIndex-1][colIndex-1])
element(arr1,3,4)      

        

