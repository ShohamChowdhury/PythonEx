num = input("Enter number : ")
num=int(num)
num1 = 0
num2 = 1
start = 0
print('0\n'+'1')
while start < num - 2 :
    add = num1 + num2
    print(add)
    num1 = num2
    num2 = add
    start+=1 