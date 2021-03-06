from rotor import *


class EnigmaMachine:
    alphabet = list_maker('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    
    def __init__(self, fast_rotor, medium_rotor, slow_rotor, reflector):
        self.fast_rotor = fast_rotor
        self.medium_rotor = medium_rotor
        self.slow_rotor = slow_rotor
        self.reflector = reflector
        self.message_input = ''
        self.message_output = ''
        self.rotation_counter = 0
        self.output = ''

    def message_to_list(self, message):
        """Creates a list from the message entered"""
        message_list = []
        for letter in message:
            if letter == ' ' or '':
                pass
            try:
                if letter.upper() in EnigmaMachine.alphabet:
                    message_list.append(letter.upper())
            except:
                print('please enter a valid character')

        self.message_input = message_list
        return message_list

    def int_to_output(self):
        """Takes message and converts it into a str and inserts a blank
        space every 6 letters to mimic actual Enigma Machine output"""
        output_list = []
        output_str = ''
        space_counter = 0
        for number in self.message_output:
            letter = EnigmaMachine.alphabet[number]
            output_list.append(letter)
            space_counter += 1
            if space_counter == 5:
                output_list.append(' ')
                space_counter = 0
        self.output = (output_str.join(output_list))

    def rotate_mechanism(self):
        """Creates the the function that rotates the rotors as each
        letter passes through"""

        self.fast_rotor.rotate()  # Spins the fast rotor once for every letter

        if self.medium_rotor.alphabet[0] == self.medium_rotor.rotation_notch:  # Creates Double stepping mechanism
            self.medium_rotor.rotate()
            if self.medium_rotor.alphabet[25] == self.medium_rotor.rotation_notch:  # Spins Slow Rotor
                self.slow_rotor.rotate()

        if self.fast_rotor.alphabet[25] == self.fast_rotor.rotation_notch:  # Spins Medium Rotor
            self.medium_rotor.rotate()

    def reset_rotors(self):
        pass

    def run_machine(self):
        """Passes the message through the Enigma Machine one
        letter at a time"""
        number_list = []
        for letter in self.message_input:
            number = EnigmaMachine.alphabet.index(letter)
            self.rotate_mechanism()
            step_one = self.fast_rotor.encrypt(number)
            step_two = self.medium_rotor.encrypt(step_one)
            step_three = self.slow_rotor.encrypt(step_two)
            step_four = self.reflector.encrypt(step_three)
            step_five = self.slow_rotor.decrypt(step_four)
            step_six = self.medium_rotor.decrypt(step_five)
            step_seven = self.fast_rotor.decrypt(step_six)
            number_list.append(step_seven)
        self.message_output = number_list
