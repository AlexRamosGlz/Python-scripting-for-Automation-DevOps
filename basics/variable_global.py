var_global = 1

    # En Python si simplemente quieres acceder a una variable global dentro
    # de un code block, basta con llamarla por su nombre, pero para poder modificar 
    # el valor de esta variable global es necesario la keyword "global"
    #
    #   global var_name
    #   var_name = "Nuevo Valor"

def unmodified_global_var() -> None:
    var_global = 3
    
    # Si no se usa el keyword "Global", solamente estaras declarando una nueva variable local
    # con el mismo nombre de la varia global, pero no se modificara
    
    print(f"El valor de var_global es {var_global}")
    
def modified_global_var() -> None:
    global var_global
    var_global = '8'
    
    print(f"El valor de var_global es {var_global}")

print(var_global)
unmodified_global_var()
print(var_global)
modified_global_var()
print(var_global)
