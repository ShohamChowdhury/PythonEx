def triangle(n):
    k=n
    for i in range(n,0,-1):
        j=1
        while(j<=i):
            print(j,end=" ")
            j+=1
        print()   
num = int(input())
triangle(num)