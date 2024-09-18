def fact(n):
    if 0<=n<=1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))