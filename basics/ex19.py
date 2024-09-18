# Check if a word is pangram or not
import string

def isPangram(text,alphabet=string.ascii_lowercase):
    alphabet_set = set(alphabet)
    text = text.replace(" ","")
    text = text.lower()
    text = set(text)
    return text == alphabet_set

line = "The quick brown fox jumps over the lazy dog"
print(isPangram(line))
