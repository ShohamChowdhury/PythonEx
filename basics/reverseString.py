def reversed_string(string):
    reverse = ""
    for i in string:
        reverse = i + reverse
    return reverse

string = input("Give me a string :\n")
print(reversed_string(string))
    