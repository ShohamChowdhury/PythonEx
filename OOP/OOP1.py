class Pet:
    def __init__(self,name,age):
        self.name = name
        self.age = age
class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old. My color is {self.color}")
kitto = Cat("Kitty",10,"White")
kitto.show()
        
    