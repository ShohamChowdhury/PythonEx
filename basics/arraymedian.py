def arrayMedian(nums1: list[int], nums2: list[int]):
    num = nums1+nums2
    num.sort()
    k = len(num)
    if(k%2==1):
        return num[(k//2)]
    else:
        return (num[k//2-1]+num[(k//2)])/2
    
print(arrayMedian([1,2],[4,5]))