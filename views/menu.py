class MenuView:
    def main_menu(self):
        print("1. Gestion des utilisateurs")
        print("2. Gestion des clients")
        choice = int(input(" "))
        return choice

    def user_menu(self):
        print("1. Créer un nouvel utilisateur")
        print("2. Modifier un utilisateur")
        print("3. Supprimer un utilisateur")
        print("4. Afficher la liste des utilisateurs")
        choice = int(input(" "))
        return choice

