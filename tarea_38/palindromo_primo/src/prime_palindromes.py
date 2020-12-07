from aux_functions_pp import get_non_negative_int_in_range

def get_smallest_prime_palindrome(n):
    while not (is_palindrome(n) and is_prime(n)):
        n += 1
    return n


def is_prime(num):
    """
    Comprobar si un número es primo.
    Un número primo es un entero mayor que 1 que tiene únicamente dos divisores distintos: 1 y él mismo

    :param num: número dado para comprobar si es primo
    :return: True si el número primo, en caso contrario False
    """

    if num < 2:
        # si el número es menor que 2 no es primo
        return False
    else:
        for i in range(2, num):
            # desde  2 hasta el entero anterior al numéro a comprobar
            if num % i == 0:
                # si el resto da 0 es que es divisible por otro número, por lo que no es primo
                return False
        return True


def is_palindrome(num):
    """
    Comprobar si un número es Palíndromo.
    Un número es palíndromo si  se obtiene el mismo número al invertir el orden de sus cifras.

    :param num: número para comprobar si es palindromo
    :return:  True si el número es palíndromo, en caso contrario False
    """
    # convertir los números en cadenas para comprobar si son palindromas
    txt_num = str(num)
    revere_txt_num = ""
    # recorrer la cadena en orden inverso para obtener la cadena inversa
    for c in reversed(txt_num):
        revere_txt_num += c
    # sin ambas cadenas son iguales el número es palindromo
    return True if txt_num == revere_txt_num else False


def main():
    # obtener datos entrada
    num = get_non_negative_int_in_range("Indica un número entero entre 1 y 1.000.000: ")
    print("El menor entero palindromo primo mayor o igual que {0} es : {1} ".format(num, get_smallest_prime_palindrome(
        num)))


if __name__ == '__main__':
    main()
