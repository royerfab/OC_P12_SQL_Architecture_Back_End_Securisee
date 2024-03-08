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
        print("7. Quitter le programme")
        choice = self.input.input_in_array_of_int(" ", range(1, 8))
        return choice

    def user_menu(self):
        print("1. Créer un nouvel utilisateur (gestion)")
        print("2. Modifier un utilisateur (gestion)")
        print("3. Supprimer un utilisateur (gestion)")
        print("4. Afficher la liste des utilisateurs")
        print("5. Retour")
        choice = self.input.input_in_array_of_int(" ", range(1, 6))
        return choice

    def client_menu(self):
        print("1. Créer un nouveau client (commerical)")
        print("2. Modifier un client (commerical)")
        print("3. Supprimer un client (gestion)")
        print("4. Afficher la liste des clients")
        print("5. Retour")
        choice = self.input.input_in_array_of_int(" ", range(1, 6))
        return choice

    def contract_menu(self):
        print("1. Créer un nouveau contrat (gestion)")
        print("2. Modifier un contrat (gestion et commercial)")
        print("3. Supprimer un contrat (gestion)")
        print("4. Afficher les contrats")
        print("5. Retour")
        choice = self.input.input_in_array_of_int(" ", range(1, 6))
        return choice

    def contract_display_menu(self):
        print("1. Afficher tous les contrat")
        print("2. Afficher les contrats pas signés (commercial)")
        print("3. Afficher les contrats pas payés (commercial)")
        print("4. Retour")
        choice = self.input.input_in_array_of_int(" ", range(1, 5))
        return choice

    def event_menu(self):
        print("1. Créer un nouvel événement (commercial)")
        print("2. Modifier un événement (support)")
        print("3. Supprimer un événement (gestion)")
        print("4. Afficher la liste des événements")
        print("5. Afficher vos événements (support)")
        print("6. Afficher les événements sans support (gestion)")
        print("7. Assigner un contact support à un événement (gestion)")
        print("8. Retour")
        choice = self.input.input_in_array_of_int(" ", range(1, 9))
        return choice
