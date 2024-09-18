fn = lambda x : not x%2
lis = [x for x in range(11)]
list1 = list(filter(fn,lis))
print(list1)

fn1 = lambda x: x + 'hi' if x == '' else 0
lis2 = ['', 'k', '', 'll']
list2 = list(filter(fn1, lis2))
print(list2)