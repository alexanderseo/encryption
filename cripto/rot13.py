from encryption import LatinDictForRot13


class Rot13:
    def __init__(self, shift=13):
        dictalphabet = LatinDictForRot13()
        self.orig_dict = dictalphabet.originalphabet()
        self.move_dict = dictalphabet.movealphabet()
        self.shift = shift
    def encrypt(self, message):
        cipher = ''
        for letter in message:
            if letter != ' ':
                if letter.isalpha():
                    if letter.isupper():
                        num = (self.orig_dict[letter] + self.shift) % 26
                        cipher += self.move_dict[num]
                    else:
                        letter = letter.upper()
                        num = (self.orig_dict[letter] + self.shift) % 26
                        cipher += self.move_dict[num].lower()
                else:
                    cipher += letter
            else:
                cipher += ' '
        return cipher
