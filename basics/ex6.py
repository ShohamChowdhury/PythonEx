#Given an integer n, return True if n is within
# 10 of either 100 or 200
def checker(x):
    if x>100:
        c = x%100
        if c<10:
            return True
        else:
            return False
    else:
        if x<10:
            return True
        else:
            return False
print(checker(55))
        