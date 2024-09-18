def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print(f"My fruit is {kwargs['fruit']}")
    if 'food' in kwargs:
        print(f"My food is {kwargs['food']}")
myfunc(fruit='mango',food='burger',veggies='potato')