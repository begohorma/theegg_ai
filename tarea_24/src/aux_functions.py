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
