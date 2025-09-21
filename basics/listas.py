
to_do: list[str] = ["Ir al hotel", 
                    "ir a almorzar",
                    "Visitar un museo",
                    "Volver al hotel"]


# list len
print(len(to_do))

# slicing
print(to_do[0:2])
print(to_do[2:])


# agregar un valor al final de la lista
to_do.append("Dormir")
print(to_do)

# Insertar un valor en el indice especificado
to_do.insert(0, "Viajar")
print(to_do)

# Obtener el index de la primera aparicion de un valor especifico
print(to_do.index("ir a almorzar"))

#Obtener el valor mayor y menor de una lista de ints o floats
number = [1,2,3,4,.67, 1.54]
print(f"El mayor valor es {max(number)} y el menor es {min(number)}")


# Eliminar un elemento de la lista por su index
del number[-1]

    # o la lista completa con...
    #
    #       del number
    #
    # NOTA: tambien se elimina de la memoria, ya no se puede referenciar
    #       en niguna otra parte del codigo

print(number)


# Copiar una lista
list_one = [1,2,3]
list_two = list_one

print(f"list_one: {list_one}, list_two: {list_two}")
list_two.append(4)
print(f"list_one: {list_one}, list_two: {list_two}")

    # Ambas listas apuntan al mismo espacio de memporia, por lo que al modificar una
    # se modifica la otra
    #
    # NOTA: para imprimir el id del espacio de memoria de la vairable, se usa la funcion id()
    #
    #       print(id(list_one)) -> 131517315323392
    
# Crear una copia independiente de una lista
list_three = list_one.copy()
list_three.append(5)
print(f"list_one: {list_one}, list_three: {list_three}")

    # Otro metodo seria usar slicing
    #
    #       list_three = list_one[:]
    #
    
    
# Matrices
matrix: list[list[int]] = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# Acceder a un valor anidado 
print(matrix[0][0]);

# Ejemplo de como iterar una matriz
for level in matrix:
    for value in level:
        print(f"Nivel: {matrix.index(level)} Valor: {value} ", end='')
    print()
    
matrix_2: list[list[list[int]]] = [
    [[1,2,3], [4,5,6]],
    [[7,8,9], [10, 11, 12]]
]

print(matrix_2[1][0][-1])

# Tuplas
number: tuple[int] = (1,2,3,4,5)

    # A diferencia de las listas o las matrices las tuplas son inmutables,
    # pero comparten la misma forma en que se pueden acceder a sus valores
    #

print(f"Primer valor de la tupla number es {number[0]}")

    # Tambien comparten los métodos index() y count(), y 
    # también soportan funciones y operaciones como len(), sorted()
    #
    # NOTA: tambien se pueden declara notas de la siguiente manera...
    #
    #               another_tuple: tuple[int] = 6,7,8,9,10
    

#####################################
##      comprehesions list         ##
#####################################

# Las comprehensions list son una forma concisa y eficiente de crear listas basadas en otros
# iterables existentes.
#
# Condensa la logica de un loop for y opcionalmente una condicion if en una sola linea
# de codigo.
#
farenheit = [(temp * 9/5) * 32 for temp in range(10, 50, 10)]

    # ['expression' for 'item' in 'iterable' if 'condition']

print(farenheit)

even_numbers = [num for num in range(20) if num%2 == 0]
print(even_numbers)