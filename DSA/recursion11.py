def dec_bin(n):
    assert n>=0 and int(n)==n,"Wrong Input"
    if n==0:
        return 0
    else:
        return (n%2)+dec_bin(n//2)*10
print(dec_bin(16))