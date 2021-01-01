from aux_functions import get_correct_input_text
import operator
import re


def get_all_matches(regex, input_text):
    pattern = re.compile(regex)
    result = pattern.findall(input_text)
    return result


def get_words(input_text):
    # como \w incluye cualquier carácter de palabra menos el guión, éste se incluye explicitamente.
    # los carácteres de palabra son [a-zA-Z0-9_]
    return get_all_matches(r'[\w\-]+', input_text)


def get_characters_with_spaces(input_text):
    return get_all_matches(r'.|\s', input_text)


def get_characters_without_spaces(input_text):
    return get_all_matches(r'[^\s]', input_text)


def get_word_frequency(words):
    #  generar diccionario con las palabras como clave y su frecuencia como valor
    wordfrec = {}
    for w in words:
        wordfrec[w] = words.count(w)
    return wordfrec


def print_word_frequency_sorted(words_frequency):
    #  opetator permite indicar el elemento por el que se quiere ordenar el diccionario
    #  0: la clave, 1: el valor
    #  se ordena el diccionario en orden descendente de los valores de las fecuencias
    #  se obtiene una lista de tuplas. El primer elemento de la tupla es la palabra y el segundo la frecuencia.
    words_frequency_sort = sorted(words_frequency.items(), key=operator.itemgetter(1), reverse=True)

    print("Ranking")
    # se recorre la lista ordenada para obtener la palabras y su frecuencia
    # cada word es una tupla.
    for word in enumerate(words_frequency_sort):
        print("La palabra '{0}' aparece {1} veces.".format(word[1][0], word[1][1]))


def main():
    # obtener texto de entrada
    input_text = get_correct_input_text("Indica la ruta del fichero que contiene el  texto a analizar: ")

    words = get_words(input_text)
    words_frequency = get_word_frequency(words)
    print("")
    print("Número de caracteres del texto sin espacios es: {0}".format(len(get_characters_without_spaces(input_text))))
    print("Número de caracteres del texto con espacios es: {0}".format(len(get_characters_with_spaces(input_text))))
    print("Número de palabras del texto es: {0}".format(len(words)))
    print("")
    print_word_frequency_sorted(words_frequency)


if __name__ == '__main__':
    main()
