#traversing 2d array
import numpy as np
arr1 = np.array([[10,15,20,25],
                 [ 1, 3, 5, 7],
                 [20,19,18,17]])
for i in range(len(arr1)):
    for j in range(len(arr1[i])):
        print(arr1[i][j],end=' ')
    print('') 