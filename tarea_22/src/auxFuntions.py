# funciones validadoras
def get_non_negative_int(prompt):
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


def get_valid_list_of_ints(prompt, length):
    while True:
        try:
            list_of_ints = list(int(num) for num in input(prompt).strip().split(sep=','))[:length]
        except ValueError:
            print("Los valores deben ser números enteros.")
            continue
        if len(list_of_ints) != length:
            print("El número de valores debe ser igual al número de vacas a la venta.")
            continue
        else:
            break
    return list_of_ints
