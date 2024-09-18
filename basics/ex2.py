#Write a function which takes a two word string and 
# returns True if both words begin with the same letter 
def checker(t):
    text = t.lower().split()
    return text[0][0]==text[1][0]
    #returning text's(tuple variable) element with the 
    # indexing showing elements of the string
text = input()
print(checker(text))