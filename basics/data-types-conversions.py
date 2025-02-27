#!/usr/bin/env python3


# integer
print(type(1))

# float
print(type(1.5))

# string
print(type("Hello world"))


print("### Modern Annotation")

##       -- Anotacion moderna (typing) --       ##
lastName: str = "Velazques"
age: int = 25
price: float = 19.99

# Define a variable of type list
list_of_numbers: typing.List[int] = [1, 2, 3]

# Define a variable of type tuple
tuple_of_numbers: typing.Tuple[int, int, int] = (1, 2, 3)

# Define a variable of type dict
dictionary: typing.Dict[str, int] = {"key1": 1, "key2": 2}

# Define a variable of type set
set_of_numbers: typing.Set[int] = {1, 2, 3}


print(type(lastName))
print(type(age))
print(type(price))

##      -- Convertions --    ##
print("\nConvertions:")
print(1 + 1.5) # conversion implicita (implicit convertion), el interprete convierte automaticamente un data type en otro

print("This " + "is " + "cool")

""" Explicitit convertion """
base: int = 6
height: int = 3
area = ((base*height)/2)
print("El area del triangulo es: " + str(area)) # Conversion explicita (explicit convertion ), es cuando manualmente convertimos un data type a otro usando data type convertion function "str(), int(), float()..."
