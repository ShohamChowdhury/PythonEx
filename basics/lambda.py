#with def
def nxt (x):
    return x*4
num = [i for i in range(10)]  
new_nums = [nxt(num[k]) for k in num]
print(new_nums)

#with lambda
nxt2 = lambda x : x*5
new_nums2 = [nxt2(num[i])for i in num]
print(new_nums2)
    
