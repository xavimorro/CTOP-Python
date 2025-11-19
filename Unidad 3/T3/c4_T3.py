# Autor: Xavi Morro
# Fecha: 17/11/2025
# Descripción: Correccion del codigo para que calcule el area del rectangulo

def area_rectangulo(base, altura):
    area = base * altura
    return area

base = int(input('Introduce la base: '))
altura = int(input('Introduce la altura: '))
area = area_rectangulo(base, altura)

print('El area es: ', area)

#Error 1: Le falta una coma en el print.
#Error 2: Quitamos un * para que la operacion se pueda hacer ya que el debugger da error.
#Error 3: Añadimos int a los inputs porque sino el debugger nos dice que no se pueden multiplicar dos strings.