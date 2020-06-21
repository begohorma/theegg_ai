# obtener el número introducido
# según enunciado no se muestra mensaje de solicitud al usurio
# en una versión más elaborada se debería comprobar que el valor es un número que pertenece al rango permitido

num = float(input())  # convertir a float para poder operar cómo número

# transformar número en fracción con numerador y denominador
numerador = num * 10000
denominador = 10000  # porque el número de entrada debería tener como máximo 4 decimales

# los factores de 10000 son 2 y 5 por lo que se divide numerador y denominador entre 2 y 5
# todas las veces que sea posible mientras el resultado sea un entero

while numerador % 2 == 0:
    numerador = numerador / 2
    denominador = denominador / 2

while numerador % 5 == 0:
    numerador = numerador / 5
    denominador = denominador / 5

# mostrar la fracción como un string de números enteros
print(str(int(numerador)) + "/" + str(int(denominador)))
