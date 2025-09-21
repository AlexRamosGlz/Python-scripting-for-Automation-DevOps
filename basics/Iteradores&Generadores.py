#!/bin/python3


#####################################################
##                   Iteradores                    ##
#####################################################

number: list[int] = [1,2,3,4,5,6]

# los iteradores son otra forma de consumir collections
number_iterator = iter(number)

    # Estos son muy utiles cuando se quiere pausar y resumir un loop
    #
    
print(next(number_iterator))

    # la funcion next returna el siguiente objeto del iterator


text: str = "Hola Mundo"

text_iter = iter(text)

# En este ejemplo vemos que se puede loopear un objecto iter
# y su estado no esta ligado al bucle, entonces si este se interrumpe
# el loop, el siguiente estado del iter queda intacto
#
for char in text:
    print(next(text_iter))

    
    if(char == ' '):
        break
        
        # Si el siguiente objeto del text_ite es un espacio, el bucle se rempe
        #

print(next(text_iter))
    
    # Aunque el bucle se interrumpio el siguiente estado del iterador
    # es el correspondiente y no el primer objeto
    


#####################################################
##                  Generadores                    ##
#####################################################

# Los generadores son una forma simple, poderosa eficiente de memoria para crear iteradores
# en vez de retornar un solo valor y terminar, los generadores usan "yield" para retornar un valor y pausar su estado
# la proxima vez que se llame al generador, este reanuda su ejecucion justo despues del ultimo yield.
#
# los generadores son utiles para trabajar con secuencias grandes o infinitas.
def my_generator():
    for number in range(5):
        yield number
        # cada vez que se llama al generador, este retorna el siguiente valor y pausa su estado

for value in my_generator():
    print(value)
    # cada vez que se itera sobre el generador, este produce el siguiente valor en la secuencia