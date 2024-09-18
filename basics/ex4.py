#Write a function that capitalizes the first and fourth 
#letter of a word
def capital(a):
    new_a =''
    for i in range(len(a)):
        if i==0 or i==3:
            new_a+=a[i].upper()
        else:
            new_a+=a[i]
a='macdonald'
print(capital(a))