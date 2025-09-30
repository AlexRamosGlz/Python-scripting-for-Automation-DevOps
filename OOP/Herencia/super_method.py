
class Person:
    name: str
    age: int
    
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        
    def greet(self) -> None:
        print(f"Hola, soy una persona")
        
class Student(Person):
    student_id: int
    
    def __init__(self, name: str, age: int, student_id: int):
        super().__init__(name, age)
        
            # La funcion super nos permite llamar a un metodo o atribute de la super-clase desde la sub-clase
        
        self.student_id = student_id
        
    def greet(self):
        super().greet()
        print(f"Y me llamo {self.name}")
        
tere = Student("Tere", 20, 12345)

tere.greet()
        