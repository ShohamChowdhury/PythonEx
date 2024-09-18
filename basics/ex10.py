#Return the sum of the numbers in the array, 
# except ignore sections of numbers starting with a 6 and 
# extending to the next 9. return 0 for no numbers.

def crusher(k):
    k.sort()
    for i in range(len(k)):
        if k[i] >= 6 and k[i]<=9:
            k[i]=0
    print(sum(k))
     
x = [2,1,6,9,11]
crusher(x)
            