#6
#1 2 3 3 2 4
#answer = 2

list = []
index = []
for i in range(int(input())):
    num = int(input())
    if num in list:
        index.append(i)
        index.append(list.index(num))
        list.append(num)
    else:
        list.append(num)
print("the first repeating number : ",list[min(index)])
print(list)
print(index)