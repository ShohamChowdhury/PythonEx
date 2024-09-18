def triangle(n):
    for i in range(0,n,+1):
        for j in range(0,n,+1):
            if(j>=i):
                print("*",end="")
            else:
                print(" ",end="")
        print()
num = int(input("Enter the number :\n"))
print(triangle(num))