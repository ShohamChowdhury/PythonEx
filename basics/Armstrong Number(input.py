num = input("Give me a number\n")
size=len(str(num))
num=int(num)
finum = num
sum = 0
while(num):
    digit = pow(num%10,size)
    sum += digit
    num=num//10
if(sum==finum):
    print("Yes")
else:
    print("No")
    