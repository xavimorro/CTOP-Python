# Autor: Xavi Morro
# Fecha: 14/11/2025
# Descripción: Calcula la operacion elegida por el usuario de dos numeros
try:
    #variables con valor introducido por el usuario
    n1 = int(input('Introduce un numero: '))
    n2 = int(input('Introduce un numero: '))
    operacion = input('Introduce la operacion a realizar: ')
except ValueError as e:
    print('Error: ', e)

#posibles casos de la operacion    
if operacion == '+':
    print(n1+n2)
elif operacion == '-':
    print(n1-n2)
elif operacion == '*':
    print(n1*n2)
elif operacion == '/':
    print(n1/n2)
else:
    print('Introduce una operacion (+, -, *, /)')