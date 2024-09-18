def power(x,n):
    assert n>=0 and int(n)==n, "Wrong Input"
    if n == 0:
        return 1
    else:
        return x*power(x,n-1)
print(power(2,5))