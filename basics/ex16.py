#Write a python function that takes a list and 
# returns the unique elements of that list

def unique(listt):
    return set(listt)

x = [10,1,1,1,1,2,2,2,2,3,3,3,3,3,5,8,5,5,5,5,8,'p','g']
print(unique(x))