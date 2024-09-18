def sum_dig(n):
    assert n>=0 and int(n)==n,'Wrong Input'
    if n == 0:
        return 0
    else:
        return n%10+sum_dig(n//10)
print(sum_dig(356.8))