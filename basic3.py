# Función que acepta un número variable de argumentos posicionales y de palabra clave
numeros_pares = []
def funcion_variable_args(*args):
     global numeros_pares  # Indica que estamos utilizando la variable global numeros_pares
     for numero in args:
         if numero % 2 == 0:
              numeros_pares.append(numero)
   



# Llamar a la función con diferentes argumentos
funcion_variable_args(1,2,3,4,5,6,7,8,9,10)


print("Números pares:", numeros_pares)
