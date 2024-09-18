def perfectnum(n):
    sum = 0
    for i in range(1,n,+1):
        if(n%i==0):
            sum += i
    if(sum==n):
        return True
    else:
        return False
num=int(input("Enter The Lower Bound :\n"))      
num2=int(input("Enter The Upper Bound :\n"))
for i in range(num,num2+1,+1):
    if(perfectnum(i)):
        print(i,"is a Perfect Number\n")
    else:
        print(i,"is not a Perfect Number\n")