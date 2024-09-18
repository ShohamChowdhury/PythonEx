print(" Showing Armstrong number from 1 to 1001 ")
rem = []
for i in range(1,1001):
    num = i
    sum = 0
    while(num):
        digit = (num%10)**len(str(i))
        sum+=digit
        num=num//10
    if(i==sum):
        print(i," Yes")
    else:
        rem.append(i)
print("\nThese are not Armstrong number :\n",rem)