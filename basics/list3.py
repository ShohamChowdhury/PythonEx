list69 = []
dictionary = {'a':1,'b':2,'c':3}
for x,y in dictionary.items():
    for _ in range(y):
        list69.append(x)
        
print(list69)