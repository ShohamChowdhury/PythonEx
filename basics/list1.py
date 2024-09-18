done = False
my_list = []

while not done:
    val = input("Enter a value: ")
    if val == "":
        done = True
    else:
        my_list.append(int(val))

print(f"Printing List: {my_list}")

key = int(input("Which element you want to count?\n"))
print(f"Count of {key} = {my_list.count(key)}")

my_list.sort()
print(f"Sorted list: {my_list}")

print(f"Max size element: {max(my_list)}")
print(f"Min size element: {min(my_list)}")
print(f"Sum of elements in list: {sum(my_list)}")

ind = int(input("Which element's first appearance you want?\n"))
print(f"Index is: {my_list.index(ind)}")

app = int(input("Any new element you want to add?\n"))
my_list.append(app)
print(f"New List: {my_list}")

inp = int(input("Give the desired location you want to input an element:\n"))
ele = int(input("Give the desired element:\n"))
my_list.insert(inp, ele)
print(f"New list: {my_list}")

pop = int(input("Provide the index of the element you want to remove:\n"))
my_list.pop(pop)
print(f"New list: {my_list}")

rem = int(input("Provide the element you want to remove:\n"))
my_list.remove(rem)
my_list.sort()
print(f"New list : {my_list}")
my_list.reverse()
print(f"New reversed sorted list :{my_list}")