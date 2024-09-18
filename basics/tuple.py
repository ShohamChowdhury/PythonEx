#tuple may look same as a list
#but it is immutable, meaning you can't change it's value
#instead of [list] , (tuple)
#creating tuple :

values : tuple[int | str,...] = (1,2,4,"Shoham")
print(values)

#Here, in the above snippet we are considering a variable called 
#values which holds a tuple that consists of either int or str, 
#the ‘…’ means that the tuple will hold more than one int or str.

mytuple = ("Shoham",)
print(type(mytuple))

#NOT a tuple
mytuple = ("Chowdhury")
print(type(mytuple))

#In case your generating a tuple with a single element, 
# make sure to add a comma after the element.

tup1 = (1,2,3,4)
tup2 : tuple[int|str,...] = (5,6,7,"end") 
tup3 = tup1+tup2
print(tup3[::-1])
print(tup1*5)
#converting list and string to a Tuple
list = [0,1,2,3,4]
string = "Python"
t1 = tuple(list)
t2 = tuple(string)
print(t1,t2)

#tuple unpacking
tupl = [("Shoham",10),("Piyush",20),("Parag",30)]
for x,y in tupl:
    print(x,y)