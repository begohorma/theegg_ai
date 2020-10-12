from aux_functions import get_non_negative_int


def decimal_to_binary(n_dec):
    remainders = []
    if n_dec == 0:
        remainders.append(n_dec)
    else:
        while n_dec > 0:
            remainders.append(int(n_dec % 2))
            # división entera
            n_dec = n_dec // 2
    remainders.reverse()
    n_bi = "".join(str(num) for num in remainders)

    return n_bi


if __name__ == '__main__':
    num_decimal = get_non_negative_int("Introducir número decimal entero positivo: ")
    num_binario = decimal_to_binary(num_decimal)
    print("número binario: " + num_binario)
