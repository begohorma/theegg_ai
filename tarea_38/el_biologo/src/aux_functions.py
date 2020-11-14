# funciones validadoras
import re


def get_correct_dna_sequence(prompt):
    while True:
        value = str(input(prompt)).upper()

        if chek_dna_sequence(value):
            break
        else:
            print("La secuencia sólo puede contener los caracteres de las bases A, C, G y T ")

    return value


def chek_dna_sequence(sequence):
    # la cadena tiene que estar formada sólo por caracteres de las bases A,C,G y T
    # desde el inicio  al final $  de la cadena
    # los caracteres deben coincidir con alguno de los especificados en el conjunto []

    if re.match('^[ACGT]+$', sequence):
        return True
    else:
        return False
