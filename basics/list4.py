mystring1  = 'Shoham'
#string to list(traditional)
mylist1 = []
for letter in mystring1:
    mylist1.append(letter)
#string to list(short but not readable)
mystring2 = "Pooja"
mylist2 = [letter for letter in mystring2]
print(mylist2)

print([x if x % 2 == 0 else 'odd' for x in range(20)])