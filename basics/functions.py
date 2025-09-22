#!/usr/bin/env python3

def greeting(name: str, department: str) -> None:
    print("Welcome, " + name)
    print("You are part of " + department)

greeting("Tere", "Veterinaria")
greeting("Jorge", "DevOps")

greeting(department = "Ingeniero", name = "Fabio")

    # Normalmente las funciones esperan que los valores que les pases sean en el orden correcto
    # pero en python puedes hacerlo en el orden que quieras siempre y cuando se especifique a que
    # argumento corresponde el valor
    


########################################################
##                                                    ##
##              Funciones Lambda                      ##    
##                                                    ##
########################################################

multiply = lambda number_1, number_2: number_1 + number_2

    # Las funciones lambda son funciones anonimas que pueden tomar varios argumentos
    # pero solo puede tener una expresion 
    #
    #       lambda arguments: expression
    #

print(multiply(1, 2))


# Combinar funciones lambda con 'built-in functions'
square_numbers = list(map(lambda number: number**2, range(10)))

    # Es parecido a las arrow functions de javascript
    #
    # () => {..}

print(square_numbers)

even_square_numbers = list(filter(lambda number: number%2 == 0, square_numbers)) 
print(even_square_numbers)


########################################################
##                                                    ##
##              Recursividad                          ##    
##                                                    ##
########################################################


def non_recursive_factorial(n) -> int:
    total: int = 1
    
    for number in range(1, n):
        total *= number + 1
        
    return total

print(f"Non Recursive Factorial: {non_recursive_factorial(5)}") 


def recursive_factorial(n) -> int:
    
    # Caso base (base case)
    if n == 0:
        return 1
    
    # Caso Recursivo (Recursive Case)
    return n * recursive_factorial(n - 1)

    # Recursion es una tecnica en programacion donde una funcion se llama a si misma directa o
    # indirectamente para resolver un problema en pequeñas partes
    #
    #   base case: Es la condicion que prevee una recursion infinita 
    #
    #   recursive case: la parte de la funcion donde se llama asi misma pero con parametros modificados 
    
    """
        En Python, una función recursiva recuerda sus valores entre recursiones a través de la pila de llamadas (call stack). Cada vez que una función se llama a sí misma, se crea un nuevo contexto de ejecución con sus propios valores de parámetros y variables locales.

        Esto significa que:

         - Cada llamada recursiva tiene su propio espacio en memoria (frame) donde se guardan los valores de esa llamada específica.
         - Cuando una llamada recursiva finaliza (es decir, retorna un valor), ese valor se propaga hacia atrás en la pila hasta llegar a la llamada original.
         
         Si llamas a recursive_factorial(3), la ejecución se ve así:

                1 → recursive_factorial(3)

                2 → 3 * factorial(2)

                3 → 3 * (2 * recursive_factorial(1))

                4 → 3 * (2 * (1 * recursive_factorial(0)))

                5 → 3 * (2 * (1 * 1))

                6 → 3 * (2 * 1)

                7 → 3 * 2

                8 → 6

            Cada llamada a recursive_factorial(n) recuerda el valor de n en su propia ejecución, gracias a la pila de llamadas.
    """
    

print(f"Recursive Factorial: {recursive_factorial(10)}")


def fibonacci(n):

    if n == 0: 
        return 0
    
    if n == 1:
        return 1
    
    return fibonacci(n - 1) + fibonacci(n - 2)

for number in range(10):
    print(fibonacci(number), end=' ')
    

def summatory_natural_numbers(natural_number) -> int:
    if(natural_number == 0):
        return 0
    
    return natural_number + summatory_natural_numbers(natural_number - 1)

print()
print(summatory_natural_numbers(5))