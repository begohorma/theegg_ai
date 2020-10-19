# funciones validadoras
def get_correct_attack_value(prompt):
    value = -1
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("El valor debe ser un número entero.")
            continue

        if 0 <= value >= 100:
            print("El valor debe estar comprendido entre 1 y 100 ambos incluidos.")
            continue
        else:
            break
    return value
