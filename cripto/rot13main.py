from encryption.rot13 import Rot13

if __name__ == "__main__":
    x = Rot13()
    message = input(str('Введите текст: '))
    print(x.encrypt(message))
