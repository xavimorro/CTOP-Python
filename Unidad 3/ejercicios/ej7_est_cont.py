#escribe un programa que recorra una lista de 5 nombres e imprima solo los que tengan mas de 4 letras.

nombres = ["xavi", "juan", "manu", "alejandro", "erick"]

for nombre in nombres:
    if len(nombre) > 4:
        print(nombre)
    
