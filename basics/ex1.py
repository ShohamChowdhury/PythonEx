#Write a function that returns the lesser of two given
#numbers if both numbers are even, but returns the greater
#if one or both numbers are odd
def lesser_one(x,y):
    if(x%2==0 and y%2==0):
        return min(x,y)
    else:
        return max(x,y)
print(lesser_one(2,5))
        