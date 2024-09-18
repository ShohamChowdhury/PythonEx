stack = []
def push():
    print("Enter the Element :")
    stack.append(input())
    print(stack)
def pop_element():
    if not stack:
        print("The stack is empty !")
    else:
        el = stack.pop()
        print("Removed element : ",el)
        print(stack)
while True:
    print("Select the operation :\n"+"1.Push\n2.Pop\n3.Quit")
    choice = int(input())
    if choice==1:
        push()
    elif choice==2:
        pop_element()
    elif choice==3:
        break
    else:
        print("Select a correct option.")


    