# serach algorithms that return the number of iterations performed to find a
# given element
# algortimos de búsqueda que devuelven el número de itraciones realizadas para
# encontrar  un elemento dado.

def linear_search(vector, to_find):
    """
      Devuelve el número de iteraciones para encontrar el valor to_find en la lista.
      Se realiza una búsqueda lineal recorriendo todos los elementos de la lista
      comprobando  si cada elemento es el buscado
    """

    iterations = 0

    for elem in vector:
        iterations += 1
        if elem == to_find:
            break
    return iterations


def binary_search(ordered_vector, to_find):
    """
    Devuelve el número de iteraciones para encontrar el valor to_find en la lista ordenada.
    Se realiza una búsqueda binaria en la lista ordenada.
    Se comprueba si el elemento está en la posición media de lista. Si no lo es se comprueba se ese elemento es mayor
    o menor al buscado y se continua buscando sólo en la parte de la lista correspondiente.
    """

    iterations = 0
    first = 0
    last = len(ordered_vector) - 1

    while first <= last:
        mid = (first + last) // 2
        iterations += 1
        if ordered_vector[mid] == to_find:
            return iterations
        elif ordered_vector[mid] < to_find:
            first = mid + 1
        elif ordered_vector[mid] > to_find:
            last = mid - 1

    return iterations
