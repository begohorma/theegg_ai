from src.deck import Deck


class Solitaire:
    def __init__(self):

        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.deck = Deck("")  # se ganera baraja con el orden por defecto

    def encrypt(self, in_text, k):
        # quitar los espacios en blanco
        no_spaces_original_text = in_text.replace(" ", "")
        # completar el texto si su longuitud no es múltiplo de 5
        complete_text = self.complete_with_x(no_spaces_original_text)
        # convertir el texto original en números según orden abecedario
        original_numbers = self.letters_to_numbers(complete_text)
        # convertir el texto de la clave a sus valores numérico según abecedario
        key_numbers = self.letters_to_numbers(k)
        # generar el stream con el solitario
        no_spaces_stream_text = self.generate_stream(complete_text, key_numbers)
        # convertir el stream en números según orden abecedario
        stream_numbers = self.letters_to_numbers(no_spaces_stream_text)
        # sumar en modulo 26 los números correspondientes al texto original y el stram
        cipher_numbers = self.add_mod26(original_numbers, stream_numbers)
        # convertir a texto la suma
        cipher_text = self.numbers_to_letters(cipher_numbers)
        # agrupar texto salida en grupos de 5
        cipher_text = self.group_in_five(cipher_text)
        return str(cipher_text)

    def decrypt(self, cipher_text, k):
        # quitar los espacios en blanco
        no_spaces_cipher_text = cipher_text.replace(" ", "")
        # completar el texto si su longuitud no es múltiplo de 5
        complete_cipher_text = self.complete_with_x(no_spaces_cipher_text)
        # convertir el texto de la clave a sus valores numérico según abecedario
        key_numbers = self.letters_to_numbers(k)
        # generar el stream con el solitario
        no_spaces_stream_text = self.generate_stream(complete_cipher_text, key_numbers)
        # convertir el texto cifrado en números según orden abecedario
        cipher_numbers = self.letters_to_numbers(complete_cipher_text)
        # convertir el stream en números según orden abecedario
        stream_numbers = self.letters_to_numbers(no_spaces_stream_text)
        # restar en modulo 26 los números correspondientes al texto cifrado y el stram
        cipher_numbers = self.substract_mod26(cipher_numbers, stream_numbers)
        # convertir a texto la resta
        original_text = self.numbers_to_letters(cipher_numbers)
        # # agrupar texto salida en grupos de 5
        # original_text = self.group_in_five(original_text)
        return str(original_text)

    def letters_to_numbers(self, text):
        numbers = []
        for car in text:
            numbers.append(self.letter_to_number(car))

        return numbers

    def letter_to_number(self, letter):
        if letter == "":
            return 0
        else:
            return self.alphabet.find(letter) + 1

    def numbers_to_letters(self, numbers):
        text = ""
        for num in numbers:
            text += self.number_to_letter(num)
        return text

    def number_to_letter(self, number):
        return self.alphabet[number - 1]

    def complete_with_x(self, in_text):
        # añadir X para que la longuitud del texto sea múltiplo de 5
        if len(in_text) % 5 != 0:
            new_text = in_text + ("X" * (5 - (len(in_text) % 5)))
        else:
            new_text = in_text
        return new_text

    def group_in_five(self, in_text):
        # dividir el texto de entrada en grupos de 5 letras
        # # quitar los espacios en blanco
        s1 = in_text.replace(" ", "")
        # insertar un blanco cada 5 caracteres
        for n in range(len(s1) - 5, 4, -5):
            s1 = s1[:n] + " " + s1[n:]
        return s1

    def generate_stream(self, in_text, key_numbers):
        output_stream = ""
        # inicializar la baraja con la clave
        self.deck.apply_key(key_numbers)
        for c in range(0, len(in_text)):
            output_num = self.generate_output_number()
            output_stream += self.number_to_letter(output_num)
        return output_stream

    def generate_output_number(self):
        while True:
            # mover JokerA
            ja_position = self.deck.find_card_position_by_rank(53)
            self.deck.move_card_one_position_down(ja_position)
            # mover JokerB
            jb_position = self.deck.find_card_position_by_rank(54)
            self.deck.move_card_two_position_down(jb_position)
            # triple corte
            ja_position = self.deck.find_card_position_by_rank(53)
            jb_position = self.deck.find_card_position_by_rank(54)
            if ja_position < jb_position:
                self.deck.triple_cut(ja_position, jb_position)
            else:
                self.deck.triple_cut(jb_position, ja_position)
            # corte segun posición valor última carta
            self.deck.count_cut(self.deck.get_cards()[53].card_to_number())
            num = self.deck.get_cards()[0].card_to_number()
            # convertir primera carta
            if self.deck.get_cards()[num].is_joker():
                continue
            else:
                break
        final_num = self.deck.get_cards()[num].card_to_number_1_to_26()
        return final_num

    def add_mod26(self, original_numbers, stream_numbers):
        addition = []

        for i in range(len(original_numbers)):
            add = original_numbers[i] + stream_numbers[i]
            if add > 26:
                addition.append(add - 26)
            else:
                addition.append(add)
        return addition

    def substract_mod26(self, cipher_numbers, stream_numbers):
        substraction = []

        for i in range(len(cipher_numbers)):
            if cipher_numbers[i] <= stream_numbers[i]:
                substraction.append((26 + cipher_numbers[i]) - stream_numbers[i])
            else:
                substraction.append(cipher_numbers[i] - stream_numbers[i])
        return substraction
