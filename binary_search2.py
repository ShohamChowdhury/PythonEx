def binary_search(array,target):
    left , right = 0, len(array) - 1
    while left <= right:
        mid = (left + right)//2
        if array[mid] == target:
            print(target , "at" , mid + 1)
            break
        elif array[mid] < target:
            left  = mid + 1
        else:
            right = mid - 1
            
list = [16,27,29,30,35,49,52]

binary_search(list,30)
binary_search(list,49)