decimal = float("Introduce un numero decimal: ")
entero = int(input("Introduce un numero entero: "))

try:
    cadena_num = int(num)
    resultado = cadena_num + 10
    print("El numero convertido de cadena a entero es: " + resultado)
Except ValueError as e
print('Error: ' , e)    

