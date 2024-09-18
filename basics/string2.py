name = input("What's your name ?\n")
score = float(input("What's your score?\n"))
#using f format method
print(f"Hey, How are you {name} ?")
print(f"You scored {score}")

#using old format method
age = int(input("What's your age ?\n"))
print("You are {} years old".format(age))
scor = 123.654987123
print(f"score is {scor : 1.3f}")
