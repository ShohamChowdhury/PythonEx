#Write a function that returns the number of 
# prime numbers that exist up to and including a given number

def isPrime(x):
    count = 0
    if x<=1:
        return False
    for i in range(2,x):
        if x%i==0:
            count += 1
    if count>0:
        return False
    else:
        return True
def count_Prime(x):
    count = 0
    for i in range(x+1):
        if isPrime(i)==True:
            count+=1
    return count
print(count_Prime(100))
                
        