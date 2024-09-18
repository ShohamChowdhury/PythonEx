# Write a function that takes in a list of integers and 
# return True if it contains 007 in order  
# eg. [1,2,0,3,2,0,5,7] or [ 1,2,0,0,7,5,6] - both True

def spy_game(x):
    line = ""
    for i in range(len(x)):
        if x[i]==0 or x[i]==7:
            line = line + str(x[i])
        #print(line)
    if "007" in line:
        return True
    return False

print("First game : ",spy_game([1,1,3,0,1,7,2,3,0]))
print("Second game : ",spy_game([1,2,3,0,0,7,2,3,5]))
        
    