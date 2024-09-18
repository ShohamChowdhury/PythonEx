#Write a function that counts the number of times a given 
# pattern appears in a string, including overlap

#if you use count function eg.
#text = "hahahah" - > "hah" appears 3 times (including overlap)
#text.count("hah") will only count 2 times as hah-a-hah 
# (dissing the overlap)

def checker(pattern,text):
    count = 0
    for i in range(len(text)):
        if pattern == text[:len(pattern)]:
            count+=1
            text = text[1:]
        else:
            text = text[1:]
    return count
print(checker('hah','hahahah'))
    