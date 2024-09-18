def digits(n):
    assert n>=0 and int(n) == n, "Wrong Input"
    if n==0:
        return 0
    else:
        return n%10 + digits(n//10)
print(digits(1445867))