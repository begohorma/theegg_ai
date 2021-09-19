from aux_functions import *


def main():
    first_level = set()
    second_level = set()
    print("\n Alumnos de nivel primario.")
    print("-----------------------------------\n")
    first_level = get_a_set_of_names(first_level)
    print("\n Alumnos de nivel secundario.")
    print("-----------------------------------\n")
    second_level = get_a_set_of_names(second_level)

    print("\nLos nombres de pilas de todos los estudiantes son: \n")
    for name in first_level | second_level:
        print(name)
    print("\nLos nombres comunes en ambos niveles son:\n")
    for name in first_level & second_level:
        print(name)
    print("\nLos nombres del nivel primario que no están en el secundario son:\n ")
    for name in first_level-second_level:
        print(name)


if __name__ == '__main__':
    main()
