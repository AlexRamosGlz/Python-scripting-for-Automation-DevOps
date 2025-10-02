



# Leer un archivo linea por linea

# with open("cuento.txt", "r") as file:
    
#     # El "with" statement nos ayuda con el manejo de recursos, se encarga
#     # de que no dejemos recursos abiertos, como archivos o conexiones
#     # a bases de datos
#     #
#     # Este statement es un remplazo para el try...finally. A continuacion su
#     # equivalente sin usar "with":
#     #
#     # f = open("cuento.txt", "r")
#     #
#     #  try:
#     #      contenido = f.read()
#     #  finally:
#     #   f.close()
    
#     for line in file:
#         print(line.strip)
        

# Leer todas las lineas en una lista

with open("cuento.txt", "r") as file:
    lines: list = file.readlines()
    print(lines)
    