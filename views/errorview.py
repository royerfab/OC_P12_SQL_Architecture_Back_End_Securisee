import re


class InputCheckView:
    def __init__(self):
        self.error_handler = ErrorHandlerView()

    # On sépare les deux cas d'update ou pas pour pouvoir préciser à la fin que s'il n'y a pas d'user_input on peut mettre une chaîne de caractère vide
    # dans notre vue on veut ça pour laisser des choses comme elles sont
    def check_string(self, message, updated=False):
        while True:
            user_input = input(message)
            if (not updated and re.search('^[\\w ]{3,}$', user_input)) or (updated and (re.search('^[\\w ]{3,}$', user_input) or not user_input)):
                return user_input          
            self.error_handler.display_error('Mauvais format')

    def check_int(self, message, updated=False):
        while True:
            user_input = input(message)
            if (not updated and user_input.strip().isdigit()) or (updated and (user_input.strip().isdigit() or not user_input)):
                return int(user_input)
            self.error_handler.display_error('Mauvais format')

    def check_date(self, message, updated=False):
        while True:
            user_input = input(message)
            if (not updated and re.match(r"^\d{4}/\d{2}/\d{2}$", user_input)) or (updated and (re.match(r"^\d{4}/\d{2}/\d{2}$", user_input) or not user_input)):
                return user_input
            self.error_handler.display_error('Mauvais format')

    def check_sex(self, message):
        while True:
            user_input = input(message)
            if user_input == 'M' or user_input == 'F':
                return user_input
            self.error_handler.display_error('Mauvais format (M ou F)')

    def input_in_array_of_int(self, message, array, updated=False):
        while True:
            user_input = int(input(message))
            if (not updated and user_input in array) or (updated and (user_input in array or not user_input in array)):
                return user_input
            self.error_handler.display_error('numéro inconnu')

    def role_option(self):
        while True:
            print('Entrez le numéro de votre équipe : ')
            print('1: Gestion')
            print('2: Commercial')
            print('3: Support')
            user_input = input('Votre choix: ')
            if user_input == '1':
                return 'gestion'
            elif user_input == '2':
                return 'commercial'
            elif user_input == '3':
                return 'support'
            else:
                self.error_handler.display_error('mauvais format')


class ErrorHandlerView:
    @staticmethod
    def display_error(error):
        print(f'\033[31mErreur\033[00m: {error}')
