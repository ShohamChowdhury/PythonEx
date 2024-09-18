#insertion
import numpy as np
arr = np.array([[1, 2, 3, 4] , 
                [5, 6, 7, 8] , 
                [9,10,11,12] ])
newarr = np.insert(arr,3,[13,14,15,16],axis=0)
print(newarr)