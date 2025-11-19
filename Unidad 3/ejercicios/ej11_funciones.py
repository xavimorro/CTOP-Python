# Definir funcion presentar(nombre, edad=18) que muestre un mensaje con ambos datos. Llama la funcion con y sin el argumento edad.

def presentar (nombre, edad = 18):
    print(f'Tu nombre es: {nombre}, y tu edad: {edad}')
    
presentar('Xavi', 28)
presentar ('Xavi')
