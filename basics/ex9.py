#Given three integers between 1-11, 
# if their sum is <=21, return their sum. 
# if their sum >21 and there's an 11, 
# reduce the total sum by 10. Finally, 
# if the sum(even after adjustment) >21, return "BUST"

def black_jack(x,y,z):
    sum = x+y+z
    if sum<=21:
        return sum
    else:
        if 11 in [x,y,z]:
            sum = sum - 10
            if sum > 21 :
                return "BUST"
            else:
                return sum
        else:
            return "BUST"

print(black_jack(9,9,11))
        