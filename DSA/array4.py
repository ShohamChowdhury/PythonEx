import numpy as np
arr1 = np.array([[1,5,9,7],[6,3,2,4],[10,41,52,98]])
def search_element(array,req_num):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == req_num:
                return(f"Element Found in Row = "+str(i+1),
                       'Column = '+str(j+1))
    return("Element not found")
print(search_element(arr1,5))
            