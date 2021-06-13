import config

def get_correct_input_string(prompt):
    value = ""
    max_length = config.input_text_max_length
    while True:
        try:
            value = str(input(prompt))
        except ValueError:
            print("La entrada debe ser una cadena de texto")
            continue

        if len(value) > max_length:
            print("Texto de entrada INCORRECTO. La longitud máxima de la cadena de entrada es {0} ".format(max_length))
            print("La longitud de la cadena de introducida es: {0}".format(len(value)))
            continue
        else:
            break
    return value


def get_input_text_max_length(prompt):
    try:
        config.input_text_max_length = int(input(prompt))
    except ValueError:
        print("El valor de la longitud máxima de la cadena de entrada debe ser un número entero.")


