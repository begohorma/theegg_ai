from aux_functions_rw import get_non_negative_int, get_correct_sentence


def reverse_words(lst):
    for i, s in enumerate(lst):
        num = i + 1
        words = s.split(" ")
        words.reverse()
        s = "Case #" + format(num) + ": " + ' '.join(words)
        print(s)


def main():
    cases = []
    # obtener datos entrada
    num_cases = get_non_negative_int("Indica la cantidad de frases a analizar: ")
    for i in range(0, num_cases):
        case = get_correct_sentence("Indica la frase " + str(i + 1) + ": ")
        cases.append(case)

    reverse_words(cases)


if __name__ == '__main__':
    main()
