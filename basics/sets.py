lis = [10,2,3,5,4,6,8,4,9,2,1,3,2,3]
l = len(lis)
s = set()
for _ in range(l):
    s.add(lis[_])
print(s)
s.remove(10)
print("after removing 10 :\n",s)
s.update(lis)
print(s)