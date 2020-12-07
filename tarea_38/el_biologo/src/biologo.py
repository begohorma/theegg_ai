from aux_functions import get_correct_dna_sequence


def find_common_sequence(seq1, seq2):
    # candidato a ser la secuencia común más larga
    candidate = ""

    # por cada caracter de la secuencia 1
    for i in range(0, len(seq1)):
        # obtener el índice de todas las ocurrencias del caracter de la
        # secuenia 1 en la secuencia 2
        occurrences = find_occurrences(seq1[i], seq2)
        # para cada posible substring de la secuencia 2 que cominence con
        # el caracter que se está analizando de la secuencia 1
        #
        for index_s2 in occurrences:
            # asignar al nuevo candidato el caracter común en ambas secuencias
            new_candidate = seq1[i]
            # comprobar si hay un mejor candidato por si sólo coincide una letra
            candidate = check_new_candidate(candidate, new_candidate)
            # avanzar el indice de la secuencia1 para comparar el siguiente caracter
            index_s1 = i + 1
            # se va avanzando el indice de ambas secuencias mientras los cacteres
            # coincidan en ambas cadenas
            for j in range(index_s2 + 1, len(seq2)):
                # el indice de la secuencia 2 va desde la siguiente posición a la ocurrencia
                # hasta el final de la secuencia 2

                # hay que comprobar que no se excede la longitud de la secuencia 1
                if index_s1 == len(seq1) or j > len(seq2):
                    # si la nueva secuencia común es mas larga que la última
                    # encontrada pasa a ser la candidata
                    candidate = check_new_candidate(candidate, new_candidate)
                    break
                if seq1[index_s1] == seq2[j]:
                    # si los caracteres coinciden se añaden al nuevo candidato.
                    new_candidate += seq2[j]
                    index_s1 += 1
                    candidate = check_new_candidate(candidate, new_candidate)

                else:
                    # reiniciar el indice para la primera secuencia
                    index_s1 = i
                    candidate = check_new_candidate(candidate, new_candidate)
                    break

    return candidate


def check_new_candidate(candidate, new_candidate):
    if len(new_candidate) > len(candidate):
        candidate = new_candidate
    return candidate


def find_occurrences(character, string):
    """
        obtener los índices de todas las ocurrencias de un caracter en una cadena
        y devolver una lista con los índices.
    """
    indices = []
    for i in range(len(string)):
        if string[i] == character:
            indices.append(i)
    return indices


def main():
    # obtener las secuencias a comparar
    seq1 = get_correct_dna_sequence("Indica la primera secuencia de adn: ")
    seq2 = get_correct_dna_sequence("Indica la segunda secuencia de adn: ")

    common_seq = find_common_sequence(seq1, seq2).lower()
    print(" La mayor secuencia común de bases es: " + common_seq)


if __name__ == '__main__':
    main()
