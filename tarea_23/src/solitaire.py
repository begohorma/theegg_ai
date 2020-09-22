class Solitaire:
    def __init__(self):

        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        # deck

    def encrypt(self, input_text, key):
        # TODO real implementation

        # quitar los espacios en blanco
        no_spaces_original_text = input_text.replace(" ", "")
        # convertir el texto original en números según orden abecedario
        original_numbers = self.letters_to_numbers(no_spaces_original_text)
        # generar el stream con el solitario
        no_spaces_stream_text = self.generate_stream(input_text, key)
        # convertir el stream en números según orden abecedario
        stream_numbers = self.letters_to_numbers(no_spaces_stream_text)
        # sumar en modulo 26 los números correspondientes al texto original y el stram
        cipher_numbers = self.add_mod26(original_numbers, stream_numbers)
        # convertir a texto la suma
        cipher_text = self.numbers_to_letters(cipher_numbers)
        # agrupar texto salida en grupos de 5
        cipher_text = self.group_in_five(cipher_text)
        return str(cipher_text)
        #return "OSKJJ JGTMW"

    def decrypt(self, cipher_text, key):
        # TODO real implementation
        # quitar los espacios en blanco
        no_spaces_cipher_text = cipher_text.replace(" ", "")
        # generar el stream con el solitario
        no_spaces_stream_text = self.generate_stream(cipher_text, key)
        # convertir el texto cifrado en números según orden abecedario
        cipher_numbers = self.letters_to_numbers(no_spaces_cipher_text)
        # convertir el stream en números según orden abecedario
        stream_numbers = self.letters_to_numbers(no_spaces_stream_text)
        # restar en modulo 26 los números correspondientes al texto cifrado y el stram
        cipher_numbers = self.substract_mod26(cipher_numbers, stream_numbers)
        # convertir a texto la resta
        cipher_text = self.numbers_to_letters(cipher_numbers)
        # agrupar texto salida en grupos de 5
        cipher_text = self.group_in_five(cipher_text)
        return str(cipher_text)
        #return "DO NOT USE PC"

    def letters_to_numbers(self, text):
        numbers = []
        for car in text:
            numbers.append(self.letter_to_number(car))

        return numbers

    def letter_to_number(self, letter):
        return self.alphabet.find(letter) + 1

    def numbers_to_letters(self, numbers):
        text = ""
        for num in numbers:
            text += self.number_to_letter(num)
        return text

    def number_to_letter(self, number):
        return self.alphabet[number - 1]

    def group_in_five(self, input_text):
        # dividir el texto de entrada en grupos de 5 letras y usar X para completar el último grupo
        # quitar los espacios en blanco
        s1 = input_text.replace(" ", "")
        # el número de "X"s a añadir será el modulo de dividir la longitud del texto sin espacios entre 5, menos 1
        s2 = s1 + "X" * ((len(s1) % 5) - 1)
        # insertar un blanco cada 5 caracteres
        for n in range(len(s2) - 5, 4, -5):
            s2 = s2[:n] + " " + s2[n:]
        return s2

    def generate_stream(self, input_text,  key):
        # TODO real implementation
        return "KDWUPONOWT"

    def add_mod26(self, original_numbers, stream_numbers):
        addition = []

        for i in range(len(original_numbers)):
            s = original_numbers[i] + stream_numbers[i]
            if s > 26:
                addition.append(s - 26)
            else:
                addition.append(s)
        return addition

    def substract_mod26(self, cipher_numbers, stream_numbers):
        substraction = []

        for i in range(len(cipher_numbers)):
            if cipher_numbers[i] <= stream_numbers[i]:
                substraction.append((26 + cipher_numbers[i]) - stream_numbers[i])
            else:
                substraction.append(cipher_numbers[i] - stream_numbers[i])
        return substraction
    
    
if __name__ == '__main__':
    s = Solitaire()
    input_text = "DO NOT USE PC"
    input_text2 = "USE A DECK "
    input_text3 = "USE A DECK DO NOT USE PC"
    key = ""
    output = s.encrypt(input_text, key)
    print(output)
    subs = s.substract_mod26([15, 19, 11, 10, 10, 10, 7, 20, 13, 23],[11, 4, 23, 21, 16, 15, 14, 15, 23, 20])
    print(subs)
