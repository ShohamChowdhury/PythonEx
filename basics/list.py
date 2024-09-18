list = [1,2,3,4,5]
list2 = []
for i in range(len(list)):
    b = list.pop()
    list2.append(b)
    print(list2)