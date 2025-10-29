try:
    n1 = int(input("introduce n1: "))
    n2 = int(input("introduce n2: "))
except ValueError as e:
    print("Error introduce un numero" , e)

if n1 < n2 :
    print(n1 , " es menor que " , n2)
elif n1 > n2:
    print(n1, " es mayor que ", n2)
else:
    print("son iguales")           