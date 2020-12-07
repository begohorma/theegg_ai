def get_non_negative_int_in_range(prompt):
    value = 0
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("El valor debe ser un número entero.")
            continue

        if value < 1 or value > 1000000:
            print("El valor debe estar comprendido entre 1 y 1.000.000.")
            continue
        else:
            break
    return value
