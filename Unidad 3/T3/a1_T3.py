# Autor: Xavi Morro
# Fecha: 14/11/2025
# Descripción: Calcula cual de los tres enteros introducidos por el usuario es mayor.

try:
    #variables con valor introducido por el usuario
    n1 = int(input('Introduce el primer numero: '))
    n2 = int(input('Introduce el segundo numero: '))
    n3 = int(input('Introduce el tercero numero: '))
    
except ValueError as e:
    print('Error: ', e)
    
#codiciones para determinar cual de los tres es el numero mayor
if n1 > n2 and n1 > n3:
    print('El numero mayor es: ', n1)
elif n2 > n1 and n2 > n3:
    print('El numero mayor es: ', n2)
elif n3 > n1 and n3 > n2:
    print('El numero mayor es: ', n3)
else:
    print('Dos o mas numeros son iguales')