# Autor: Xavi Morro
# Fecha: 14/11/2025
# Descripción: Calcular la eficiencia en tiempo de dos sumas usando bucle for y sum(range).
import time

#primera operacion: iniciamos variable y guardamos el tiempo de inicio
# cuando acaba el for guarda el tiempo de nuevo y restamos los dos.
suma = 0;
inicio = time.time()
for i in range(1, 1000001):
    suma += i
print(suma)
fin = time.time()
print('Primera op - Tiempo: ', fin - inicio, 'segundos')

#segunda operacion: hacemos lo mismo que en la primera pero con un sum(range()) asi comparamos cual es mas rapido.
inicio = time.time()
resul = sum(range(1, 1000001))
print(resul)
fin=time.time()
print('Segunda op - Tiempo: ', fin - inicio, 'segundos')