from src import auxFunctions as aux

if __name__ == '__main__':
    # obtener datos de entrada
    action = aux.get_correct_operation("Indicar operación a realizar. E para encriptar, D para desencriptar: ")
    print(action)
    input_text = aux.get_correct_input_text("Introducir texto a encriptar o desencriptar. Usar letras del alfabeto ingles: ")
    print(input_text)
    key = aux.get_correct_input_text("Introducir clave :")
    print(key)

    # Según la opción seleccionada,llamar al método correspondiente de la clase Solitaire
    s = Solitaire()
    if action == "C":
        output = s.encrypt(input_text, key)
    else:
        output = s.decrypt(input_text, key)
    # Mostrar resultado
    print(output)


