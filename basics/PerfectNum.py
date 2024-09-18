def perfectnum(n):
    sum = 0
    for i in range(1,n,+1):
        if(n%i==0):
            sum += i
    if(sum==n):
        return True
    else:
        return False
num=int(input("Enter The Number :\n"))      
print(perfectnum(num))