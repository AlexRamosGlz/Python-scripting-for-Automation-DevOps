

# String simple
name: str = "Tere"
print(type(name))

# string multilinea (multiline string)
multiline_string: str = """Esto es un string
multilinea"""
print(multiline_string)

# indecsacion de strings (string indexing)
print("First character: " + name[0]) # -> 'T'
print("Last character: " + name[-1]) # -> 'e'

# Concatenacion de strings (string concatenation)
fullname: str = name + " Velasquez Gomez"
print(fullname) # -> 'Teresa Velasquez Gomez'

# Replicacion (Replication)
print(name * 5) # -> 'Tere Tere Tere Tere Tere'

# longitud de string (len)
print(len(name)) # -> 4

# A minuscula (.lower()) 
print(name.lower())

# A mayuscula (.upper())
print(name.upper())

# strip() similar a trim() de JavaScript
print(fullname.strip())

# Formatear texto con replacement fields '{}'
print("Tere tiene {0} letras en su nombre".format(len(name)))

# Parametro sep
print("Hola", "mundo", "!", sep="@") 

    # Te permite especificar el caracter separador
    #
    #  -> Hola@mundo@!
 
    
# Formato con f-strings
print(f"{name} tiene {len(name)} letras en su nombre")

    # f-string permite usar variables dentro de los strings
    
    
# Controlar el formato de numeros
print("Valor: {:.2f}".format(1.2323423))

    # :.2f indica el numero de decimales a mostrar, en este caso 2
    
