from aux_functions import *


def main():
    print("\nCrear una lista de números enteros.")
    print("-----------------------------------\n")
    list_of_numbers = get_a_list_of_numbers()
    print("La lista creada es: {0}".format(list_of_numbers))

    print("\nEliminar un elemento de la lista.")
    print("-----------------------------------\n")
    list_of_numbers = delete_a_list_element(list_of_numbers)
    print("La lista resultante es: {0}".format(list_of_numbers))

    print("\nSuma de los elementos de la lista.")
    print("-----------------------------------\n")
    print("La suma de los elementos de la lista es: {0}".format(get_list_elements_sum(list_of_numbers)))

    print("\nLista con los elementos menores a un número.")
    print("----------------------------------------------\n")
    result = get_elements_less_than_number(list_of_numbers)
    print("Los números menores que {0} son: ".format(result[0]))
    for element in result[1]:
        print(element)

    print("\nFrecuencia de los elementos de la lista")
    print("---------------------------------------\n")
    f_result = get_elements_frequency(list_of_numbers)
    for element in f_result:
        if element[1] == 1:
            print("El elemento {0} aparece {1} vez".format(element[0], element[1]))
        else:
            print("El elemento {0} aparece {1} veces".format(element[0], element[1]))


if __name__ == '__main__':
    main()
