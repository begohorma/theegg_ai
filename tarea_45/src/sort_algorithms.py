# Se realiza una implementación simple del algoritmo de búaqueda quicksort
# utilizando listas auxiliares para  el particionado

def partition(vector):
    # selecionar como pivote el primer elemento de la lista
    pivot = vector[0]
    lower_values = []
    higher_values = []

    for i in range(1, len(vector)):
        if vector[i] < pivot:
            lower_values.append(vector[i])
        else:
            higher_values.append(vector[i])
    return lower_values, pivot, higher_values


def quick_sort_simple_version(vector):
    if len(vector) < 2:
        return vector

    lower_values, pivot, higher_values = partition(vector)

    return quick_sort_simple_version(lower_values) + [pivot] + quick_sort_simple_version(higher_values)
