def sum(n):
    assert n>=0 and int(n)==n,"Wrong Input"
    if n in [0,1]:
        return n
    else:
        return n+sum(n-1)
print(sum(6))
        