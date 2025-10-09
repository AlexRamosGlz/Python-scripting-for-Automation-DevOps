def outer_function():
    
    x = "enclosing"
    print(f"x antes de inner_function(): {x}")
    
    def inner_function():
        nonlocal x
            
            # nonlocal hace una funcion similar a global, solo que es usado
            # para modificar variable declarados en un (non-global) scope desde
            # una funcion anidada
            
        x = 'modified'
        
    inner_function()
    print(f"x despues de inner_function(): {x}")
    
outer_function()