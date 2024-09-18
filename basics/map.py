fn = lambda x : x*4
list1 = [x for x in range(10)]
new_nums = list(map(fn,list1))
print(new_nums)