#Given a sentence, return a sentence with 
# the words reversed
def reverse(x):
    word_list = x.split()
    sentence = ' '.join(reversed(word_list))
    print(sentence)
reverse("hello from the other side")
