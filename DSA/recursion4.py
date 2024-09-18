def fib(n):
    assert n>=0 and int(n)==n , "Wrong Input"
    if n in [0,1] :
        return n
    else:
        fibnum = fib(n-1)+fib(n-2)
        return fibnum
print(fib(2.5))