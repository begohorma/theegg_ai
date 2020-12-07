import re


def get_non_negative_int(prompt):
    value = 0
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("El valor debe ser un número entero.")
            continue

        if value < 0:
            print("El valor no puede ser negativo.")
            continue
        else:
            break
    return value


def get_correct_sentence(prompt):
    """ cadenas compuestas por caracteres separadas por un único espacio blanco """
    value = ""
    while True:
        try:
            value = str(input(prompt))
        except ValueError:
            print("El valor debe ser una cadena  de texto.")
            continue
        # para que python3 interprete toda la expresión como un string que puede tener carácteres de escape
        # hay que preceder la expresion de una r
        if re.match(r'^([a-zA-Z]+[\s]??)+$', value):
            break
        else:
            print("El texto de entrada debe estar compuesto sólo por caracteres de texto separados por un único "
                  "espacio en blanco")
            continue
    return value
