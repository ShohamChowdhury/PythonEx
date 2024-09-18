def triangle(n):
    k = 1
    for i in range(0,n,+1):
        for j in range(0,i,+1):
            print(k,end=" ")
            k+=1
        print()
num = int(input())
print(triangle(num))