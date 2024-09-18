#Given a value, return a value that is twice
#as far away on the other side of 7
def returner(x):
    if x<7:
        return (7-x)*2+7
    else:
        return 7-(x-7)*2
print(returner(12))