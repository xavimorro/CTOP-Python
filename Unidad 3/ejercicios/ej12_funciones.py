# 1. Crea un a funcion que calcule la media aritmetica de dos input float. 
# 2. Ahora crea una version de la funcion pero que admita un numero variable de argumentos, que calcule la media de dos o mas valores.

def media (n1, n2):
        media = (n1 + n2) / 2
        return media

def media_dinamica (*numeros):
    media_dinamica = sum(numeros) / len(numeros)
    return media_dinamica

try:
    
    n1 = float(input('Introduce el primer numero: ' ))
    n2 = float(input('Introduce el segundo numero: ' ))
        
except ValueError as e:
    print('Error' , e)
        
print (f'La media de {n1} y {n2} es: ', media(n1, n2))
print(f'La media dinamica es: ', media_dinamica(5, 9, 6, 7))     