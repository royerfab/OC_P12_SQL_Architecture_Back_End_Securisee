from .errorview import InputCheckView
from rich.console import Console
from rich.table import Table


class UserView:
    def __init__(self):
        self.input = InputCheckView()

    def get_user_data(self):
        username = self.input.check_string("Entrer le nom d'utilisateur : ")
        password = self.input.check_string("Entrer le mot de passe : ")
        role = self.input.role_option()
        return username, password, role

    # staticmethod : plus accès aux input check
    # def display_users(self, users):
    #    for user in users:
    #        print(user)

    def display_users(self, users):
        table = Table(title="Liste des utilisateurs")
        table.add_column("User id")
        table.add_column("Username")
        table.add_column("Role")

        for user in users:
            table.add_row(str(user.id), str(user.username), str(user.role))

        console = Console()
        console.print(table)

    def get_user_id(self, user_id_list):
        choice = self.input.input_in_array_of_int(
            "Entrer l'id de l'utilisateur concerné : ", user_id_list)
        return choice

    def update_user(self, user):
        print("Taper Entrée pour conserver la valeur sans modification")
        username = self.input.check_string(f"usernanme ({user.username}) : ", updated=True) or user.username
        password = self.input.check_string("password (****) : ")
        return username, password
