import re


# funciones validadoras
def get_correct_operation(prompt):
    while True:
        value = input(prompt).upper()
        if value == 'E' or value == 'D':
            break
        else:
            print("La acción a realizar deber indicarse con el caracter E para ENCRIPTAR y D para DESENCRIPTAR.")
            continue
    return value


def get_correct_input_text(prompt):
    # el texto de entrada sólo puede contener cararteres de texto del alfabeto inglés y espacios
    while True:
        value = input(prompt).upper()
        if re.match("[A-Z ]", value):
            break
        else:
            print("El texto de entrada debe estar compuesto sólo por caracteres de texto del alfabeto ingles")
            continue
    return value
