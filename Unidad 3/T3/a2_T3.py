# Autor: Xavi Morro
# Fecha: 14/11/2025
# Descripción: Imprimprime los numeros enteros desde 1 hasta el numero elegido por el usuario.
try:
    #se pide el valor de la variable al usuario
    n1 = int(input('Introduce un numero entero positivo: '))
    
except ValueError as e:
    print('Error: ', e);
    
#imprime todos los numeros desde 1 hasta el introducido
if n1 > 0:
    for i in range(1, n1 +1):
        print(i)    