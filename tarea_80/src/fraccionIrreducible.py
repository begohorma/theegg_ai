def get_valid_input_float(prompt):
    value = 0.0000

    while True:
        try:
            value = float(input(prompt))
            lon = len(str(value))
        except ValueError:
            print("El valor debe ser un número decimal.")
            continue

        if 0.0001 <= value <= 0.9999 and lon <= 6:
            break
        else:
            print("El texto de entrada debe ser un número entre 0.0001 y 0.9999 con 4 dígitos decimales como máximo.")
            continue

    return value


def main():
    # obtener datos entrada. Número decimal entre 0,0001 y 0,9999
    num = get_valid_input_float("Introduce un número entre 0.0001 y 0.9999 :")

    # transformar el número en una fracción con numerador y denominador
    numerator = num * 10000
    denominator = 10000  # porque el número de entrada debería tener como máximo 4 decimales

    # los factores de 10000 son 2 y 5 por lo que se divide numerator y denominador entre 2 y 5
    # todas las veces que sea posible mientras el resultado sea un entero

    while numerator % 2 == 0:
        numerator = numerator / 2
        denominator = denominator / 2

    while numerator % 5 == 0:
        numerator = numerator / 5
        denominator = denominator / 5

    # mostrar la fracción como un string de números enteros
    print("La fracción irreducible de {0} es: {1}/{2}".format(num, int(numerator), int(denominator)))


if __name__ == '__main__':
    main()
