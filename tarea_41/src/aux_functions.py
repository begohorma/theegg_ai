def get_correct_input_text(prompt):
    while True:
        filepath = input(prompt)
        try:

            if filepath.lower().endswith(('.txt', '.rtf')):

                with open(filepath, "r", encoding='utf8') as file:
                    input_text = file.read()
                    file.close()
                    break
            else:
                print("La extensión del fichero deber ser txt o o rtf")
                continue
        except FileExistsError:
            print("El fichero indicado no existe")
            continue
        except FileNotFoundError:
            print("El fichero indicado no se encuentra")
            continue
        except IOError:
            print("La ruta del fichero es incorrecta")
            continue

    return input_text
