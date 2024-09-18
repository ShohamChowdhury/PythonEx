n = int(input())
elements = list(map(int,input().split()))
t = tuple(elements)
print(hash(t))