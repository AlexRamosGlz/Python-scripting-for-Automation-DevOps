def pyramid(stores: int):
    
    '''
    Esta funcion imprime una piramide en la consola, esta empieza desde la punta 
    hasta la base y se le pueden cambiar el numero de pizos que tendra la piramide
    '''
    
    if stores < 3:
        return print("La piramide no puede tener menos de 3 pizos")
    
    number_of_spaces = stores - 1
    number_of_asterisco = 1

    for index in range(stores):
        print(' ' * (number_of_spaces), end='')
        print('*' * number_of_asterisco)
        
        number_of_asterisco += 2
        number_of_spaces -= 1
    
pyramid(10)