def poweroftwo(n):
    if n==0:
        return 1
    else:
        power = poweroftwo(n-1)
        return power*2
print(poweroftwo(6))