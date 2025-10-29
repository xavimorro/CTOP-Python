vocales= "aeiouAEIOU";
contador=0
frase="Hola, aqui programando en Python";

for char in frase:
    if char in vocales:
        contador+=1

        print("Nº de vocales: ", contador);