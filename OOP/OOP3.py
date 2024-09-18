import datetime

class Person:
    def __init__(self, name, country, DOB):
        self.name = name
        self.country = country
        self.DOB = DOB

    def age(self):
        birth_date = datetime.datetime.strptime(self.DOB, "%d/%m/%Y").date()
        today = datetime.date.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age

P1 = Person("Shoham", "India", "18/12/2002")
print(P1.age())
