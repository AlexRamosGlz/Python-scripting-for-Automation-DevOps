#!/bin/python3

numbers: list[int]= [1,2,3,4,5,6]

# Iteracion tradicional en python
for number in numbers:
    print(number)
    
    
# La funcion range nos regresa una secuencia de numeros
for number in range(20, 30):
    print(number)

    # tambien se le puede indicar el numero en el cual queremos que empiece
    # la secuencia (1er parametro)
    #
    # ...range(5, 10)
    #

x = 0

# El bucle while
while x <= 5:
    print(f"Vuelta numero {x}")

    if(x == 3):
        print(f"Omitiendo vuelta 3")
        break
    
    x += 1
    
