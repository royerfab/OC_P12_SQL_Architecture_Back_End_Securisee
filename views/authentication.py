from .errorview import InputCheckView


class AuthenticationView:
    def __init__(self):
        self.input = InputCheckView()

    def get_login_data(self):
        username = self.input.check_string("Entrez votre nom d'utilisateur : ")
        password = self.input.check_string("Entrez votre mot de passe : ")
        return username, password