#Given a string, return a string where for every character 
#in the original there are three characters
def increaser(text):
    new_text=""
    for i in range(len(text)):
        new_text = new_text + text[i]*3
    print(new_text)
increaser("hello")       