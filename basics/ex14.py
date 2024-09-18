# Write a function that checks whether 
# a number is in a given range 
# (inclusive of high and low)

def finder(num,low,high):
    return (num in range(low,high+1))
print(finder(9,2,7))