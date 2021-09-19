def get_a_set_of_names(names):
    while True:
        try:
            name = str(input("Introduce el nombre de pila del alumno.(x para finalizar). :"))
        except ValueError:
            print("El nombre debe ser un string.")
            continue

        if name == "x" or name=="X":
            break
        else:
            names.add(name)
            continue
    return names