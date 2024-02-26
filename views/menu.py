from .errorview import InputCheckView


class MenuView:
    def __init__(self):
        self.input = InputCheckView()

    def main_menu(self):
        print("1. Gestion des utilisateurs")
        print("2. Gestion des clients")
        print("3. Gestion des contrats")
        print("4. Gestion des événements")
        print("5. Se connecter")
        print("6. Se déconnecter")
        choice = self.input.check_int(" ")
        return choice

    def user_menu(self):
        print("1. Créer un nouvel utilisateur")
        print("2. Modifier un utilisateur")
        print("3. Supprimer un utilisateur")
        print("4. Afficher la liste des utilisateurs")
        choice = int(input(" "))
        return choice

    def client_menu(self):
        print("1. Créer un nouveau client")
        print("2. Modifier un client")
        print("3. Supprimer un client")
        print("4. Afficher la liste des clients")
        choice = self.input.check_int(" ")
        return choice

    def contract_menu(self):
        print("1. Créer un nouveau contrat")
        print("2. Modifier un contrat")
        print("3. Supprimer un contrat")
        print("4. Afficher la liste des contrats")
        choice = self.input.check_int(" ")
        return choice

    def event_menu(self):
        print("1. Créer un nouvel événement")
        print("2. Modifier un événement")
        print("3. Supprimer un événement")
        print("4. Afficher la liste des événements")
        choice = self.input.check_int(" ")
        return choice

