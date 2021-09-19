

def get_a_list_of_numbers():
    numbers = []
    while True:
        try:
            num = int(input("Introduce un número entero.(0 para finalizar la lista). :"))
        except ValueError:
            print("El valor debe ser un número entero")
            continue

        if num == 0:
            break
        else:
            numbers.append(num)
            continue
    return numbers


def delete_a_list_element(numbers):
    while True:
        try:
            num = int(input("Introduce un número a eliminar:"))
        except ValueError:
            print("El valor a eliminar debe ser un número entero")
            continue
        if num in numbers:
            numbers.remove(num)
            return numbers
        else:
            print("El número {0} no está en la lista".format(num))
            return numbers


def get_list_elements_sum(numbers):
    addition = 0
    for element in numbers:
        addition += element
    return addition


def get_elements_less_than_number(numbers):
    new_list = []
    while True:
        try:
            num = int(input("Introduce un número de referencia:"))
        except ValueError:
            print("El valor a eliminar debe ser un número entero")
            continue
        for element in numbers:
            if element < num:
                new_list.append(element)
        return num, new_list


def get_elements_frequency(numbers):
    new_list = []

    for element in numbers:
        t = (element, numbers.count(element))
        if t not in new_list:
            new_list.append(t)

    return new_list
