import sys
import time
from aux_functions import *
from compressor import Compressor


def main():

    get_input_text_max_length("Indica el número máximo de caracteres del texto a comprimir: ")

    print("Longitud máxima del texto a comprimir:{0} ".format(config.input_text_max_length))

    in_text = get_correct_input_string("Indica el texto a comprimir:")

    print("Texto a comprimir: {0}".format(in_text))
    print("Número de caracteres del texto: {0}".format(len(in_text)))

    t0 = time.time()

    c = Compressor()
    output = c.compress(in_text)

    t1 = time.time()

    print("Tuplas que representan el texto comprimido: {0}".format(output))
    print("Espacio en memoria el texto comprimido: {0}".format(sys.getsizeof(output)))
    print("Número de tuplas: {0}".format(len(output)))
    print("la compresión ha tardado en ejecutarse {0} segundos.".format(round(t1 - t0, 8)))

    output_des = c.decompress(output)
    print("texto descomprimido: {0}".format(output_des))
    print("Espacio en memoria del texto descomprimido: {0} ".format(sys.getsizeof(output_des)))


if __name__ == '__main__':
    main()
