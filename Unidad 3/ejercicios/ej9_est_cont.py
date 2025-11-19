# pedir un num verificar que sea del 1 al 10  y mostrar su tabla de multiplicar usando for

num = int(input("Escribe un num del 1 al 10: "))

if num >= 1 and num <= 10 :
    
    for i in range(1, 11):
        print(num, " multiplicado por", i, " = ", num * i)
else:
    print("escribe un num del 1 al 10")    
    

