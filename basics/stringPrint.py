string = input("Enter the string :\n")
size = len(string)

for i in range(0,size+1,+1):
    for j in range(0,i,+1):
        print(string[j],end=" ")
    print()
    