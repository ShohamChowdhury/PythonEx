#declaration
my_dict = {}
val = False
while not val:
    key = input("Please insert a key : ")
    value = input("Please enter a value : ")
    if key =="":
        val = True
    else :
        my_dict.update({key:value})
#dictionary made
print(my_dict)

# copy() method
dict2 = my_dict.copy()
print(dict2)

# clear() method
my_dict.clear()
print(my_dict)

# get() method
print(dict2.get(1))

# items() method
print(dict2.items())

# keys() method
print(dict2.keys())

# pop() method
#dict2.pop()
print(dict2)

# popitem() method
dict2.popitem()
print(dict2)

# update() method
dict2.update({3: "Scala"})
print(dict2)

# values() method
print(dict2.values())

list69 = []
dictionary = {'a':1,'b':2,'c':3}
for x,y in dictionary.items:
    for _ in range(y):
        list69.append(x)
        
print(list69)