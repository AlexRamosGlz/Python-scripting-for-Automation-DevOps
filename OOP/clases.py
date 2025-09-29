import dataclasses

class Person:
    
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        
    def greet(self):
        print(f"Hola me llamo {self.name} y tengo {self.age} años")
        

tere = Person("Tere", 25)
tere.greet()

