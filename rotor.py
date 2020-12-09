"""
M3 rotor
Rotor #	ABCDEFGHIJKLMNOPQRSTUVWXYZ	Date

I	    EKMFLGDQVZNTOWYHXUSPAIBRCJ	1930
II	    AJDKSIRUXBLHWTMCQGZNPYFVOE	1930
III	    BDFHJLCPRTXVZNYEIWGAKMUSQO	1930
IV	    ESOVPZJAYQUIRHXLNFTGKDCMWB	1938
V	    VZBRGITYUPSDNHLXAWMJQOFECK	1938
VI	    JPGVOUMFYQBENHZRDKASXLICTW	1939
VII	    NZJHGRCXMYSWBOUFAIVLPEKQDT	1939
VIII	FKQHTLXOCBJSPDZRAMEWNIUYGV	1939

"""


def list_maker(str_list):
    """Takes list in a string and outputs a list"""
    output_list = []
    output_list[:0] = str_list
    return output_list


def strtoint(text_input):
    alphabet = list_maker('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    output = []
    for letter in text_input:
        index = alphabet.index(letter)
        output.append(index)
    return output


class Rotor:
    def __init__(self):
        self.rotor_wiring = ''
        self.rotor_alphabet = list_maker(self.rotor_wiring)
        self.rotor_position = 0
        self.alphabet_wiring = ''
        self.alphabet = list_maker(self.alphabet_wiring)

    def show_position(self):
        """Show the rotors current position"""
        return self.alphabet[0]

    def rotate(self):
        """Take the letter at the beginning of the alphabet
        and put it at the end of the alphabet"""
        self.alphabet.append((self.alphabet[0]))
        self.alphabet.pop(0)
        self.rotor_alphabet.append(self.rotor_alphabet[0])
        self.rotor_alphabet.pop(0)

    def set_position(self, position):
        self.rotor_alphabet = list_maker(self.rotor_wiring)
        for letter in range(0, position):
            self.rotate()

    def reset_position(self):
        self.rotor_alphabet = list_maker(self.rotor_wiring)
        for letter in range(0):
            self.rotate()

    def encrypt(self, text_input):
        new_letter = self.rotor_alphabet[text_input]
        new_index = self.alphabet.index(new_letter)
        return new_index

    def decrypt(self, input_value):
        new_letter = self.alphabet[input_value]
        new_index = self.rotor_alphabet.index(new_letter)
        return new_index


class RotorI(Rotor):
    def __init__(self):
        super().__init__()
        self.rotor_wiring = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'
        self.rotor_alphabet = list_maker(self.rotor_wiring)
        self.alphabet = list_maker('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        self.rotation_notch = 'Q'


class RotorII(Rotor):
    def __init__(self):
        super().__init__()
        self.rotor_wiring = 'AJDKSIRUXBLHWTMCQGZNPYFVOE'
        self.rotor_alphabet = list_maker(self.rotor_wiring)
        self.alphabet = list_maker('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        self.rotation_notch = 'E'


class RotorIII(Rotor):
    def __init__(self):
        super().__init__()
        self.rotor_wiring = 'BDFHJLCPRTXVZNYEIWGAKMUSQO'
        self.rotor_alphabet = list_maker(self.rotor_wiring)
        self.alphabet = list_maker('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        self.rotation_notch = 'V'


class RotorIV(Rotor):
    def __init__(self):
        super().__init__()
        self.rotor_wiring = 'ESOVPZJAYQUIRHXLNFTGKDCMWB'
        self.rotor_alphabet = list_maker(self.rotor_wiring)
        self.alphabet = list_maker('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        self.rotation_notch = 'J'


class RotorV(Rotor):
    def __init__(self):
        super().__init__()
        self.rotor_wiring = 'ESOVPZJAYQUIRHXLNFTGKDCMWB'
        self.rotor_alphabet = list_maker(self.rotor_wiring)
        self.alphabet = list_maker('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        self.rotation_notch = 'J'


class ReflectorB(Rotor):
    def __init__(self):
        super().__init__()
        self.wiring_B = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'
        self.rotor_alphabet = list_maker(self.wiring_B)
        self.alphabet = list_maker('ABCDEFGHIJKLMNOPQRSTUVWXYZ')


class ReflectorC(Rotor):
    def __init__(self):
        super().__init__()
        self.wiring_C = 'FVPJIAOYEDRZXWGCTKUQSBNMHL'
        self.rotor_alphabet = list_maker(self.wiring_C)
        self.alphabet = list_maker('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
