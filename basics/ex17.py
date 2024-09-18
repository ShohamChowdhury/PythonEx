# Write a Python function to multiply 
# all the numbers in a list

def multi(listt):
    multi = 1
    for i in listt:
        multi = multi*listt[i]
    return multi
x = [1,2,3,-4]
print(multi(x))
        
    
