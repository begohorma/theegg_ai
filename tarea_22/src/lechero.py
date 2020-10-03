from auxFuntions import get_non_negative_int, get_valid_list_of_ints
from maximizer import Maximizer
if __name__ == '__main__':
    # obtener datos de entrada
    cows_total_num = get_non_negative_int("Indique el número total de vacas a la venta: ")
    lorry_total_weight = get_non_negative_int("Indique el peso máximo que puede llevar el camión: ")
    cows_weights = get_valid_list_of_ints(
        "Indique el peso en kg de las vacas separado por comas. Deben ser números enteros.: ", cows_total_num)
    cows_production_day = get_valid_list_of_ints(
        "Indique los litros de producción diaria de las vacas separado por comas. Deben ser números enteros.: ",
        cows_total_num)

    # obtener y mostrar la producción máxima
    m = Maximizer(cows_total_num, lorry_total_weight, cows_weights, cows_production_day)
    print(" La cantidad máxima de producción de leche que se puede obtener es : ", m.get_maximun_production())
