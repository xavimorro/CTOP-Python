import sys

def sumar(a, b):
    return "La suma de " + str(a) + " más " + str(b) + " es = " + str(a + b)
def restar(a, b):
    return "La resta de " + str(a) + " menos " + str(b) + " es = " + str(a - b)

if __name__ == "__main__":
    print('No me ejecutes, solo soy un módulo.')
    print(__name__)
    sys.exit(1)
else:
    
    print(__name__)