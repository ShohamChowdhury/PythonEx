num1 = input("Provide first number\n")
num2 = input("Provide second number\n")
op = input("Give an operation(+,-,*,/,%)\n")
num1=int(num1)
num2=int(num2)
if   op == '+':
   print(num1+num2)
elif op =='-':
   print(num1-num2)
elif op == '*':
   print(num1*num2)
elif op == '/':
   print(num1/num2)
elif op == '%':
   print(num1%num2)
else :
    print("Not a valid Operator") 