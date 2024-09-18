def GCD(a,b):
    if(a==0):
        return b
    else:
        return GCD(b%a,a)
num1 = int(input("Please enter first number :\n"))
num2 = int(input("Please enter second number :\n"))
print("GCD is",GCD(num1,num2))