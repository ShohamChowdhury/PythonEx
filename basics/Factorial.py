def fact(n):
    sum = 1
    for i in range(n,0,-1):
        sum*= i   
    return sum

num = int(input("Give me a number :\n"))
print("The Factorial of",num,"is :",fact(num))

"""
import math
num = int(input("\n"))
result = math.factorial(num)
print(result)
"""