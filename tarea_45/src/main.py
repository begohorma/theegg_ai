from search_algorithms import *
from sort_algorithms import *


def main():
    original_list = [3, 56, 33, 874, 123, 66, 1000, 23, 45, 65, 56]
    #obtener una lista ordenada  para poder utilizar la búsqueda binaria
    ordered_list = quick_sort_simple_version(original_list)

    to_find = 875

    print("Búsqueda del elemento : {0} en la lista: {1} ".format(to_find, ordered_list))
    print("----")
    it_l = linear_search(ordered_list, to_find)
    print("iteraciones del algoritmo de búsqueda lineal: {0}".format(it_l))
    it_b = binary_search(ordered_list, to_find)
    print("iteraciones del algoritmo de búsqueda binaria: {0}".format(it_b))



if __name__ == '__main__':
    main()
