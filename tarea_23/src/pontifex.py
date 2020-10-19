from auxFunctions import get_correct_input_text, get_correct_operation
from solitaire import Solitaire
import sys


def main():
    # obtener datos de entrada
    action = get_correct_operation("Indicar operación a realizar. E para encriptar, D para desencriptar: ")
    input_text = get_correct_input_text("Introducir texto a encriptar o desencriptar. Usar letras del alfabeto ingles: ")
    key = get_correct_input_text("Introducir clave :")

    # Según la opción seleccionada,llamar al método correspondiente de la clase Solitaire
    s = Solitaire()
    if action == "E":
        output = s.encrypt(input_text, key)
    else:
        output = s.decrypt(input_text, key)
    # Mostrar resultado
    print(output)


if __name__ == '__main__':
    main()
