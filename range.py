#    Ejemplo 1: Generar una secuencia de números del 0 al 4 (exclusivo)

for num in range(5):
    print(num)



#  Ejemplo 2: Generador
#  Este código utiliza .range (2,
#  el primer número en el
#  Fin del rango (stop): 9 Es 2 hasta 8, pero no incluirá el 9.
#  Tamaño del paso (step):  2 es el tamaño del paso. 
# Esto significa que la secuencia se incrementará en pasos de8.

for num in range(2, 9, 2):
    print(num)


#  Ejemplo 3: Crear una lista de números del 1 al 10


lista_numeros = list(range(1, 11))
print(lista_numeros)