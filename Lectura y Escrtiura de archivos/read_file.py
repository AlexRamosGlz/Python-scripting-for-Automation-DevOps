



# Leer un archivo linea por linea

with open("cuento.txt", "r") as file:
    
    # El "with" statement nos ayuda con el manejo de recursos, se encarga
    # de que no dejemos recursos abiertos, como archivos o conexiones
    # a bases de datos
    #
    # Este statement es un remplazo para el try...finally. A continuacion su
    # equivalente sin usar "with":
    #
    # f = open("cuento.txt", "r")
    #
    #  try:
    #      contenido = f.read()
    #  finally:
    #   f.close()
    
    for line in file:
        print(line.strip)
        

# Leer todas las lineas en una lista

with open("./cuento.txt", "r") as file:
    lines: list = file.readlines()
    print(lines)


# Append texto a un archivo

with open("cuento.txt", 'a') as file:
    file.write("\n\nBy: ChatGPT")
    
    
# Sobreescribir un archivo

with open("cuento.txt", "w") as file:
    file.write("Nuevo Texto")
    
    
    # open(file, mode)...
    #
    # los modos mas utilizados son...
    #
    #   'r'   -> Read, abre un archivo en modo lectura (default)
    #   'a'   -> Append, abre un archivo para append, crea el archivo si no existe
    #   'w'   -> Write, abre el archivo para sobreescribir todo su contenido, crea el archivo si no existe
    #   'x'   -> Create, crea el archivo especificado, retorna un error si el arcivo existe

try:
    open("cuento.txt", 'x')
except FileExistsError as error:
    print("Ya existe ese archivo")