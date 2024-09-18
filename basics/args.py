def myfunc(*args):
    return sum(args)*0.05

num = []
while True:
    inp = input()
    if inp=="":
        break
    num.append(int(inp))
res=myfunc(*num)
print(res)