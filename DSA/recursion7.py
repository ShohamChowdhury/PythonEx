def GCD(a,b):
    assert int(a)==a and int(b)==b, "Wrong Input"
    if a<0:
        a = (-1)*a
    if b<0:
        b = (-1)*b
    if b == 0:
        return a
    else:
        return GCD(b,a%b)
print(GCD(15,35))
    