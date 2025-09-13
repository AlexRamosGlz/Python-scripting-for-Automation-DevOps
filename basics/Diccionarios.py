
# Los diccionarios es una estructura de datos basado en key + value pair (muy parecido aun objeto en JavaScript)
number = {1: 'uno', 2: 'dos', 3: 'tres'}
information = {"name": "Teresa",
               "Apellido": "Velazques",
               "ALtura": 1.70,
               "Edad": 25}

    # Al igual que en las listas tambien podemos acceder a los valores del dictionary 
    # por sus keys...
    #
    #   number[1] -> "uno"
    #
    #
    # Tambien para eliminar una llave y su valor, se usa del..
    #
    #   del numbers[1]
    #

number_keys = number.keys()
number_values = number.values()

print(f"llaves del dicitonario: {number_keys}\nValores del diccionario: {number_values}")

pairs = information.items()

print(f"EL diccionario completo de information es: {pairs}")

for pair in pairs:
    print(pair)
    
    # Para poder iterar entre los pares de key + value la funcion items()
    # es muy util
    #
