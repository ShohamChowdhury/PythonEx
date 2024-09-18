# Write a python function that checks if the word is palindrome

def isPalindrome(x):
    x = x.replace(" ","")
    x = x.lower()
    return x == x[::-1]

word = "Race car"
print(isPalindrome(word))